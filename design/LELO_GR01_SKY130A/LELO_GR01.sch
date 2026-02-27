v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 250 -450 280 -450 {lab=VSS}
N 250 -490 280 -490 {lab=VDD_1V8}
N 250 -510 280 -510 {lab=VSS}
N 250 -530 280 -530 {lab=VDD_1V8}
N 580 -510 730 -510 {lab=#net1}
N 730 -510 730 -450 {lab=#net1}
N 730 -450 1070 -450 {lab=#net1}
N 750 -470 1070 -470 {lab=#net2}
N 750 -530 750 -470 {lab=#net2}
N 580 -530 750 -530 {lab=#net2}
N 1030 -510 1070 -510 {lab=VSS}
N 1030 -530 1070 -530 {lab=VDD_1V8}
N 1370 -530 1410 -530 {lab=OSC_TEMP_1V8}
C {cborder/border_xs.sym} 0 0 0 0 {
user="wulff"
company="wulff"}
C {devices/ipin.sym} 100 -600 0 0 {name=p1 lab=VDD_1V8}
C {devices/ipin.sym} 100 -100 0 0 {name=p2 lab=VSS}
C {devices/ipin.sym} 100 -300 0 0 {name=p3 lab=PWRUP_1V8}
C {LELO_GR01_SKY130A/bandgap.sym} 430 -490 0 0 {name=x7}
C {devices/lab_wire.sym} 250 -450 0 0 {name=p25 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 250 -490 0 0 {name=p26 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} 250 -530 0 0 {name=p14 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} 250 -510 0 0 {name=p15 sig_type=std_logic lab=VSS}
C {LELO_GR01_SKY130A/oscillator.sym} 1220 -490 0 0 {name=x8}
C {devices/lab_wire.sym} 1030 -530 0 0 {name=p4 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} 1030 -510 0 0 {name=p5 sig_type=std_logic lab=VSS}
C {devices/opin.sym} 1410 -530 0 0 {name=p7 lab=OSC_TEMP_1V8}
