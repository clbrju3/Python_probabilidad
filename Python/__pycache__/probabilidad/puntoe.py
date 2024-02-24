import numpy as np
import os
import math
import random 
def fi(a):
    return 1/(a**5+1)
def fii(a):
    return 1/math.log(100-90*a)
def fiii(a):
    return math.sqrt(math.exp(math.exp(a))+math.tan(a))
n=int(input("Defina el numero de datos simulados: "))
u=[random.uniform(9,19) for _ in range(n)]
prom=0
for i in range(n):
    prom+=fi(u[i])
res=10*prom/n
#calculos para el punto bono, para eso n=10000
siii=0
for i in range (n):
    siii+=(fi(u[i])-res/10)**2
sigii=siii/(n-1)
sigii=str(sigii)
res=str(res)
#simga cuadrado aproximada
print("Aproximacion="+res)
print("Sigma cuadrado="+sigii)
os.system("pause")
os.system("cls")
print("Segunda integral \n")
n=int(input("Defina el numero de datos simulados: "))
u=[random.uniform(0.0,1.0) for _ in range(n)]
vec=np.vectorize(fii)(u)
prom=0
for i in range (n):
    prom+=vec[i]
res=90*prom/n
res=str(res)
print("Aproximación="+res)
#calculos para el punto bono, para eso n=10000
si=0
for i in range (n):
    si+=(vec[i]-prom/n)**2
sig=si/(n-1)
sig=str(sig)
#sigma cuadrado (varianza) aproximada
print("Sigma cuadrado="+sig)
os.system("pause")
os.system("cls")
print("Tercera integral \n")
n=int(input("Defina el numero de datos simulados: "))
u=[random.uniform(0,1) for _ in range(n)]
prom=0
for i in range(n):
    prom+=fiii(u[i])
res=prom/n
#calculos para el punto bono, para eso n=10000
sii=0
for i in range (n):
    sii+=(fiii(u[i])-res)**2
sigi=sii/(n-1)
sigi=str(sigi)
res=str(res)
#sigma cuadrado aproximada
print("Aproximacion="+res+"\n", "Sigma cuadrado="+sigi)
os.system("pause")