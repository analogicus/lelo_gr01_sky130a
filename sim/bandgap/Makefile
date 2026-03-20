

all: typical etc mc summary



TB=tran
AC_TB=ac
DC_TB=dc
VIEW=Sch
#VIEW=Lay
CELL=bandgap
LIB =diffamp_1
OPT=

include ../../tech/make/sim.make

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

dc: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_dc ${DC_TB} ${VIEW} Gt Ktt Tt Vt

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
