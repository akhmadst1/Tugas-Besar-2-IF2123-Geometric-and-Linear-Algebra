import cv2
import os
import numpy

folder = input("Masukkan nama folder: ")
images = []
sum_images = [[0 for j in range(256)] for i in range(256)]
count = 0
for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
    if img is not None:
        img = cv2.resize(img, (256, 256))
        images.append(img)
        sum_images = numpy.add(sum_images, img)
        count += 1

mean = numpy.divide(sum_images, count)
print(mean)
cv2.imwrite("test\contoh.jpg", mean)