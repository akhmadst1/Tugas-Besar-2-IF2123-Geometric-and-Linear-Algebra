import cv2
import os
import numpy
import numpy.linalg as lin
from eigenvalues import *
import time

#EKSTRASI DATA SET 
def ekstrasiDataSet(path_folder):
    images_clr = []  # image berwarna
    images_bnw = []  # memori untuk nyimpen tiap foto yang ada di folder ke array images, udah dikonversi ke matriks grayscale
    count = 0  # jumlah foto yang valid

    for filename in os.listdir(path_folder):
        img1 = cv2.imread(os.path.join(path_folder, filename), cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(os.path.join(path_folder, filename), cv2.IMREAD_UNCHANGED)
        width = 256
        height = 256
        dim = (width, height)
        if img1 is not None:
            img1 = cv2.resize(img1, (256, 256))  # resize foto ke ukuran 256x256
            img1 = img1.flatten() # ubah dimensi matriks foto jadi 1 dimensi: 256^2 x 1
            images_bnw.append(img1)  # tiap training set disimpen ke array images
            count += 1
        if img2 is not None:
            # resize image
            resized = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)
            # img2 = cv2.resize(img2, (256, 256))  # resize foto ke ukuran 256x256
            # img2 = img2.flatten() # ubah dimensi matriks foto jadi 1 dimensi: 256^2 x 1
            images_clr.append(resized)  # tiap training set disimpen ke array images
    # newimages_clr = numpy.vstack(images_clr)
    # newimages_clr = transpose(images_clr)
    newimages = numpy.vstack(images_bnw)
    newimages = transpose(images_bnw)
    return images_bnw, count, newimages, images_clr                             #outputnya images gabungan hasil flatten extract foto 

def extract_test_input(path_input):
    image = []
    # filename = input("Masukkan nama file tanpa format .jpg : ") # contoh input: taylor
    img = cv2.imread(path_input, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (256, 256))
    img = img.flatten()
    image.append(img)
    newimagetest = numpy.vstack(image)
    newimagetest = transpose(image)
    return newimagetest

def get_test_image(path_input):
    img = cv2.imread(path_input, cv2.IMREAD_UNCHANGED)
    width = 256
    height = 256
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(r"..\Algeo02-21115\src\assets\training.png", resized)

def rataRata(matrix):
    mean = matrix.mean(1)
    return mean

def selisihMatrix(newimages, meanface):
    size = newimages.shape[1]
    newfaces = numpy.zeros(newimages.shape)
    for i in range(0, size):
        newfaces[:, i] = np.subtract(newimages[:, i], meanface)
    return newfaces

def covariant(newfaces):
    L = numpy.dot(numpy.transpose(newfaces), newfaces)
    return L 

def eigenvectors(L):
    eigenvalues, eigenvectors = HessenbergQR(L)
    return eigenvectors

def eigenface(newfaces,eigenvectors):
    u = numpy.dot(newfaces, eigenvectors)
    return u 

def weight(u,newfaces):
    ut = numpy.transpose(u)
    w = numpy.dot(ut, newfaces)
    return ut, w

def mainprogram(path_folder, path_input):
    start = time.time()

    # Proses training images 
    images, count, newimages, newimages_clr = ekstrasiDataSet(path_folder)
    mean = rataRata(newimages)
    # size = (256, 256)
    # meanface = mean.reshape(size)
    # cv2.imwrite(r"..\Algeo02-21115\test\mean\mean.jpg", meanface)

    # Selisih training images dengan image rata-rata
    newfaces = selisihMatrix(newimages, mean)
    # Matriks kovarian 
    L = covariant(newfaces)
    # cv2.imwrite(r"..\Algeo02-21115\test\covariant\cov.jpg",L)

    #eigenvalue dan eigenvektor
    eigenvector = eigenvectors(L)
   
    

    # Matrix u 
    u = numpy.dot(newfaces, eigenvector)
    # Write eigen face 
    # size = (256, 256)
    # for i in range(0, u.shape[1]):
    #     eigenface = u[:, 5]
    #     eigenfaces = eigenface.reshape(size)
        # cv2.imwrite(r"..\Algeo02-21115\test\eigenfaces\faces{}.jpg".format(i), eigenfaces)

    # Nyari weight 
    v, w = weight(u, newfaces)

    ############################################################# TRAINING IMAGES FOR DATA TEST #######################################################################

    newimagestest = extract_test_input(path_input)

    # Selisih 
    newfacestest = selisihMatrix(newimagestest, mean)

    ut, wtest = weight(u, newfacestest)

    ############################################################ MENCARI JARAK #######################################################################
    wtest = numpy.transpose(wtest)
    w = numpy.transpose(w) 
    distance = []
    for i in range(0, wtest.shape[0]):
        distance = [lin.norm(numpy.subtract(wtest[i],wdatabase)) for wdatabase in w]
    # mencari nilai paling kecil dan indeks paling kecil 
    nilaimin = numpy.min(distance)
    idx = numpy.where(distance == nilaimin)
    #Misal kayak database taylor tapi test nya stephen jadi gak cocok 
    if(nilaimin > 1000000000):
        hasil = None
    else:
        # print("Foto Ditemukan") 
        # print(nilaimin)
        hasil = newimages_clr[(idx[0])[0]]
        # cv2.imwrite(r"..\Algeo02-21115\test\result\result.png", hasil)
        cv2.imwrite(r"..\Algeo02-21115\src\assets\result.png", hasil)

    end = time.time()
    duration = end-start

    return hasil, duration
    # mainprogram(r"C:\Users\Lenovo\Documents\tube\Algeo02-21115\test\dataset_taylor", r"C:\Users\Lenovo\Documents\tube\Algeo02-21115\test\dataset_test\taylor.jpg")