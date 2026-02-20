v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 120 -80 150 -80 {lab=VSS}
N 120 -120 150 -120 {lab=VDD_1V8}
N 120 -100 150 -100 {lab=IB_BG}
N 120 -140 150 -140 {lab=VSS}
N 120 -160 150 -160 {lab=VDD_1V8}
N 450 -140 600 -140 {lab=#net1}
N 600 -140 600 -80 {lab=#net1}
N 600 -80 940 -80 {lab=#net1}
N 620 -100 940 -100 {lab=#net2}
N 620 -160 620 -100 {lab=#net2}
N 450 -160 620 -160 {lab=#net2}
N 900 -120 940 -120 {lab=IB_OSC}
N 900 -140 940 -140 {lab=VSS}
N 900 -160 940 -160 {lab=VDD_1V8}
N 1240 -160 1280 -160 {lab=VOUT_OSC}
C {devices/ipin.sym} -180 -30 0 0 {name=p11 lab=VSS}
C {devices/ipin.sym} -180 -80 0 0 {name=p7 lab=VDD_1V8}
C {devices/ipin.sym} -180 20 0 0 {name=p9 lab=IB_OSC}
C {LELO_GR01_SKY130A/bandgap.sym} 300 -120 0 0 {name=x7}
C {devices/lab_wire.sym} 120 -80 0 0 {name=p25 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 120 -120 0 0 {name=p26 sig_type=std_logic lab=VDD_1V8}
C {devices/ipin.sym} -180 70 0 0 {name=p27 lab=IB_BG}
C {devices/lab_wire.sym} 120 -100 0 0 {name=p28 sig_type=std_logic lab=IB_BG}
C {devices/lab_wire.sym} 120 -160 0 0 {name=p14 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} 120 -140 0 0 {name=p15 sig_type=std_logic lab=VSS}
C {LELO_GR01_SKY130A/oscillator.sym} 1090 -120 0 0 {name=x8}
C {devices/lab_wire.sym} 900 -160 0 0 {name=p1 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} 900 -140 0 0 {name=p2 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 900 -120 0 0 {name=p3 sig_type=std_logic lab=IB_OSC}
C {devices/opin.sym} 1280 -160 0 0 {name=p4 lab=VOUT_OSC}
