from scipy.optimize import fsolve
import math

#https://stackoverflow.com/questions/8739227/how-to-solve-a-pair-of-nonlinear-equations-using-python

def equations(p):
    x, y = p
    return (x+y**2-4, math.exp(x) + x*y - 3)

x, y =  fsolve(equations, (1, 1))

print equations((x, y))