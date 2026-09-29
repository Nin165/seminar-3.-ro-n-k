# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


for o in range(1,11):
    print(o)

n = int(input("cislo"))
for i in range (1,n+1):
    print(i, end=",")
print(" ")
for n in range (1,16):
    if n ==15:
        print(n, end=".")

    else:
        print(n, end=",")
print(" ")
j=15
for j in range(5,j+1,2):
    print(j,end=",")