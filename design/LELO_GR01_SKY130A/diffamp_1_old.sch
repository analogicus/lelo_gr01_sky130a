v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
P 4 1 20 30 {}
P 4 1 -120 -290 {}
N 440 -600 440 -570 {lab=#net1}
N 440 -400 440 -380 {lab=TAIL}
N 440 -380 600 -380 {lab=TAIL}
N 600 -400 600 -380 {lab=TAIL}
N 600 -430 600 -400 {lab=TAIL}
N 440 -430 440 -400 {lab=TAIL}
N 780 -500 820 -500 {lab=VOUT}
N 370 -430 400 -430 {lab=VIN}
N 520 -380 520 -280 {lab=TAIL}
N -360 -340 -360 -310 {lab=VSS}
N 520 -250 520 -220 {lab=VSS}
N -400 -380 -360 -380 {lab=VBN1}
N -360 -380 -360 -370 {lab=VBN1}
N 520 -220 520 -180 {lab=VSS}
N -360 -310 -360 -280 {lab=VSS}
N -320 -380 -320 -340 {lab=VBN1}
N -360 -380 -320 -380 {lab=VBN1}
N 640 -430 670 -430 {lab=VIP}
N 520 -660 520 -600 {lab=#net1}
N 520 -600 600 -600 {lab=#net1}
N 440 -600 520 -600 {lab=#net1}
N 600 -600 600 -570 {lab=#net1}
N 440 -540 440 -460 {lab=#net2}
N 600 -540 600 -460 {lab=#net3}
N 260 -540 260 -280 {lab=VBN2}
N 300 -570 400 -570 {lab=#net2}
N 640 -570 740 -570 {lab=#net3}
N 780 -600 780 -570 {lab=#net1}
N 260 -600 260 -570 {lab=#net1}
N 780 -240 780 -210 {lab=VSS}
N 260 -250 260 -220 {lab=VSS}
N 780 -540 780 -270 {lab=VOUT}
N 260 -600 440 -600 {lab=#net1}
N 600 -600 780 -600 {lab=#net1}
N 380 -570 380 -510 {lab=#net2}
N 380 -510 440 -510 {lab=#net2}
N 600 -510 660 -510 {lab=#net3}
N 660 -570 660 -510 {lab=#net3}
N 260 -220 260 -200 {lab=VSS}
N 780 -210 780 -180 {lab=VSS}
N 300 -300 300 -250 {lab=VBN2}
N 260 -300 300 -300 {lab=VBN2}
N 450 -250 480 -250 {lab=VBN1}
N 700 -240 740 -240 {lab=VBN2}
C {cborder/border_xs.sym} 0 0 0 0 {
user="nikolai"
company="wulff"}
C {devices/ipin.sym} 510 -660 0 0 {name=p1 lab=VDD_1V8}
C {devices/ipin.sym} 370 -430 0 0 {name=p4 lab=VIN}
C {devices/ipin.sym} 670 -430 0 1 {name=p5 lab=VIP}
C {devices/opin.sym} 820 -500 0 0 {name=p6 lab=VOUT}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 400 -430 0 0 {name=x1 }
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 400 -570 0 0 {name=x2 }
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 640 -570 0 1 {name=x4 }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 640 -430 0 1 {name=x3 }
C {devices/lab_pin.sym} 520 -380 0 0 {name=p8 sig_type=std_logic lab=TAIL}
C {devices/lab_wire.sym} -580 -400 0 0 {name=p3 sig_type=std_logic lab=VDD_1V8}
C {LELO_GR01_SKY130A/GM_cell.sym} -430 -390 0 0 {name=x5}
C {devices/ipin.sym} 520 -180 0 0 {name=p2 lab=VSS}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 480 -250 0 0 {name=x6 }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} -320 -340 0 1 {name=x7[4:0] }
C {devices/lab_wire.sym} -580 -360 0 0 {name=p7 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} -360 -280 0 0 {name=p9 sig_type=std_logic lab=VSS}
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 300 -570 0 1 {name=x8[9:0] }
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 740 -570 0 0 {name=x9[9:0] }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 740 -240 0 0 {name=x10 }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 300 -250 0 1 {name=x11 }
C {devices/lab_pin.sym} -320 -380 0 1 {name=p10 sig_type=std_logic lab=VBN1}
C {devices/lab_pin.sym} 260 -200 0 0 {name=p11 sig_type=std_logic lab=VSS}
C {devices/lab_pin.sym} 780 -180 0 0 {name=p12 sig_type=std_logic lab=VSS}
C {devices/lab_pin.sym} 450 -250 0 0 {name=p13 sig_type=std_logic lab=VBN1}
C {devices/lab_pin.sym} 300 -300 0 1 {name=p14 sig_type=std_logic lab=VBN2}
C {devices/lab_pin.sym} 700 -240 0 0 {name=p15 sig_type=std_logic lab=VBN2}
