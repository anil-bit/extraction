

import imageio as iio
import cv2
image = "/home/anil/Videos/work/extraction/image/230843001-SFR.png"
read_image = iio.imread(image)
path = "/home/anil/Videos/work/extraction/split_image/"
#height*width format
split = read_image[300:800,600:1300]
cv2.imwrite(path+"centre.png",split)
