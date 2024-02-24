#Colecciones que guardan en un mismo espacio una clave y un valor
dic={10:"Messi",7:"El bicho",9:"El gato"}
print(dic[10])#Muestra el valor que acompaña a la clave
dic[11]="Bale"#Agrega un nuevo elemento
dic[9]="Lewandoski"#modifica un elemento
print(dic)
del(dic[11])#Elimina el elemento con clave 11
print(dic)
print(dic.get(10,"no existe ese numero"))#Se usa si no se sabe si el valor esta en el diccionario y así evita que salga el error
a=list(dic.keys())
print(a)