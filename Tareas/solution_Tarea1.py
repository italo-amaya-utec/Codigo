class Solution:
    # RECORDAR RETORNAR LA RESPUESTA

    def palabrasUtecsinas(self, palabra):
        dic = {
            "u" : False,
            "t" : False,
            "e" : False,
            "c" : False
        }
        list = ["u","t","e","c"]
        for letra in palabra:
            for character in list:
                if letra == character:
                    dic[character] = True
        if dic["u"] == True and dic["t"] == True and dic["e"] == True and dic["c"] == True:
            return True
        else:
            return False

    def aprobe(self,T1,T2,E1,E2,TC,P1,P2):
        modulo_1 = (0.15)*T1 + (0.15)*T2 + (0.35)*E1 + (0.35)*E2
        modulo_2 = (0.3)*TC + (0.15)*P1 + (0.45)*P2

        return True if modulo_1 >= 10.5 and modulo_2 >= 10.5 else False

    def IMvsCap (self,mensaje):
        i = 0
        c = 0
        def res():
            if i > c:
                return "Iron Man"
            elif c > i:
                return "Capitan America"
            elif c == i:
                return "Empate"

        for letra in mensaje:
            if letra == "I":
                i += 1
            if letra == "C":
                c += 1

        return res()

    def rectanguloEspecial(self,longitud,altura,letra_base,letra_especial):
        det = abs(longitud - altura)
        # this checks is all the parameters are valid for the program
        def checks():
            if longitud == altura and longitud == 0 or altura == 0:
                print("Problemas con la altura y la longitud")
        # this prints the  rectangle with the condition 
        def rectangulo():
            rsp = ""
            for row in range(0,altura):
                for column in range(0,longitud):
                    if special(row,column):
                        rsp = rsp + letra_especial + ""
                    else:
                        rsp = rsp + letra_base + ""
                if row != altura-1:
                    rsp = rsp + "\n"


            return rsp
        ## Checks the special condition
        def special(i,j):
            return True if (i+j) % det == 0 else False
        
        #executes the code
        checks()
        return rectangulo()

# === CASOS EJEMPLO ===
print(Solution().palabrasUtecsinas("cuenta")) # output en consola: True
print(Solution().aprobe(13,15,16,11,17,10,13)) # output en consola: True
print(Solution().IMvsCap("ICICICIICI")) # output en consola: "Iron Man"
print(Solution().rectanguloEspecial(6,4,"O","L"))
"""
output en consola:      LOLOLO
                        OLOLOL
                        LOLOLO
                        OLOLOL
"""

