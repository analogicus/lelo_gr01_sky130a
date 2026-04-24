v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 70 -550 70 -510 {lab=VDPWR}
N 70 -430 70 -400 {lab=VGND}
N -40 -520 -40 -490 {lab=VDPWR}
N -40 -520 70 -520 {lab=VDPWR}
N -40 -450 -40 -420 {lab=VGND}
N -40 -420 70 -420 {lab=VGND}
N 110 -470 190 -470 {lab=TIE_L}
N 250 -470 300 -470 {lab=uio_oe[7:0]}
N 300 -470 370 -470 {lab=uio_oe[7:0]}
N 310 -220 380 -220 {lab=uo_out[0]}
N 130 -220 180 -220 {lab=uo_out[0]}
N -240 -210 -170 -210 {lab=#net1}
N -220 -250 -170 -250 {lab=VDPWR}
N -220 -170 -170 -170 {lab=VGND}
N 180 -220 190 -220 {lab=uo_out[0]}
N 250 -220 310 -220 {lab=uo_out[0]}
N -330 -210 -300 -210 {lab=#net1}
N 190 -220 250 -220 {lab=uo_out[0]}
N -300 -210 -240 -210 {lab=#net1}
N 40 -670 260 -670 {lab=uio_out[7:0]}
N 260 -670 260 -590 {lab=uio_out[7:0]}
N 260 -590 360 -590 {lab=uio_out[7:0]}
N -590 -650 -560 -650 {lab=rst_n}
N -480 -650 -260 -650 {lab=#net2}
N -460 -200 -420 -200 {lab=ui_in[0]}
N -460 -220 -420 -220 {lab=pwrup_digital}
C {devices/opin.sym} 360 -710 0 0 {name=p4 lab=uo_out[7:2]}
C {devices/opin.sym} 360 -590 0 0 {name=p6 lab=uio_out[7:0]}
C {JNW_TR_SKY130A/JNWTR_TAPCELLB_CV.sym} -40 -470 0 0 {name=x8 }
C {JNW_TR_SKY130A/JNWTR_TIEL_CV.sym} 70 -430 0 0 {name=x9 }
C {devices/lab_wire.sym} 70 -550 0 0 {name=p30 sig_type=std_logic lab=VDPWR}
C {devices/lab_wire.sym} 70 -400 0 0 {name=p31 sig_type=std_logic lab=VGND}
C {sky130_fd_pr/res_generic_m4.sym} 220 -470 1 0 {name=R1[7:0]
W=0.3
L=0.3
model=res_generic_m4
mult=1}
C {devices/opin.sym} 370 -470 0 0 {name=p32 lab=uio_oe[7:0]}
C {devices/lab_wire.sym} 170 -470 0 0 {name=p7 sig_type=std_logic lab=TIE_L}
C {devices/ipin.sym} -490 -580 0 0 {name=p1 lab=VDPWR}
C {devices/ipin.sym} -490 -410 0 0 {name=p2 lab=VGND}
C {devices/ipin.sym} -490 -540 0 0 {name=p3 lab=ui_in[7:0]}
C {devices/ipin.sym} -490 -470 0 0 {name=p5 lab=uio_in[7:0]}
C {devices/ipin.sym} -490 -350 0 0 {name=p8 lab=ena}
C {devices/ipin.sym} -590 -650 0 0 {name=p10 lab=rst_n}
C {devices/lab_wire.sym} -460 -200 0 0 {name=p25 sig_type=std_logic lab=ui_in[0]}
C {devices/lab_wire.sym} -170 -170 0 0 {name=p9 sig_type=std_logic lab=VGND}
C {devices/lab_wire.sym} -170 -250 0 0 {name=p11 sig_type=std_logic lab=VDPWR}
C {LELO_GR01_SKY130A/LELO_GR01.sym} -20 -190 0 0 {name=x1}
C {devices/ipin.sym} -490 -320 0 0 {name=p13 lab=clk
}
C {devices/noconn.sym} 360 -710 0 0 {name=l2}
C {LELO_GR01_SKY130A/digital.sym} -110 -660 0 0 {name=x2}
C {devices/opin.sym} -260 -610 0 1 {name=p14 lab=uo_out[0]}
C {devices/lab_wire.sym} 380 -220 0 1 {name=p12 sig_type=std_logic lab=uo_out[0]}
C {JNW_TR_SKY130A/JNWTR_IVX1_CV.sym} -560 -650 0 0 {name=x3 }
C {devices/lab_wire.sym} -520 -610 0 0 {name=p15 sig_type=std_logic lab=VGND}
C {devices/lab_wire.sym} -520 -690 0 0 {name=p16 sig_type=std_logic lab=VDPWR}
C {devices/lab_wire.sym} -260 -710 0 0 {name=p17 sig_type=std_logic lab=VDPWR}
C {devices/lab_wire.sym} -260 -690 0 0 {name=p18 sig_type=std_logic lab=VGND}
C {devices/lab_wire.sym} -260 -670 0 0 {name=p19 sig_type=std_logic lab=clk}
C {devices/opin.sym} 40 -690 0 0 {name=p20 lab=uo_out[1]}
C {JNW_TR_SKY130A/JNWTR_ORX1_CV.sym} -420 -200 0 0 {name=x4 }
C {devices/lab_wire.sym} -380 -250 0 0 {name=p21 sig_type=std_logic lab=VDPWR}
C {devices/lab_wire.sym} -380 -170 0 0 {name=p22 sig_type=std_logic lab=VGND}
C {devices/lab_wire.sym} 40 -710 0 1 {name=p23 sig_type=std_logic lab=pwrup_digital}
C {devices/lab_wire.sym} -460 -220 0 0 {name=p24 sig_type=std_logic lab=pwrup_digital}
C {devices/lab_wire.sym} -260 -630 0 0 {name=p26 sig_type=std_logic lab=ui_in[1]}
