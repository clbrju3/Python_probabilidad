def fi(l):
 for i in range (len(l)-1):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            z=l[j]
            l.pop(j)
            l.insert(j+1,z)
    else:
        pass
 return(l)
