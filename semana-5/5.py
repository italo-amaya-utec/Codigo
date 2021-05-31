print("Ejercicio 1")
print("-"*40)
numeros = [1, 3, 5, 10]
#Programación Imperativa
suma = 0
for i in numeros:
    suma += i*2
print(suma)

#Programación declarativa
suma = sum([x*2 for x in numeros])
print(suma)
print()

print("Ejercicio 2")
print("-"*40)
nombres = ["JUAN", "KARLA", "MANUEL", "FIORELLA"]
nombres_minus = []
for nom in nombres:
    nom = nom.lower()
    nombres_minus.append(nom)
print(nombres_minus)

#Programación declarativa
nombres_minus = [nom.lower() for nom in nombres]
print(nombres_minus)

print()
print("Ejercicio 3")
print("-"*40)
#lee 5 números enteros desde teclado y almacénalos en una lista
lista = []
for i in range(5):
    n = int(input("ingrese un numero: "))
    lista.append(n)
print(lista)

#Programación declarativa
lista = [int(input()),int(input()),int(input()),int(input()),int(input())]
print(lista)


print()
print("Ejercicio 4")
print("-"*40)
numeros = [1,2,3,4,5]
pares = []
for i in numeros:
    if i%2 == 0:
        pares.apend(i)
print(pares)