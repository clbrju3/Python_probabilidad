def pre(a,b,c):
    print("Su producto es",a,"su precio con descuento es",(b-(b*c/10)))
a,b,c=input("Digite el nombre del producto, su precio y por ultimo el codigo de descuento ").split()
b=int(b)
c=int(c)
while c<0 or c>2:
    c=int(input("Su numero de descuento no es valido, digitelo de nuevo: "))
if c==0:
    pre(a,b,c)
if c==1:
    pre(a,b,c)
if c==2:
    pre(a,b,c)

    