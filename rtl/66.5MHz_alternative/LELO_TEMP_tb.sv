`timescale 1ns/1ps

module LELO_TEMP_tb;

    localparam real CLK_FREQ = 66.5e6;
    localparam real CLK_PERIOD = 1/CLK_FREQ * 1e9; // ns

    reg clk;
    reg rst;
    reg request;
    reg value_read;
    real temperature;

    wire pwr_osc;
    wire done;
    wire [15:0] out;
    wire oscillator;

    // Setup devices
    LELO_TEMP dut( // DUT
        .clk(clk),
        .rst(rst),
        .request(request),
        .oscillator(oscillator),
        .value_read(value_read),
        .pwr_osc(pwr_osc),
        .done(done),
        .out(out)
    );

    osc_sim u_osc( // Oscillator sim
        .enable(pwr_osc),
        .temperature(temperature),
        .osc_out_pulse(oscillator)
    );

    // Generating the fast main clock
    initial clk = 0;
    always #(CLK_PERIOD/2.0) clk = ~clk;

    integer csv_file;
    real temp;
    integer timeout;

    initial begin
        csv_file = $fopen("results.csv", "w");
        $fwrite(csv_file, "temperature_C,count,freq_MHz\n");

        // Reset before we begin to ensure stable state
        rst = 1;
        request = 0;
        value_read = 0;
        temperature = -40.0;
        repeat (5) @(posedge clk);
        rst = 0;
        repeat (5) @(posedge clk);

        // Sweep temperature from -40 to 125 in steps of 5
        for (temp = -40.0; temp <= 125.0; temp = temp + 1.0) begin
            temperature = temp;
            repeat (2) @(posedge clk);

            // Request a measurement
            @(posedge clk);
            request = 1;
            @(posedge clk);
            request = 0;

            // Wait for done with timeout
            timeout = 0;
            while (!done && timeout < 100000) begin
                @(posedge clk);
                timeout = timeout + 1;
            end

            if (timeout >= 100000) begin
                $display("TIMEOUT at T=%0.1f C", temp);
            end else begin
                $display("T=%0.1f C  count=%0d  freq=%0.6f MHz", temp, out, u_osc.freq_mhz);
                $fwrite(csv_file, "%0.1f,%0d,%0.6f\n", temp, out, u_osc.freq_mhz);
            end

            // Acknowledge the value
            @(posedge clk);
            value_read = 1;
            @(posedge clk);
            value_read = 0;

            // Small gap between measurements
            repeat (10) @(posedge clk);
        end

        $fclose(csv_file);
        $display("Results written to results.csv");
        $finish;
    end

endmodule
