f=10
w=[1,2,3,4,5,6,7,8,9,10]
for i in range(1,round(f/2)+1):
    print(i)
    w.pop(i)
    print(w)
