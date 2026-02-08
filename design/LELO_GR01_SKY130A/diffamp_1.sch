v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
P 4 1 20 30 {}
N 480 -570 560 -570 {lab=#net1}
N 440 -540 440 -460 {lab=#net1}
N 600 -540 600 -460 {lab=VOUT}
N 440 -500 520 -500 {lab=#net1}
N 520 -570 520 -500 {lab=#net1}
N 440 -620 440 -600 {lab=VDD_1V8}
N 440 -620 600 -620 {lab=VDD_1V8}
N 600 -620 600 -600 {lab=VDD_1V8}
N 220 -620 440 -620 {lab=VDD_1V8}
N 440 -600 440 -570 {lab=VDD_1V8}
N 600 -600 600 -570 {lab=VDD_1V8}
N 440 -400 440 -380 {lab=tail}
N 440 -380 600 -380 {lab=tail}
N 600 -400 600 -380 {lab=tail}
N 600 -430 600 -400 {lab=tail}
N 440 -430 440 -400 {lab=tail}
N 520 -380 520 -340 {lab=tail}
N 600 -500 750 -500 {lab=VOUT}
N 220 -430 400 -430 {lab=VIN}
N 220 -370 640 -370 {lab=VIP}
N 640 -430 640 -370 {lab=VIP}
N 520 -280 520 -260 {lab=VSS}
N 520 -310 520 -280 {lab=VSS}
N 220 -220 520 -220 {lab=VSS}
N 520 -260 520 -220 {lab=VSS}
N 220 -340 310 -340 {lab=IB}
N 310 -340 400 -340 {lab=IB}
N 400 -340 400 -310 {lab=IB}
N 400 -310 480 -310 {lab=IB}
N 350 -310 400 -310 {lab=IB}
N 310 -310 310 -220 {lab=VSS}
N 140 -340 220 -340 {lab=IB}
C {cborder/border_xs.sym} 0 0 0 0 {
user="nikolai"
company="wulff"}
C {devices/ipin.sym} 220 -220 0 0 {name=p2 lab=VSS}
C {devices/ipin.sym} 220 -620 0 0 {name=p1 lab=VDD_1V8}
C {devices/ipin.sym} 140 -340 0 0 {name=p3 lab=IB}
C {devices/ipin.sym} 220 -430 0 0 {name=p4 lab=VIN}
C {devices/ipin.sym} 220 -370 0 0 {name=p5 lab=VIP}
C {devices/opin.sym} 750 -500 0 0 {name=p6 lab=VOUT}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 400 -430 0 0 {name=x1 }
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 480 -570 0 1 {name=x2 }
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 560 -570 0 0 {name=x4 }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 640 -430 0 1 {name=x3 }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 480 -310 0 0 {name=x5 }
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} 350 -310 0 1 {name=x6 }
C {devices/lab_wire.sym} 520 -380 0 0 {name=p7 sig_type=std_logic lab=tail}
