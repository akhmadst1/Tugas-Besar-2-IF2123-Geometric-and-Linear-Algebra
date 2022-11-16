import cv2
import os
import numpy

# 1. EKSTRAKSI DATASET
folder = input("Masukkan nama folder dataset: ") # contoh input: dataset_taylor
images = []  # memori untuk nyimpen tiap foto yang ada di folder ke array images, udah dikonversi ke matriks
count = 0  # jumlah foto yang valid

for filename in os.listdir(r"..\Algeo02-21115\test\{}".format(folder)):
    img = cv2.imread(os.path.join(r"..\Algeo02-21115\test\{}".format(folder), filename), cv2.IMREAD_GRAYSCALE)
    if img is not None:
        img = cv2.resize(img, (256, 256))  # resize foto ke ukuran 256x256
        img = img.flatten() # ubah dimensi matriks foto jadi 1 dimensi: 256^2 x 1
        images.append(img)  # tiap training set disimpen ke array images
        count += 1

# 2. MENCARI NILAI RATAAN DATASET
sum_images = [0 for j in range(65536)]  # array penyimpan jumlah semua nilai matrix images: (256^2 = 65536)
for i in range(count):
    sum_images = numpy.add(sum_images, images[i])  # ngejumlahin tiap pixel semua matrix foto
mean = numpy.divide(sum_images, count)

# 3. MENCARI SELISIH TRAINING SET DENGAN RATAAN
for i in range(count):
    images[i] = numpy.subtract(images[i], mean)

# 4. MENCARI KOVARIAN
# kovarian ukuran m x m (m jumlah training set)
covariant = numpy.dot(images, numpy.transpose(images))
# print(covariant)
cv2.imwrite(r"..\Algeo02-21115\test\covariant.jpg", covariant)

# (!!!!! JANGAN DICOBAA !!!!!)
# kovarian ukuran 65536 x 65536
# covariant2 = numpy.dot(numpy.transpose(images), images)
# # print(covariant2)
# cv2.imwrite(r"..\Algeo02-21115\test\covariant2.jpg", covariant2)