import random

def simatomb():
    tomb = [1,2,3,4,5,6,7,8,9,10]
    i= 0
    while i<len(tomb):
        print(tomb[i])
        i= i+1

def bekerostomb():
    mennyi= int(input("Hány elemű legyen a tömbünk?"))
    i=0
    tomb2=[]
    while i<mennyi:
        tomb2.append(int(input("Adj egy számot, amit beteszek a tömbbe")))
        i= i+1
    print("Vége a feladatnak")

def randomtomb():
    mennyi= int(input("Hány elemű legyen a tömbünk?"))
    tomb3= []
    i=0
    while i<mennyi:
        tomb3.append(random.randint(0, 1000))
        print(tomb3[i])
        i= i+1
    print("Vége a feladatnak")





