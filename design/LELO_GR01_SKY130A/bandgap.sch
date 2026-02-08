v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
B 2 230 -510 1030 -110 {flags=graph
y1=1.3374999
y2=3.3374999
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=3.8532699e-07
x2=1.0385326e-05
divx=5
subdivx=1
xlabmag=1.0
ylabmag=1.0
node=vout
color=4
dataset=-1
unitx=1
logx=0
logy=0
rawfile=/home/nikolai/pro/aicex/ip/lelo_gr01_sky130a/sim/bandgap/output_tran/tran_SchGtKttTtVt.raw
sim_type=tran}
B 2 310 -35 1110 365 {flags=graph
y1=0
y2=2
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0
x2=10e-6
divx=5
subdivx=1
xlabmag=1.0
ylabmag=1.0
node=""
color=""
dataset=-1
unitx=1
logx=0
logy=0
rawfile=/home/nikolai/pro/aicex/ip/lelo_gr01_sky130a/sim/bandgap/output_tran/tran_SchGtKttTtVt.raw
sim_type=tran}
P 4 1 60 -60 {}
P 4 1 -130 -150 {}
P 4 1 -80 420 {}
T {.control
  save all
  op
  ac dec 10 1 10G
  write bandgap_gui.raw
.endc} -605 -315 0 0 0.4 0.4 {}
N 0 0 0 90 {lab=VOUT}
N -20 270 -20 380 {lab=VIP}
N 20 270 20 380 {lab=VIN}
N 45 580 45 630 {lab=RES_NET}
N 45 500 45 520 {lab=VIN}
N 20 420 45 420 {lab=VIN}
N -45 420 -45 630 {lab=VIP}
N -20 380 -20 420 {lab=VIP}
N -90 30 -90 420 {lab=VIP}
N -90 -30 -90 0 {lab=VDD_1V8}
N 0 -120 0 -100 {lab=VDD_1V8}
N -90 -50 -90 -30 {lab=VDD_1V8}
N -40 270 -40 310 {lab=VDD_1V8}
N -90 420 -20 420 {lab=VIP}
N -0 270 -0 310 {lab=IB}
N 5 730 5 760 {lab=VSS}
N 20 380 20 420 {lab=VIN}
N -50 0 50 0 {lab=VOUT}
N 90 -50 90 -30 {lab=VDD_1V8}
N -90 -70 90 -70 {lab=VDD_1V8}
N 90 -0 90 420 {lab=VIN}
N 45 420 90 420 {lab=VIN}
N 45 420 45 500 {lab=VIN}
N 90 -70 90 -50 {lab=VDD_1V8}
N -90 -70 -90 -50 {lab=VDD_1V8}
N -0 -100 -0 -70 {lab=VDD_1V8}
C {LELO_GR01_SKY130A/diffamp_1.sym} 0 120 3 0 {name=X2}
C {devices/lab_wire.sym} -40 310 0 0 {name=p2 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} -20 365 0 0 {name=p3 sig_type=std_logic lab=VIP}
C {devices/lab_wire.sym} 0 310 0 0 {name=p4 sig_type=std_logic lab=IB}
C {devices/lab_wire.sym} 20 350 0 0 {name=p5 sig_type=std_logic lab=VIN}
C {devices/lab_wire.sym} 40 270 3 0 {name=p6 sig_type=std_logic lab=VSS}
C {devices/ipin.sym} -220 380 0 0 {name=p7 lab=VDD_1V8}
C {devices/ipin.sym} -220 420 0 0 {name=p8 lab=VIP}
C {devices/ipin.sym} -220 460 0 0 {name=p9 lab=IB}
C {devices/ipin.sym} -220 500 0 0 {name=p10 lab=VIN}
C {devices/ipin.sym} -220 540 0 0 {name=p11 lab=VSS}
C {LELO_GR01_SKY130A/Diodes.sym} -55 680 0 0 {name=x1}
C {sky130_fd_pr/res_generic_m1.sym} 45 550 0 0 {name=R1
W=5
L=100000
model=res_generic_m1
mult=1}
C {devices/lab_wire.sym} 0 -120 0 0 {name=p1 sig_type=std_logic lab=VDD_1V8}
C {devices/lab_wire.sym} 5 760 0 0 {name=p12 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 0 55 0 0 {name=p13 sig_type=std_logic lab=VOUT}
C {devices/lab_wire.sym} 45 615 0 0 {name=p14 sig_type=std_logic lab=RES_NET}
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} 50 0 0 0 {name=x5}
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} -50 0 0 1 {name=x3[7:0]}
C {JNW_TR_SKY130A/JNWTR_CAPX1.sym} 0 -60 2 1 {name=xd1[4:0]}
