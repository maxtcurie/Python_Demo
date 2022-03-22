# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
  
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False

# using filter function
filtered = filter(fun, sequence)

import numpy as np
seq=np.arange(10)
seq_filter=filter(lambda x: x % 2 != 0, seq)
print(list(seq_filter))

