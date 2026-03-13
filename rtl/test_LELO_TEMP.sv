`timescale 1ns / 1ps


module testbench;

reg clk = 0;
always #5 clk = ~clk;

reg rst = 1'b0;


wire [7:0] temp; //Output digital temperature

LELO_TEMP lelo (
    .clk(clk),
    .rst(rst),
    .temp(temp)
);




initial begin

    //Save all the waveforms from the testbench
    $dumpfile("wave.vcd");
    $dumpvars(0, testbench);

    //Reset at startup
    rst = 1'b1;
    repeat(5) @(posedge clk);
    rst = 1'b0;


    #200 $finish;


end

endmodule
