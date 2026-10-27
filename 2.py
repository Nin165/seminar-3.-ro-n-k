number = int(input('zadaj cislo: '))
sucet = 0 #iniciacia
while number > 0:
    cifra = number % 10
    sucet += cifra
    number = number // 10
print(f'sucet cifier je {sucet}')
