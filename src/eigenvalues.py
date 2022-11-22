from function import *
import numpy as np 
import math 
import numpy.linalg as lin
import copy

def coVarianMatriks(selisihmatrix):
    return np.dot(selisihmatrix, transpose(selisihmatrix))

#test case
'''selisihmatrix = [[1,0,0,0,1,0],
                [1,1,0,0,0,0],
                [0,0,1,1,0,1]]
#test case
displayMatrix(coVarianMatriks(selisihmatrix))'''

def gMatrix(row1, row2, column, matrix):
    G = makeMatrix(len(matrix))
    length = (math.sqrt(math.pow((matrix[row1][column]), 2) + math.pow((matrix[row2][column]), 2)))
    for i in range(len(G)):
        if(i == row1 or i == row2):
            G[i][i] = (matrix[row1][column]) / length
        else:
            G[i][i] = 1
    G[row1][row2] = (matrix[row2][column]) / length
    G[row2][row1] = (-matrix[row2][column]) / length
    return G

#Get upper Hessenberg form
def UpperHessenberg(matrix):
    H = copy.deepcopy(matrix)
    PG = makeMatrix(len(H))
    for i in range(len(H)):
        PG[i][i] = 1

    for col in range(len(matrix) - 2):
        for row in range(col + 2, len(matrix)):
            G = gMatrix(col + 1, row, col, H)
            H = multiply(multiply(G, H),transpose(G))
            PG = multiply(G, PG)
    return H, PG

def qrDecomposition(matrix):
    R = copy.deepcopy(matrix)
    Q = makeMatrix(len(R))
    for i in range(len(R)):
        Q[i][i] = 1
    for i in range(len(R)-1):
        G = gMatrix(i, i+1, i, R)
        Q = multiply(G, Q)
        R = multiply(G, R)
    return(transpose(Q),R)

def HessenbergQR(matrix):
    A = copy.deepcopy(matrix)
    QQ = makeMatrix(len(A))
    for i in range(len(QQ)):
        QQ[i][i] = 1

    mat, mat2 = UpperHessenberg(A)

    for i in range(10):
        eig, eigV = qrDecomposition(mat)
        mat = multiply(eigV, eig)
        QQ = multiply(QQ,eig)
    eigenvalues = []
    for i in range(len(mat)):
        eigenvalues.append(mat[i][i])
    QQ = multiply(transpose(mat2), QQ)
    return(eigenvalues, QQ)

A = [[21,4],
    [3,21]]


eigenvaluesMatA, eigenVectorMatB = HessenbergQR(coVarianMatriks(A))

'''print(sorted(eigenvaluesMatA))
(u,v) = lin.eig(coVarianMatriks(A))
print(sorted(u))



displayMatrix(v)
print("prittttttttttttt")
displayMatrix((eigenVectorMatB))

B = [[1,4,3,1,5,7],
    [7,5,4,2,1,3],
    [3,2,4,43,1,1],
    [11,2,32,2,3,2]]

eigenvalues, vektor = HessenbergQR(coVarianMatriks(B))
(x,y) = lin.eig(coVarianMatriks(B))
print(sorted(x))

print(sorted(eigenvalues))
print("----------------")
displayMatrix(vektor)
print("!!!!!!!!!!!!!!")
print(y)


# problem : di eigenvektor kadang jawaban dia beda negatif sama linag blm solved
'''