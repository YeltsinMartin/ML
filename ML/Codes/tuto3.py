import numpy
import pandas
import os
import matplotlib.pyplot as plt

path =  os.getcwd().replace('Codes','DataSets')+"\pima-indians-diabetes.data.csv"

name_lst = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(path, names=name_lst)

#print data.head(20)

pandas.set_option('display.width', 120)
pandas.set_option('precision',3)
print data.describe()

'''
plt.figure(1)
plt.subplot(811)
plt.scatter(list (data.preg),list (data['class']) )
plt.subplot(812)
plt.scatter(list (data.plas),list (data['class']) )
plt.subplot(813)
plt.scatter(list (data.pres),list (data['class']) )
plt.subplot(814)
plt.scatter(list (data.skin),list (data['class']) )
plt.subplot(815)
plt.scatter(list (data.test),list (data['class']) )
plt.subplot(816)
plt.scatter(list (data.mass),list (data['class']) )
plt.subplot(817)
plt.scatter(list (data.pedi),list (data['class']) )
plt.subplot(818)
plt.scatter(list (data.age),list (data['class']) )
'''
print data.groupby('class').size()

#plt.title('Varaition with names')
#plt.scatter(list(data.preg),list(data['class']))            
#plt.show()

'''
correlations = data.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(name_lst)
ax.set_yticklabels(name_lst)
plt.show()
'''

from pandas.tools.plotting import scatter_matrix
scatter_matrix(data)
plt.show()
