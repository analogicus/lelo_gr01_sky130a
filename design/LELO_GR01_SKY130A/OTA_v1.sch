v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
P 4 1 210 50 {}
P 4 1 220 0 {}
P 4 1 210 -40 {}
N -20 -150 60 -150 {lab=#net1}
N 100 -120 100 -30 {lab=Vout}
N -60 -120 -60 -30 {lab=#net1}
N -60 30 -60 60 {lab=#net2}
N -60 60 20 60 {lab=#net2}
N 20 60 100 60 {lab=#net2}
N 100 30 100 60 {lab=#net2}
N 20 60 20 100 {lab=#net2}
N -60 -200 -60 -180 {lab=VDD_1V8}
N 100 -200 100 -180 {lab=VDD_1V8}
N 100 -150 120 -150 {lab=VDD_1V8}
N 120 -190 120 -150 {lab=VDD_1V8}
N 100 -190 120 -190 {lab=VDD_1V8}
N -80 -150 -60 -150 {lab=VDD_1V8}
N -80 -190 -80 -150 {lab=VDD_1V8}
N -80 -190 -60 -190 {lab=VDD_1V8}
N 80 -0 100 0 {lab=#net2}
N 80 -0 80 60 {lab=#net2}
N -60 0 -40 0 {lab=#net2}
N -40 0 -40 60 {lab=#net2}
N 100 -60 160 -60 {lab=Vout}
N -60 -200 20 -200 {lab=VDD_1V8}
N 20 -200 100 -200 {lab=VDD_1V8}
N 20 -260 20 -200 {lab=VDD_1V8}
N 160 -60 190 -60 {lab=Vout}
N 140 0 180 0 {lab=Vinn}
N -140 -0 -100 -0 {lab=Vinp}
N 20 100 20 120 {lab=#net2}
N 20 180 20 220 {lab=VSS}
N -240 150 -20 150 {lab=#net3}
N -280 180 -280 200 {lab=VSS}
N -280 200 20 200 {lab=VSS}
N -300 150 -280 150 {lab=VSS}
N -300 150 -300 200 {lab=VSS}
N -300 200 -280 200 {lab=VSS}
N 20 150 40 150 {lab=VSS}
N 40 150 40 190 {lab=VSS}
N 30 190 40 190 {lab=VSS}
N 20 190 30 190 {lab=VSS}
N -280 0 -280 120 {lab=#net3}
N -220 100 -220 150 {lab=#net3}
N -280 100 -220 100 {lab=#net3}
N -280 -240 -280 -80 {lab=VDD_1V8}
N -280 -240 20 -240 {lab=VDD_1V8}
N -10 -150 -10 -110 {lab=#net1}
N -60 -110 -10 -110 {lab=#net1}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 140 0 0 1 {name=x1 }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} -100 0 0 0 {name=x3 }
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 60 -150 0 0 {name=x2 }
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} -20 -150 0 1 {name=x4 }
C {devices/opin.sym} 190 -60 0 0 {name=p1 lab=Vout}
C {devices/ipin.sym} -140 0 0 0 {name=p2 lab=Vinp}
C {devices/ipin.sym} 180 0 0 1 {name=p3 lab=Vinn}
C {devices/ipin.sym} 20 220 0 0 {name=p4 lab=VSS}
C {devices/ipin.sym} 20 -260 0 0 {name=p5 lab=VDD_1V8}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} -20 150 0 0 {name=x5 }
C {devices/ipin.sym} -320 100 0 0 {name=p6 lab=PWRUP_1V8}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} -240 150 0 1 {name=x6 }
C {JNW_TR_SKY130A/JNWTR_RPPO2.sym} -280 0 3 0 {name=x7 }
