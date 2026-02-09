[![GDS](../../actions/workflows/gds.yaml/badge.svg)](../../actions/workflows/gds.yaml)
[![DRC](../../actions/workflows/drc.yaml/badge.svg)](../../actions/workflows/drc.yaml)
[![LVS](../../actions/workflows/lvs.yaml/badge.svg)](../../actions/workflows/lvs.yaml)
[![DOCS](../../actions/workflows/docs.yaml/badge.svg)](../../actions/workflows/docs.yaml)

# Who
Nicolas, Nikolai and Walter, aka. Group 1

# Module 1: Bandgap

## Why

In order to create a temperature dependent output that we can measure later, we have created a bandgap that outputs a current which varies based on temperature. 



## How

The bandgap works since the voltage across our "diodes" (two diode-connected PNP transistors) will vary based on a factor of kT/q  where T is the temperature in kelvin (and the size). So, both our diodes have a known voltage drop VD1 and VD2 which depends on the temperature. In order to use this voltage drop to create a varying output current we set a resistor above one of the diodes. Then we force the voltage above the resistor VR1 to be the same as the voltage above the other diode VD2. The voltage drop across the resistor (and thus the current) will then be VR1 - VD1, or VD2 - VD1. By setting the diodes as different sizes, we will then get a temperature dependent current through the loop.

The schematic of this circuit can be found in design/LELO_GR01_SKY130A/bandgap.sch

## What


| What            |        Cell/Name |
| :----           |  :----:       |
| Schematic       | design/LELO_GR01_SKY130A/bandgap.sch |




## Signal interface


| Signal       | Direction | Domain  | Description                               |
| :---         | :---:     | :---:   | :---                                      |
| VDD_1V8      | Input     | VDD_1V8 | 1.8V Main supply                               |
| VSS          | Input     | Ground  |                                           |
| PWRUP_1V8    | Input     | VDD_1V8 | Power up the circuit                      |
| IB           | Input     | VDD_1V8 | 10µA reference input current              |
| VREF         | Output    | VDD_1V8 | 1.22V reference voltage generated         |
| VR           | Output    | VDD_1V8 | CTAT voltage which decreases with temperature  |




## Key parameters


| Parameter           | Min     | Typ             | Max     | Unit  |
| :---                | :---:   | :---:           | :---:   | :---: |
| Technology          |         | Skywater 130 nm |         |       |
| AVDD                | 1.7     | 1.8             | 1.9     | V     |
| Temperature         | -40     | 27              | 125     | C     |
