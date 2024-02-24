#Bucle que si tiene sus repeticiones definidas, ya sea por una coleccion, una cadena o un objeto
for i in[1,5,4,"Jose",8.98]:#Lista,tupla,conjunto o diccionario
    print("Jaja salu2")#Se ejecuta el codigo del bucle cuantas veces encuentre un elemento en la coleccion
dic={2:"cacerola",3:"Jose"}
for nom in dic:
    print(dic[nom])
    print(nom)
for clave,valor in dic.items():
    print(clave,valor)
    