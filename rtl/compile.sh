
#compile the verilog code, Start the simulation and plot the signals
iverilog -g2012 -o sim.out test_LELO_TEMP.sv LELO_TEMP.sv && vvp sim.out  
#iverilog -o sim.out test_LELO_TEMP.sv LELO_TEMP.sv && vvp sim.out && gtkwave wave.vcd 

