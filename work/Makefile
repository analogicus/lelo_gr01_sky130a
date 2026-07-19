
#- Core makefile provides the following commands:
# -----------------------------------------------------------
# gds: generate gds/<CELL>.gds
# cdl: generate cdl/<CELL>.cdl
# xsch: generate xsch/<CELL>.spice
# lvs: Check cdl/<CELL>.cdl versus ../design/<LIB>/<CELL>.mag
# lpe: Extract parasitics lpe/<CELL>.spi
# drc: Run design rule checks on ../design/<LIB>/<CELL>.mag
# -----------------------------------------------------------

PREFIX=
LIB=LELO_GR01_SKY130A
#CELL=LELO_GR01
CELL=tt_um_lelo_gr01_analogicus
VERILOG_FILE=../rtl/runs/RUN_2026-04-17_15-08-10/final/pnl/LELO_TEMP.pnl.v


#- Provide cells you want to check for the lvsall drcall commands
CELLS = LELO_GR01

include ../tech/make/core.make

# Add missing PNP to GDS by overriding Makefile
# https://www.gnu.org/software/make/manual/html_node/Overriding-Makefiles.html
# .PHONY: gds force lvs_tt
# gds:
# 	test -d ${PDK_ROOT}/sky130A/libs.ref/sky130_fd_pr/gds || mkdir ${PDK_ROOT}/sky130A/libs.ref/sky130_fd_pr/gds
# 	test -f ${PDK_ROOT}/sky130A/libs.ref/sky130_fd_pr/gds/sky130_fd_pr.gds || cp ../design/${LIB}/sky130_fd_pr.gds ${PDK_ROOT}/sky130A/libs.ref/sky130_fd_pr/gds/
# 	@$(MAKE) -f ../tech/make/core.make PREFIX=${PREFIX} LIB=${LIB} CELL=${CELL} gds

# %: force
# 	@$(MAKE) -f ../tech/make/core.make PREFIX=${PREFIX} LIB=${LIB} CELL=${CELL} $@
# force: ;

define TCL_FOR_NETGEN
	set layout [readnet spice lvs/${TT_CELL}.spi]
	set source [readnet spice xsch/${TT_CELL}.spice]
	readnet spice $$env(PDK_ROOT)/sky130A/libs.ref/sky130_fd_sc_hd/spice/sky130_fd_sc_hd.spice $$source
	readnet verilog ${VERILOG_FILE} $$source
	lvs "$$layout ${TT_CELL}" "$$source ${TT_CELL}" $$env(PDK_ROOT)/sky130A/libs.tech/netgen/sky130A_setup.tcl lvs/${TT_CELL}_lvs.log > lvs/${TT_CELL}_netgen_lvs.log
endef
export TCL_FOR_NETGEN
define TCL_FOR_MAGIC
	set SUB 0
	set OPATH lvs/ext
	load ../design/${LIB}/${TT_CELL}.mag

	extract path $${OPATH}
	extract all
	ext2spice lvs
	ext2spice -p $${OPATH} -o lvs/${TT_CELL}.spi
	quit
endef
export TCL_FOR_MAGIC

# Analog + digital LVS
# https://web.open-source-silicon.dev/t/16936037/hi-we-are-working-on-mixed-signal-design-we-have-a-digital-m
# https://github.com/ajcci/sky130_ajc_ip__overvoltage/tree/main?tab=readme-ov-file#layout-vs-schematic-lvs
# https://xschem.sourceforge.io/stefan/xschem_man/tutorial_use_existing_subckt.html
# http://repo.hu/projects/xschem/xschem_man/tutorial_busses.html

lvs_tt:
	test -d lvs || mkdir lvs
# Create schematic netlist + digital placeholder
	make xsch CELL=${TT_CELL}
# Create layout extracted netlist
	echo "$$TCL_FOR_MAGIC" > lvs/${TT_CELL}_spi.tcl
	magic -noconsole -dnull lvs/${TT_CELL}_spi.tcl > lvs/${TT_CELL}_spi.log 2>&1
# Run netgen
	echo "$$TCL_FOR_NETGEN" > netgen.tcl
	netgen -batch source netgen.tcl

lpe_tt:
	test -d lpe || mkdir lpe
# Create schematic netlist (needed for comparison or simulation prep)
	make xsch CELL=${TT_CELL}
# Create layout extracted netlist with Parasitics (LPE)
	echo "load ${TT_CELL}.mag; \
	      extract all; \
	      ext2sim labels on; \
	      ext2sim; \
	      ext2spice lvs; \
	      ext2spice cthresh 0; \
	      ext2spice rthresh 0; \
	      ext2spice -o lpe/${TT_CELL}_lpe.spi; \
	      exit" > lpe/${TT_CELL}_lpe.tcl
	magic -noconsole -dnull lpe/${TT_CELL}_lpe.tcl > lpe/${TT_CELL}_lpe.log 2>&1
