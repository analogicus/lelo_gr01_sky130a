

all: typical etc mc summary



TB=tran
AC_TB=ac
VIEW=Sch
#VIEW=Lay
CELL=diffamp_1
LIB =diffamp_1
OPT=

include ../../tech/make/sim.make

test:
	${MAKE} typical OPT="Debug"

typical: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_typical ${TB} ${OPT} ${VIEW} Gt Ktt Tt Vt --no-sha
	cicsim run --replace replace.yaml --name ${VIEW}_ac_typical ${AC_TB} ${OPT} ${VIEW} Gt Ktt Tt Vt --no-sha

tran:
	cicsim run --replace replace.yaml --name ${VIEW}_tran ${TB} ${OPT} ${VIEW} Gt Ktt Tt Vt --no-sha

slow: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_slow ${TB} ${OPT} ${VIEW} Gt Kss "Th,Tl" Vl

fast: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_fast ${TB} ${OPT} ${VIEW} Gt Kff "Th,Tl" Vh

tfs: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_tfs ${TB} ${OPT} ${VIEW} Gt "Ktt,Kss,Kff" "Tt,Th,Tl" "Vt,Vl,Vh"

etc: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_etc ${TB} ${OPT} ${VIEW} Gt "Kss,Kff,Ksf,Kfs" "Th,Tl" "Vl,Vh"
	cicsim run --replace replace.yaml --name ${VIEW}_ac_etc ${AC_TB} ${OPT} ${VIEW} Gt "Kss,Kff,Ksf,Kfs" "Th,Tl" "Vl,Vh"

mc: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_mc --count 30 ${TB} ${OPT} ${VIEW} Gt "Kttmm" "Tt" "Vt"

ntc: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_ntc ${TB} ${OPT} ${VIEW} Gt "Ktt,Kss,Kff" "Tt" Vt

temp: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_temp ${TB} ${OPT} ${VIEW} Gt "Ktt" "Tt,Th,Tl" Vt

ac_typical: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_ac_typical ${AC_TB} ${OPT} ${VIEW} Gt Ktt Tt Vt

ac_etc: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_ac_etc ${AC_TB} ${OPT} ${VIEW} Gt "Kss,Kff,Ksf,Kfs" "Th,Tl" "Vl,Vh"

ac_temp: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_ac_temp ${AC_TB} ${OPT} ${VIEW} Gt "Ktt" "Tt,Th,Tl" Vt

vcm_sweep: netlist
	cicsim run --replace replace.yaml --name ${VIEW}_acvcm acvcm ${OPT} ${VIEW} Gt Ktt Tt Vt --no-sha
	python3 plot_vcm.py

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
