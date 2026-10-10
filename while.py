sucet = 0
pocet = 0
cislo = (int(input('napis cislo: ')))
while cislo !=0:
    sucet += cislo
    pocet += 1
    cislo = (int(input('napis cislo: ')))
if pocet > 0:
    priemer = sucet/pocet
    print('arit. priemer je: ', priemer)


a = 0
while True:
    slovo = input('napis slovo: ')

    if slovo.lower().startswith('x'):
        break
    a += len(slovo)
print('celkovy pocet znakov je: ', a)


import random
random.randint(1,100)

while True:
    c = random.randint(1,100)
    print(c)
    if '8' in str(c):
        break

b = random.randint(1,5)
c = 0
d = int(input('napis cislo: '))
c += 1
while d!=b:
    print("zle")
    d = int(input('napis cislo: '))
    c+=1
print("spravne")


while True:
    e = random.randint(1,50)
    f = random.randint(1,50)
    print(e ,' + ', f)
    g = e + f
    h = int(input('vysledok: '))
    if g == h:
        print('spravne')
        break
    else:
        print('nespravne')


i= random.randint(1,100)
k = 0
while True:
    j= int(input('hadaj cislo: '))
    k += 1
    if i>j:
        print("pridaj")
    elif i<j:
        print("uber")
    elif i==j:
        print("spravne")
        print('pocet pokusov: ', k)
        break


def cs(cislo):
    cs = 0
    r = str(cislo)
    for z in r:
        cs += int(z)
    return cs
def hladaj(n):
    pocitadlo = 0
    x = 19
    while pocitadlo < n:
        if cs(x) == 10:
            print(x)
            pocitadlo += 1
        x = x + 1
hladaj(5)


def prvocislo(cis):
    if cis <2:
        return False
    for m in range(2,cis):
        if cis % m == 0:
            return False
    return True
def pprvocislo(o):
    ppocet = 0
    p = 2
    while ppocet < o:
        if prvocislo(p):
            print(p)
            ppocet += 1
        p = p + 1
pprvocislo(10)

