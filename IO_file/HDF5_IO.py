import h5py
import numpy as np

#pip install h5py

#write in hdf5
f = h5py.File("mytestfile.hdf5", "w")
data0=np.arange(0,100,1)
data1=np.outer(data0,data0)

#dset = f.create_dataset("mydataset", (100,), dtype='i')
f.create_dataset('dataset_0', data=data0)

f.create_dataset('dataset_1', data=data1)
#read from hdf5
hf = h5py.File('mytestfile.hdf5', 'r')
Key=list(hf.keys())

print(Key)

for i in range(len(Key)):
	print(hf.get(Key[i]))
	array_output=np.array(hf.get(Key[i]))
	print(array_output)

