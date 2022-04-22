#Calculator

def sumar(a,b):
    print (f"{a} {op} {b} =  {a+b}")
    return a+b
def restar(a,b):
    print (f"{a} {op} {b} =  {a-b}")
    return a-b
def multiplicar(a,b):
    print (f"{a} {op} {b} =  {a*b}")
    return a*b
def dividir(a,b):
    print (f"{a} {op} {b} =  {a/b}")
    return a/b
a = float(input("Whats the first number?: "))
continuar = True
while(continuar):
    op = input("+ \n-\n*\n/\n Pick an operation(only one of those): ")
    b = float(input("whats the next number?: "))
    if op == '+':
        a = sumar(a,b)
    elif op == '-':
        a = restar(a,b)
    elif op == '*':
        a = multiplicar(a,b)
    else:
        a = dividir(a,b)
    if(input("Quieres salir 'y' o 'n'?:") == 'n'):
        if input(f"Type 'y' to continue calculating with {a}, or type 'n' to start a new calculation: ") == 'n':
            a = float(input("Whats the first number?: "))
    else:
        continuar = False