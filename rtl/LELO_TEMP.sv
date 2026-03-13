


module LELO_TEMP(input clk, input rst, input oscillator, output logic[7:0] temp);

    always @ (posedge clk) begin
        if (rst) temp <= 'b0;

        else temp <= temp + 1;
    end


endmodule
