import random
import os

def radir():
    input("Nyomj egy gombot a terminál letörléséhez ")
    os.system('cls' if os.name=='nt' else 'clear')



tomb = []
hanydarabszam = int(input("Hány darab számot generáljak?"))
kezdet = int(input("Mely számtól kezdődjön a random?"))
vege = int(input("Mely számig legyen a random?"))
i = 0

while (i<hanydarabszam):
    tomb.append(random.randint(kezdet,vege))
    i=i+1

melyiket = int(input("melyik elemet írjam ki?"))

if(melyiket>(i-1)):
    print("Túl nagy számot írtál be")
else:
    print(tomb[melyiket])

radir()
i=0
while i<hanydarabszam:
    print(tomb[i])
    i=i+1
radir()
