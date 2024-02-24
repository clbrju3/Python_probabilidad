def su(a):
    b=[]
    for i in a:
        z=str(i).strip()
        b.append(z)
    return b
def error(k):
    a=[]
    a=input("Digite el nuevo documento etc: ").split()
    while True:
        for i in range(0,len(k),4):
            if k[i]==a[0]:
                a[0]=input("Digite otro documento ")
            else:
                break
        return a
def ing(k):
    a=error(k)
    with open("cono.txt","a") as t:
        for i in a:
            t.write(i+"\n")
def eli(k):
    a=input("Digite el documento ")
    for i in range(0,len(k),4):
        if k[i]==a:
            w=i
    with open("cono.txt","w") as t:
        if w==0:
            t.write(k[4]+"\n")
        else:
            t.write(k[0]+"\n")
    for i in range(1,w):
        with open("cono.txt","a") as t:
            t.write(k[i]+"\n")
    for i in range(w+4,len(k)):
        with open("cono.txt","a") as t:
            t.write(k[i]+"\n")
def act(k):
    a=input("Digite el documento que quiere modificar datos: ")
    for i in range(0,len(k),4):
        if k[i]==a:
            w=i
            print(w)
    b=input("Quiere cambiar el documento? ").lower()
    if b=="si":
        c=input("Digite el nuevo documento ")
        with open("cono.txt","w") as t:
            for i in range(w):
                t.write(k[i]+"\n")
            t.write(c+"\n")
        with open("cono.txt","a") as t:
            for i in range(w+1,len(k)):
                t.write(k[i]+"\n")
        return b
    if b=="no":
        c=input("Digite el nuevo correo ")
        with open("cono.txt","w") as t:
            for i in range(w+3):
                t.write(k[i]+"\n")
            t.write(c+"\n")
        with open("cono.txt","a") as t:
            for i in range(w+4,len(k)):
                t.write(k[i]+"\n")
with open ("cono.txt","r") as t:
    k=t.readlines()
    k=su(k)
w=input("Digite la operacion ")
c=0
if w=="ing":
    z=int(input("Digite el numero de ususarios "))
    while True:
        ing(k)
        c+=1
        if c==z:
           break
if w=="eli":
    eli(k)
if w=="act":
    act(k)
else:
    print(k)
