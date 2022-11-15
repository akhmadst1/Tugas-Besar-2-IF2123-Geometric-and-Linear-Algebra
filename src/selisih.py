from extract_dataset import sum_images
from extract_dataset import mean

matrixSelisih = []

for i in range(0, len(sum_images)):
    res = 0
    row =[]
    for j in range(0, len(sum_images[0])):
        res = sum_images[i][j] - mean
        row.append(res)            
    print(row)
    matrixSelisih.append(row)

print(matrixSelisih)

