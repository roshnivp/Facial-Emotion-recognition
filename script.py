#!/Users/roshni/miniconda2/bin/python
import os
from shutil import copy, rmtree

base_image = '/Users/roshni/Desktop/CS297/week5/KDEF/'
image_folders = os.listdir(base_image)
folderSep = "/"
output_folder = '/Users/roshni/Desktop/CS297/week5/KDEF_Images'
label_file = '/Users/roshni/Desktop/CS297/week5/label.txt'

#def get_immediate_subdirectories(a_dir):
 #    return [base_image + a_dir + folderSep + name for name in os.listdir(base_image + a_dir)
  #              if (os.path.isfile(os.path.join(base_image + a_dir + folderSep, name)))] 

#image_list = [get_immediate_subdirectories(name) for name in image_folders 
 #                     if os.path.isdir(base_image + name)]

#if  os.path.exists(output_folder):
 #    rmtree(output_folder)

#if not os.path.exists(output_folder):
 #    os.makedirs(output_folder)

# # Loop through images
#for images in image_list:
 # for image_file in images:
  #  if (os.path.isfile(image_file)) :
   #   copy(image_file, output_folder)


# NE = neutral -> 0
# HA = happy -> 1
# SA = sad -> 2
# SU = surprised -> 3
# AN = angry -> 4
# DI = disgusted -> 5
# AF = fear -> 6

emotions = dict({'NE':0, 'HA':1, 'SA':2, 'SU':3, 'AN':4, 'DI':5, 'AF':6})
straight_images = os.listdir(output_folder)
count =0
with open(label_file, 'w') as outfile :	
	for image in straight_images:
		code = image[4:6]
                count =count+1
                print count
		print code, emotions.get(code)
	        outfile.write(str(emotions.get(code))+'\n')
