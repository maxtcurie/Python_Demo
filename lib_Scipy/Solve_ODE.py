#https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

#solving y'=y from t=0~10, y(t=0)=1
#the answer is y=exp(t)
def y_prime(t,y):
	return y
t_span=(0,10)
y0=[1]
solver_result=solve_ivp(y_prime,t_span,y0,max_step=0.001)


t_solution=solver_result.t
y_solution=solver_result.y

print(np.shape(t_solution))
print(np.shape(y_solution))

plt.clf()
plt.plot(t_solution,y_solution[0,:])
plt.yscale('log')
plt.show()
