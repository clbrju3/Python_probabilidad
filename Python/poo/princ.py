from MOdulos import prenda
import os
def main():
    os.system("cls")
    a=input("Digite su talla: ")
    camisa=prenda()
    camisa.talla=a
    camisa.tipo="Camisa manga larga"
    print(f"Tipo:{camisa.tipo}")
    print(f"Talla:{camisa.talla}")
if __name__=="__main__":
    main()