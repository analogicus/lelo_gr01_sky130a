v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
P 4 1 370 -960 {}
N 580 -240 720 -240 {lab=#net1}
N 540 -100 760 -100 {lab=VSS}
N 760 -210 760 -100 {lab=VSS}
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
N 740 -680 760 -680 {lab=#net3}
N 760 -680 760 -660 {lab=#net3}
N 760 -490 760 -460 {lab=#net4}
N 580 -430 650 -430 {lab=#net2}
N 540 -680 740 -680 {lab=#net3}
N 950 -410 950 -290 {lab=IBN}
N 650 -430 720 -430 {lab=#net2}
N 540 -380 600 -380 {lab=#net2}
N 540 -610 540 -580 {lab=#net3}
N 540 -680 540 -610 {lab=#net3}
N 540 -550 540 -460 {lab=#net3}
N 600 -380 630 -380 {lab=#net2}
N 630 -380 630 -370 {lab=#net2}
N 630 -430 630 -380 {lab=#net2}
N 630 -310 630 -240 {lab=#net1}
N 600 -180 630 -180 {lab=PWRUP_N_1V8}
N 540 -580 540 -550 {lab=#net3}
N 660 -730 660 -680 {lab=#net3}
N 590 -380 590 -340 {lab=#net2}
N 630 -340 630 -310 {lab=#net1}
N 760 -240 780 -240 {lab=VSS}
N 950 -240 970 -240 {lab=VSS}
N 540 -210 540 -100 {lab=VSS}
N 520 -240 540 -240 {lab=VSS}
N 670 -100 670 -30 {lab=VSS}
N 670 -150 670 -100 {lab=VSS}
N 670 -180 670 -150 {lab=VSS}
N 670 -240 670 -210 {lab=#net1}
N 590 -760 620 -760 {lab=PWRUP_N_1V8}
N 660 -790 660 -760 {lab=VDD_1V8}
N 660 -820 660 -790 {lab=VDD_1V8}
N 710 -530 740 -530 {lab=VSS}
N 760 -660 760 -580 {lab=#net3}
N 540 -460 540 -430 {lab=#net3}
N 760 -460 760 -430 {lab=#net4}
C {JNW_ATR_SKY130A/JNWATR_NCH_2C1F2.sym} 580 -240 0 1 {name=x1}
C {JNW_ATR_SKY130A/JNWATR_NCH_2C1F2.sym} 720 -240 0 0 {name=x2}
C {JNW_ATR_SKY130A/JNWATR_PCH_2C1F2.sym} 720 -430 0 0 {name=x4}
C {JNW_ATR_SKY130A/JNWATR_PCH_2C1F2.sym} 580 -430 0 1 {name=x3}
C {JNW_ATR_SKY130A/JNWATR_NCH_2C1F2.sym} 910 -240 0 0 {name=x5[5:0]}
C {JNW_TR_SKY130A/JNWTR_RPPO4.sym} 760 -570 1 0 {name=x6 }
C {devices/ipin.sym} 660 -820 0 0 {name=p2 lab=VDD_1V8}
C {devices/ipin.sym} 950 -410 0 0 {name=p3 lab=IBN}
C {devices/opin.sym} 670 -30 0 0 {name=p4 lab=VSS}
C {JNW_ATR_SKY130A/JNWATR_NCH_2C1F2.sym} 590 -340 0 0 {name=x7}
C {JNW_ATR_SKY130A/JNWATR_NCH_2C1F2.sym} 630 -180 0 0 {name=x8}
C {devices/lab_pin.sym} 520 -240 0 0 {name=p1 sig_type=std_logic lab=VSS}
C {devices/lab_pin.sym} 780 -240 0 1 {name=p5 sig_type=std_logic lab=VSS}
C {devices/lab_pin.sym} 960 -240 0 1 {name=p6 sig_type=std_logic lab=VSS}
C {devices/ipin.sym} 590 -760 0 0 {name=p7 lab=PWRUP_N_1V8}
C {JNW_ATR_SKY130A/JNWATR_PCH_2C1F2.sym} 620 -760 0 0 {name=x9}
C {devices/lab_pin.sym} 710 -530 0 0 {name=p10 sig_type=std_logic lab=VSS}
C {devices/ipin.sym} 280 -520 0 0 {name=p8 lab=PWRUP_1V8}
C {devices/lab_pin.sym} 600 -180 0 0 {name=p9 sig_type=std_logic lab=PWRUP_N_1V8}
