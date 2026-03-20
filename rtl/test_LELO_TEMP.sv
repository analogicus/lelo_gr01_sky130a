`timescale 1ns / 1ps


module testbench;

reg clk = 0;
always #30518 clk = ~clk; //Main clock with frequency of 32768Hz

reg oscillator_clk = 0;
always #500 oscillator_clk = ~oscillator_clk;  //Oscillator clock


reg rst = 1'b0;

logic request = 1'b0;
logic pwr;
logic done;

logic [7:0] out; //Output digital temperature

LELO_TEMP lelo (
    .clk(clk),
    .rst(rst),
    .request(request),
    .oscillator_clk(oscillator_clk),
    .pwr(pwr),
    .done(done),
    .out(out)
);




initial begin

    //Save all the waveforms from the testbench
    $dumpfile("wave.vcd");
    $dumpvars(0, testbench);

    //Reset at startup
    rst = 1'b1;
    repeat(5) @(posedge clk);
    rst = 1'b0;


    //Starting a measurement
    repeat(3) @(posedge clk);
    request = 1'b1;
    @(posedge clk);
    request = 1'b0;


    //Wait a bit and start a new measurement
    repeat(10) @(posedge clk);
    request = 1'b1;
    @(posedge clk);
    request = 1'b0;





    repeat(20) @(posedge clk);
    $finish;


end

endmodule
