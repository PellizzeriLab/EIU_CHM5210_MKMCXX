# EIU_CHM5210_MKMCXX

Materials for running and analyzing kinetic Monte Carlo simulations in EIU
CHM5210 (Bonding and Reactivity). The repository is ready to launch with
[Binder](https://mybinder.org/); `environment.yml` supplies the only runtime
dependency, Python.

## Run the example

From a terminal, run:

```bash
./mkmcxx examples/isomerization.inp
python analysis/analyze_mkmcxx.py trajectory.csv
```

The executable writes a CSV trajectory (the output filename is set by the
`output` line in the input file), and the analysis script reports the final and
mean population of each species. The input format is intentionally readable:
define `steps`, `seed`, `output`, `species NAME COUNT`, and
`reaction SOURCE -> PRODUCT RATE` lines.

To use Binder, open this repository at
<https://mybinder.org/> and click **Launch**. Run the same commands in a
terminal or notebook opened in the Binder session.
