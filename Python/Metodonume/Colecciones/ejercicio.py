a=set([1,4,3,"Mateo","Jose",6,2,2,3,4])#Elimina los elementos repetidos volviendolo un conjunto
b=set([2,5,4,"Jose",6])
d=a&b
e=a-b
f=b-a
print("Elementos compartidos",d,"elementos de a y no de b",e,"elementos de b pero no de a",f)