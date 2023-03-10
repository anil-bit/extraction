#step1: preprocess
#step2: divide
#step3: digit_extraction
import os
import pandas as pd
from preprocess import preprocess_image
from divide_image import divide
from digit_extraction import digit_extraction


location = "/home/anil/Videos/work/extraction/image"
green_image_location = "/home/anil/Videos/work/extraction/green_images/green.png"
files = os.listdir(location)
print(files)


def create_data_frame():
    df = pd.DataFrame()
    return df


frame = create_data_frame()
for i in range(len(files)):
    #do preprocess step
    preprocess_image(location+"/"+files[i]).extract_green()
    #devide the image
    divide(green_image_location).initiate_divide()
    #do the extraction of numbers
    data_frame_ = digit_extraction().initiate_digit_extraction()
    #save the data in the datframe
    save_data = digit_extraction().saving_dataframe(data_frame_[0],data_frame_[1],data_frame_[2],data_frame_[3],data_frame_[4])
    #append the data in the orignal dataframe
    latest_data_frame = digit_extraction().apppend_dataf(som=frame,anil=save_data)

    frame = latest_data_frame
    print(frame)
#convert into excel
cc = frame.set_index([files], append=True)
print(cc)
digit_extraction().convert_into_excel(cc)


