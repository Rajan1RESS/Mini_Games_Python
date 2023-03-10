import numpy as np
import random
from termcolor import cprint 

br_red = [0,0,1,-1]
br_kolone = [1,-1,0,0]

def promjena_mape(mat):
    for i in range(M):
        for j in range(N):
                if(mat[i][j]==0):
                    cprint(mat[i][j],'red',end=" ")
                elif(mat[i][j]==1):
                    cprint(mat[i][j],'blue',end=" ")          
        print("")  

def mapa():
    global M,N,mat
    M = 5
    N = 5
    mat = np.zeros(M*N,dtype=int)
    n = random.randint(1,24)
    mat[:n] = 1
    np.random.shuffle(mat)
    mat = mat.reshape((M,N))
     

def granica(mat,red,kol):
    if red < 0 or kol < 0:
        return False
    if red > len(mat)-1 or kol > len(mat[0])-1:
        return False
    return True

def complement(mat,red,kolona):
    if (mat[red][kolona] == 0):
        mat[red][kolona] = 1
    elif (mat[red][kolona] == 1):
        mat[red][kolona] = 0    

def klik(mat,p):
    global kord_red,kord_kol
    kord_red = (p-1)//M
    kord_kol = (p-1)%N
    
    if(granica(mat,kord_red,kord_kol)==True):
        complement(mat,kord_red,kord_kol)
    else:
        print("Nepostojece polje")
        return None    
    for i in range(4):
        if(granica(mat,kord_red+br_red[i],kord_kol+br_kolone[i])==True):
            complement(mat,kord_red+br_red[i],kord_kol+br_kolone[i])

def igraj():
    
    mapa()
    promjena_mape(mat)
    sum = 1
    br = 0
    while (sum!=25 or sum!= 0):
        sum = 0
        print("Unesite polje:")
        polje = int(input())
        klik(mat,polje)
        promjena_mape(mat)

        for i in range(M):
            for j in range(N):
                sum+=mat[i][j]
        if(granica(mat,kord_red,kord_kol)==True):
            br+=1
        print(br)


igraj()
