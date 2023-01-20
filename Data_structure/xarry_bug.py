import xarray as xr
import numpy as np 
#from: https://xarray.pydata.org/en/v0.10.4/examples/quick-overview.html#create-a-dataarray

dim=3

template0=np.zeros(1)
template1=np.zeros(dim)
template2=np.zeros((dim,dim))
x_coord=np.linspace(0,10,dim)

xr_arry = xr.Dataset(
	data_vars=dict(	num_0=(["single"],template0),\
					array_0=(["dim1"],template1),\
					array_01=(["dim1"],template1),\
					array_1=(["dim1",'dim2'],template2)\
					),
	coords=dict( x_coord=(['x_coord'],x_coord) ),
	attrs=dict(description="this is a demo xarray")
	)


x=np.arange(dim)
x_2=np.arange(dim)*2
x_2D=[[i*j for i in np.arange(dim)]
		for j in np.arange(dim)]
x_2D=np.array(x_2D)

#for i in range(dim):
#	xr_arry.array_0[i]=x[i]
#	for j in range(dim):
#		xr_arry.array_1[i,j]=x_2D[i,j]
#
#print(xr_arry.array_0)
#print(xr_arry.array_1)


xr_arry.array_0[:]=x
xr_arry.array_01[:]=x_2
xr_arry.array_1[:,:]=x_2D


array0=np.array(xr_arry.array_01)
print(array0)
array0=np.array(xr_arry.array_0)
print(array0)
print('*********')
array1=np.array(xr_arry.array_1)
print(array1)

