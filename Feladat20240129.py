import random

a= int(input("Kérlek adj meg egy számot 0 és 99 között "))
b =random.randint(0,99)

while (a!=b):
    if(a<b):
        print("a szám kisebb a bekért számnál")
    else:
        print("A szám nagyobb a bekért számnál")
    print(b)
    b= random.randint(0,99)
    
print("A számok egyenlőek")