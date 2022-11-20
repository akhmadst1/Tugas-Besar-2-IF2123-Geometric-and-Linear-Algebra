import cv2
import os
import numpy
import numpy.linalg as lin
from eigenvalues import *
#EKSTRASI DATA SET 
def ekstrasiDataSet(folder):
    images = []  # memori untuk nyimpen tiap foto yang ada di folder ke array images, udah dikonversi ke matriks
    count = 0  # jumlah foto yang valid

    for filename in os.listdir(r"..\Algeo02-21115\test\{}".format(folder)):
        img = cv2.imread(os.path.join(r"..\Algeo02-21115\test\{}".format(folder), filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            img = cv2.resize(img, (256, 256))  # resize foto ke ukuran 256x256
            img = img.flatten() # ubah dimensi matriks foto jadi 1 dimensi: 256^2 x 1
            images.append(img)  # tiap training set disimpen ke array images
            count += 1
    newimages = numpy.vstack(images)
    newimages = transpose(images)
    return images,count ,newimages                               #outputnya images gabungan hasil flatten extract foto 

def rataRata(matrix):
    mean = newimages.mean(1)
    return mean
def selisihMatrix(newimages,meanface):
    size = newimages.shape[1]
    newfaces = numpy.zeros(newimages.shape)
    for i in range(0,size):
        newfaces[:,i] = np.subtract(newimages[:,i],meanface)
    return newfaces
def covariant(newfaces):
    L = numpy.dot(numpy.transpose(newfaces),newfaces)
    return L 
def eigenvectors(L):
    eigenvalues,eigenvectors = HessenbergQR(L) 
    return eigenvectors
def eigenface(newfaces,eigenvectors):
    u = numpy.dot(newfaces, eigenvectors)
    return u 
def weight(u,newfaces):
    ut = numpy.transpose(u)
    w = numpy.dot(ut, newfaces)
    return ut , w
#proses training images 
images,count,newimages = ekstrasiDataSet("dataset_taylor")
mean = rataRata(newimages)
size = (256,256)
meanface = mean.reshape(size)
cv2.imwrite(r"..\Algeo02-21115\test\mean\mean.jpg", meanface)

#selisih 
newfaces = selisihMatrix(newimages,mean)
#covarian 
L = covariant(newfaces)
cv2.imwrite(r"..\Algeo02-21115\test\covariant\cov.jpg",L)

#eigenvalue dan eigenvektor 
ev, eigenvectors = HessenbergQR(L)

#Matrix u 
u = numpy.dot(newfaces,eigenvectors)
#write eigen face 
size = (256,256)
for i in range(0,u.shape[1]):
    eigenface = u[:,5]
    eigenfaces = eigenface.reshape(size)
    cv2.imwrite(r"..\Algeo02-21115\test\eigenfaces\faces6.jpg",eigenfaces)

#nyari weight 
v,w = weight(u,newfaces)


############################################################# TRAINING IMAGES FOR DATA TEST #######################################################################

imagestest,counttest,newimagestest = ekstrasiDataSet("dataset_test")
#selisih 
newfacestest = selisihMatrix(newimagestest,mean)

ut,wtest = weight(u, newfacestest)

############################################################ MENCARI JARAK #######################################################################
wtest = numpy.transpose(wtest)
w = numpy.transpose(w) 
distance = []
for i in range(0, wtest.shape[0]):
    distance = [lin.norm(numpy.subtract(wtest[i],wdatabase)) for wdatabase in w]
#mencari nilai paling kecil dan indeks paling kecil 
nilaimin = numpy.min(distance)
idx = numpy.where(distance==nilaimin)
#Misal kayak database taylor tapi test nya stephen jadi gak cocok 
if(nilaimin > 10000):
    print("Sorry Foto Tidak Ditemukan di Database")
else:
    print("Foto Ditemukan") 
    print(nilaimin)
    print(idx)
    hasil = newimages[:,idx]
    size = (256,256)
    hasil = hasil.reshape(size)
    cv2.imwrite(r"..\Algeo02-21115\test\result\result.jpg", hasil)

#Kalo mau nyoba yang stephen pake linalg aja nyari eigenvektornya soalnya lama banget kalo pake yang manual 