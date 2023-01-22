#from: https://stackoverflow.com/questions/11632905/python-get-key-of-index-in-dictionary

i={'foo':'bar', 'baz':'huh?'}
keys=list(i.keys())  #in python 3, you'll need `list(i.keys())`
values=list(i.values())
print(keys[values.index("bar")])  #'foo'