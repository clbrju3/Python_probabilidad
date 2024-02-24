from orden import fi as f
def u():
    with open("C:/Users/EQUIPO/Desktop/GLOBANT.csv","r") as t:
        a=t.readlines()
        return len(a)-1
li,r=[],[]
def l():
    with open("jose.csv","w") as t:
        t.write("Analisis de acciones\n")
    with open("C:/Users/EQUIPO/Desktop/GLOBANT.csv","r") as y:
        a=y.readline()
        for i in range(u()):
            a=y.readline().split(",")
            with open("jose.csv","a") as t:
                t.write(a[0]+"  ")
                f=float(a[1])-float(a[4])
                r.append(round(f,3))
                if f>0:
                    t.write("Baja\n")
                elif f==0:
                    t.write("Estable\n")
                else:
                    t.write("Sube\n")
    return r
w=f(l())
print("Valor menor:",w[0],"Valor mayor:",w[len(w)-1])
            
        