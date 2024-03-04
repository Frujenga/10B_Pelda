def osszead(a,b):
    return a+b

def kivon(a,b):
    return a-b

def szoroz(a,b):
    return a*b

def oszt(a,b):
    if(b==0):
        return "nem osztható semmi sem nullával"
    else:
        return a/b

elsoszam= int(input("Kérem az 'a' értéket"))
masodikszam = int(input("Kérem a 'b' értéket"))

print(osszead(elsoszam,masodikszam))
print(kivon(elsoszam,masodikszam))
print(szoroz(elsoszam,masodikszam))
print(oszt(elsoszam,masodikszam))