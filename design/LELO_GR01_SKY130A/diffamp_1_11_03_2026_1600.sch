v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
P 4 1 20 30 {}
P 4 1 -120 -290 {}
N 310 -570 340 -570 {lab=VIP}
N 540 -570 570 -570 {lab=VIN}
N 200 -430 340 -430 {lab=#net1}
N 540 -430 680 -430 {lab=#net2}
N 160 -400 160 -360 {lab=VSS}
N 160 -340 380 -340 {lab=VSS}
N 380 -400 380 -360 {lab=VSS}
N 380 -340 500 -340 {lab=VSS}
N 500 -400 500 -360 {lab=VSS}
N 500 -340 720 -340 {lab=VSS}
N 720 -400 720 -360 {lab=VSS}
N 440 -340 440 -310 {lab=VSS}
N 500 -540 500 -460 {lab=#net2}
N 380 -540 380 -460 {lab=#net1}
N 380 -600 440 -600 {lab=#net3}
N 440 -600 500 -600 {lab=#net3}
N 160 -800 160 -460 {lab=#net4}
N 720 -800 720 -460 {lab=VOUT}
N 200 -830 680 -830 {lab=#net4}
N 240 -830 240 -780 {lab=#net4}
N 160 -780 240 -780 {lab=#net4}
N 720 -700 760 -700 {lab=VOUT}
N 720 -880 720 -860 {lab=VDD_1V8}
N 160 -920 720 -920 {lab=VDD_1V8}
N 160 -880 160 -860 {lab=VDD_1V8}
N 440 -960 440 -920 {lab=VDD_1V8}
N 720 -860 720 -830 {lab=VDD_1V8}
N 160 -860 160 -830 {lab=VDD_1V8}
N 380 -600 380 -570 {lab=#net3}
N 500 -600 500 -570 {lab=#net3}
N 500 -430 500 -400 {lab=VSS}
N 720 -430 720 -400 {lab=VSS}
N 160 -430 160 -400 {lab=VSS}
N 380 -430 380 -400 {lab=VSS}
N 560 -470 560 -430 {lab=#net2}
N 500 -470 560 -470 {lab=#net2}
N 320 -470 320 -430 {lab=#net1}
N 320 -470 380 -470 {lab=#net1}
N 720 -920 720 -880 {lab=VDD_1V8}
N 160 -920 160 -880 {lab=VDD_1V8}
N 720 -360 720 -340 {lab=VSS}
N 500 -360 500 -340 {lab=VSS}
N 380 -360 380 -340 {lab=VSS}
N 160 -360 160 -340 {lab=VSS}
N 630 -360 630 -340 {lab=VSS}
N 280 -360 280 -340 {lab=VSS}
N 280 -430 280 -420 {lab=#net1}
N 630 -430 630 -420 {lab=#net2}
N 630 -390 630 -360 {lab=VSS}
N 280 -390 280 -360 {lab=VSS}
N 590 -390 590 -370 {lab=PWRUP_N_1V8}
N 240 -370 590 -370 {lab=PWRUP_N_1V8}
N 240 -390 240 -370 {lab=PWRUP_N_1V8}
N 80 -370 240 -370 {lab=PWRUP_N_1V8}
N 440 -680 500 -680 {lab=#net5}
N 500 -750 500 -680 {lab=#net5}
N 490 -750 500 -750 {lab=#net5}
N 440 -620 440 -600 {lab=#net3}
N 220 -650 220 -370 {lab=PWRUP_N_1V8}
N 220 -650 400 -650 {lab=PWRUP_N_1V8}
N 440 -680 440 -650 {lab=#net5}
N 640 -750 720 -750 {lab=VOUT}
N 640 -810 640 -780 {lab=VDD_1V8}
N 640 -920 640 -810 {lab=VDD_1V8}
N 470 -850 470 -830 {lab=#net4}
N 470 -920 470 -910 {lab=VDD_1V8}
N 470 -910 470 -880 {lab=VDD_1V8}
N 370 -880 430 -880 {lab=PWRUP_1V8}
N 410 -880 410 -810 {lab=PWRUP_1V8}
N 410 -810 600 -810 {lab=PWRUP_1V8}
N 600 -810 600 -780 {lab=PWRUP_1V8}
C {cborder/border_xs.sym} 0 0 0 0 {
user="walterbr"
company="Walter"}
C {devices/ipin.sym} 440 -960 0 0 {name=p1 lab=VDD_1V8}
C {devices/ipin.sym} 310 -570 0 0 {name=p4 lab=VIP}
C {devices/ipin.sym} 570 -570 0 1 {name=p5 lab=VIN}
C {devices/opin.sym} 760 -700 0 0 {name=p6 lab=VOUT}
C {devices/lab_wire.sym} 310 -770 0 0 {name=p3 sig_type=std_logic lab=VDD_1V8}
C {LELO_GR01_SKY130A/GM_cell.sym} 460 -760 0 0 {name=x5}
C {devices/ipin.sym} 440 -310 0 0 {name=p2 lab=VSS}
C {devices/lab_wire.sym} 310 -730 0 0 {name=p7 sig_type=std_logic lab=VSS}
C {LELO_ATR_SKY130A/LELOATR_PCH_12C5F0.sym} 540 -570 0 1 {name=x2}
C {LELO_ATR_SKY130A/LELOATR_PCH_12C5F0.sym} 340 -570 0 0 {name=x3}
C {LELO_ATR_SKY130A/LELOATR_NCH_4C5F0.sym} 340 -430 0 0 {name=x4}
C {LELO_ATR_SKY130A/LELOATR_NCH_4C5F0.sym} 200 -430 0 1 {name=x6 }
C {LELO_ATR_SKY130A/LELOATR_NCH_4C5F0.sym} 540 -430 0 1 {name=x7}
C {LELO_ATR_SKY130A/LELOATR_NCH_4C5F0.sym} 680 -430 0 0 {name=x8 }
C {LELO_ATR_SKY130A/LELOATR_PCH_12C5F0.sym} 200 -830 0 1 {name=x11}
C {LELO_ATR_SKY130A/LELOATR_PCH_12C5F0.sym} 680 -830 0 0 {name=x10}
C {LELO_ATR_SKY130A/LELOATR_NCH_4C5F0.sym} 590 -390 0 0 {name=x1 }
C {LELO_ATR_SKY130A/LELOATR_NCH_4C5F0.sym} 240 -390 0 0 {name=x9 }
C {devices/ipin.sym} 80 -370 0 0 {name=p8 lab=PWRUP_N_1V8}
C {LELO_ATR_SKY130A/LELOATR_PCH_12C5F0.sym} 400 -650 0 0 {name=x12}
C {LELO_ATR_SKY130A/LELOATR_PCH_12C5F0.sym} 600 -780 0 0 {name=x13}
C {LELO_ATR_SKY130A/LELOATR_PCH_12C5F0.sym} 430 -880 0 0 {name=x14}
C {devices/ipin.sym} 370 -880 0 0 {name=p9 lab=PWRUP_1V8}
