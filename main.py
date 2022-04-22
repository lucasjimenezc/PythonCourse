#import numpy as np

def importar():
    
    with open('texto.txt') as f:
        x = 0
        y = 0
        palabras = []
        for o in range(10):
            palabras.append([""])
        for linea in f:
            p = ""
            for i in linea:
                if(i == " " or i == "\n"):
                    palabras[x][y] = p
                    p = ""
                    y += 1
                else:
                    p += i
            x += 1
        print(palabras)

            
        

                



def main():
    print("Bienvenido\n")
    salir = False
    while(not salir):
        a = input("1-Importar palabras clave\n2-Mostrar palabras clave\n0-Salir\n");
        if(a == '1'):
            importar()
        elif(a == '2'):
            print("mostrar()")
        elif(a == '0'):
            salir = True
            print("------Adios------")
        else:
            print("------Caracter invalido-------")


if __name__ == "__main__":
    main()

