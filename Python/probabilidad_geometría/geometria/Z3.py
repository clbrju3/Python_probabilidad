def mulmodulo(a,b):
    c=(a*b)%3
    return c
def dumodulo(a,b):
    c=(a+b)%3
    return c

direcciones=[]
direccion=[]
for i in range(4):
    linea=[]
    for j in range(3):
        d=mulmodulo(i,j)
        linea.clear
        tupla=(d,j)
        linea.append(tupla)
    direcciones.append(linea)
print(direcciones)
    


    