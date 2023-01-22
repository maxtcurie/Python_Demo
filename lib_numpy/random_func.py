import numpy as np

a = np.random.rand(2,2)
print(a)

a=np.arange(0,10)
np.random.shuffle(a)
print(a)


for i in range(10):
    print(np.random.choice([1,2],size=1, p=[0.3,0.7]))