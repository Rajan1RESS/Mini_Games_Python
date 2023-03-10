import numpy as np
from termcolor import cprint

br_red =    [1,1,1,0,0,-1,-1,-1]
br_kolone = [1,0,-1,1,-1,-1,1,0]

def printMat(mat):
    for i in range(1,8):
        cprint(i,'green',end=" ")
    print("")    
    for i in range(M):
        for j in range(N):
            if(mat[i][j] == 1):
                cprint(mat[i][j],'yellow',end=" ")
            elif(mat[i][j] == 2):
                cprint(mat[i][j],'red',end=" ")
            else:
                print(mat[i][j],end=" ")        
        print("")    

def granica(mat,red,kol):
    if red < 0 or kol < 0:
        return False
    if red > M-1 or kol > N-1:
        return False
    return True       

def startna_matrica():
    global M,N,mat
    M = 6
    N = 7
    mat = np.zeros(M*N,int)
    mat = mat.reshape((M,N))

    for i in range(1,8):
        cprint(i,'green',end=" ")
    print("")  
    for i in range(M):
        for j in range(N):
            print(mat[i][j],end=" ")
        print(" ")    

def pravila(mat,unos):
    global brojac
    for i in range(N):
        zad = 5
        if i == unos:
            while(mat[zad][i]!=0):
                zad-=1
                if(zad == -1):
                    print("Popunjena kolona") 
                    return None        
            mat[zad][i] = igrac 
            for z in range(8):
                brojac=1
                if(granica(mat,zad+br_red[z],i+br_kolone[z])==True):
                    if(mat[zad+br_red[z]][i+br_kolone[z]] == igrac):
                        brojac+=1
                if(granica(mat,zad+br_red[z]+br_red[z],i+br_kolone[z]+br_kolone[z])==True):
                    if(mat[zad+br_red[z]+br_red[z]][i+br_kolone[z]+br_kolone[z]] == igrac):
                        brojac+=1
                if(granica(mat,zad+br_red[z]+br_red[z]+br_red[z],i+br_kolone[z]+br_kolone[z]+br_kolone[z])==True):
                    if(mat[zad+br_red[z]+br_red[z]+br_red[z]][i+br_kolone[z]+br_kolone[z]+br_kolone[z]] == igrac):
                        brojac+=1              

                if brojac == 4:
                    print("Igrac ",igrac," je pobjedio")
                    return None

def igraj():
    global igrac
    startna_matrica()
    igrac = 2
    while True:
        if(igrac == 1):
            igrac = 2
        elif(igrac == 2):
            igrac = 1  
        unos = int(input())-1
        pravila(mat,unos)

        printMat(mat)
        if(brojac == 4):
            break


igraj()