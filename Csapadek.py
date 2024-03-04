#létrehoztunk egy aprilisiCsapadek nevű tömböt
aprilisiCsapadek = []
#megnyitjuk a kívánt txt file-t
with open('Aprilis_csapadek.txt', 'r') as file:
    #kiolvassa soronként az értékeket
    for line in file:
        #elhelyezi a számokat a tömbben
        aprilisiCsapadek.append(int(line.strip()))

osszes= sum(aprilisiCsapadek)
print(osszes)
i = 0
while i<len(aprilisiCsapadek) or aprilisiCsapadek[i]>8000:
    i= i+1
melyik_nap=-1
if i==len(aprilisiCsapadek):
    print("Nincs ilyen elem")
else:
    melyik_nap= aprilisiCsapadek[i]

#3. Hányszor volt a vízállás 9000 mm fölött?
i=0
kilencezerFelett=0
while i<len(aprilisiCsapadek):
    if aprilisiCsapadek[i]>9000:
        kilencezerFelett= kilencezerFelett+1
    i=i+1
#4. Mennyi volt a hónap második felének a vízállása?
i= int(len(aprilisiCsapadek)/2 -1)
masodikfel=0
while i<len(aprilisiCsapadek):
    masodikfel= masodikfel+aprilisiCsapadek[i]
    i=i+1
#7. Mennyi volt a hónapban a legmagasabb és a legalacsonyabb érték?
minimum= min(aprilisiCsapadek)
maximum= max(aprilisiCsapadek)





