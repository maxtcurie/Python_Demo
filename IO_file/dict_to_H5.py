import h5py
import numpy as np

#pip install h5py

def save_dict_to_hdf5(dictionary, h5file):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            group = h5file.create_group(key)
            save_dict_to_hdf5(value, group)
        else:
            h5file.create_dataset(key, data=value)

dictionary={}
h5file='./test.h5'
save_dict_to_hdf5(dictionary, h5file)