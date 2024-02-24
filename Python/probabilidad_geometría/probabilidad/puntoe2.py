import math
import random 
def fiii(a):
    return 1/(a**5+1)
n=int(input("Defina el numero de datos simulados: "))
u=[random.uniform(9,19) for _ in range(n)]
prom=0
for i in range(n):
    prom+=fiii(u[i])
res=10*prom/n
print(res)
#calculos para el punto bono, para eso n=10000
siii=0
for i in range (n):
    siii+=(fiii(u[i])-res/10)**2
sigii=siii/(n-1)
#desviación estandar aproximada
print(sigii)