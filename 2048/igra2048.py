import numpy as np
import random
from termcolor import cprint

def printMat(mat):
    for i in range(4):
        for j in range(4):
            a = mat[i][j]
            if(mat[i][j] == 0):
                cprint('%2i' %a,'white',end="   ")
            elif(mat[i][j] == 2):
                cprint('%2i' %a,'yellow',end="   ")
            elif(mat[i][j] == 4):
                cprint('%2i' %a,'red',end="   ")
            elif(mat[i][j] == 8):
                cprint('%2i' %a,'green',end="   ")
            elif(mat[i][j] == 16):
                cprint('%2i' %a,'cyan',end="   ")
            else:
                cprint('%2i' %a,'blue',end="   ")    
        print(" ")

def mapa():
    global mat
    mat = np.zeros(4*4,int)
    mat[:2] = 2
    np.random.shuffle(mat)
    mat = mat.reshape((4,4))
    

def dodavanjeNovog(mat):
    red = []
    kolona = []
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 0):
                red.append(i)
                kolona.append(j)

    pozicija = list(zip(red, kolona))
    np.random.shuffle(pozicija)
    red,kolona = zip(*pozicija)

    mat[red[0],kolona[0]] = 2

def potez(mat,strana):
    stack = []
    if(strana == "R"):
        for i in range(4):
            for j in range(4):
                if(mat[i][j] != 0):
                    stack.append(mat[i][j])
                    mat[i][j] = 0
                if(j == 3):
                   pozicija = 3 
                   n = len(stack)
                   while(n!= 0): 
                    n = len(stack) 
                    if(n != 0 and n != 1):
                        one = stack.pop()
                        two = stack.pop()
                        if(one != two):
                            mat[i][pozicija] = one
                            pozicija -= 1
                            stack.append(two)
                        elif(one == two):
                            temp = one + two
                            mat[i][pozicija] = temp
                            pozicija -=1    
                    elif(n != 0):
                        one = stack.pop()
                        mat[i][pozicija] = one

    elif(strana == "L"):
        for i in range(4):
            for j in range(4):
                if(mat[i][j] != 0):
                    stack.append(mat[i][j])
                    mat[i][j] = 0
                if(j == 3):
                   stack.reverse() 
                   pozicija = 0
                   n = len(stack)
                   while(n!= 0): 
                    n = len(stack) 
                    if(n != 0 and n != 1):
                        one = stack.pop()
                        two = stack.pop()
                        if(one != two):
                            mat[i][pozicija] = one
                            pozicija += 1
                            stack.append(two)
                        elif(one == two):
                            temp = one + two
                            mat[i][pozicija] = temp
                            pozicija +=1    
                    elif(n != 0 and n<2):
                        one = stack.pop()
                        mat[i][pozicija] = one                                    

    elif(strana == "U"):
        for i in range(4):
            for j in range(4):
                if(mat[j][i] != 0):
                    stack.append(mat[j][i])
                    mat[j][i] = 0
                if(j == 3):
                   stack.reverse() 
                   pozicija = 0
                   n = len(stack)
                   while(n!= 0): 
                    n = len(stack) 
                    if(n != 0 and n != 1):
                        one = stack.pop()
                        two = stack.pop()
                        if(one != two):
                            mat[pozicija][i] = one
                            pozicija += 1
                            stack.append(two)
                        elif(one == two):
                            temp = one + two
                            mat[pozicija][i] = temp
                            pozicija +=1    
                    elif(n != 0):
                        one = stack.pop()
                        mat[pozicija][i] = one

    elif(strana == "D"):
        for i in range(4):
            for j in range(4):
                if(mat[j][i] != 0):
                    stack.append(mat[j][i])
                    mat[j][i] = 0
                if(j == 3):
                   pozicija = 3
                   n = len(stack)
                   while(n!= 0): 
                    n = len(stack) 
                    if(n != 0 and n != 1):
                        one = stack.pop()
                        two = stack.pop()
                        if(one != two):
                            mat[pozicija][i] = one
                            pozicija -= 1
                            stack.append(two)
                        elif(one == two):
                            temp = one + two
                            mat[pozicija][i] = temp
                            pozicija -=1    
                    elif(n != 0):
                        one = stack.pop()
                        mat[pozicija][i] = one
    elif(strana == "^Z"):
        exit()
    else:
        print("Pogresna komanda")
        return None

    dodavanjeNovog(mat)

    



mapa()
printMat(mat)
br0 = 1
kopija = np.zeros(4*4,int)
kopija = kopija.reshape((4,4))
while True:
    if(kopija.all()==mat.all() and br0 == 0):
        break
    
    kopija = mat.copy()
    strana = input()
    br0 = 0
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 0):
                br0 += 1     
    potez(mat,strana)
    printMat(mat)

 


print("Kraj igre")

mapa()