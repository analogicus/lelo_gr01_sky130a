v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N -90 100 -90 150 {lab=VSS}
N -100 150 -90 150 {lab=VSS}
N -90 70 -90 100 {lab=VSS}
N -160 70 -130 70 {lab=VIN}
N -160 -30 -160 70 {lab=VIN}
N -160 -30 -130 -30 {lab=VIN}
N -90 0 -90 40 {lab=VOUT}
N -90 -0 -90 40 {lab=VOUT}
N -90 -60 -90 -30 {lab=VDD}
N -90 -110 -90 -60 {lab=VDD}
N -100 -110 -90 -110 {lab=VDD}
N -190 20 -160 20 {lab=VIN}
N -90 20 -50 20 {lab=VOUT}
C {devices/ipin.sym} -100 -110 0 0 {name=p1 lab=VDD}
C {devices/ipin.sym} -190 20 0 0 {name=p2 lab=VIN}
C {devices/ipin.sym} -100 150 0 0 {name=p3 lab=VSS}
C {devices/opin.sym} -50 20 0 0 {name=p4 lab=VOUT}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_2C5F0.sym} -130 70 0 0 {name=x1 }
C {LELO_ATR_SKY130A/LELOATR_LVT_PCH_2C5F0.sym} -130 -30 0 0 {name=x2 }
