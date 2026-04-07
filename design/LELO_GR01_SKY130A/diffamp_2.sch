v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 90 -120 170 -120 {lab=#net1}
N 50 -90 50 -10 {lab=#net1}
N 210 -90 210 -10 {lab=VOUT}
N 50 -50 130 -50 {lab=#net1}
N 130 -120 130 -50 {lab=#net1}
N 50 -170 50 -150 {lab=VDD_1V8}
N 50 -260 210 -260 {lab=VDD_1V8}
N 210 -170 210 -150 {lab=VDD_1V8}
N -170 -260 50 -260 {lab=VDD_1V8}
N 50 50 50 70 {lab=TAIL}
N 50 70 210 70 {lab=TAIL}
N 210 50 210 70 {lab=TAIL}
N 210 -50 360 -50 {lab=VOUT}
N 250 150 290 150 {lab=VDD_1V8}
N 230 340 230 370 {lab=VSS}
N 210 70 210 120 {lab=TAIL}
N 250 20 280 20 {lab=VIP}
N 210 120 210 150 {lab=TAIL}
N 160 230 170 230 {lab=PWRUP_N_1V8}
N 160 260 170 260 {lab=PWRUP_1V8}
N 130 -160 130 -120 {lab=#net1}
N 130 -260 130 -190 {lab=VDD_1V8}
N 50 -260 50 -170 {lab=VDD_1V8}
N 210 -260 210 -170 {lab=VDD_1V8}
N 80 -190 90 -190 {lab=PWRUP_1V8}
N 190 20 210 20 {lab=VSS}
N 50 20 70 20 {lab=VSS}
N 210 -150 210 -120 {lab=VDD_1V8}
N 50 -150 50 -120 {lab=VDD_1V8}
N -40 20 10 20 {lab=VIN}
C {devices/ipin.sym} -170 -260 0 0 {name=p1 lab=VDD_1V8}
C {devices/ipin.sym} -40 20 0 0 {name=p4 lab=VIN}
C {devices/ipin.sym} 280 20 0 1 {name=p5 lab=VIP}
C {devices/opin.sym} 360 -50 0 0 {name=p6 lab=VOUT}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 10 20 0 0 {name=x1}
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 90 -120 0 1 {name=x2 }
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 170 -120 0 0 {name=x4 }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 250 20 0 1 {name=x3}
C {devices/lab_pin.sym} 130 70 0 0 {name=p8 sig_type=std_logic lab=TAIL}
C {devices/lab_wire.sym} 290 150 2 0 {name=p3 sig_type=std_logic lab=VDD_1V8}
C {LELO_GR01_SKY130A/GM_cell_N.sym} 250 300 1 0 {name=x5}
C {devices/ipin.sym} 160 230 0 0 {name=p2 lab=PWRUP_N_1V8}
C {devices/ipin.sym} 160 260 0 0 {name=p9 lab=PWRUP_1V8}
C {devices/ipin.sym} 230 370 0 0 {name=p10 lab=VSS}
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 90 -190 0 0 {name=x7 }
C {devices/lab_pin.sym} 80 -190 0 0 {name=p11 sig_type=std_logic lab=PWRUP_1V8}
C {devices/lab_pin.sym} 190 20 0 0 {name=p7 sig_type=std_logic lab=VSS}
C {devices/lab_pin.sym} 70 20 0 1 {name=p12 sig_type=std_logic lab=VSS}
