nakup=[]
for i in range(5):
    i=input('produkt: ')
    nakup.append(i)
print(nakup)

teplota=[]
for i in range(5):
    teplota.append(int(input('teplota: ')))
print(teplota)
print('najvyssia: ',max(teplota),' najnizsia: ',min(teplota))
print('priemer', sum(teplota)/len(teplota))

body=[]
for z in range(6):
    z=int(input('body ziaka: '))
    body.append(z)
print(body,'priemer= ',sum(body)/len(body))
poc=0
for p in body:
    if p>=15:
        poc+=1
print(poc)
#list comprehension
cisla = [c for c in range(1,21)]
print(cisla)

mocniny = [m **2 for m in range(1,11)]
print(mocniny)

cislaa = [n for n in range(1,51)if n %5==0]
print(cislaa)

znamky = [int(input('znamky: ')) for z in range(5)]
print(znamky,'priemer: ',sum(znamky)/len(znamky))
