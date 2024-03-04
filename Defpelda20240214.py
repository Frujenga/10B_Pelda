import random
import os

def radir():
    input("Nyomj egy gombot a terminál letörléséhez ")
    os.system('cls' if os.name=='nt' else 'clear')

def tombnagysagkeres(mennyiseg):
    i=0
    tomb=[]
    while i<mennyiseg:
        tomb.append(random.randint(0,1000))
        i=i+1
    return tomb

def kiirato(kiirandotomb):
    i=0
    while i<len(kiirandotomb):
        print(kiirandotomb[i])
        i=i+1

def osszead(osszeadandoszamok):
    i=0
    osszeg= 0
    while i<len(osszeadandoszamok):
        osszeg= osszeg+osszeadandoszamok[i]
        i=i+1
    return osszeg

def atlag1(atlagolandotomb):
    i=0
    osszeg= 0
    while i<len(atlagolandotomb):
        osszeg= osszeg+atlagolandotomb[i]
        i=i+1
    return (osszeg/len(atlagolandotomb))

def atlag2(atlagolandotomb):
    osszeg = osszead(atlagolandotomb)
    return osszead/len(atlagolandotomb)

def szorzas(szorzandotomb):
    szorzat=1
    i=0
    while i<len(szorzandotomb):
        szorzat= szorzat*szorzandotomb[i]
        i=i+1
    return szorzat


kellennyi = int(input("Hány elemű legyen a tömbünk?"))
eredmenytomb = tombnagysagkeres(kellennyi)
print("Sikeres tömb feltöltés")
kiirato(eredmenytomb)
osszeadasEredmenye = osszead(eredmenytomb)
radir()
print(osszeadasEredmenye)
print(osszead(eredmenytomb))
print(atlag2(eredmenytomb))
print(szorzas(eredmenytomb))