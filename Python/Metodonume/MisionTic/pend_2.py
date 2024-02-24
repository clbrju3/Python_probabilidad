#En un estacionamiento cobran $ 1.500 por hora o fracción. 
#Diseñe un algoritmo que determine cuanto debe pagar un cliente por el estacionamiento de su vehículo, 
#conociendo el tiempo de estacionamiento en horas y minutos.
a=int(input("Digite el tiempo en minutos "))
hor=int(a/60)+1
val=1500*hor
print(val)

