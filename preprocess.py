import cv2
import numpy as np



class preprocess_image:
    def __init__(self,image):
        self.read_image = cv2.imread(image)
        self.colour_path = "/home/anil/Videos/work/extraction/green_images/"
        

    
    def extract_green(self):
        lower_red = np.array([0, 255, 0], dtype = "uint8")
        upper_red= np.array([0, 255, 0], dtype = "uint8")
        mask = cv2.inRange(self.read_image, lower_red, upper_red)
        detected_output = cv2.bitwise_and(self.read_image, self.read_image, mask =  mask)
        cv2.imwrite(self.colour_path+"green.png",detected_output)
        #cv2.imshow("red color detection", detected_output)
        #cv2.waitKey(0)

        
#preprocess_image("/home/anil/Downloads/03FFBWFOCUSSFR/ALL/230843001-SFR.png").extract_green()


'''
import cv2
img = cv2.imread('/home/anil/Videos/work/extraction/split_image/bottom_left.png')
b, g, r = cv2.split(img)
cv2.imshow('green', g)
cv2.imwrite("convert.png",g)
cv2.waitKey(0)


import cv2

import numpy as np

image = cv2.imread('/home/anil/Videos/work/extraction/split_image/bottom_right.png')

lower_red = np.array([0, 255, 0], dtype = "uint8")

upper_red= np.array([0, 255, 0], dtype = "uint8")

mask = cv2.inRange(image, lower_red, upper_red)

detected_output = cv2.bitwise_and(image, image, mask =  mask)

cv2.imshow("red color detection", detected_output)

cv2.waitKey(0)

'''
