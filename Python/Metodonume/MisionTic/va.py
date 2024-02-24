def pr(genero,tipo):
    if genero=="MASCULINO" or genero=="HOMBRE":
        print("Usted es un",tipo)
    if genero=="FEMENINO" or genero=="MUJER":
        print("Usted es una",tipo)
def pre(edad,genero):
    if edad<=5 :
        return "bebe"
    elif edad<=12:
        if genero=="MASCULINO" or genero=="HOMBRE":
            return "niño grande"
        elif genero=="FEMENINO" or genero=="MUJER":
            return "niña grande"
    elif edad<=20:
        return "adolescente"
    elif edad<=55:
        if genero=="HOMBRE" or genero=="MASCULINO":
            return "adulto"
        elif genero=="FEMENINO" or genero=="MUJER":
            return "adulta"
    elif edad<=120:
        if genero=="MASCULINO" or genero=="HOMBRE":
            return "adulto mayor"
        elif genero=="FEMENINO" or genero=="MUJER":
            return "adulta mayor"
c=int(input("Digite su edad "))
while c<0 or c>120:
    c=int(input("Edad no valida, digite su edad: "))
a=input("Digite su genero ").upper()
b=pre(c,a)
pr(a,b)

    

    

