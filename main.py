import image
import transform

img = image.generate(128, 128, 100)
matrix = transform.transform(img)

print(matrix)
image.display(img)