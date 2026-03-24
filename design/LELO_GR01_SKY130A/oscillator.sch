v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 1090 -290 1170 -290 {lab=VSS}
N 1090 -370 1170 -370 {lab=VDD_1V8}
N 1490 -330 1540 -330 {lab=#net1}
N 1590 -300 1590 -280 {lab=VSS}
N 1420 -300 1420 -280 {lab=VSS}
N 1420 -380 1420 -360 {lab=VDD_1V8}
N 1590 -380 1590 -360 {lab=VDD_1V8}
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
N 1800 -560 1800 -530 {lab=VDD_1V8}
N 1800 -410 1800 -370 {lab=VSS}
N 1840 -440 1890 -440 {lab=VOUT_OSC}
N 1890 -600 1890 -440 {lab=VOUT_OSC}
N 1710 -600 1890 -600 {lab=VOUT_OSC}
N 1710 -600 1710 -500 {lab=VOUT_OSC}
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
N 1660 -330 1680 -330 {lab=#net2}
N 1680 -330 1730 -330 {lab=#net2}
C {devices/ipin.sym} 350 -280 0 0 {name=p11 lab=VSS}
C {devices/ipin.sym} 350 -330 0 0 {name=p7 lab=VDD_1V8}
C {LELO_GR01_SKY130A/diffamp_2.sym} 1320 -330 0 0 {name=x1}
C {devices/lab_wire.sym} 1090 -290 0 0 {name=p6 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 1090 -370 0 0 {name=p2 sig_type=std_logic lab=VDD_1V8}
C {LELO_GR01_SKY130A/not_gate.sym} 1420 -330 0 0 {name=x2}
C {LELO_GR01_SKY130A/not_gate.sym} 1590 -330 0 0 {name=x3}
C {devices/lab_wire.sym} 1420 -380 0 1 {name=p1 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} 1590 -380 0 1 {name=p3 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} 1420 -280 2 0 {name=p5 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 1590 -280 2 0 {name=p8 sig_type=std_logic lab=VSS}
C {JNW_TR_SKY130A/JNWTR_CAPX1.sym} 790 -230 2 0 {name=xd1[4:0]}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 980 -200 0 1 {name=x4}
C {devices/lab_wire.sym} 790 -40 2 0 {name=p10 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 1090 -350 0 0 {name=p17 sig_type=std_logic lab=VREF_BG
}
C {JNW_TR_SKY130A/JNWTR_DFRNQNX1_CV.sym} 1740 -440 0 0 {name=x5 }
C {devices/lab_wire.sym} 1800 -560 0 1 {name=p13 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} 1800 -370 2 0 {name=p21 sig_type=std_logic lab=VSS}
C {devices/opin.sym} 2010 -440 0 0 {name=p22 lab=VOUT_OSC}
C {devices/lab_wire.sym} 1770 -340 2 0 {name=p24 sig_type=std_logic lab=VDD_1V8}
C {devices/ipin.sym} 350 -140 0 0 {name=p16 lab=VREF_BG}
C {devices/ipin.sym} 350 -180 0 0 {name=p14 lab=IBP_BG}
C {devices/lab_wire.sym} 790 -400 0 0 {name=p4 sig_type=std_logic lab=IBP_BG
}
