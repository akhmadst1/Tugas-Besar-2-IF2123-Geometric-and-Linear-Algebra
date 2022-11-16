import cv2
import os
import numpy
from function import *
from eigenvalues import *
import numpy.linalg as lin 
import math
def extractFoto():       
    folder = input("Masukkan nama folder dataset: ") # contoh input: dataset_taylor
    images = []  # memori untuk nyimpen tiap foto yang ada di folder ke array images, udah dikonversi ke matriks
    sum_images = [[0 for j in range(256)] for i in range(256)]  # matriks untuk nyimpen hasil penjumlahan semua foto, dipake 256x256
    count = 0  # jumlah foto yang valid

    for filename in os.listdir(r"..\Algeo02-21115\test\{}".format(folder)):
        img = cv2.imread(os.path.join(r"..\Algeo02-21115\test\{}".format(folder), filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            img = cv2.resize(img, (256, 256))  # resize foto ke ukuran 256x256
            images.append(img)  # tiap foto disimpen ke array images
            sum_images = numpy.add(sum_images, img)  # ngejumlahin tiap pixel semua foto
            count += 1
    return sum_images,count,images
def meanExtract(m,count):         #m disini sum_images yang didapet dari extract
    mean = numpy.divide(sum_images, count) # jumlah matriks image dibagi jumlah fotonya
    #cv2.imwrite(r"..\Algeo02-21115\test\{}\mean_image.jpg".format(folder), mean)    # image hasil rata-rata disimpen ke mean_image.jpg
                                                                                    # di folder test/dataset_namaorangnya (cth: dataset_taylor)
    return mean # ngetes print nilai matriks foto yang udah dirata-ratain

def selihsihExtract(images,matrixmean):
    matrixSelisih = [[0 for j in range(0)] for i in range(len(matrixmean))]
    selisih = []
    for i in range(0, len(images)):
        nilai = images[i] - matrixmean
        matrixSelisih = np.concatenate((matrixSelisih,nilai), axis=1)
        selisih.append(nilai)
    return matrixSelisih,selisih

#buat test case aja
'''A = [[2,0,1],
    [1,2,0],
    [0,2,4]]

B = [[1,1,1],
    [0,1,0],
    [1,2,2]]

sum_images = numpy.add(A, B)

mat = meanExtract(sum_images,2)
print("matrix rata-rata")
displayMatrix(mat)
images = []
images.append(A)
images.append(B)

print("matrix selisih")
m = selihsihExtract(images, mat)
displayMatrix(m)

m = coVarianMatriks(m)
print(m)

d,n = HessenbergQR(m)

displayMatrix(n)
#hanya test case
a,b = lin.eig(m)
print("pembanding")
displayMatrix(b)

#setelah dicari eigenvektor '''

def eigenface(selisihmatrix,images):
    w,x = HessenbergQR(coVarianMatriks(selisihmatrix))
    #w,x = lin.eig(selihsihmatrix)
    database = []
    for i in range(len(images)):
        m = np.dot(x,images[i])
        database.append(m)
    return database 

#eigenface
#mencari vektor eigen dari covarian matriks 

def matcher(mneweigenface,database):            # m adalah eigenface yang baru
    hasilmatcher = []
    for i in range(len(database)):
        mat = numpy.subtract(mneweigenface[0],database[i])
        sum = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                sum = sum + math.pow(mat[i][j], 2)
        h = math.sqrt(sum)
        hasilmatcher = numpy.append(hasilmatcher, h)
    min = numpy.min(hasilmatcher)
    idxmin = numpy.where(hasilmatcher==min)[0][0]
    #acces matrix eigenvalues idxmin 
    m = database[idxmin]
    return m,min
    #cek


#test case dataset megumi 2x2

#training database 

sum_images,count,images = extractFoto()
#print("imagesss")
displayList(images)

#cari mean 
mean = meanExtract(sum_images, count)
print(mean)
#mencari matrixselisih
matrixSelisih,selisih = selihsihExtract(images, mean)
#print(matrixSelisih)
displayList(selisih)

#covarian matrix
mcov = coVarianMatriks(matrixSelisih)
#displayMatrix(mcov)

#mencari eigenvector 
eigenvalues,eigenvector = HessenbergQR(mcov)
displayMatrix(eigenvector)

#bandingkan dengan linald
#beda minus dan urutan tapi harusnya katanya sama
#m,n = lin.eig(mcov)
#displayMatrix(n)

#cari database
print("database")
database = eigenface(matrixSelisih, selisih)
displayList(database)

#misal suatu foto baru masuk 
sum_imagestest,counttest,imagestest = extractFoto()
mat, simpan = selihsihExtract(imagestest, mean)
displayMatrix(mat)
displayList(simpan)

mneweigenface = eigenface(mat, simpan)
displayList(mneweigenface)

hasil,nilaimin = matcher(mneweigenface, database)
displayMatrix(hasil)
print(nilaimin)
for i in range(len(database)):
    result = numpy.where(database==hasil)
cv2.imwrite(r"..\Algeo02-21115\test\{}\mean_image.jpg".format("result"), hasil)


