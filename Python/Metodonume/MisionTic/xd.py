print("Digite la opcion que quiere\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Numero par o impar")
w,z,q,p,x=0,0,0,0,0
while w!=True or z!=True or x!=True or q!=True or p!=True:
    a=int(input("Digite la opcion que desea: "))
    while a<=0 or a>=6:
        print("Su numero no sirve ") 
        a=int(input("Digite una opcion valida: "))
    if a==1:
        print("Digite dos numeros: ")
        c,b=(input().split())
        c,b=int(c),int(b)
        print(c+b)
        w=True
    elif a==2:
        print("Digite dos numeros: ")
        c,b=(input().split())
        c,b=int(c),int(b)
        print(c-b)
        z=True
    elif a==3:
        print("Digite dos numeros: ")
        c,b=(input().split())
        c,b=int(c),int(b)
        print(c*b)
        x=True
    elif a==4:
        print("Digite dos numeros: ")
        c,b=(input().split())
        c,b=int(c),int(b)
        print(c/b)
        q=True
    elif a==5:
        print("Digite su numero: ")
        c=int(input())
        if c%2==0:
            print("Su numero es par")
        else:
            print("Su numero es impar")
        p=True

