v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 370 -70 400 -70 {lab=VSS}
N 370 -110 400 -110 {lab=VDD_1V8}
N 370 -150 400 -150 {lab=VDD_1V8}
N 900 -140 940 -140 {lab=VSS}
N 900 -160 940 -160 {lab=VDD_1V8}
N 1240 -160 1280 -160 {lab=VOUT_OSC}
N 700 -80 940 -80 {lab=#net1}
N 700 -140 720 -140 {lab=#net2}
N 720 -140 720 -100 {lab=#net2}
N 720 -100 940 -100 {lab=#net2}
C {devices/ipin.sym} -180 -30 0 0 {name=p11 lab=VSS}
C {devices/ipin.sym} -180 -80 0 0 {name=p7 lab=VDD_1V8}
C {devices/ipin.sym} -180 20 0 0 {name=p9 lab=IB_OSC}
C {LELO_GR01_SKY130A/bandgap.sym} 550 -110 0 0 {name=x7}
C {devices/lab_wire.sym} 370 -70 0 0 {name=p25 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 370 -110 0 0 {name=p26 sig_type=std_logic lab=VDD_1V8}
C {devices/ipin.sym} -180 70 0 0 {name=p27 lab=IB_BG}
C {devices/lab_wire.sym} 370 -150 0 0 {name=p14 sig_type=std_logic lab=VDD_1V8}
C {LELO_GR01_SKY130A/oscillator.sym} 1090 -120 0 0 {name=x8}
C {devices/lab_wire.sym} 900 -160 0 0 {name=p1 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} 900 -140 0 0 {name=p2 sig_type=std_logic lab=VSS}
C {devices/opin.sym} 1280 -160 0 0 {name=p4 lab=VOUT_OSC}
