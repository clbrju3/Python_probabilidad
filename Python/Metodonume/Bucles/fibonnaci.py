
a,b,x=0,1,0
lista=[]
c=int(input("Digite los terminos de la secuencia de fibonacci que quiere: "))
while x<c/2:
    b=a+b
    a=b+a
    x+=1
    lista.append(a)
    lista.append(b)
#lista=lista.sort(reverse=False)
for i in range(c-1):
    if lista[i]>lista[i+1]:
        z=lista[i]
        lista.pop(i)
        lista.insert(i+1,z)
    else:
        pass
for i in range(c):
    print(lista[i],end=(" ,"))
