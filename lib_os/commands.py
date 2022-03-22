import os

try: 
    os.mkdir('1test_dir')
except:
    pass

dir1=os.path.join('1test_dir','dir1')
print(dir1)