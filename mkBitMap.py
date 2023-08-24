################################################################################
#	
#			Create a .h file with images as arrays.
#			pixel format is the form 0xrrggbbaa
#
################################################################################


import numpy as np
import csv
import matplotlib.pyplot as plt
import cv2
import os

## file of image to read
image = "flower.ppm"
file_path = "./"

#output path for .h file
path = "./"  
f_out = "image_data.h"

name = 'image_data' # name of array in .h file to hold pixel data

# image dimensions to be resized 
rsize_w = 160
rsize_h = 200

LittleEndian = False
'''
img=cv2.imread(file)
print(img.shape)
img2 = cv2.resize(img, dsize=(rsize_h,rsize_w), interpolation=cv2.INTER_LINEAR)
print(img2.shape)

if (not LittleEndian):
	img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)
'''

'''
#plt.figure()
#plt.imshow(img2)
print('Displaying Image')
cv2.imshow('', img2);
cv2.waitKey(0);
cv2.destroyAllWindows();
'''

# Create .h file to write images in

fo = open(path+f_out, 'w')
fo.write("#ifndef _NUMBERS_DATA_h_\n#define _NUMBERS_DATA_h_\n\n")
fo.write("#include <stdint.h>\n\n")
fo.write('#define max_num_pix '+str(rsize_h)+'*'+str(rsize_w)+'\n\n')

max_pix = rsize_w*rsize_h;
pix_counter = 0
#fo.write('image_data[max_num_pix]={')
#num= 256



img2 =cv2.imread(file_path+image,1); 
print("%s\n" %(name) )

fo.write("uint32_t "+name+'[max_num_pix]={')
for y in np.arange(rsize_h):
		for x in np.arange(rsize_w):
		    pix_counter= pix_counter+1;
		    pix = img2[y][x][:]
		    #pix_data = (pix[0]<<16)+(pix[1]<<8)+(pix[2]<<0)
		    pix_data = (pix[0]<<24)+(pix[1]<<16)+(pix[2]<<8)+(255) # writes R-G-B-alpha channels
		    
		    # uncomment to make white background transparent
		    #if(pix_data == 0xffffffff):
		    #	pix_data = 0xffffff00
		    
			  #if(not LittleEndian):
		    #  pix_data = (255 << 24)+(pix[0]<<16)+(pix[1]<<8)+(pix[2]<<0)
		    #else:
		    #  pix_data = (pix[0]<<24)+(pix[1]<<16)+(pix[2]<<8)+(255) # writes R-G-B-alpha channels
		    #print(hex(pix_data), pix)
		    
		    if((pix_counter % 10)==0 ):
				
		        fo.write('\n\t\t\t')
		    if(pix_counter < max_pix):		      
		      fo.write(str(hex(pix_data)) ); fo.write(",") 
		    elif(pix_counter == max_pix):
		        fo.write(str(hex(pix_data)) ); fo.write("};\n\n") # end of array
		        
pix_counter = 0

fo.write("\n#endif")            
fo.close()
