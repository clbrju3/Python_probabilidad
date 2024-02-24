import math
import random 
def f(a):
    return 1/(math.log(a))
n=int(input("Defina el numero de datos simulados: "))
u=[random.uniform(10,100) for _ in range(n)]
prom=0
for i in range(n):
    prom+=f(u[i])
res=90*prom/n
print(res)
#calculos para el punto bono
si=0
for i in range (n):
    si+=(f(u[i])-prom/n)**2
    print(f(u[i]-prom/n))
sig=si/(n-1)
#desviación estandar aproximada
sigma=math.sqrt(sig)
print(sig)