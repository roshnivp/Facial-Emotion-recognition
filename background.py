#!/Users/roshni/.virtualenvs/cv/bin/python
import cv2
import numpy as np
import os, sys, glob

fgbg = cv2.createBackgroundSubtractorMOG2()

base_image = '/Users/roshni/Desktop/CS297/Week4/jaffe'
out_path ='/Users/roshni/Desktop/CS297/Week4/background_extraction'
def Extract_background(img_path, output_path):
  for infile in glob.glob( os.path.join(img_path, "*.tiff") ):
                img = cv2.imread(infile)
                fgmask = fgbg.apply(img)
                file_name = 'extracted'+'-'+infile.split('/')[-1]
                file_path = output_path+'/'+ file_name
                cv2.imwrite(file_path, fgmask)
                print '[Preprocessing...] %s' % file_name

if __name__=="__main__":
  Extract_background(base_image, out_path)