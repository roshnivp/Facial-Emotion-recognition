#!/Users/roshni/.virtualenvs/cv/bin/python
import cv2
import os, sys, glob
import numpy as np

base_image = '/Users/roshni/Desktop/CS297/Week4/jaffe'
out_path =  '/Users/roshni/Desktop/CS297/Week4/jaffe_DCT'
#print('hello')
def DCT_conversion(img_path, output_path):
     for infile in glob.glob( os.path.join(img_path, "*.tiff") ):
     #           print('hello')
                img = cv2.imread(infile)
                img =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                #imf = np.float32(img)  # float conversion/scale
                #dst = cv2.dct(imf)           # the dct
                #img = np.uint8(dst)    # convert back
                h, w = img.shape[:2]
                vis0 = np.zeros((h,w), np.float32)
                vis0 = vis0+img[:h,:w]
                vis1 = cv2.dct(vis0)
                img2=np.uint8(vis1)
                #img2 = cv2.CreateMat(vis1.shape[0], vis1.shape[1], cv2.CV_32FC3)
                file_name = 'DCT'+'-'+infile.split('/')[-1]
                file_path = output_path+'/'+ file_name
                cv2.imwrite(file_path, img2)
                print '[Preprocessing...] %s' % file_name

if __name__=="__main__":
  DCT_conversion(base_image, out_path)