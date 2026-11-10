# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#for o in range(1,11):
 #   print(o)

#n = int(input("cislo"))
#for i in range (1,n+1):
 #   print(i, end=",")
#print(" ")
#for n in range (1,16):
 #   if n ==15:
  #      print(n, end=".")

   # else:
    #    print(n, end=",")
#print(" ")
#j=15
#for j in range(5,j+1,2):
#    print(j,end=",")

def mocnina(n):
    for b in range (1,n+1):
        print(b, b**2)
mocnina(9)

def mocnina2(odkial,pokial):
    for c in range (odkial, pokial+1):
        print(c)
mocnina2(odkial=2,pokial=8)

for x in range (1,21):
    if x==3:
        print('funkcia nie je definovana')
    else:
        y = (x**2-1)/(x-3)
        print('x=', x ,' y=', y)


def del3(e):
    for d in range (1,e+1):
        if d % 3 == 0:
            print(d)
del3(10)

for f in range (1,21):
    if f % 2 == 0:
        print(f)

def zk(z,k):
    for g in range (z,k+1):
        if g % 2 != 0:
            print(g)
zk(z=6,k=10)

def n(n):
    for h in range (n, 0,-1):
        print(h, end=' ')
n(5)

