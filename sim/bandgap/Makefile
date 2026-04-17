

all: typical etc mc summary



TB=tran
AC_TB=ac
#VIEW=Sch
VIEW=Lay
CELL=bandgap
LIB =LELO_GR01_SKY130A
OPT=

#include ../../tech/make/sim.make

cell:
	cicsim simcell  ${LIB} ${CELL} ../tech/cicsim/cell_spice/template.yaml

cellsv:
	cicsim simcell  ${LIB} ${CELL} ../tech/cicsim/cell_sv/template.yaml

netlist_cell:
	test -d ../../work/xsch || mkdir ../../work/xsch
	cd ../../work/ && make xsch LIB=${LIB} CELL=${CELL}
ifeq ($(VIEW),Lay)
#	cd ../../work && make cdl lpe LIB=${LIB} CELL=${CELL}
endif

ver:
	test -d ../../work/xsch && cd ../../work/ && make ver LIB=${LIB} CELL=${CELL}

netlist: netlist_cell
#- I've seen port ordering change between xschem version, so I also
# generate a xdut.spi file that always has the right port ordering.
#- TODO: Should I add the view here? Either xsch or lpe??
	perl ../../tech/script/genxdut ../../work/xsch/${CELL}.spice ${CELL}


netlist_sv:
	perl ../../tech/script/netlist_mdl ../../rtl/${CELL}.ys ${LIB}
	cd ../../rtl; yosys ${CELL}.ys
	perl ../../tech/script/genxdut ../../rtl/${CELL}.spice ${CELL}

test:
	${MAKE} typical OPT="Debug"

typical: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_typical ${TB} ${OPT} ${VIEW} Gt Ktt Tt Vt

slow: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_slow ${TB} ${OPT} ${VIEW} Gt Kss "Th,Tl" Vl

fast: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_fast ${TB} ${OPT} ${VIEW} Gt Kff "Th,Tl" Vh

tfs: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_tfs ${TB} ${OPT} ${VIEW} Gt "Ktt,Kss,Kff" "Tt,Th,Tl" "Vt,Vl,Vh"

etc: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_etc ${TB} ${OPT} ${VIEW} Gt "Kss,Kff,Ksf,Kfs" "Th,Tl" "Vl,Vh"

mc: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_mc --count 30 ${TB} ${OPT} ${VIEW} Gt "Kttmm" "Tt" "Vt"

ntc: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_ntc ${TB} ${OPT} ${VIEW} Gt "Ktt,Kss,Kff" "Tt" Vt

temp: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_temp ${TB} ${OPT} ${VIEW} Gt "Ktt" "Tt,Th,Tl" Vt

ac: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_ac ${AC_TB} ${VIEW} Gt Ktt Tt Vt

summary:
	cicsim summary --output "README.md"

slide:
	pandoc -s  -t slidy README.md -o README.html


clean:
	-rm -rf output_*
	-rm -rf __pycache__
	-rm *.run
	-rm *.pdf
	-rm *.csv
