#!/Users/roshni/.virtualenvs/cv/bin/python
import cv2
import os, sys, glob

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
base_image = '/Users/roshni/Desktop/CS297/week5/Processed_Images'
out_path ='/Users/roshni/Desktop/CS297/Week5/Face_Detection'
def Detect_face_and_eye(img_path, output_path):
        for infile in glob.glob( os.path.join(img_path, "*.tiff") ):
                img = cv2.imread(infile)
                print(img.shape)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                  cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                  roi_gray = gray[y:y+h, x:x+w]
                  roi_color = img[y:y+h, x:x+w]
                  eyes = eye_cascade.detectMultiScale(roi_gray)
                  for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                file_name = 'detected'+'-'+infile.split('/')[-1]
                file_path = output_path+'/'+ file_name
                cv2.imwrite(file_path, img)
                print '[Preprocessing...] %s' % file_name

if __name__=="__main__":
  Detect_face_and_eye(base_image, out_path)
