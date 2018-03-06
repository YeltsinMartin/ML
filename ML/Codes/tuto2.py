import numpy
import pandas
import csv
import os
from urllib import urlopen

path =  os.getcwd().replace('Codes','DataSets')+"\pima-indians-diabetes.data.csv"

# using numpy

raw_data = open(path, 'rb')
data = numpy.loadtxt(raw_data, delimiter=",")
print(data.shape)

'''
# using URL
url = 'https://goo.gl/vhm1eU'

raw_data = urlopen(url)
data = numpy.loadtxt(raw_data, delimiter=",")
print(data.shape)
'''



# using pandas

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(path, names=names)
print data.shape


'''
# url
data = read_csv(url, names=names)
'''
