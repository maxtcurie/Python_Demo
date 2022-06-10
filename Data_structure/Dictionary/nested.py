#From: https://www.geeksforgeeks.org/python-nested-dictionary/
#Dictionary
a={'x':{},'y':{}}
a['x']={x: x for x in (2, 4, 6)}
a['y']={x: x**2 for x in (2, 4, 6)}
print(a)
print(a['x'][2])
