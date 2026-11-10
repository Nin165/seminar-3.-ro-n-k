x=2
while x < 10:
    x = x + 3
    print(x)

p = 0
while p < 7:
    p+=1
    print('vytah sa zastavil na ', p)
print('vytah zastavil')

z = 0
po = 0
while z < 400:
    z = z + int(input('hmotnost osoby: '))
    po += 1
    if z > 400:
        print('hmotnost vsetkych je: ', z)
        print('pocet osob je: ', po)

import random


k=random.randint(1,100)
t = 0
while t != k:
    t = int(input('hladaj cislo: '))
    if t > k:
        print('cislo je mensie')
    else:
        print('cislo je vacsie')

print('uhadol si')