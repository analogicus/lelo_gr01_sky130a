v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {VR1}
E {}
L 4 20 440 160 440 {}
L 4 160 440 160 620 {}
L 4 20 620 160 620 {}
L 4 20 440 20 620 {}
P 4 1 60 -60 {}
P 4 1 -130 -150 {}
P 4 1 -80 420 {}
P 4 1 -290 700 {}
N 0 0 0 90 {lab=VOUT}
N -90 420 -90 630 {lab=VIP}
N -90 30 -90 420 {lab=VIP}
N -90 -30 -90 0 {lab=VDD_1V8}
N 0 -120 0 -100 {lab=VDD_1V8}
N -90 -50 -90 -30 {lab=VDD_1V8}
N -40 270 -40 310 {lab=VDD_1V8}
N -90 420 -20 420 {lab=VIP}
N 0 730 0 760 {lab=VSS}
N -50 0 50 0 {lab=VOUT}
N 90 -50 90 -30 {lab=VDD_1V8}
N -90 -70 90 -70 {lab=VDD_1V8}
N 90 -70 90 -50 {lab=VDD_1V8}
N -90 -70 -90 -50 {lab=VDD_1V8}
N -0 -100 -0 -70 {lab=VDD_1V8}
N -0 660 -0 730 {lab=VSS}
N -50 690 -0 690 {lab=VSS}
N -0 690 50 690 {lab=VSS}
N 90 420 90 450 {lab=VIN}
N 20 420 90 420 {lab=VIN}
N 70 490 70 580 {lab=VSS}
N 90 530 90 540 {lab=#net1}
N 90 -30 90 -0 {lab=VDD_1V8}
N -250 70 -250 110 {lab=VOUT}
N -250 70 0 70 {lab=VOUT}
N -250 140 -200 140 {lab=VSS}
N -250 220 -200 220 {lab=VSS}
N -250 170 -250 190 {lab=VS1}
N -290 190 -250 190 {lab=VS1}
N -290 190 -290 220 {lab=VS1}
N -210 310 -170 310 {lab=VIP}
N -310 310 -250 310 {lab=VDD_1V8}
N -250 250 -250 280 {lab=#net2}
N -250 340 -250 360 {lab=VSS}
N -50 660 -30 660 {lab=VSS}
N -20 270 -20 330 {lab=VIP}
N 20 270 20 330 {lab=VIN}
N 90 620 90 630 {lab=VR1}
N 90 -70 250 -70 {lab=VDD_1V8}
N 450 -30 450 0 {lab=VDD_1V8}
N 380 0 410 0 {lab=VOUT}
N 450 30 450 60 {lab=VREF}
N 450 60 490 60 {lab=VREF}
N 450 150 450 160 {lab=#net3}
N 450 240 450 250 {lab=#net4}
N 50 690 250 690 {lab=VSS}
N 410 660 410 690 {lab=VSS}
N 430 110 430 290 {lab=VSS}
N 450 330 450 340 {lab=#net5}
N 430 290 430 380 {lab=VSS}
N -20 330 -20 420 {lab=VIP}
N 20 330 20 420 {lab=VIN}
N 90 30 90 70 {lab=VIN}
N 90 70 90 100 {lab=VIN}
N 90 130 90 370 {lab=VIN}
N 90 370 90 420 {lab=VIN}
N 250 -70 440 -70 {lab=VDD_1V8}
N 250 690 450 690 {lab=VSS}
N 450 -70 450 -30 {lab=VDD_1V8}
N 440 -70 450 -70 {lab=VDD_1V8}
N 90 100 90 130 {lab=VIN}
N -90 690 -50 690 {lab=VSS}
N -30 660 -0 660 {lab=VSS}
N 0 660 50 660 {lab=VSS}
N 450 420 450 430 {lab=#net6}
N 430 380 430 470 {lab=VSS}
N 450 600 450 630 {lab=#net7}
N 450 510 450 520 {lab=#net8}
N 430 470 430 560 {lab=VSS}
N 450 60 450 70 {lab=VREF}
N 390 520 450 520 {lab=#net8}
N 390 600 450 600 {lab=#net7}
N 360 560 370 560 {lab=VSS}
N 450 -70 710 -70 {lab=VDD_1V8}
N 710 -70 710 -20 {lab=VDD_1V8}
N 710 -20 710 10 {lab=VDD_1V8}
N 640 10 670 10 {lab=VOUT}
N 710 40 710 60 {lab=IPTAT}
N 710 60 760 60 {lab=IPTAT}
N 30 450 30 610 {lab=VR1}
N 30 610 30 620 {lab=VR1}
N 30 620 90 620 {lab=VR1}
C {devices/lab_wire.sym} -40 310 0 0 {name=p2 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} 40 270 3 0 {name=p6 sig_type=std_logic lab=VSS}
C {devices/ipin.sym} 0 -120 0 0 {name=p7 lab=VDD_1V8}
C {devices/ipin.sym} 0 760 0 0 {name=p11 lab=VSS}
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 50 0 0 0 {name=x5}
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} -50 0 0 1 {name=x3[7:0]}
C {JNW_TR_SKY130A/JNWTR_CAPX1.sym} 0 -60 2 1 {name=xd1[4:0]}
C {sky130_fd_pr/pnp_05v5.sym} -70 660 0 1 {name=Q2
model=pnp_05v5_W3p40L3p40
m=1
spiceprefix=X
}
C {sky130_fd_pr/pnp_05v5.sym} 70 660 0 0 {name=Q1[7:0]
model=pnp_05v5_W3p40L3p40
m=1
spiceprefix=X
}
C {devices/lab_wire.sym} 90 370 2 0 {name=p3 sig_type=std_logic lab=VIN}
C {devices/lab_wire.sym} -90 370 2 0 {name=p5 sig_type=std_logic lab=VIP
}
C {JNW_TR_SKY130A/JNWTR_RPPO8.sym} 90 450 1 0 {name=x2 }
C {JNW_TR_SKY130A/JNWTR_RPPO4.sym} 90 540 1 0 {name=x3 }
C {devices/lab_wire.sym} 70 540 0 0 {name=p14 sig_type=std_logic lab=VSS}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} -290 140 0 0 {name=x4[3:0]}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} -290 220 0 0 {name=x6[3:0]}
C {devices/ipin.sym} -460 360 0 0 {name=p15 lab=PWRUP_1V8}
C {devices/lab_wire.sym} -200 140 0 0 {name=p17 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} -200 220 0 0 {name=p18 sig_type=std_logic lab=VSS}
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} -210 310 0 1 {name=x7}
C {devices/lab_wire.sym} -170 310 0 0 {name=p19 sig_type=std_logic lab=VIP
}
C {devices/lab_wire.sym} -310 310 0 0 {name=p20 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} -250 360 0 0 {name=p21 sig_type=std_logic lab=VSS}
C {devices/opin.sym} 760 60 0 0 {name=p23 lab=IPTAT}
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 410 0 0 0 {name=x8}
C {devices/lab_wire.sym} 380 0 0 0 {name=p16 sig_type=std_logic lab=VOUT}
C {devices/opin.sym} 490 60 0 0 {name=p24 lab=VREF}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 450 70 1 0 {name=x9}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 450 160 1 0 {name=x10 }
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 450 250 1 0 {name=x11 }
C {sky130_fd_pr/pnp_05v5.sym} 430 660 0 0 {name=Q1
model=pnp_05v5_W3p40L3p40
m=1
spiceprefix=X
}
C {devices/lab_wire.sym} 430 170 0 0 {name=p25 sig_type=std_logic lab=VSS}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 450 340 1 0 {name=x12 }
C {LELO_GR01_SKY130A/diffamp_1.sym} 0 120 3 0 {name=x1}
C {devices/lab_wire.sym} 0 50 0 0 {name=p9 sig_type=std_logic lab=VOUT}
C {devices/lab_wire.sym} -290 190 0 0 {name=p26 sig_type=std_logic lab=VS1}
C {JNW_TR_SKY130A/JNWTR_RPPO4.sym} 450 430 1 0 {name=x4 }
C {JNW_TR_SKY130A/JNWTR_RPPO8.sym} 450 520 1 0 {name=x6}
C {JNW_TR_SKY130A/JNWTR_RPPO4.sym} 390 520 1 0 {name=x13[1:0]}
C {devices/lab_wire.sym} 360 560 0 0 {name=p4 sig_type=std_logic lab=VSS}
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 670 10 0 0 {name=x13}
C {devices/lab_wire.sym} 640 10 0 0 {name=p8 sig_type=std_logic lab=VOUT}
C {devices/lab_wire.sym} 30 450 2 0 {name=p1 sig_type=std_logic lab=VR1}
