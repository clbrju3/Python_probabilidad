#En un juego de preguntas a las que se responde Si o No gana quien responda correctamente las tres preguntas.
#Si se responde mal a cualquiera de ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:
# ¿Colon descubrió América?  ¿La independencia de México fue en el año 1810?  ¿The Doors fue un grupo de rock Americano?
print("Bienvenido al juego xd")
a=input("Responda las preguntas, si contesta mal se termina el juego\n ¿Colon descubrió América? ").upper()
w=0
if(a=="SI"):
        print("CORRECTO!")
        w+=1
        b=input("Siguiente pregunta:\n ¿La independencia de México fue en el año 1810? ").upper()
        if(b=="SI"):
            print("CORRECTO")
            w+=1
            c=input("Siguiente y ultima pregunta:\n ¿The Doors fue un grupo de rock Americano? ").upper()
            if(c=="SI"):
               print("CORRECTO!\nGanó el juego")
               w+=1
            else:
                print("Perdió con 0 puntos")
        else:
            print("Perdió con 1 punto")
else:
    print("Perdió con 2 puntos")
if w==3:
    print("Ganó el juego con puntuacion perfecta ")
else:
    pass
