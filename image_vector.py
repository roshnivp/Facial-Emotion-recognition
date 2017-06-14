#!/Users/roshni/tensorflow/bin/python
import numpy as np
import os, sys, glob
from scipy.misc import imread
import matplotlib.image as mpimg
from PIL import Image
base_image = '/Users/roshni/Desktop/CS297/Week4/jaffe'
new_list= []
image =[]
def image_vector(img_path):
    for infile in glob.glob( os.path.join(img_path, "*.tiff") ):
                img = Image.open(infile)
                new_list =list(img.getdata())
                image.append(new_list)
    return np.array(image)
if __name__ =="__main__":
  #imageArray =[]
  image =image_vector(base_image)
  print(image)
  print(image.shape)
  #print(imageArray)
