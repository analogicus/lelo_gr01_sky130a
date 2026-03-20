v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N -20 -20 50 -20 {lab=#net1}
N -60 -170 90 -170 {lab=VDD_1V8}
N 10 -230 10 -170 {lab=VDD_1V8}
N 90 10 90 70 {lab=#net1}
N 10 40 90 40 {lab=#net1}
N 10 -20 10 40 {lab=#net1}
N -60 10 -60 190 {lab=#net2}
N 90 130 90 160 {lab=#net3}
N 20 160 90 160 {lab=#net3}
N 20 160 20 220 {lab=#net3}
N -20 220 20 220 {lab=#net3}
N 90 250 90 260 {lab=#net4}
N 90 160 90 170 {lab=#net3}
N 70 300 70 340 {lab=VSS}
N 70 340 90 340 {lab=VSS}
N -60 250 -60 340 {lab=VSS}
N -60 340 70 340 {lab=VSS}
N 90 -50 90 -20 {lab=VDD_1V8}
N -60 -50 -60 -20 {lab=VDD_1V8}
N -60 100 50 100 {lab=#net2}
N 90 100 90 130 {lab=#net3}
N -340 -50 -340 -30 {lab=#net5}
N -340 -170 -60 -170 {lab=VDD_1V8}
N -340 50 -340 70 {lab=#net6}
N -340 60 -270 60 {lab=#net6}
N -270 60 -270 100 {lab=#net6}
N -300 100 -240 100 {lab=#net6}
N -340 130 -340 340 {lab=VSS}
N -340 340 -60 340 {lab=VSS}
N -340 100 -340 130 {lab=VSS}
N -200 100 -200 130 {lab=#net2}
N -200 130 -60 130 {lab=#net2}
N -200 -50 -200 70 {lab=VDD_1V8}
N -60 220 -60 250 {lab=VSS}
N -60 340 -60 380 {lab=VSS}
N -340 -170 -340 -130 {lab=VDD_1V8}
N -200 -170 -200 -50 {lab=VDD_1V8}
N -60 -170 -60 -50 {lab=VDD_1V8}
N 90 -170 90 -50 {lab=VDD_1V8}
N 70 210 70 300 {lab=VSS}
N 90 -170 260 -170 {lab=VDD_1V8}
N 260 -170 260 -50 {lab=VDD_1V8}
N 260 -50 260 -20 {lab=VDD_1V8}
N 260 10 260 40 {lab=IBP}
N 210 -20 220 -20 {lab=#net1}
N 90 40 170 40 {lab=#net1}
N 170 -20 170 40 {lab=#net1}
N 170 -20 210 -20 {lab=#net1}
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_4C5F0.sym} 50 -20 0 0 {name=x1 }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_4C5F0.sym} 50 100 0 0 {name=x2 }
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 90 260 1 0 {name=x3 }
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_4C5F0.sym} -20 -20 0 1 {name=x5 }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_4C5F0.sym} -20 220 0 1 {name=x6 }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_4C5F0.sym} -300 100 0 1 {name=x8 }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_4C5F0.sym} -240 100 0 0 {name=x9 }
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} -340 -30 1 0 {name=x10 }
C {devices/lab_wire.sym} -360 10 0 0 {name=p16 sig_type=std_logic lab=VSS}
C {devices/ipin.sym} -60 380 0 0 {name=p2 lab=VSS}
C {devices/ipin.sym} 10 -230 0 0 {name=p3 lab=VDD_1V8}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} -340 -130 1 0 {name=x11 }
C {devices/lab_wire.sym} -360 -90 0 0 {name=p4 sig_type=std_logic lab=VSS}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 90 170 1 0 {name=x4 }
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_4C5F0.sym} 220 -20 0 0 {name=x7[1:0]}
C {devices/opin.sym} 260 40 0 0 {name=p6 lab=IBP}
