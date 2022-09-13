import numpy as np
import pandas as pd

q=5.
mi_me=1836.152*2.
e=1.5
factor=1./q*((mi_me)**0.5)*(e**2.5)/8.

# 8 types of collsions ee, ei, ie, ii, iz ....

print(factor)
print(0.15*factor)
print(1.2*factor)