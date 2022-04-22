#Hangman - Day 7
import random


palabras = ["casa","coche","barco","piso","hospital"]
palabra = palabras[random.randint(0,4)]
print("Bienvenido al ahorcado")
vidas = 5
actual = ""
for i in range(len(palabra)):
    actual += "_"
fin = False
while vidas > 0 and not fin:
    print(actual)
    esta = False
    letra = input("\nIntroduce una letra\n")
    indice = 0
    for a in palabra:
        if a == letra:
            list_ = list(actual)
            list_[indice] = letra
            actual = ''.join(list_)
            esta = True
        indice += 1
    if not esta:
        vidas -= 1
    if palabra == actual:
        fin = True
if(vidas < 0):
    print("\n Te has quedado sin vidas")
else:
    print("Enhorabuena")

    