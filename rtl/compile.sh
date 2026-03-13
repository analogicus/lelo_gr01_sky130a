
#compile the verilog code, Start the simulation and plot the signals
iverilog -o sim.out test_LELO_TEMP.sv LELO_TEMP.sv && vvp sim.out  
#iverilog -o sim.out test_LELO_TEMP.sv LELO_TEMP.sv && vvp sim.out && gtkwave wave.vcd 

