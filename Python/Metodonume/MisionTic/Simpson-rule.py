import math
def coseno(siu, total):
    z=((siu*math.sqrt(math.pi))**2/((math.sqrt(2)*total)**2))
    w=math.cos(z)
    return w
num=int(input("Digite el numero de intervalos (Debe ser un numero par) "))
a=math.sqrt(math.pi)/(3*num*math.sqrt(2))
if(num%2!=0):
    print("Se le dijo que tenía que ser un numero par ")
else:
    c,u=0,0
    for i in range(num-1):
        x=coseno(i,num)+3*coseno(i+1,num)-coseno(i+2,num)
        c=c+x
    for j in range(2,num-1):
        y=(-1)**(j-1)*coseno(j,num)
        u=u+y
te=u+c
ter=te+2*coseno(num-1,num)
to=(ter*a)+2*coseno(num,num)
print(to)
    
    


