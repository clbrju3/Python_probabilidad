
a,b,x,y=0,1,0,0
lista=[]
c=int(input("Digite los terminos de la secuencia de fibonacci que quiere: "))
if c%2==0:
 while x<(c/2):
    b=a+b
    a=b+a
    lista.append(b)
    lista.append(a)
    x+=1
else:
    while True:
        b=a+b
        a=b+a
        x+=1
        lista.append(b)
        if x>=c/2:
            break
        else:
            lista.append(a)
print(lista)

