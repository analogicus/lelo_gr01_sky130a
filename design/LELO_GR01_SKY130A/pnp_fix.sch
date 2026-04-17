v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 20 -60 20 -30 {lab=e}
N -20 0 -20 30 {lab=VSS}
N -20 30 20 30 {lab=VSS}
N 20 30 20 70 {lab=VSS}
C {sky130_fd_pr/pnp_05v5.sym} 0 0 0 0 {name=Q3
model=pnp_05v5_W3p40L3p40
m=1
spiceprefix=X}
C {devices/opin.sym} 20 70 0 0 {name=p2 lab=VSS}
C {devices/ipin.sym} 20 -60 0 0 {name=p1 lab=e}
