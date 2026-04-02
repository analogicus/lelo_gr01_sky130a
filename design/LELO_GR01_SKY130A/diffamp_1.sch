v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
P 4 1 20 30 {}
P 4 1 -120 -290 {}
N 480 -570 560 -570 {lab=#net1}
N 440 -540 440 -460 {lab=#net1}
N 600 -540 600 -460 {lab=VOUT}
N 440 -500 520 -500 {lab=#net1}
N 520 -570 520 -500 {lab=#net1}
N 440 -620 440 -600 {lab=VDD_1V8}
N 600 -620 600 -600 {lab=VDD_1V8}
N 440 -600 440 -570 {lab=VDD_1V8}
N 600 -600 600 -570 {lab=VDD_1V8}
N 440 -400 440 -380 {lab=TAIL}
N 440 -380 600 -380 {lab=TAIL}
N 600 -400 600 -380 {lab=TAIL}
N 600 -430 600 -400 {lab=TAIL}
N 440 -430 440 -400 {lab=TAIL}
N 600 -500 750 -500 {lab=VOUT}
N 220 -430 400 -430 {lab=VIN}
N 220 -370 640 -370 {lab=VIP}
N 640 -430 640 -370 {lab=VIP}
N 520 -380 520 -280 {lab=TAIL}
N 390 -280 390 -250 {lab=#net2}
N 320 -250 390 -250 {lab=#net2}
N 390 -250 480 -250 {lab=#net2}
N 280 -250 280 -220 {lab=VSS}
N 280 -220 520 -220 {lab=VSS}
N 520 -250 520 -220 {lab=VSS}
N 390 -220 390 -190 {lab=VSS}
N 240 -290 280 -290 {lab=#net2}
N 280 -290 280 -280 {lab=#net2}
N 280 -290 390 -290 {lab=#net2}
N 390 -290 390 -280 {lab=#net2}
N 520 -650 520 -620 {lab=VDD_1V8}
N 440 -620 520 -620 {lab=VDD_1V8}
N 520 -620 600 -620 {lab=VDD_1V8}
N 220 -680 520 -680 {lab=VDD_1V8}
N 520 -680 520 -650 {lab=VDD_1V8}
N 10 -680 220 -680 {lab=VDD_1V8}
N 520 -320 690 -320 {lab=TAIL}
N 690 -320 760 -320 {lab=TAIL}
N 760 -320 760 -280 {lab=TAIL}
N 760 -250 760 -220 {lab=VSS}
N 520 -220 760 -220 {lab=VSS}
N 800 -250 820 -250 {lab=PWRUP_N_1V8}
C {cborder/border_xs.sym} 0 0 0 0 {
user="nikolai"
company="wulff"}
C {devices/ipin.sym} 10 -680 0 0 {name=p1 lab=VDD_1V8}
C {devices/ipin.sym} 220 -430 0 0 {name=p4 lab=VIN}
C {devices/ipin.sym} 220 -370 0 0 {name=p5 lab=VIP}
C {devices/opin.sym} 750 -500 0 0 {name=p6 lab=VOUT}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 400 -430 0 0 {name=x1 }
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 480 -570 0 1 {name=x2 }
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 560 -570 0 0 {name=x4 }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 640 -430 0 1 {name=x3 }
C {devices/lab_pin.sym} 520 -380 0 0 {name=p8 sig_type=std_logic lab=TAIL}
C {devices/lab_wire.sym} 60 -310 0 0 {name=p3 sig_type=std_logic lab=VDD_1V8}
C {LELO_GR01_SKY130A/GM_cell.sym} 210 -300 0 0 {name=x5}
C {devices/ipin.sym} 390 -190 0 0 {name=p2 lab=VSS}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 480 -250 0 0 {name=x6 }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 320 -250 0 1 {name=x7 }
C {devices/lab_wire.sym} 60 -270 0 0 {name=p7 sig_type=std_logic lab=VSS}
C {devices/ipin.sym} 10 -530 0 0 {name=p9 lab=PWRUP_1V8}
C {devices/ipin.sym} 10 -500 0 0 {name=p10 lab=PWRUP_N_1V8}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 800 -250 0 1 {name=x8 }
C {devices/lab_pin.sym} 820 -250 0 1 {name=p11 sig_type=std_logic lab=PWRUP_N_1V8}
