v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N -20 -140 50 -140 {lab=#net1}
N -60 -170 90 -170 {lab=#net2}
N 10 -230 10 -170 {lab=#net2}
N 90 -110 90 -50 {lab=#net1}
N 10 -80 90 -80 {lab=#net1}
N 10 -140 10 -80 {lab=#net1}
N -60 -110 -60 70 {lab=#net3}
N 90 10 90 40 {lab=#net4}
N 20 40 90 40 {lab=#net4}
N 20 40 20 100 {lab=#net4}
N -20 100 20 100 {lab=#net4}
N 90 130 90 140 {lab=#net5}
N 90 40 90 50 {lab=#net4}
N 70 90 70 180 {lab=VSS}
N 70 180 70 220 {lab=VSS}
N 70 220 90 220 {lab=VSS}
N -60 130 -60 220 {lab=VSS}
N -60 220 70 220 {lab=VSS}
N 90 -80 210 -80 {lab=#net1}
N 210 -140 210 -80 {lab=#net1}
N 210 -140 240 -140 {lab=#net1}
N 90 -170 280 -170 {lab=#net2}
N 280 -170 280 -140 {lab=#net2}
N 90 -170 90 -140 {lab=#net2}
N -60 -170 -60 -140 {lab=#net2}
N -60 -20 50 -20 {lab=#net3}
N 90 -20 90 10 {lab=#net4}
N 280 -110 280 -60 {lab=IBP}
N -340 -170 -340 -150 {lab=#net2}
N -340 -170 -60 -170 {lab=#net2}
N -340 -70 -340 -50 {lab=#net6}
N -340 -60 -270 -60 {lab=#net6}
N -270 -60 -270 -20 {lab=#net6}
N -300 -20 -240 -20 {lab=#net6}
N -340 10 -340 220 {lab=VSS}
N -340 220 -60 220 {lab=VSS}
N -340 -20 -340 10 {lab=VSS}
N -200 -20 -200 10 {lab=#net3}
N -200 10 -60 10 {lab=#net3}
N -200 -170 -200 -50 {lab=#net2}
N -60 100 -60 130 {lab=VSS}
N -60 220 -60 260 {lab=VSS}
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 50 -140 0 0 {name=x1 }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 50 -20 0 0 {name=x2 }
C {JNW_TR_SKY130A/JNWTR_RPPO8.sym} 90 140 1 0 {name=x3 }
C {JNW_TR_SKY130A/JNWTR_RPPO4.sym} 90 50 1 0 {name=x4 }
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} -20 -140 0 1 {name=x5 }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} -20 100 0 1 {name=x6 }
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 240 -140 0 0 {name=x7 }
C {devices/opin.sym} 280 -60 0 0 {name=p1 lab=IBP}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} -300 -20 0 1 {name=x8 }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} -240 -20 0 0 {name=x9 }
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} -340 -150 1 0 {name=x10 }
C {devices/lab_wire.sym} -360 -110 0 0 {name=p16 sig_type=std_logic lab=VSS}
C {devices/ipin.sym} -60 260 0 0 {name=p2 lab=VSS}
C {devices/ipin.sym} 10 -230 0 0 {name=p3 lab=VDD_1V8}
