import csv
#a=input("Digite pelicula y eso ").split()
#with open("nombre.csv","a",newline="") as t:
    #writer= csv.writer(t,delimiter=",")
    #writer.writerow([a[0],a[1],a[2]])
with open("nombre.csv","r",newline="") as x:
    reader= csv.reader(x)
    for i in reader:
        print(i)