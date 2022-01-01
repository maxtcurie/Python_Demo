print('Hello, world!')
import numpy as np
import pandas as pd

x_list=np.array([0.955]*5)
m_list=np.array([5]*5)
x_peak=0.195
a=np.array([x_list, m_list,abs(x_list-x_peak)])
b=a.transpose()
df=pd.DataFrame(b,columns = ['x_list','m_list','peak_distance'])

print(df)