#!/Users/roshni/.virtualenvs/cv/bin/python
import cv2
import os, sys, glob
import numpy as np

base_image = '/Users/roshni/Desktop/CS297/Week4/jaffe'
out_path=  '/Users/roshni/Desktop/CS297/Week4/jaffe_IS_smoothed'
def smoothing(img_path, output_path):
    for infile in glob.glob( os.path.join(img_path, "*.tiff") ):
                img = cv2.imread(infile)
                blur = cv2.blur(img,(5,5),0)
                file_name = 'smoothed'+'-'+infile.split('/')[-1]
                file_path = output_path+'/'+ file_name
                cv2.imwrite(file_path, blur)
                print '[Preprocessing...] %s' % file_name

if __name__=="__main__":
  smoothing(base_image, out_path)