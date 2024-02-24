#El colegio Los Robles, tiene actualmente 750 estudiantes. Se espera tener un crecimiento anual de 12%. 
#Elabore un algoritmo que calcule e imprima la población estudiantil que se espera tener en el año 2035
es=int(input("Digite cuantas bendiciones hay: "))
w=es
a=int(input("Digite el año del cual quiere proyectar el crecimiento: "))
x=2022
while x<a:
    z=es
    ar=es*0.12
    es+=ar
    x+=1
    print(f"Año {x}: {round(es-z,0)}")
print(f"Crecimiento total={round(es-w,0)}")
