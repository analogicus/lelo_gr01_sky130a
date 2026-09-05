#!/usr/bin/env python3
"""Post process the TT top level transient.

cicsim calls main() with the run stem (e.g. output_tran/tran_LayGtKttTtVt)
after ngspice has written <stem>.yaml from tran.meas. We derive the
oscillator frequency and output swing and write them back so tran.yaml can
spec check them.

If the oscillator is dead the meas keys are missing. We deliberately write
freq = 0 rather than crash, so the spec table shows the failure.
"""
import yaml

#- Number of periods between the RISE=2 and RISE=12 crossings in tran.meas
NPERIODS = 10


def main(name):
    yamlfile = name + ".yaml"

    with open(yamlfile) as fi:
        obj = yaml.safe_load(fi)

    if obj is None:
        obj = {}

    t1 = obj.get("t1")
    t2 = obj.get("t2")

    if t1 is not None and t2 is not None and t2 > t1:
        obj["freq"] = float(NPERIODS / (t2 - t1))
    else:
        #- No oscillation found in the measurement window
        obj["freq"] = 0.0

    for key, hi, lo in (("vswing", "vosc_max", "vosc_min"),):
        vmax = obj.get(hi)
        vmin = obj.get(lo)
        if vmax is not None and vmin is not None:
            obj[key] = float(vmax - vmin)
        else:
            obj[key] = 0.0

    with open(yamlfile, "w") as fo:
        yaml.dump(obj, fo)
