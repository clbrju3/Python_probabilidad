'''El eje pedalier debe ubicarse entre 240 y 300 mm del piso.
Las bielas deben medir máximo 180 mm y mínimo 160 mm.
La longitud del sillín debe ser mínimo 240 mm y máximo 275mm
El manilar debe tener máximo 50 cm de ancho.
Por tal razón, le han encomendado a usted la selección de los diseños que cumplen con las 
condiciones del reglamento, así que debe construir el software que procesará los datos de las bases 
de datos donde reposan los diseños en el sistema.Su misión es crear un programa en Python que
permita mostrarle a los equipos ciclisticos la lista de las bicicletas que cumplen con los 
requerimientos y por supuesto el valor de las mismas para su consideración.'''
def res(med):
    med[0]=float(med[0])
    med[1]=med[1].upper()
    return med
def fu(medida,i,a):
    if medida[1]=="MM":
        medida[0]/=10
        return medida
    elif medida[1]=="CM":
        return medida
    elif medida[1]=="M":
        medida[0]*=100
        return medida
    else: 
        while medida[1]!="MM" and medida[1]!="CM" and medida[1]!="M":
            medida[1]=input(f"Digite la unidad correcta de la medida #{a}\nde la bicicleta #{i+1}: ").upper()
            print (medida[1])
        if medida[1]=="MM":
            medida[0]/=10
            return medida
        elif medida[1]=="CM":
            return medida
        elif medida[1]=="M":
            medida[0]*=100
            return medida
    
a=int(input("Digite el numero de bicicletas que necesita: "))
precios={}
q=0
x=False
for i in range(a):
    print(f"Digite las caracteristicas de su bicicleta numero {i+1}")
    b=input().split()
    p=1
    c=input().split()
    xd=2
    d=input().split()
    xc=3
    c,b,d=res(c),res(b),res(d)
    b,c,d=fu(b,i,p),fu(c,i,xd),fu(d,i,xc)
    lisa=[b,c,d]
    if b[0]>=24 and b[0]<=30:
        if b[0]<=27:
            precios[0]=30000
        else: 
            precios[0]=35000
    else:
        print("No existe")
        x=True
    if c[0]>=16 and c[0]<=18:
        if c[0]<=17:
            precios[1]=30000
        else: 
            precios[1]=35000
    else:
        print("No existe")
        x=True
    if d[0]>=24 and d[0]<=27.5:
        if c[0]<=25:
            precios[2]=30000
        else: 
            precios[2]=35000
    else:
        print("No existe")
        x=True
    if x==False:
        for i in range(3):
            q+=precios[i]
            print(f"El precio de su bicicleta es {q}")
    else:
        print("Su bicicleta no existe")




