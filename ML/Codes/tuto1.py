import numpy
import matplotlib.pyplot as plt
import pandas

arr1 = numpy.array([1,1,1,1])
arr2 = numpy.array([1,2,3,4])

plt.plot(arr1, arr2)
plt.scatter(arr1, arr2)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
