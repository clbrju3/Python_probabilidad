#Grupo de elemntos sin orden específico delimitado por {} y no acepta elementos repetidos
conjunto=set()#Se usa este metodo para diferenciarlo de los diccionarios
conjunto={1,2,3,"juan",6.45,True}
conjunto.add(4)
#operaciones entre conjuntos
con=set()
con={3,6,8,"jose",2,False}
w=conjunto|con
#Se puede convertir una lista en conjunto así
b=[1,5,4,2,3,2,True,True]
print(b)
a=set(b)
print(a)
