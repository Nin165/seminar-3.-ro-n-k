number = int(input('zadaj cislo: '))
sucet = 0 #iniciacia
mocdes= 1
while number > 0:
    cifra = number % 3
    sucet += cifra*mocdes
    mocdes= mocdes*10
    number = number // 3
print(f'cislo v dvoj sustave je {sucet}')

