#- Functional transient on the tapeout top level.
#-
#- Note: we deliberately do NOT include ../../tech/make/sim.make. Its
#- netlist_cell target runs "cd ../../work && make cdl lpe" whenever
#- VIEW=Lay, which would re-extract the layout. We reuse the existing
#- work/lpe/${CELL}_lpe.spi and only regenerate xdut.spi, which is cheap
#- and guarantees the port order matches the netlist.

TB=tran
VIEW=Lay
CELL=tt_um_lelo_gr01_analogicus
LIB=LELO_GR01_SKY130A
OPT=
THREADS=4

all: typical digital summary

netlist:
	perl ../../tech/script/genxdut ../../work/xsch/${CELL}.spice ${CELL}

#- Re-extract the layout. Only needed if the layout changed.
lpe:
	cd ../../work && ${MAKE} cdl lpe LIB=${LIB} CELL=${CELL}

test:
	${MAKE} typical OPT="Debug"

typical: netlist
	cicsim run --threads ${THREADS} --replace replace.yaml --name ${VIEW}_typical ${TB} ${OPT} ${VIEW} Gt Ktt Khvt Tt Vt

#- The digital handshake testbench. Much longer, it has to cover four
#- periods of the 32768 Hz clock.
digital: netlist
	cicsim run --threads ${THREADS} --replace replace.yaml --name ${VIEW}_typical dig ${OPT} ${VIEW} Gt Ktt Khvt Tt Vt

summary:
	cicsim summary --output "README.md"

wave:
	cicsim wave output_${TB}/${TB}_${VIEW}GtKttKhvtTtVt.raw

clean:
	-rm -rf output_*
	-rm -rf __pycache__
	-rm -f *.run
