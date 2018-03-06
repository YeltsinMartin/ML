import numpy
import matplotlib.pyplot as plt
import pandas
import math


arr1 = numpy.array([-10,1,2,10])
arr2 = numpy.array([0,0,0,0])

# matplotlib
plt.plot(arr1, arr2)
plt.scatter(arr1, arr2)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()


lst1 = []
lst2 = []
for theta in range(0,365,5):
  lst1.append(math.sin(theta*math.pi/180))
  lst2.append(theta)

plt.plot(numpy.array([0,360]),numpy.array([0,0]))
plt.plot(numpy.array(lst2),numpy.array(lst1))
plt.xlabel('Theta')
plt.ylabel('Sin(Theta)')
plt.show()

m = 0.5
c = 1
#y = m*X + C

lst1 = []
lst2 = []

for x in range(-10,10,1):
  y = m*x + c
  lst1.append(y)
  lst2.append(x)
  
plt.plot(numpy.array(lst2),numpy.array(lst1))
plt.plot(numpy.array([-10,10]),numpy.array([0,0]))
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# pandas 

colum_name = ['a','b','c','d']
index_name = ['one','two']
arr1 = numpy.array([-10,1,2,10])
arr2 = numpy.array([[1,2,3,4],[5,6,7,8]])

series = pandas.Series(arr1, index=colum_name )
print series.a
print series['a']
print series
dat = pandas.DataFrame(arr2, index=index_name, columns =colum_name )

print dat
print dat['a']
print dat.b
