import pathlib
import os
def a(b):
    w=[]
    os.system("cls")
    for i in range(b):
        d=input("Nombre: ")
        c=input("duracion: ")
        e=input("Año: ")
        l=[d,c,e]
        w+=l
    return w
def siu(z):
    ruta=pathlib.Path(".")
    arch=ruta/"peli.csv"
    d=a(z)
    for i in range(z):
        if arch.exists():
            with open("peli.csv","a") as t:
                t.write(f"Nombre: {d[i*3]}\n")
                t.write(f"Nombre: {d[i*3+(1)]}\n")
                t.write(f"Nombre: {d[i*3+(2)]}\n")
        else:
            with open("peli.csv","w") as t:
                t.write(f"Nombre: {d[i*3]}\n")
                t.write(f"Nombre: {d[i*3+1]}\n")
                t.write(f"Nombre: {d[i*3+2]}\n")
    arch.replace(ruta/"mintic"/arch.name)
z=int(input("Digite el numero de peliculas que va a agregar: "))
siu(z)
