import numpy as np
import matplotlib.pyplot as plt

def generate(height, width, opixels):
    img = np.zeros((height, width), dtype=np.uint8)
    rows = np.random.randint(0, height, size=opixels)
    cols = np.random.randint(0, width, size=opixels)
    img[rows, cols] = 1
    return img

def display(img):
    plt.imshow(img, cmap="gray_r", vmin=0, vmax=1)
    plt.show()