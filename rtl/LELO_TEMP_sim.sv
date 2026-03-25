

`timescale 1ns/1ps

module osc_sim(
    input enable,
    input real temperature, // input temperature in degrees C
    output reg osc_out_pulse
);

    reg [256*8:1] csv_file;
    initial csv_file = "Typical_csvs/tran_SchGtKttTtVt_oscillator.csv"; // Default CSV, can be overridden by testbench for use with different CSVs

    // Read CSV and return frequency (MHz) for the given temperature
    function real get_freq(input real temp);
        integer fd, n;
        reg [256*8:1] line;
        real t_val, f_val;
        integer found;
        begin
            fd = $fopen(csv_file, "r");
            if (fd == 0) begin $display("ERROR: cannot open %0s", csv_file); $finish; end
            void'($fgets(line, fd)); // skip first line

            get_freq = 0.0;
            found = 0;

            while (!$feof(fd) && !found) begin // Scan through the file until we find our temperature
                n = $fscanf(fd, " %f ; %f", t_val, f_val);
                if (n == 2 && t_val == temp) begin
                    get_freq = f_val / 1.0e6;
                    found = 1;
                end
            end
            $fclose(fd);
            if (!found)
                $display("WARNING: temp %0.1f not found in %0s", temp, csv_file);
        end
    endfunction

    real freq_mhz, period_ns;
    real last_temp;

    initial begin // Initial setup, make sure it starts
        osc_out_pulse = 0;
        freq_mhz = 0.0;
        last_temp = -999.0;
    end

    always begin
        if (temperature != last_temp) begin // Only recheck freq if temp changed, otherwise sim is slow
            freq_mhz = get_freq(temperature);
            last_temp = temperature;
        end
        if (freq_mhz < 0.001) freq_mhz = 0.001;
        period_ns = 1000.0 / freq_mhz;

        if (enable) begin
            #(period_ns/2.0);
            osc_out_pulse = ~osc_out_pulse;
        end else begin
            osc_out_pulse = 0;
            #1; // Slight delay to decrease sim complexity, without it there is an event every timestep
        end
    end

endmodule
