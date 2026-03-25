

// Convert count to temperature as signed 8.8 fixed-point (divide by 256 to get °C)
// Based on: freq = 1.5 + 0.0093*(T+40) MHz, count = 16*66.5e6/freq
// Inverted: T_fp = 29288602 / count - 51530
function automatic logic signed [15:0] count_to_temperature(input logic [15:0] count);
    logic signed [31:0] temp_fp;
    if (count == 0)
        count_to_temperature = 16'sh7FFF;
    else begin
        temp_fp = $signed(32'd29288602 / {16'd0, count}) - 32'sd51530;
        count_to_temperature = temp_fp[15:0];
    end
endfunction

module LELO_TEMP(
    input clk, // approx 66.5MHz
    input rst, 
    input request, 
    input oscillator, // when pwr_osc high, between 1 and 4MHz depending on temperature
    input value_read,
    output logic pwr_osc, 
    output logic done, 
    output logic[15:0] out);

    parameter MAX_PULSES = 16;

    reg [15:0] fast_clk_counter;
    reg [3:0] pulse_counter;
    reg osc_prev; // for rise detection

    enum logic [1:0] {IDLE, WAIT_FOR_START, MEASURE, VALUE_READY} current_state;

    wire osc_risen = oscillator & ~osc_prev;

    // Main loop, does all state updates and output logic
    always_ff @ (posedge clk, posedge rst) 
    begin
        if (rst) begin
            current_state <= IDLE;
            pwr_osc <= 0;
            done <= 0;
            out <= 0;
            fast_clk_counter <= 0;
            pulse_counter <= 0;
            osc_prev <= 0;

        end else begin
            osc_prev <= oscillator;
            case (current_state)
                IDLE:
                    if (request) begin 
                        current_state <= WAIT_FOR_START;
                        pwr_osc <= 1;
                        fast_clk_counter <= 0;
                        pulse_counter <= 0;
                    end else begin
                        current_state <= IDLE;
                        pwr_osc <= 0;
                    end

                // Wait for first rising edge before counting
                WAIT_FOR_START: begin
                    if (osc_risen) begin
                        current_state <= MEASURE;
                        fast_clk_counter <= 0;
                    end
                end

                MEASURE: begin
                    fast_clk_counter <= fast_clk_counter + 1;
                    if (osc_risen) begin
                        pulse_counter <= pulse_counter + 1;
                        if (pulse_counter == MAX_PULSES - 1) begin
                            current_state <= VALUE_READY;
                            out <= fast_clk_counter;
                            done <= 1;
                            pwr_osc <= 0;
                        end
                    end
                end

                VALUE_READY:
                    if (value_read) begin
                        current_state <= IDLE;
                        done <= 0;
                        out <= 0;
                    end else begin
                        current_state <= VALUE_READY;
                    end
            endcase
        end
    end

endmodule
