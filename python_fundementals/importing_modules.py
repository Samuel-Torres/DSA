# Python has built-in modules. You can access these modules here:
# https://docs.python.org/3/py-modindex.html
# access dir with dir(module-name)
# __name__ are private members cannot be used by devs
# can use all public members without __
# you can alias the name of the module by using the as keyword in python#

import math as m # m is an alias
print(dir(m))

# selecting specified modules from math:
from math import pi, pow, floor
# from math import pi as p , pow as po# can alias specified modules
# from math import * # imports all modules

# print(math.degrees(100))
print(pi)

