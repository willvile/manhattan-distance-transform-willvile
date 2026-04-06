import matplotlib.pyplot as plt
import image
import transform

img = image.generate(16, 16, 20)
matrix = transform.transform(img)

print(matrix)
image.display(img)
transform.display(matrix)
plt.show()