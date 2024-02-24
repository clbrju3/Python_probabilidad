
dis,max,t=input().split()
dis=float(dis)
max=float(max)
t=int(t)
velocidad=dis/1000*3600/t
if velocidad<0 or max<0:
    print("ERROR")
elif velocidad<=max:
    print("OK")
else:
    if velocidad<max*1.2:
        print("MULTA")
    elif velocidad>=max*1.2:
        print("CURSO SENSIBILIZACION")

