from tkinter import W


def usi(a):
    if a==0 or a==1:
        return a
    elif a>1:
        #print(a+usi(a-1))
        return a+usi(a-1)
z=open("mi.txt","w")
for i in range(10):
    z.write(f"{i}")