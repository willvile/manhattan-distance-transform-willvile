import numpy as np
import matplotlib.pyplot as plt

def transform(img):
#store indexes of image pixels in an array
    indexes = []
    for row in range(len(img)):
        for col in range(len(img[row])):
            if (img[row, col] == 1):
                indexes.append([row, col])
#creates matrix with manhattan distance transform
    dtransform = np.zeros((len(img), len(img[1])), dtype=int)
    for row in range(len(img)):
        for col in range(len(img[row])):
            distances = []
            for i in range(len(indexes)):
                distances.append(abs(row-indexes[i][0]) + abs(col-indexes[i][1]))
            dtransform[row, col] = min(distances)
    return dtransform

def display(matrix):
    fig, ax = plt.subplots()
    ax.axis("off")
    table = ax.table(cellText=matrix, loc="center", cellLoc="center")