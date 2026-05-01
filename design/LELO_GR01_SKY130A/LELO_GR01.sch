v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 120 -170 150 -170 {lab=VSS}
N 120 -220 150 -220 {lab=PWRUP_1V8}
N 120 -250 150 -250 {lab=VDD_1V8}
N 580 -240 620 -240 {lab=VSS}
N 580 -260 620 -260 {lab=VDD_1V8}
N 450 -180 620 -180 {lab=VREF}
N 450 -240 490 -240 {lab=#net1}
N 490 -240 490 -200 {lab=#net1}
N 490 -200 620 -200 {lab=#net1}
N 920 -260 930 -260 {lab=OSC_TEMP_1V8}
N 120 -200 150 -200 {lab=PWRUP_N_1V8}
N 790 -350 790 -300 {lab=PWRUP_N_1V8}
N 740 -350 740 -300 {lab=PWRUP_1V8}
N -200 -80 -200 -60 {lab=VSS}
N -200 -180 -200 -160 {lab=VDD_1V8}
N -290 -220 120 -220 {lab=PWRUP_1V8}
N 20 -200 120 -200 {lab=PWRUP_N_1V8}
N 30 -200 30 -120 {lab=PWRUP_N_1V8}
N -160 -120 30 -120 {lab=PWRUP_N_1V8}
N -240 -220 -240 -120 {lab=PWRUP_1V8}
C {cborder/border_xs.sym} 0 10 0 0 {
user="wulff"
company="wulff"}
C {devices/ipin.sym} 120 -250 0 0 {name=p1 lab=VDD_1V8}
C {devices/ipin.sym} 120 -170 0 0 {name=p2 lab=VSS}
C {devices/ipin.sym} -290 -220 0 0 {name=p3 lab=PWRUP_1V8}
C {LELO_GR01_SKY130A/bandgap.sym} 300 -210 0 0 {name=x7}
C {LELO_GR01_SKY130A/oscillator.sym} 770 -220 0 0 {name=x8}
C {devices/lab_wire.sym} 580 -260 0 0 {name=p4 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} 580 -240 0 0 {name=p5 sig_type=std_logic lab=VSS}
C {devices/opin.sym} 930 -260 0 0 {name=p7 lab=OSC_TEMP_1V8}
C {devices/lab_wire.sym} 740 -350 0 0 {name=p8 sig_type=std_logic lab=PWRUP_1V8}
C {devices/lab_wire.sym} 790 -350 2 0 {name=p9 sig_type=std_logic lab=PWRUP_N_1V8}
C {devices/lab_wire.sym} -200 -180 0 1 {name=p10 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} -200 -60 2 0 {name=p11 sig_type=std_logic lab=VSS}
C {JNW_TR_SKY130A/JNWTR_IVX1_CV.sym} -240 -120 0 0 {name=x3 }
C {devices/lab_wire.sym} 20 -200 2 1 {name=p6 sig_type=std_logic lab=PWRUP_N_1V8}
C {devices/lab_wire.sym} 530 -180 3 0 {name=p12 sig_type=std_logic lab=VREF}
