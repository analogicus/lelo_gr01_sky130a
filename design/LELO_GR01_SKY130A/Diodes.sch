v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N -120 20 130 20 {lab=VSS}
N -80 -10 -80 20 {lab=VSS}
N 90 -10 90 20 {lab=VSS}
N -120 -80 -120 -40 {lab=I2}
N 130 -80 130 -40 {lab=I1}
N -0 20 0 60 {lab=VSS}
C {sky130_fd_pr/pnp_05v5.sym} 110 -10 0 0 {name=Q1[7:0]
model=pnp_05v5_W3p40L3p40
spiceprefix=X}
C {sky130_fd_pr/pnp_05v5.sym} -100 -10 0 1 {name=Q2
model=pnp_05v5_W3p40L3p40
spiceprefix=X}
C {devices/opin.sym} 0 60 0 0 {name=p3 lab=VSS}
C {devices/ipin.sym} -120 -80 0 0 {name=p1 lab=I2}
C {devices/ipin.sym} 130 -80 0 0 {name=p2 lab=I1}
