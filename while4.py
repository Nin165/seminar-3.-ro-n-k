
'''cislo = int(input('cislo: '))
pocet = 0
while cislo > 0 :
    cifra = cislo % 10
    if cifra % 2 == 0 :
        pocet += 1
    cislo = cislo // 10
print(pocet)


c = int(input('cislo: '))
p = 0
if c == 0:
    p =1
elif c > 0:
    while c > 0:
        c = c // 10
        p += 1
print(p)

ci = int(input('cislo: '))
while ci > 0:
    print(ci % 10, end='')
    ci //= 10
print()


cis = int(input('cislo: '))
poz = 1
p = 0
d = 0
while cis > 0:
    cif = cis % 10
    if poz % 2 == 0:
        p = p*10 + cif
    else:
        d = d * 10 + cif
    poz += 1
    cis //= 10
print(p)
print(d)'''



cisl = int(input('cislo: '))
o=0
while cisl > 0:
   o=o*10 + (cisl % 10)
   cisl //= 10
pozi = 1
pr = 0
dr = 0
while o > 0:
    cifr = o % 10
    if pozi % 2 == 0:
        pr = pr*10 + cifr
    else:
        dr = dr * 10 + cifr
    pozi += 1
    o //= 10
print(pr)
print(dr)




