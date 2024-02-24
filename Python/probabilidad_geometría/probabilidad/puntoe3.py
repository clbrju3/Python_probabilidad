import numpy as np
import math
import random 
def fii(a):
    return math.sqrt(math.exp(math.exp(a))+math.tan(a))
n=int(input("Defina el numero de datos simulados: "))
u=[random.uniform(0,1) for _ in range(n)]
prom=0
for i in range(n):
    prom+=fii(u[i])
res=prom/n
#calculos para el punto bono, para eso n=10000
sii=0
for i in range (n):
    sii+=(fii(u[i])-res)**2
sigi=sii/(n-1)
#desviación estandar aproximada
print(res,sigi)