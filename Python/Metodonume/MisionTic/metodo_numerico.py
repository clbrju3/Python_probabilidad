import math
def num(i):
    w=math.sqrt(i**4+1)/(2*i**2)+math.sqrt((i+1)**4+1)/(2*(i+1)**2)
    return w
g=int(input("digite el numero de intervalos "))
r=math.sqrt(2)/g
x=0
for j in range(1,g+1):
    z=num(j)
    x+=z
print(x*r)

