def repre(a):
    res=""
    j=1
    while(j<buscar(a)[2]):
        res+="0"
        j+=1
    return res+"1"
def fibo(a):
    if(a<2):
        return a
    else:
        return fibo(a-2)+fibo(a-1)
def buscar(a):
    i=2
    fibon=[]
    f=0
    while(fibo(i)<=a):
        f=fibo(i)
        fibon.append(f)
        i+=1
    return [fibon,f,len(fibon)]
re=[]
a1=input("Digite el numero que quiere representar: ")
a=int(a1)
if(buscar(a)[1]==a):
    print(a1+" = ("+repre(a)+")f")
else:
    f1=a-buscar(a)[1]
    r0=repre(a)
    while(True):
        f1=a-buscar(a)[1]
        re.append(buscar(f1)[2])
        a=f1
        f1=f1-buscar(f1)[1]
        if(f1==0):
             break
    res=list(r0)
    for i in re:
        res[i-1]="1"
        r= "".join(res)
    print(a1+" = ("+r+")f")
            
