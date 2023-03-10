from glob import glob
import numpy as np
import random


br_red =    [1,1,1,0,0,-1,-1,-1]
br_kolone = [1,0,-1,1,-1,-1,1,0]



def prikazi_stanje(mat):

    for i in range(M):
        for j in range(N):
            if(mat[i][j] == -1 or mat[i][j] == -2):
                print("N",end=" ")
            elif(mat[i][j] == -3):
                print("X",end=" ")
            elif(mat[i][j] == -4):
                print("B",end=" ")
            else:
                print(mat[i][j],end=" ")
        print("")

def generisi_pocetno_stanje():
    print("Unesite dimenzije matrice: ")
    global M,N,K,mat,posjecen
    M = int(float(input('')))
    N = int(float(input('')))
    K = int(input("Unesite broj mina: "))

    mat =  np.zeros(M*N,int)
    mat[:K] = -2
    mat[K:M*N] = -1
    np.random.shuffle(mat)
    mat = mat.reshape((M,N))   

    for i in range(M):
        for j in range(N):
            print("N",end=" ")
        print()    

def granica(mat,red,kol):
    if red < 0 or kol < 0:
        return False
    if red > M-1 or kol > N-1:
        return False
    return True       

def otkrij_polje(mat,p):
    global kord_red,kord_kolona
    kord_red = (p-1)//M
    kord_kolona = (p-1)%N
    

    if(mat[kord_red][kord_kolona] == -1):
        br = 0

        for i in range(8):
            if(granica(mat,kord_red+br_red[i],kord_kolona+br_kolone[i])==True):
                if(mat[kord_red+br_red[i]][kord_kolona+br_kolone[i]] == -2 or mat[kord_red+br_red[i]][kord_kolona+br_kolone[i]] == -3):
                    mat[kord_red+br_red[i]][kord_kolona+br_kolone[i]] = -3
                    br+=1
                elif(mat[kord_red+br_red[i]][kord_kolona+br_kolone[i]] == -1):
                    komsija_br = 0
                    for j in range(8):
                        if(granica(mat,kord_red+br_red[i]+br_red[j],kord_kolona+br_kolone[i]+br_kolone[j])==True):
                              if(mat[kord_red+br_red[i]+br_red[j]][kord_kolona+br_kolone[i]+br_kolone[j]] == -2 or \
                                mat[kord_red+br_red[i]+br_red[j]][kord_kolona+br_kolone[i]+br_kolone[j]] == -3):
                                komsija_br+=1
                    mat[kord_red+br_red[i]][kord_kolona+br_kolone[i]] = komsija_br

        mat[kord_red][kord_kolona] = br


    elif(mat[kord_red][kord_kolona] == -2):
        print("Kraj igre, izgubio")
        mat[kord_red][kord_kolona] = -4
        prikazi_stanje(mat)
        quit()
    elif(mat[kord_red][kord_kolona] == -3 or mat[kord_red][kord_kolona] != -1 or mat[kord_red][kord_kolona] != -2):
        print("Vec otvoreno polje")
        return None             

def igraj():
    global polje
    generisi_pocetno_stanje()
    br_polja = 1
    while(br_polja > 0):
        polje = int(input("Unesite polje: "))
        if(polje > N*M):
            print("Nepostojece polje")
            continue
        else:        
            otkrij_polje(mat,polje)
            prikazi_stanje(mat)

        br_polja = 0
        for i in range(M):
            for j in range(N):
                if(mat[i][j] == -1):
                    br_polja=br_polja+1

    print("Pobjeda")

igraj()