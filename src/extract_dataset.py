import cv2
import os
import numpy

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

mean = numpy.divide(sum_images, count) # jumlah matriks image dibagi jumlah fotonya
cv2.imwrite(r"..\Algeo02-21115\test\{}\mean_image.jpg".format(folder), mean)    # image hasil rata-rata disimpen ke mean_image.jpg
                                                                                # di folder test/dataset_namaorangnya (cth: dataset_taylor)
print(mean) # ngetes print nilai matriks foto yang udah dirata-ratain