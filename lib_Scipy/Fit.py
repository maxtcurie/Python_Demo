import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

def gaussian(x, amplitude, mean, stddev):
        return amplitude * np.exp(-((x - mean) / (1.*stddev))**2.)

def gaussian_fit_manual(x,data):
    x,data=np.array(x), np.array(data)

    #warnings.simplefilter("error", OptimizeWarning)
    judge=0

    try:
        popt, pcov = optimize.curve_fit(gaussian, x,data)  
        max_index=np.argmax(data)
        
        
        plt.clf()
        plt.plot(x,data, label="data")
        plt.plot(x, gaussian(x, *popt), label="fit")
        plt.axvline(x[max_index],color='red',alpha=0.5)
        plt.axvline(x[max_index]+popt[2],color='red',alpha=0.5)
        plt.axvline(x[max_index]-popt[2],color='red',alpha=0.5)
        plt.legend()
        plt.show()

        judge=int(input("Is the fit okay?  0. No 1. Yes"))

    except RuntimeError:
        print("Curve fit failed, need to restrict the range")

        judge=0
        
        popt=[0]*3  
        max_index=np.argmax(data)
        popt[0]=data[max_index] #amplitud
        popt[1]=x[max_index]    #mean

        plt.clf()
        plt.plot(x,data, label="data")
        plt.axvline(x[max_index],color='red',alpha=0.5)
        plt.legend()
        plt.show()

        while judge==0:

            popt[2]=float(input("sigma="))*np.sqrt(2.)  #stddev

            plt.clf()
            plt.plot(x,data, label="data")
            plt.plot(x, gaussian(x, *popt), label="fit")
            plt.axvline(x[max_index],color='red',alpha=0.5)
            plt.axvline(x[max_index]+popt[2],color='red',alpha=0.5)
            plt.axvline(x[max_index]-popt[2],color='red',alpha=0.5)
            plt.legend()
            plt.show()

            judge=int(input("Is the fit okay?  0. No 1. Yes"))


    while judge==0:

        popt=[0]*3  
        max_index=np.argmax(data)
        popt[0]=data[max_index] #amplitud
        popt[1]=x[max_index]    #mean

        popt[2]=float(input("sigma="))*np.sqrt(2.)  #stddev

        plt.clf()
        plt.plot(x,data, label="data")
        plt.plot(x, gaussian(x, *popt), label="fit")
        plt.axvline(x[max_index],color='red',alpha=0.5)
        plt.axvline(x[max_index]+popt[2],color='red',alpha=0.5)
        plt.axvline(x[max_index]-popt[2],color='red',alpha=0.5)
        plt.legend()
        plt.show()

        judge=int(input("Is the fit okay?  0. No 1. Yes"))

            
    amplitude=popt[0]
    mean     =popt[1]
    stddev   =popt[2] 

    return amplitude,mean,stddev

