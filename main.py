import matplotlib.pyplot as pyplot
import numpy as np

data = np.array([40,20,10,25,5])
labels = ['python','android','java','javascript','go']


pyplot.pie(data,labels = labels,shadow=True)
pyplot.show()
