import csv
import pandas as pd 
import Quandl

from sklearn import preprocessing, cross_validation, svm


df=Quandl.get('WIKI/GOOGL')