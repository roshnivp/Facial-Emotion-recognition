#!/Users/roshni/.virtualenvs/cv/bin/python
import cv2
import numpy as np
import os, sys, glob


base_image = '/Users/roshni/Desktop/CS297/Week4/jaffe'
out_path ='/Users/roshni/Desktop/CS297/Week4/foreground_extraction'
def Extract_background(img_path, output_path):
  for infile in glob.glob( os.path.join(img_path, "*.tiff") ):
                img = cv2.imread(infile)
                mask = np.zeros(img.shape[:2],np.uint8)
                bgdModel = np.zeros((1,65),np.float64)
                fgdModel = np.zeros((1,65),np.float64)
                rect = (161,79,150,150)
                cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
                mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
                img = img*mask2[:,:,np.newaxis]


                file_name = 'extracted'+'-'+infile.split('/')[-1]
                file_path = output_path+'/'+ file_name
                cv2.imwrite(file_path, img)
                print '[Preprocessing...] %s' % file_name

if __name__=="__main__":
  Extract_background(base_image, out_path)