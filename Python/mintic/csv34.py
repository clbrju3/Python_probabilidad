import numpy as n
lista1=[]
def y():
    with open("C:/Users/EQUIPO/Desktop/libro.csv","r") as t:
        a=t.readlines()
        return len(a)-1
def l():
 with open("Datos_csv.csv","w") as t:
    t.write("Analisis de datos csv\n")
 with open("C:/Users/EQUIPO/Desktop/libro.csv","r") as t:
    datos=t.readline()
    for i in range(y()):
        datos=t.readline().split(";")
        lista1.append(datos[0])
 with open("Datos_csv.csv","a") as t:
    for i in lista1:
        t.write(i+"siu\n")
l()

 

        
