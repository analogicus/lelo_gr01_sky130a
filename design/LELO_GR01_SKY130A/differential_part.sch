v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N -370 -300 -370 -200 {lab=#net1}
N -170 -300 -170 -200 {lab=VOUT}
N -330 -330 -210 -330 {lab=#net1}
N -280 -330 -280 -270 {lab=#net1}
N -370 -270 -280 -270 {lab=#net1}
N -370 -140 -370 -90 {lab=#net2}
N -370 -80 -270 -80 {lab=#net2}
N -370 -90 -370 -80 {lab=#net2}
N -170 -140 -170 -80 {lab=#net2}
N -270 -80 -170 -80 {lab=#net2}
N -430 -170 -410 -170 {lab=VIN}
N -130 -170 -100 -170 {lab=VIP}
N -440 -410 -170 -410 {lab=VDD_1V8}
N -370 -410 -370 -360 {lab=VDD_1V8}
N -170 -410 -170 -360 {lab=VDD_1V8}
N -430 20 -270 20 {lab=VSS}
N -270 -20 -270 20 {lab=VSS}
N -370 -170 -170 -170 {lab=#net2}
N -170 -330 -140 -330 {lab=VDD_1V8}
N -140 -410 -140 -330 {lab=VDD_1V8}
N -170 -410 -140 -410 {lab=VDD_1V8}
N -170 -240 -110 -240 {lab=VOUT}
N -330 -170 -330 -80 {lab=#net2}
C {devices/ipin.sym} -430 -170 0 0 {name=p1 lab=VIN}
C {devices/ipin.sym} -100 -170 0 1 {name=p2 lab=VIP
}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} -410 -170 0 0 {name=x1 }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} -130 -170 0 1 {name=x2 }
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} -210 -330 0 0 {name=x3 }
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} -330 -330 0 1 {name=x4 }
C {sky130_fd_pr/res_xhigh_po_0p35.sym} -270 -50 0 0 {name=R1
L=0.35
model=res_xhigh_po_0p35
spiceprefix=X
mult=1}
C {devices/ipin.sym} -430 20 0 0 {name=p3 lab=VSS}
C {devices/ipin.sym} -440 -410 0 0 {name=p4 lab=VDD_1V8}
C {devices/opin.sym} -110 -240 0 0 {name=p5 lab=VOUT}
