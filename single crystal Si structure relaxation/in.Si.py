Python 3.11.0 (v3.11.0:deaf509e8f, Oct 24 2022, 14:43:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from lammps import PyLammps
L = PyLammps()
LAMMPS output is captured by PyLammps wrapper
L.units('metal')
L.dimension(3)
L.atom_style('atomic')
L.boundary('p p p')
L.read_data('data.lammps')
['Reading data file ...', '  orthogonal box = (0 0 0) to (16.331106 16.331106 16.331106)', '  1 by 1 by 1 MPI processor grid', '  reading atoms ...', '  216 atoms', '  read_data CPU = 0.028 seconds']
L.pair_style('tersoff')
L.pair_coeff('* * Si.tersoff Si')
'Reading tersoff potential file Si.tersoff with DATE: 2007-10-25'
L.mass('* 28')
L.thermo(10)
L.run(100)
["WARNING: No fixes with time integration, atoms won't move (src/verlet.cpp:60)", 'Neighbor list info ...', '  update every 1 steps, delay 10 steps, check yes', '  max neighbors/atom: 2000, page size: 100000', '  master list distance cutoff = 5.2', '  ghost atom cutoff = 5.2', '  binsize = 2.6, bins = 7 7 7', '  1 neighbor lists, perpetual/occasional/extra = 1 0 0', '  (1) pair tersoff, perpetual', '      attributes: full, newton on', '      pair build: full/bin/atomonly', '      stencil: full/bin/3d', '      bin: standard', 'Setting up Verlet run ...', '  Unit style    : metal', '  Current step  : 0', '  Time step     : 0.001', 'Per MPI rank memory allocation (min/avg/max) = 3.079 | 3.079 | 3.079 Mbytes', '   Step          Temp          E_pair         E_mol          TotEng         Press     ', '         0   0             -1000.1069      0             -1000.1069     -6622.3887    ', '        10   0             -1000.1069      0             -1000.1069     -6622.3887    ', '        20   0             -1000.1069      0             -1000.1069     -6622.3887    ', '        30   0             -1000.1069      0             -1000.1069     -6622.3887    ', '        40   0             -1000.1069      0             -1000.1069     -6622.3887    ', '        50   0             -1000.1069      0             -1000.1069     -6622.3887    ', '        60   0             -1000.1069      0             -1000.1069     -6622.3887    ', '        70   0             -1000.1069      0             -1000.1069     -6622.3887    ', '        80   0             -1000.1069      0             -1000.1069     -6622.3887    ', '        90   0             -1000.1069      0             -1000.1069     -6622.3887    ', '       100   0             -1000.1069      0             -1000.1069     -6622.3887    ', 'Loop time of 0.0439561 on 1 procs for 100 steps with 216 atoms', '', 'Performance: 196.560 ns/day, 0.122 hours/ns, 2274.996 timesteps/s', '99.1% CPU use with 1 MPI tasks x no OpenMP threads', '', 'MPI task timing breakdown:', 'Section |  min time  |  avg time  |  max time  |%varavg| %total', '---------------------------------------------------------------', 'Pair    | 0.043432   | 0.043432   | 0.043432   |   0.0 | 98.81', 'Neigh   | 0          | 0          | 0          |   0.0 |  0.00', 'Comm    | 0.00029955 | 0.00029955 | 0.00029955 |   0.0 |  0.68', 'Output  | 9.0415e-05 | 9.0415e-05 | 9.0415e-05 |   0.0 |  0.21', 'Modify  | 1.1083e-05 | 1.1083e-05 | 1.1083e-05 |   0.0 |  0.03', 'Other   |            | 0.0001228  |            |       |  0.28', '', 'Nlocal:            216 ave         216 max         216 min', 'Histogram: 1 0 0 0 0 0 0 0 0 0', 'Nghost:            648 ave         648 max         648 min', 'Histogram: 1 0 0 0 0 0 0 0 0 0', 'Neighs:              0 ave           0 max           0 min', 'Histogram: 1 0 0 0 0 0 0 0 0 0', 'FullNghs:         6048 ave        6048 max        6048 min', 'Histogram: 1 0 0 0 0 0 0 0 0 0', '', 'Total # of neighbors = 6048', 'Ave neighs/atom = 28', 'Neighbor list builds = 0', 'Dangerous builds = 0']
>>> L.thermo(1000)
>>> L.fix('1 all nve')
>>> L.fix('2 all langevin 0 298 0.1 123456')
>>> L.timestep(0.005)
>>> L.run(100000)

>>> L.dump('3 all atom 500 dump.Si')
>>> L.run(100000)

