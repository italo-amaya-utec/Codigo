# ejercicio 
import random
def uno():
    n = random.randint(1,9)
    for i in range(1,n):
        for e in range(1,n):
            print("*", end=" ")
        print("")
uno()
#ejer 2

def dos():
    n = random.randint(1,9)
    for i in range(1,n):
        for e in range(1,i):
            print("*", end=" ")
        print("")
dos()

#ejer 3

def tres():
    n = 4#random.randint(1,9)
    for i in range(1,n):
        for e in range(1,n):
            print("*", end=" ") if e % i == 0 or i % e == 0 else print(" ",end=" ")
        print(i)

tres()

#quatro

def quatro():
    n = random.randint(1,9)
    for i in range(1,n+1):
        for e in range(1,i):
            print(e, end=" ")
        print(i)
quatro()












