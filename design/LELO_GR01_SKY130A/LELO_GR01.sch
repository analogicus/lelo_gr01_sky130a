v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 890 -330 910 -330 {lab=OSC_TEMP_1V8}
N 100 -300 130 -300 {lab=PWRUP_1V8}
N 190 -300 830 -300 {lab=#net1}
N 830 -330 830 -300 {lab=#net1}
C {cborder/border_xs.sym} 0 0 0 0 {
user="wulff"
company="wulff"}
C {devices/ipin.sym} 100 -600 0 0 {name=p1 lab=VDD_1V8}
C {devices/ipin.sym} 100 -100 0 0 {name=p2 lab=VSS}
C {devices/ipin.sym} 100 -300 0 0 {name=p3 lab=PWRUP_1V8}
C {devices/opin.sym} 910 -330 0 0 {name=p29 lab=OSC_TEMP_1V8}
C {sky130_fd_pr/res_generic_m4.sym} 860 -330 1 0 {name=R2
W=0.3
L=0.4
model=res_generic_m4
mult=1}
C {sky130_fd_pr/res_generic_m4.sym} 160 -300 1 0 {name=R1
W=0.3
L=0.4
model=res_generic_m4
mult=1}
