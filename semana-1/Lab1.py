num = 42

base = 2

#Primera division
residuo = num % base
cociente = num // base
bit1 = residuo

#Segunda division
residuo = cociente % base
cociente = cociente // base
bit2 = residuo

#Tercera division
residuo = cociente % base
cociente = cociente // base
bit3 = residuo

#Cuarta division
residuo = cociente % base
cociente = cociente // base
bit4 = residuo

#Quinta division
residuo = cociente % base
cociente = cociente // base
bit5 = residuo

#Sexto division
residuo = cociente % base
cociente = cociente // base
bit6 = residuo



print("{}={}{}{}{}{}{}".format(num,bit6,bit5,bit4,bit3,bit2,bit1))