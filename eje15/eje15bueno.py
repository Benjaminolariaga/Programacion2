import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps

im = Image.open("paisaje.JPG")
im_gris = ImageOps.grayscale(im)
matriz = np.array(im_gris)
fyc=matriz.shape
fil=fyc[0]
col=fyc[1]
print(fil)
print(col)
mitCol=col//2
print (mitCol)
for i in range (fil):
    for x in range (mitCol):
        aux=matriz[i][x]
        ind_op=col-1-x
        matriz[i][x]=matriz[i][ind_op]
        matriz[i][ind_op]=aux
plt.imshow(matriz, cmap="grey")
plt.show()
