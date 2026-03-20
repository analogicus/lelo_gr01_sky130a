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
N 50 -170 210 -170 {lab=VDD_1V8}
N 210 -170 210 -150 {lab=VDD_1V8}
N -170 -170 50 -170 {lab=VDD_1V8}
N 50 -150 50 -120 {lab=VDD_1V8}
N 210 -150 210 -120 {lab=VDD_1V8}
N 50 50 50 70 {lab=TAIL}
N 50 70 210 70 {lab=TAIL}
N 210 50 210 70 {lab=TAIL}
N 210 20 210 50 {lab=TAIL}
N 50 20 50 50 {lab=TAIL}
N 210 -50 360 -50 {lab=VOUT}
N -170 20 10 20 {lab=VIN}
N -170 80 250 80 {lab=VIP}
N 250 20 250 80 {lab=VIP}
N 170 120 210 120 {lab=VDD_1V8}
N 150 310 150 340 {lab=VSS}
N 130 70 130 120 {lab=TAIL}
C {devices/ipin.sym} -170 -170 0 0 {name=p1 lab=VDD_1V8}
C {devices/ipin.sym} -170 20 0 0 {name=p4 lab=VIN}
C {devices/ipin.sym} -170 80 0 0 {name=p5 lab=VIP}
C {devices/opin.sym} 360 -50 0 0 {name=p6 lab=VOUT}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 10 20 0 0 {name=x1 }
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 90 -120 0 1 {name=x2 }
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 170 -120 0 0 {name=x4 }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 250 20 0 1 {name=x3 }
C {devices/lab_pin.sym} 130 70 0 0 {name=p8 sig_type=std_logic lab=TAIL}
C {devices/lab_wire.sym} 210 120 2 0 {name=p3 sig_type=std_logic lab=VDD_1V8}
C {LELO_GR01_SKY130A/GM_cell_N.sym} 170 270 1 0 {name=x5}
C {devices/lab_wire.sym} 150 340 0 0 {name=p7 sig_type=std_logic lab=VSS}
