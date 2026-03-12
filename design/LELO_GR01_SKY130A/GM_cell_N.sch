v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
P 4 1 370 -960 {}
N 580 -240 720 -240 {lab=#net1}
N 540 -240 540 -100 {lab=VSS}
N 540 -100 760 -100 {lab=VSS}
N 760 -210 760 -100 {lab=VSS}
N 760 -240 760 -210 {lab=VSS}
N 650 -320 650 -240 {lab=#net1}
N 650 -320 760 -320 {lab=#net1}
N 760 -320 760 -270 {lab=#net1}
N 760 -400 760 -320 {lab=#net1}
N 540 -400 540 -270 {lab=#net2}
N 760 -100 950 -100 {lab=VSS}
N 950 -210 950 -100 {lab=VSS}
N 950 -290 950 -270 {lab=IBN}
N 880 -240 910 -240 {lab=#net1}
N 880 -320 880 -240 {lab=#net1}
N 760 -320 880 -320 {lab=#net1}
N 760 -580 760 -570 {lab=#net3}
N 740 -620 740 -530 {lab=VDD_1V8}
N 740 -680 740 -620 {lab=VDD_1V8}
N 740 -680 760 -680 {lab=VDD_1V8}
N 760 -680 760 -660 {lab=VDD_1V8}
N 760 -490 760 -460 {lab=#net4}
N 580 -430 650 -430 {lab=#net4}
N 650 -480 650 -430 {lab=#net4}
N 650 -480 760 -480 {lab=#net4}
N 540 -460 540 -430 {lab=VDD_1V8}
N 540 -680 540 -460 {lab=VDD_1V8}
N 540 -680 740 -680 {lab=VDD_1V8}
N 380 -360 380 -330 {lab=#net2}
N 380 -280 380 -100 {lab=VSS}
N 380 -100 540 -100 {lab=VSS}
N 290 -330 340 -330 {lab=#net5}
N 250 -100 380 -100 {lab=VSS}
N 250 -360 250 -330 {lab=VDD_1V8}
N 250 -210 250 -190 {lab=#net6}
N 250 -300 250 -290 {lab=#net5}
N 250 -110 250 -100 {lab=VSS}
N 380 -300 380 -280 {lab=VSS}
N 250 -300 310 -300 {lab=#net5}
N 310 -330 310 -300 {lab=#net5}
N 380 -680 540 -680 {lab=VDD_1V8}
N 250 -680 250 -360 {lab=VDD_1V8}
N 250 -680 380 -680 {lab=VDD_1V8}
N 640 -770 650 -770 {lab=VDD_1V8}
N 650 -770 650 -680 {lab=VDD_1V8}
N 950 -410 950 -290 {lab=IBN}
N 950 -240 950 -210 {lab=VSS}
N 760 -460 760 -430 {lab=#net4}
N 720 -430 720 -380 {lab=#net2}
N 540 -380 720 -380 {lab=#net2}
N 650 -50 660 -50 {lab=VSS}
N 650 -100 650 -50 {lab=VSS}
N 380 -360 540 -360 {lab=#net2}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_4C5F0.sym} 580 -240 0 1 {name=x1}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_4C5F0.sym} 720 -240 0 0 {name=x2}
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_4C5F0.sym} 720 -430 0 0 {name=x4}
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_4C5F0.sym} 580 -430 0 1 {name=x3}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_4C5F0.sym} 910 -240 0 0 {name=x5[3:0]}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 760 -570 1 0 {name=x6 }
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 760 -660 1 0 {name=x7 }
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_4C5F0.sym} 290 -330 0 1 {name=x8}
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_4C5F0.sym} 340 -330 0 0 {name=x9}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 250 -190 1 0 {name=x10 }
C {devices/lab_wire.sym} 230 -150 0 0 {name=p1 sig_type=std_logic lab=VSS}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 250 -290 1 0 {name=x11 }
C {devices/lab_wire.sym} 230 -250 0 0 {name=p5 sig_type=std_logic lab=VSS}
C {devices/ipin.sym} 640 -770 0 0 {name=p2 lab=VDD_1V8}
C {devices/ipin.sym} 950 -410 0 0 {name=p3 lab=IBN}
C {devices/opin.sym} 660 -50 0 0 {name=p4 lab=VSS}
