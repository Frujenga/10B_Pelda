#print("Paprikás krumpli")

#01) Írd ki egytől ötig a számokat egyesével
a=1
while(a<=5):
    print(a)
    a=a+1
# 2) Kérj be egy számot és ha az nagyobb 8-nál írd ki: "Nagyobb 8-nál", 
# különben azt "Kisebb 8-nál"

#szam= input("Adj meg egy számot, kérlek ")
#szam = int(szam)
szam = 0

if(szam<8):
    print("A szám kisebb 8-nál")
elif(szam>8):
    print("A szám nagyobb 8-nál")
else:
    print("A szám értéke nyolc")

#03) Adj meg két szám változót és add meg az 
# összegüket, különbségüket, a szorzatukat és a hányadosukat
szam1= input("Kérem az első számot: ")
szam1= int(szam1)

szam2= input("Kérem a második számot: ")
szam2 = int(szam2)

print("Az összegük: ", szam1+szam2)
print("A különbségük:", szam1-szam)
print("A szorzatuk:", szam1*szam2)
print("A hányadosuk:", szam1/szam2)

#4) Kérj be nyolc számot és számítsd ki az átlagukat
szam3=0
i=0
while (i<8):
    j = input("Adj meg egy számot: ")
    j= int(j)
    szam3 = szam3+j
    i= i+1
print(szam3)

#Írd ki a kettőnek a hatványait n= 20-ig

ertek=2
eredetiertek=2
n=1
while(n<=20):
    ertek= ertek*eredetiertek
    print(ertek)
    n=n+1
