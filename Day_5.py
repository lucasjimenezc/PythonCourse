#Password generator Day 5
import random

password = ""

n_letters = int(input("How many letters would you like in your password?\n"))
n_simbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))

for i in range(n_letters):
    if random.randint(0,1) == 0:
        password += chr(random.randint(65,90))
    else:
        password += chr(random.randint(97,122))

for i in range(n_simbols):
    a =random.randint(0,3)
    if a == 0:
        password += chr(random.randint(33,47))
    elif a == 1:
        password += chr(random.randint(58,64))
    elif a == 2:
        password += chr(random.randint(91,96))
    elif a == 3:
        password += chr(random.randint(123,126))

for i in range(n_numbers):
    password += chr(random.randint(48,57))


print(''.join(random.sample(password,len(password))))