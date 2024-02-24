def va(c,d,e):
    if c>=e[0] and c<=e[2]:
        if c<=e[1]:
            q=d[e[0]]
            return q
        else: 
            q=d[e[2]]
            return q
    else: 
        print("Este parametro no existe en la tienda")
        return d
sd={24.0:30000,27.0:350000,30.0:350000}
hy={16.0:350000,17.0:455000,18.0:455000}
hj={24.0:450000,26:475000,27.5:475000}
el,la,lo=list(sd.keys()),list(hy.keys()),list(hj.keys())
z=24.0
a=va(z,sd,el)
print(a)