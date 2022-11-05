import cv2
import os
import numpy

# untuk ekstraksi foto input yang mau dicocokkan sama dataset

images = []
filename = input("Masukkan nama file tanpa format .jpg : ") # contoh input: taylor
img = cv2.imread(r"..\Algeo02-21115\test\{}.jpg".format(filename), cv2.IMREAD_GRAYSCALE)
images.append(img)

cv2.imwrite(r"..\Algeo02-21115\test\{}_extracted.jpg".format(filename), img)    # menghasilkan foto hasil ekstraksi trus
                                                                                # disimpen ke filename_extracted.jpg di folder test