import matplotlib.pyplot as plot
import numpy as np
import math
import random 
def fi(a):
    return -math.log(1-a)/2
u=[random.uniform(0.0,1.0) for _ in range(10000)]
exp=np.vectorize(fi)(u)
plot.hist(exp,1000,color='grey', edgecolor='black',  label='Histograma',density=True)
plot.show()