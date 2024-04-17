import h5py
import numpy as np

#pip install h5py

#write in hdf5
f = h5py.File("./Input/mytestfile.hdf5", "w")
data0=np.arange(0,100,1)
data1=np.outer(data0,data0)

#dset = f.create_dataset("mydataset", (100,), dtype='i')
f.create_dataset('dataset_0', data=data0)

f.create_dataset('dataset_1', data=data1)
#read from hdf5
hf = h5py.File('./Input/mytestfile.hdf5', 'r')
Key=list(hf.keys())

print(Key)

for i in range(len(Key)):
	print(hf.get(Key[i]))
	array_output=np.array(hf.get(Key[i]))
	print(array_output)


def recursively_save_dict_to_hdf5(group, dic):
    """
    Recursively save a nested dictionary to an HDF5 group.
    """
    for key, value in dic.items():
        if isinstance(value, dict):
            subgroup = group.create_group(key)
            recursively_save_dict_to_hdf5(subgroup, value)
        else:
            group[key] = value

nested_dict = {
    'group1': {
        'data1': 1.0,
        'data2': 2.0
    },
    'group2': {
        'subgroup': {
            'data3': 3.0
        },
        'data4': 4.0
    }
}

with h5py.File('nested_data.h5', 'w') as f:
    recursively_save_dict_to_hdf5(f, nested_dict)
