#data structure:https://docs.python.org/3/tutorial/datastructures.html
import random

test=True

def rand_list(dict1):
    #about dictionary: https://youtu.be/daefaLgNkw0
    keys=list(thisdict.keys())
    weights=list(thisdict.values())
  
    #print(keys)
    #print(weights)
  
    #get weighted random choice
    #https://www.geeksforgeeks.org/how-to-get-weighted-random-choice-in-python/
    [random_out] = random.choices(keys, weights=weights, k=1)

    return random_out

if test==True:
    import numpy as np
    thisdict = {
      "a": 2,
      "b": 3,
      "c": 1
    } 
    keys=np.array(list(thisdict.keys()))
    weights=np.array(list(thisdict.values()))
    
    count=np.zeros(len(keys),dtype=float)
    
    for i in range(1000000):
        random_out=rand_list(thisdict)
        for j in range(len(keys)):
            if random_out==keys[j]:
              count[j]=count[j]+1.
    weights_norm=weights/np.sum(weights)
    count_norm=count/np.sum(count)
    print('\nweights_norm')
    print(weights_norm)

    print('\ncount_norm')
    print(count_norm)
    print('\nabs(weights_norm-count_norm)')
    print(abs(weights_norm-count_norm))
