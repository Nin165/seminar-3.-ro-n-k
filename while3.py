number = int(input('zadaj cislo: '))
sucet = 0 #iniciacia
mocdes= 1
while number > 0:
    cifra = number % 3
    sucet += cifra*mocdes
    mocdes= mocdes*10
    number = number // 3
print(f'cislo v dvoj sustave je {sucet}')

n = int(input('zadaj cislo: '))
de = 2
while n != 1:
    if n % de ==0 :
        print(de, end='')
        n = n //de
    else:
        de += 1

print(' ')
nu = int(input('cislo: '))
deli = 0
for i in range(2, int(nu**0.5)):
    if nu % i ==0:
        deli += 1
        print('nie je')
        break
if deli ==0:
    print('je prvocislo') #pocitacova bezpecnost a asymetricke sifrovanie je sucet obrovskych prvocisel