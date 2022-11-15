from extract_dataset import sum_images
from extract_dataset import mean

for i in range(0, len(sum_images)):
    for j in range(0, len(sum_images[0])):
        matrixSelisih = sum_images[i][j] - mean
    print(matrixSelisih, end=' ')

