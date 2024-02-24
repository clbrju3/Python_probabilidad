'''El eje pedalier debe ubicarse entre 240 y 300 mm del piso.
Las bielas deben medir máximo 180 mm y mínimo 160 mm.
La longitud del sillín debe ser mínimo 240 mm y máximo 275mm
El manilar debe tener máximo 50 cm de ancho.
Por tal razón, le han encomendado a usted la selección de los diseños que cumplen con las 
condiciones del reglamento, así que debe construir el software que procesará los datos de las bases 
de datos donde reposan los diseños en el sistema.Su misión es crear un programa en Python que
permita mostrarle a los equipos ciclisticos la lista de las bicicletas que cumplen con los 
requerimientos y por supuesto el valor de las mismas para su consideración.'''

def va(c,d,e):
    if c>=e[0] and c<=e[2]:
        if c<=e[1]:
            q=d[e[0]]
            return q
        else: 
            q=d[e[2]]
            return q
    else: 
        print("Este parametro no existe en la tienda")
        return False
def fu(c):
    c=input().split()
    c[0],c[1]=float(c[0]),c[1].upper()
    while len(c)!=2:
        c=input("Digite de nuevo la medida, deber ser una longitud y su unidad: ").split()
    while c[1]!="CM" and c[1]!="M" and c[1]!="MM":
        c=input("Solo se pueden leer datos en mm,cm o m\nDigite de nuevo la medida y la unidad: ").split()
        c[0],c[1]=float(c[0]),c[1].upper()
    if c[1]=="MM":
        c[0]/=10
        return c[0]
    elif c[1]=="CM":
        return c[0]
    elif c[1]=="M":
        c[0]*=100
        return c[0]
def res(med):
    med[0]=float(med[0])
    med[1]=med[1].upper()
    return med
sd={24.0:30000,27.0:350000,30.0:350000}
hy={16.0:350000,17.0:455000,18.0:455000}
hj={24.0:450000,26:475000,27.5:475000}
el,la,lo=list(sd.keys()),list(hy.keys()),list(hj.keys())
b,c,d=[],[],[]
a=int(input("Digite el numero de bicicletas que necesita: "))
for i in range(a):
    print(f"Digite las medidas de la bicicleta: #{i+1}")
    b.append(fu(b))
    c.append(fu(c))
    d.append(fu(d))
    w=b+c+d
    y=va(w[0],sd,el)
    z=va(w[1],hy,la)
    tr=va(w[2],hj,lo)
    if y==False or z==False or tr==False:
        print("Su artículo no existe en la tienda")
    else:
        print(f"El valor de su bicicleta es: {y+z+tr}")
    


    
    