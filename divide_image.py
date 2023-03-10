from PIL import Image
import imageio as iio
import cv2


class divide:
    def __init__(self,image):
        self.read_image = iio.imread(image)
        self.path = "/home/anil/Videos/work/extraction/split_image/"



    def top_left_split(self):
        #height*width format
        split = self.read_image[0:450,0:850]
        cv2.imwrite(self.path+"top_left.png",split)


    def top_right_split(self):
        #height*width format
        split = self.read_image[0:450,1000::]
        cv2.imwrite(self.path+"top_right.png",split)

    def bottom_left_split(self):
        #height*width format
        split = self.read_image[650::,0:850]
        cv2.imwrite(self.path+"bottom_left.png",split)


    def bottom_right_split(self):
        #height*width format
        split = self.read_image[650::,1000::]
        cv2.imwrite(self.path+"bottom_right.png",split)


    def centre(self):
        split = self.read_image[300:800,600:1300]
        cv2.imwrite(self.path+"centre.png",split)

    def initiate_divide(self):
        self.top_left_split()
        self.top_right_split()
        self.bottom_left_split()
        self.bottom_right_split()
        self.centre()




#divide("/home/anil/Videos/work/extraction/green_images/green.png").initiate_divide()





