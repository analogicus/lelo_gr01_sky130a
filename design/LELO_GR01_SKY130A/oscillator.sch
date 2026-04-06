v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
P 4 1 1670 -590 {}
N 1090 -290 1170 -290 {lab=VSS}
N 1090 -370 1170 -370 {lab=VDD_1V8}
N 1490 -330 1540 -330 {lab=#net1}
N 1430 -280 1430 -260 {lab=VSS}
N 1430 -380 1430 -360 {lab=VDD_1V8}
N 790 -170 790 -70 {lab=VSS}
N 940 -170 940 -120 {lab=VSS}
N 790 -120 940 -120 {lab=VSS}
N 790 -70 790 -40 {lab=VSS}
N 1730 -330 1730 -200 {lab=#net2}
N 940 -200 940 -170 {lab=VSS}
N 790 -280 940 -280 {lab=IBP_BG}
N 940 -280 940 -230 {lab=IBP_BG}
N 790 -400 790 -240 {lab=IBP_BG}
N 1090 -310 1170 -310 {lab=IBP_BG}
N 1090 -350 1170 -350 {lab=VREF_BG}
N 790 -310 1090 -310 {lab=IBP_BG}
N 1800 -410 1800 -370 {lab=VSS}
N 1840 -440 1890 -440 {lab=VOUT_OSC}
N 1710 -500 1740 -500 {lab=VOUT_OSC}
N 1890 -440 2010 -440 {lab=VOUT_OSC}
N 1770 -410 1770 -340 {lab=VDD_1V8}
N 1350 -330 1370 -330 {lab=#net3}
N 1730 -440 1740 -440 {lab=#net2}
N 1440 -200 1490 -200 {lab=#net2}
N 1300 -200 1320 -200 {lab=#net2}
N 1610 -200 1730 -200 {lab=#net2}
N 990 -200 1300 -200 {lab=#net2}
N 980 -200 990 -200 {lab=#net2}
N 1490 -200 1610 -200 {lab=#net2}
N 1320 -200 1440 -200 {lab=#net2}
N 1730 -440 1730 -330 {lab=#net2}
N 550 -200 550 -120 {lab=VSS}
N 550 -120 790 -120 {lab=VSS}
N 550 -280 550 -230 {lab=IBP_BG}
N 550 -280 790 -280 {lab=IBP_BG}
N 1250 -260 1250 -240 {lab=PWRUP_1V8}
N 1270 -260 1270 -240 {lab=PWRUP_N_1V8}
N 490 -200 510 -200 {lab=PWRUP_N_1V8}
N 1370 -330 1390 -330 {lab=#net3}
N 1480 -330 1480 -320 {lab=#net1}
N 1480 -330 1490 -330 {lab=#net1}
N 1600 -280 1600 -260 {lab=VSS}
N 1600 -380 1600 -360 {lab=VDD_1V8}
N 1540 -330 1560 -330 {lab=#net1}
N 1650 -320 1730 -320 {lab=#net2}
N 1390 -330 1390 -320 {lab=#net3}
N 1470 -320 1480 -320 {lab=#net1}
N 1560 -330 1560 -320 {lab=#net1}
N 1640 -320 1650 -320 {lab=#net2}
N 1350 -330 1350 -300 {lab=#net3}
N 1350 -270 1350 -120 {lab=VSS}
N 940 -120 1350 -120 {lab=VSS}
N 1800 -550 1800 -530 {lab=#net4}
N 1800 -620 1800 -580 {lab=VDD_1V8}
N 1720 -580 1760 -580 {lab=PWRUP_N_1V8}
C {devices/ipin.sym} 350 -280 0 0 {name=p11 lab=VSS}
C {devices/ipin.sym} 350 -330 0 0 {name=p7 lab=VDD_1V8}
C {LELO_GR01_SKY130A/diffamp_2.sym} 1320 -330 0 0 {name=x1}
C {devices/lab_wire.sym} 1090 -290 0 0 {name=p6 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 1090 -370 0 0 {name=p2 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} 1430 -380 0 1 {name=p1 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} 1430 -260 2 0 {name=p5 sig_type=std_logic lab=VSS}
C {JNW_TR_SKY130A/JNWTR_CAPX1.sym} 790 -230 2 0 {name=xd1[4:0]}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 980 -200 0 1 {name=x4}
C {devices/lab_wire.sym} 790 -40 2 0 {name=p10 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 1090 -350 0 0 {name=p17 sig_type=std_logic lab=VREF_BG
}
C {JNW_TR_SKY130A/JNWTR_DFRNQNX1_CV.sym} 1740 -440 0 0 {name=x5 }
C {devices/lab_wire.sym} 1800 -620 0 1 {name=p13 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} 1800 -370 2 0 {name=p21 sig_type=std_logic lab=VSS}
C {devices/opin.sym} 2010 -440 0 0 {name=p22 lab=VOUT_OSC}
C {devices/lab_wire.sym} 1770 -340 2 0 {name=p24 sig_type=std_logic lab=VDD_1V8}
C {devices/ipin.sym} 350 -190 0 0 {name=p16 lab=VREF_BG}
C {devices/ipin.sym} 350 -230 0 0 {name=p14 lab=IBP_BG}
C {devices/lab_wire.sym} 790 -400 0 0 {name=p4 sig_type=std_logic lab=IBP_BG
}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 510 -200 0 0 {name=x6}
C {devices/ipin.sym} 1250 -240 3 0 {name=p9 lab=PWRUP_1V8}
C {devices/ipin.sym} 1270 -240 3 0 {name=p12 lab=PWRUP_N_1V8}
C {devices/lab_wire.sym} 490 -200 2 1 {name=p15 sig_type=std_logic lab=PWRUP_N_1V8}
C {devices/lab_wire.sym} 1600 -380 0 1 {name=p3 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} 1600 -260 2 0 {name=p8 sig_type=std_logic lab=VSS}
C {JNW_TR_SKY130A/JNWTR_IVX1_CV.sym} 1390 -320 0 0 {name=x2 }
C {JNW_TR_SKY130A/JNWTR_IVX1_CV.sym} 1560 -320 0 0 {name=x3 }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 1390 -270 0 1 {name=x7}
C {devices/lab_wire.sym} 1390 -270 2 0 {name=p18 sig_type=std_logic lab=PWRUP_N_1V8}
C {devices/lab_wire.sym} 1710 -500 0 0 {name=p19 sig_type=std_logic lab=VOUT_OSC}
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 1760 -580 0 0 {name=x8}
C {devices/lab_wire.sym} 1720 -580 0 0 {name=p20 sig_type=std_logic lab=PWRUP_N_1V8}
