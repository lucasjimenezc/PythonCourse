
def encrypt(message, shift):
    
    for l in range(len(message)):
        lista = list(message)
        n = ord(message[l])
        for i in range(shift):
            if n == 90:
                n = 65
            elif n == 122:
                n = 97
            else:
                if n != 32:
                    n += 1 
        lista[l] = chr(n)
        message = ''.join(lista)
    print(f"Here's the result {message}!")
seguir = True
while(seguir):
    if input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") == "encode":
        message = input("Type your message\n")
        shift = int(input("Type the shift number\n"))
        encrypt(message,shift%26)
    else:
        message = input("Type your message\n")
        shift = int(input("Type the shift number\n"))
        encrypt(message,26 -shift%26)
    if input("Type 'yes if you want to go again. Otherwise type 'no'.\n") != "yes":
        seguir = False
        print("Goodbye")
        