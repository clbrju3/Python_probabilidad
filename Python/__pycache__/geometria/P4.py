def mulmodulo(a,b):
    c=(a*b)%2
    return c
def dumodulo(a,b):
    c=(a+b)%2
    return c
def translaciones(plano):
    linea=[]
    for i in plano:
        for j in range(3):
            linea=[]
            for l in range(2):
                s=dumodulo(i[j][l][0],l)
                tupla=(s,i[j][l][1])
                linea.append(tupla)
            i[j][l]    

plano=[]
direccion=[]
linea=[]
punto1=(0,0)
punto2=(1,0)
linea.append(punto1)
linea.append(punto2)
direccion.append(linea)
plano.append(direccion)
for i in range(2):
    linea=[]
    direccion=[]
    for j in range(2):
        d=mulmodulo(i,j)
        tupla=(d,j)
        linea.append(tupla)
    direccion.append(linea)
    plano.append(direccion)
print(plano)