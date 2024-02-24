'''
csvdict.py

modulo que toma un archivo y
lo analiza
'''
import csv
import pathlib
import os
def com():
    l=[]
    c=["fecha","comportamiento"]
    if not pathlib.Path("com.csv").exists():
        with open("com.csv","w",newline="") as t:
            writer=csv.DictWriter(t, fieldnames=c)
            writer.writeheader()
    with open("C:/Users/EQUIPO/Desktop/GLOBANT.csv","r", newline="") as v:
        reader=csv.DictReader(v)
        for i in reader:
            f=list(i.keys())
            l.append(round((float(i[f[1]])-float(i[f[4]])),4))
            with open("com.csv","a",newline="") as t:
                writer=csv.DictWriter(t, fieldnames=c, delimiter=";")
                if float(i[f[1]])-float(i[f[4]])>0:
                    writer.writerow({c[0]:i[f[0]],c[1]:"Baja"})
                else:
                    writer.writerow({c[0]:i[f[0]],c[1]:"Sube"})
    return l
def siu():
    ruta=pathlib.Path("mintic")
    ca=ruta/"Analisis"
    arch=pathlib.Path("com.csv")
    ca.mkdir()
    arch.replace(ca/"com.csv")
def comp():
    l,k=[],[]
    os.system("cls")
    d=com()
    for i in d:
        if i>0:
            l.append(i)
        else:
            k.append(i)
    print(f"El máximo incremento es {max(d)}\nEl mínimo incremento fue {min(l)}\nEl máximo decremento fue {min(d)}\n el mínimo decremento fue {max(k)}")
    with open("com.csv","a",newline="") as x:
        y=["relacion","max","min"]
        writer=csv.DictWriter(x,fieldnames=y)
        writer.writeheader()
        writer.writerow({y[0]:"Aumento",y[1]:max(d),y[2]:min(l)})
        writer.writerow({y[0]:"Decremento",y[1]:min(d),y[2]:max(k)})
def main():
    if not pathlib.Path("com.csv").exists():
        comp()
    siu()
if __name__=="__main__":
    main()
