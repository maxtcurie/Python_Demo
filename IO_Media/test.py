import numpy as np 

x=np.arange(10)
y_list=x.astype("str")
y1=[y + '.png' for y in y_list]
#y1=y+'.png'
#y2=y+'_sin.png'
print(y1)
