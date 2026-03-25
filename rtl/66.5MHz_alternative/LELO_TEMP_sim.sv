// Simulates a temperature-dependent oscillator (delay-based)
// Frequency: 1.5 MHz at -40°C, increasing by 0.0093 MHz per °C
// freq(T) = 1.5 + 0.0093 * (T + 40)  [MHz]

`timescale 1ns/1ps

module osc_sim(
    input enable,
    input real temperature, // input temperature in degrees C
    output reg osc_out_pulse
);

    real freq_mhz;
    real period_ns;

    initial osc_out_pulse = 0;

    always begin
        // Recompute frequency each iteration so temperature changes take effect
        freq_mhz = -1.532093e-10*temperature**4 -2.817110e-08*temperature**3 +1.108474e-05*temperature**2 +8.094844e-03*temperature +1.842090e+00;
        if (freq_mhz < 0.001)
            freq_mhz = 0.001; // Avoid getting zero frequency, will give infinite sims
        period_ns = 1000.0 / freq_mhz;

        if (enable) begin
            #(period_ns/2.0);
            osc_out_pulse = ~osc_out_pulse;
        end else begin
            osc_out_pulse = 0;
            #1; // Slight delay to decrease sim complexity
        end
    end

endmodule
