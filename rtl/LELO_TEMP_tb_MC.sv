`timescale 1ns/1ps

/*
    To run, use:
    "iverilog -g2012 -o tb LELO_TEMP.sv LELO_TEMP_sim.sv LELO_TEMP_tb_MC.sv"
    "vvp tb"
    Then plot results with "python MC_results/MC_results_plot.py "
*/

module LELO_TEMP_tb;

    localparam real CLK_FREQ = 32768.0;       // 32.768 kHz
    localparam real CLK_PERIOD = 1/CLK_FREQ * 1e9; // ns

    reg clk;
    reg rst;
    reg request;
    real temperature;

    wire pwr;
    wire done;
    wire [11:0] out;
    wire oscillator_clk;

    // Setup devices
    LELO_TEMP dut( // DUT
        .clk(clk),
        .rst(rst),
        .request(request),
        .oscillator_clk(oscillator_clk),
        .pwr(pwr),
        .done(done),
        .out(out)
    );

    osc_sim u_osc( // Oscillator sim
        .enable(pwr),
        .temperature(temperature),
        .osc_out_pulse(oscillator_clk)
    );

    // Generating the fast main clock
    initial clk = 0;
    always #(CLK_PERIOD/2.0) clk = ~clk;

    integer csv_file;
    real temp;
    integer timeout;
    integer mc;
    reg [256*8:1] csv_out_path;

    initial begin

        // Iterate through MC runs: 0 = base, 1-29 = monte carlo
        for (mc = 0; mc <= 29; mc = mc + 1) begin
            if (mc == 0) begin
                u_osc.csv_file = "MC_csvs/tran_SchGtKttmmTtVt_oscillator.csv";
                csv_out_path = "MC_results/results_mc_0.csv";
            end else begin
                $sformat(u_osc.csv_file, "MC_csvs/tran_SchGtKttmmTtVt_%0d_oscillator.csv", mc);
                $sformat(csv_out_path, "MC_results/results_mc_%0d.csv", mc);
            end

            csv_file = $fopen(csv_out_path, "w");
            $fwrite(csv_file, "temperature_C,count,freq_MHz\n");

            $display("=== MC run %0d: %0s ===", mc, u_osc.csv_file);

            // Reset before each MC run
            rst = 1;
            request = 0;
            temperature = -40.0;
            repeat (5) @(posedge clk);
            rst = 0;
            repeat (5) @(posedge clk);

            // Sweep temperature from -40 to 125 in steps of 15 (matching CSV points)
            for (temp = -40.0; temp <= 125.0; temp = temp + 15.0) begin
                temperature = temp;
                repeat (2) @(posedge clk);

            // Request a measurement, should start our DUT
            @(posedge clk);
            request = 1;
            @(posedge clk);
            request = 0;

            // Wait for done with timeout
            timeout = 0;
            while (!done && timeout < 100000) begin // Timeout might be a bit too long
                @(posedge clk);
                timeout = timeout + 1;
            end

                if (timeout >= 100000) begin
                    $display("TIMEOUT at T=%0.1f C", temp);
                end else begin
                    $display("T=%0.1f C  count=%0d freq=%0.6f MHz", temp, out, u_osc.freq_mhz);
                    $fwrite(csv_file, "%0.1f,%0d,%0.6f\n", temp, out, u_osc.freq_mhz);
                end

                // Small gap between measurements
                repeat (10) @(posedge clk);
            end

            $fclose(csv_file);
        end

        $display("Results written to MC_results/results_mc_*.csv");
        $finish;
    end

endmodule
