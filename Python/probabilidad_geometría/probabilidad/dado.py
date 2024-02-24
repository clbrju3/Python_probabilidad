import random
import numpy as np
import matplotlib.pyplot as plt
def masa (a):
    c=0
    for i in range (1,7):
        if(a==i):
            c=1/6 
            break
    return c
def distri (a):
    b=int(a)
    c=masa(b)
    return c*b
def dado (u):
    c=1
    for i in range (1,7):
        if((u>distri(i-1)) and (u<distri(i))):
            c=i
            break
    return c
u=[random.uniform(0.0,1.0) for _ in range(10000)]
dados=np.vectorize(dado)(u)


plt.hist(dados, [1,2,3,4,5,6,7], color='grey', edgecolor='black',  label='Histograma', density=True)
plt.show()

