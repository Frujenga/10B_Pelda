def szorzas(szam1, szam2):
    return szam1*szam2

a = input("Adja meg melyik szorzó táblát szerezné?")
a= int(a)
i=0
while(i<=10):
    print(szorzas(a, i))
    i=i+1 