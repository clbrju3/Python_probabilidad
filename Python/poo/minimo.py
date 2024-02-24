a,b=input("Digite dos enteros ").split()
a,b=int(a),int(b)
if a<b:
        for i in range(1,a+1):
            for j in range(1,b+1):
                if b*i==a*j:
                    break
            if b*i==a*j:
                m=b*i
                break
        
else:
        for i in range(1,b+1):
            for j in range(1,a+1):
                if b*j==a*i:
                    break
            if b*j==a*i:
                m=a*i
                break
    
print(m)
