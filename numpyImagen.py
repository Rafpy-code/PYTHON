import numpy as np
import skimage
#from skimage import data
import matplotlib.pyplot as plt
#matplotlib inline
   
image = data.camera()  
type(image)
numpy.ndarray #la imagen es vector NumPy: 

mask = image < 87  
image[mask]=255  
plt.imshow(image, cmap='gray')