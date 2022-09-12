""" Testing scipy.constants
11 Sept 2020, Nicolas Grisouard (University of Toronto)
"""

import scipy.constants as spc

print('Gravitational constant:')
print('    spc.G =', spc.G)
print('    spc.gravitational_constant =', spc.gravitational_constant)
G = spc.physical_constants['Newtonian constant of gravitation']
print('    From the CODATA18 database:')
print('        G = {0} +- {1} {2}'.format(G[0], G[2], G[1]))

print('\nAstronomical Unit:')
print('    spc.au =', spc.au)
print('    spc.astronomical_unit =', spc.astronomical_unit)
