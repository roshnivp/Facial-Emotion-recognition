def crop_image(img_path, output_path):
   for infile in glob.glob( os.path.join(img_path, "*.tiff") ):
      img = cv2.imread(infile,0)
      img = img[70:215,80:185]
      file_name = 'cropped'+'-'+infile.split('/')[-1]
      file_path = output_path+'/'+ file_name
      cv2.imwrite(file_path, img)
 
if __name__=="__main__":
   crop_image(base_image,out_path)