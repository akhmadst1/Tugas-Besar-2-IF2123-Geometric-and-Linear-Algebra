import math
import numpy as np


#Fungsi untuk membuat matrix berukuran N dengan setiap elemen nol
def makeMatrix(N):
    return [[0 for j in range(N)] for i in range(N)]

#test case
#print(makeMatrix(5))


#Fungsi perkalian pda suatu matrix
def multiply(matrix1,matrix2):
    result = makeMatrix(len(matrix1))
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            for k in range(len(matrix1)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

#transpose matrix
def transpose(matrix):
    return np.transpose(matrix)
def displayMatrix(c):
    for i in range(len(c)):
        for j in range(len(c[0])):
            print(c[i][j], end=" ")
        print("")
#fungsi mengecek sebuah matrix segitiga atas atau bawah
def isuppertriangular(M):
    for i in range(1, len(M)):
        for j in range(0, i):
            if(M[i][j] != 0):
                    return False
    return True
