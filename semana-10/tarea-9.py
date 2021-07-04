
def quatro(n):
    print(list(dict.fromkeys(n)))
    
    #Dictionaries can't have duplicate keys

quatro([5, 8, 4, 7, 6, 2, 1, 9, 8, 4, 3, 2, 8])

def cinco():
    ls = ["a","b","c","c","a"]
    lv = ["a","x","c","c","a"]
    print('valores en comun : ')
    
# nose 
cinco()

def siete():
    def reina(posx,posy,x,y):
        dif = abs(posx - x)
        if posx - x > 0: x += dif
        elif posx - x < 0: x-= dif
        else: pass
        if posy - y > 0:y += dif
        elif posy -y < 0: y -= dif
        else: pass
        if posx == x and posy == y:
            return True
        else:
            return False
        # check the diference in any axis
        # subtract the diference in x and y 
        # it is not diagonal is it is not the pos
    def torre(posx,posy,x,y):
        if posx - x == 0 or posy - y == 0:
            return True
        else:
            return False
            # subtract the diference in x and y 
            # it is not diagonal is it is not the pos
            
    def alfil(posx,posy,x,y):
        dif = abs(posx - x)
        if posx - x > 0: x += dif
        elif posx - x < 0: x-= dif
        else: return False
        if posy - y > 0:y += dif
        elif posy -y < 0: y -= dif
        else: return False
        if posx == x and posy == y:
            return True
        else:
            return False
        # check the diference in any axis
        # subtract the diference in x and y 
            

    def printboard(posx,posy,opt):
        print("-------------------------------")
        if opt == 'c': print("reina") 
        elif opt == 'b': print("alfil")
        elif opt == 'a': print("Torre")
        for row in range(0,8):
            for column in range(0,8):
                
                if opt == 'a':
                    if torre(posx,posy,row,column):
                        print("1",end=" ")
                    else:
                        print(".",end=" ")
                if opt == 'b':
                    if alfil(posx,posy,row,column):
                        print("1",end=" ")
                    else:
                        print(".",end=" ")
                if opt == 'c':
                    if reina(posx,posy,row,column): 
                        print("1",end=" ")
                    else:
                        print(".",end=" ")
            print("")

    posx = int(input("escoja una posicion de x : "))
    posy = int(input("escoja una posicion de y : "))

    printboard(posx,posy,'a')
    printboard(posx,posy,'b')
    printboard(posx,posy,'c')
siete()

