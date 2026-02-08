v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 820 -680 840 -680 {lab=OSC_TEMP_1V8}
N 100 -100 380 -100 {lab=VSS}
N 380 -100 500 -100 {lab=VSS}
N 540 -200 640 -200 {lab=VR1}
N 490 -740 490 -660 {lab=#net1}
N 490 -740 600 -740 {lab=#net1}
N 380 -740 490 -740 {lab=#net1}
N 340 -790 340 -770 {lab=VDD_1V8}
N 340 -820 640 -820 {lab=VDD_1V8}
N 640 -790 640 -770 {lab=VDD_1V8}
N 640 -740 660 -740 {lab=VDD_1V8}
N 660 -780 660 -740 {lab=VDD_1V8}
N 640 -780 660 -780 {lab=VDD_1V8}
N 320 -740 340 -740 {lab=VDD_1V8}
N 320 -780 320 -740 {lab=VDD_1V8}
N 320 -780 340 -780 {lab=VDD_1V8}
N 480 -850 480 -820 {lab=VDD_1V8}
N 640 -710 640 -260 {lab=VD1}
N 340 -710 340 -200 {lab=VR2}
N 340 -200 450 -200 {lab=VR2}
N 460 -360 460 -320 {lab=VR2}
N 340 -320 460 -320 {lab=VR2}
N 510 -360 510 -320 {lab=VD1}
N 510 -320 640 -320 {lab=VD1}
N 560 -510 580 -510 {lab=VSS}
N 400 -510 420 -510 {lab=VDD_1V8}
N 310 -430 420 -430 {lab=PWRUP_1V8}
N 590 -740 590 -730 {lab=#net1}
N 590 -730 780 -730 {lab=#net1}
N 780 -740 780 -730 {lab=#net1}
N 640 -820 820 -820 {lab=VDD_1V8}
N 820 -790 820 -770 {lab=VDD_1V8}
N 820 -740 840 -740 {lab=VDD_1V8}
N 840 -780 840 -740 {lab=VDD_1V8}
N 820 -780 840 -780 {lab=VDD_1V8}
N 820 -710 820 -680 {lab=OSC_TEMP_1V8}
N 640 -320 680 -320 {lab=VD1}
N 820 -620 820 -590 {lab=VSS}
N 770 -650 800 -650 {lab=VSS}
N 590 -230 620 -230 {lab=VSS}
N 200 -370 200 -330 {lab=VS2}
N 200 -700 420 -700 {lab=#net1}
N 160 -350 160 -300 {lab=VS2}
N 160 -350 200 -350 {lab=VS2}
N 40 -400 60 -400 {lab=PWRUP_1V8}
N 200 -700 200 -430 {lab=#net1}
N 150 -200 200 -200 {lab=VDD_1V8}
N 60 -400 160 -400 {lab=PWRUP_1V8}
N 200 -300 240 -300 {lab=VSS}
N 200 -400 240 -400 {lab=VSS}
N 240 -200 280 -200 {lab=VR1}
N 200 -270 200 -230 {lab=#net2}
N 200 -170 200 -100 {lab=VSS}
N 420 -740 420 -700 {lab=#net1}
N 340 -820 340 -790 {lab=VDD_1V8}
N 640 -820 640 -790 {lab=VDD_1V8}
N 820 -820 820 -790 {lab=VDD_1V8}
N 530 -750 530 -740 {lab=#net1}
C {cborder/border_xs.sym} 0 0 0 0 {
user="walterbr"
company="walterbr"}
C {devices/ipin.sym} 480 -850 0 0 {name=p1 lab=VDD_1V8}
C {devices/ipin.sym} 100 -100 0 0 {name=p2 lab=VSS}
C {devices/opin.sym} 840 -680 0 0 {name=p29 lab=OSC_TEMP_1V8}
C {LELO_GR01_SKY130A/OTA.sym} 490 -510 3 0 {name=x1}
C {LELO_GR01_SKY130A/Diodes.sym} 440 -150 0 0 {name=x2}
C {sky130_fd_pr/res_high_po.sym} 640 -230 0 0 {name=R1
W=1
L=200
model=res_high_po
spiceprefix=X
mult=1}
C {JNW_ATR_SKY130A/JNWATR_PCH_12C5F0.sym} 600 -740 0 0 {name=x3 }
C {JNW_ATR_SKY130A/JNWATR_PCH_12C5F0.sym} 380 -740 0 1 {name=x4[7:0]}
C {devices/lab_pin.sym} 580 -510 0 1 {name=p4 sig_type=std_logic lab=VSS}
C {devices/lab_pin.sym} 400 -510 3 1 {name=p5 sig_type=std_logic lab=VDD_1V8}
C {JNW_ATR_SKY130A/JNWATR_PCH_12C5F0.sym} 780 -740 0 0 {name=x5}
C {sky130_fd_pr/res_high_po.sym} 820 -650 0 0 {name=R2
W=1
L=100
model=res_high_po
spiceprefix=X
mult=1}
C {devices/lab_pin.sym} 820 -590 0 1 {name=p7 sig_type=std_logic lab=VSS}
C {devices/lab_pin.sym} 770 -650 0 0 {name=p8 sig_type=std_logic lab=VSS}
C {devices/lab_pin.sym} 590 -230 0 0 {name=p9 sig_type=std_logic lab=VSS}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 160 -400 0 0 {name=xg3[3:0]}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 160 -300 0 0 {name=xg2[3:0]}
C {devices/ipin.sym} 40 -400 0 0 {name=p10 lab=PWRUP_1V8}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 240 -200 0 1 {name=xc1[3:0]}
C {devices/ipin.sym} 160 -530 0 0 {name=p11 lab=PWRUP_N_1V8}
C {devices/lab_pin.sym} 160 -350 0 0 {name=l6 sig_type=std_logic lab=VS2}
C {devices/lab_pin.sym} 150 -200 0 0 {name=l8 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_pin.sym} 240 -400 0 1 {name=l9 sig_type=std_logic lab=VSS}
C {devices/lab_pin.sym} 240 -300 0 1 {name=l12 sig_type=std_logic lab=VSS}
C {devices/lab_pin.sym} 280 -200 0 1 {name=l13 sig_type=std_logic lab=VR1}
C {devices/lab_pin.sym} 680 -320 0 1 {name=p6 sig_type=std_logic lab=VD1}
C {devices/lab_pin.sym} 340 -320 0 0 {name=p12 sig_type=std_logic lab=VR2}
C {devices/lab_pin.sym} 310 -430 0 0 {name=p3 sig_type=std_logic lab=PWRUP_1V8}
C {JNW_TR_SKY130A/JNWTR_CAPX1.sym} 530 -760 0 0 {name=x4 }
C {devices/lab_pin.sym} 620 -200 3 0 {name=p13 sig_type=std_logic lab=VR1}
