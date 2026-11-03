import random

while True:
    x = random.randint(0,50)
    if x % 2 == 0 and x != 0:
        print (x,' je parne')
    elif x % 2 != 0:
        print(x,' je neparne')
    elif x ==0:
        break

y = 1
z = 0
while y != z:
    y = random.randint(0,20)
    z = random.randint(0,20)
    if y > z:
        print(y,' je vacsie')
        print(z,' je mensie')
    elif z > y:
        print(z,' je vacsie')
        print(y,' je mensie')


