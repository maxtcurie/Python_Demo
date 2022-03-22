import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x=np.arange(0,7,0.001)
y=np.sin(x)
df=pd.DataFrame(list(zip(x, y)), columns=['x', 'sin(x)'])

df_sorted=df.sort_values('sin(x)')

plt.clf()
plt.scatter(np.arange(0,len(df['sin(x)'])),df_sorted['sin(x)'],label='sorted')
plt.scatter(np.arange(0,len(df['sin(x)'])),df['sin(x)'],label='df')
plt.legend()
plt.show()


print(df)
print(df_sorted)
