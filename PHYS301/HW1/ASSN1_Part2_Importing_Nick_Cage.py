import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img=mpimg.imread('/Users/ryank/Desktop/o_o.jpg')

lum_img = img[:,:,2]

plt.imshow(lum_img, cmap='Pastel1')