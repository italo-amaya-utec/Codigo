#Parte de Mathias de la 1 al 5
#Problema 1
print("Problema 1")
bit1 = Prob1//8
bit2 = Prob1%8
print(bit1)
print(bit2)
print("{} = {}{}".format(Prob1,bit1,bit2))
#Problema 2
print("Problema 2")
bit1 = Prob2//8
bit2 = Prob2%8
print(bit1)
print(bit2)
print("{} = {}{}".format(Prob2,bit1,bit2))
#Problema 3
print("Problema 3")
bit1 = Prob3//16
bit2 = Prob3%16
print(bit1)
print(bit2)
print("{} = {}{}".format(Prob3,bit1,bit2))
#Problema 4
print("Problema 4")
bit1 = Prob4//16
bit2 = Prob4%16
print(bit1)
print(bit2)
print("{} = {}{}".format(Prob4,bit1,bit2))
#Problema 5
print("Problema 5")
bit1 = Prob5//16
bit2 = Prob5%16
print(bit1)
print(bit2)
print("{} = {}{}".format(Prob5,bit1,bit2))

#================================================
# Parte de Italo de la 10 a la 15
print("parte de Italo")
def converter(n=0,b=0):
    #n = int(input("Introduce decimal number:"))
    #b = int(input("introduce base:  ... exmpl, binary is base 2 and hex is base 16"))
    l = []
    while n > 0:
        digit = n % b
        l.append(digit)
        n = int(n/b)
    l.reverse()
    string_list = [str(int) for int in l]
    string = "".join(string_list)
    if b == 2:
        print("0b" + string)
    if b == 16:
        print("0x" + string)
    if b == 8:
        print("0o" + string)

#pregunta 10
print("\npregunta 10 : ")
converter(788,2)
#pregunta 11
print("-----\npregunta 11 : ")
converter(1023,2)
#pregunta 12
print("------\npregunta 12 : ")
converter(1054,16)
#pregunta 13
print("------\npregunta 13 : ")
converter(3054,8)
#pregunta 14
print("-------\npregunta 14 : ")
converter(5785,2)
#pregunta 15
print("--------\npregunta 15 : ")
converter(15850,16)

#Parte de Nicol‡s de la 7 a la 9
print("parte de Nicol‡s")
ej6=104;ej7=254;ej8=305;ej9=587
print("Ejercicio 6:")
print(format(ej6,'0b'))
print("Ejercicio 7:")
print(format(ej7,'0b'))
print("Ejercicio 8:")
print(format(ej8,'0x'))
print("Ejercicio 9:")
print(format(ej9,'0o'))
