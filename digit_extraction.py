
import easyocr
import pandas as pd




class digit_extraction:
    def __init__(self):
        self.reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
        #self.ori_df = lund
       # result = reader.readtext('/home/anil/Videos/work/extraction/split_image/top_left.png')

    #function for extraction of top left value
    def top_left(self):
        result = self.reader.readtext('/home/anil/Videos/work/extraction/split_image/top_left.png')
        values = []
        for i in range(len(result)):
            indi_value = result[i][1]
            #print(result[i][1])
            values.append(indi_value)

        print(values)

        #top left outer mapping
        self.top_left_outer_y1 = values[0]
        self.top_left_outer_x1 = values[1]
        self.top_left_outer_x2 = values[2]
        self.top_left_outer_y2 = values[4]

        #top left inner mapping
        self.top_left_inner_y1 = values[3]
        self.top_left_inner_x1 = values[5]
        self.top_left_inner_x2 = values[6]
        self.top_left_inner_y2 = values[7]

        #print(self.top_left_outer_y1)
        return self.top_left_outer_x1, self.top_left_outer_x2, self.top_left_outer_y1, self.top_left_outer_y2, self.top_left_inner_x1, self.top_left_inner_x2, self.top_left_inner_y1, self.top_left_inner_y2




    #function for extraction of top right value
    def top_right(self):
        result = self.reader.readtext('/home/anil/Videos/work/extraction/split_image/top_right.png')
        values = []
        for i in range(len(result)):
            indi_value = result[i][1]
            #print(result[i][1])
            values.append(indi_value)

        print(values)

        #top right outer mapping
        self.top_right_outer_y1 = values[0]
        self.top_right_outer_x1 = values[1]
        self.top_right_outer_x2 = values[2]
        self.top_right_outer_y2 = values[4]

        #top right inner mapping
        self.top_right_inner_y1 = values[3]
        self.top_right_inner_x1 = values[5]
        self.top_right_inner_x2 = values[6]
        self.top_right_inner_y2 = values[7]

        return self.top_right_outer_x1, self.top_right_outer_x2, self.top_right_outer_y1, self.top_right_outer_y2, self.top_right_inner_x1, self.top_right_inner_x2, self.top_right_inner_y1, self.top_right_inner_y2



    #function for extraction of top right value
    def bottom_left(self):
        result = self.reader.readtext('/home/anil/Videos/work/extraction/split_image/bottom_left.png')
        values = []
        for i in range(len(result)):
            indi_value = result[i][1]
            #print(result[i][1])
            values.append(indi_value)

        print(values)

        #bottom left outer mapping
        self.bottom_left_outer_y1 = values[3]
        self.bottom_left_outer_x1 = values[5]
        self.bottom_left_outer_x2 = values[6]
        self.bottom_left_outer_y2 = values[7]

        #bottom left inner mapping
        self.bottom_left_inner_y1 = values[0]
        self.bottom_left_inner_x1 = values[1]
        self.bottom_left_inner_x2 = values[2]
        self.bottom_left_inner_y2 = values[4]

        return self.bottom_left_outer_x1, self.bottom_left_outer_x2, self.bottom_left_outer_y1, self.bottom_left_outer_y2, self.bottom_left_inner_x1, self.bottom_left_inner_x2, self.bottom_left_inner_y1, self.bottom_left_inner_y2



    def bottom_right(self):
        result = self.reader.readtext('/home/anil/Videos/work/extraction/split_image/bottom_right.png')
        values = []
        for i in range(len(result)):
            indi_value = result[i][1]
            #print(result[i][1])
            values.append(indi_value)

        print(values)

        #bottom left outer mapping
        self.bottom_right_outer_y1 = values[3]
        self.bottom_right_outer_x1 = values[5]
        self.bottom_right_outer_x2 = values[6]
        self.bottom_right_outer_y2 = values[7]

        #bottom left inner mapping
        self.bottom_right_inner_y1 = values[0]
        self.bottom_right_inner_x1 = values[1]
        self.bottom_right_inner_x2 = values[2]
        self.bottom_right_inner_y2 = values[4]

        return self.bottom_right_outer_x1, self.bottom_right_outer_x2, self.bottom_right_outer_y1, self.bottom_right_outer_y2, self.bottom_right_inner_x1, self.bottom_right_inner_x2, self.bottom_right_inner_y1, self.bottom_right_inner_y2


    def centre(self):
        result = self.reader.readtext('/home/anil/Videos/work/extraction/split_image/centre.png')
        values = []
        for i in range(len(result)):
            indi_value = result[i][1]
            #print(result[i][1])
            values.append(indi_value)

        print(values)

        #centre mapping
        self.centre_y1 = values[0]
        self.centre_x1 = values[1]
        self.centre_x2 = values[2]
        self.centre_y2 = values[3]



        return self.centre_x1, self.centre_x2, self.centre_y1, self.centre_y2




    def saving_dataframe(self,a,b,c,d,e):


        df1 = pd.DataFrame({"top_left_outer_x1":[a[0]],#top left outer starts from here
                            "top_left_outer_x2":[a[1]],
                            "top_left_outer_y1":[a[2]],
                            "top_left_outer_y2":[a[3]],
                            "top_left_inner_x1":[a[4]],#top left inner starts from here
                            "top_left_inner_x2":[a[5]],
                            "top_left_inner_y1":[a[6]],
                            "top_left_inner_y2":[a[7]],
                            "top_right_outer_x1":[b[0]],#top right outer starts from here
                            "top_right_outer_x2":[b[1]],
                            "top_right_outer_y1":[b[2]],
                            "top_right_outer_y2":[b[3]],
                            "top_right_inner_x1":[b[4]],#top right inner starts from here
                            "top_right_inner_x2":[b[5]],
                            "top_right_inner_y1":[b[6]],
                            "top_right_inner_y2":[b[7]],
                            "bottom_left_outer_x1":[c[0]],#bottom left outer starts from here
                            "bottom_left_outer_x2":[c[1]],
                            "bottom_left_outer_y1":[c[2]],
                            "bottom_left_outer_y2":[c[3]],
                            "bottom_left_inner_x1":[c[4]],#bottom left inner starts from here
                            "bottom_left_inner_x2":[c[5]],
                            "bottom_left_inner_y1":[c[6]],
                            "bottom_left_inner_y2":[c[7]],
                            "bottom_right_outer_x1":[d[0]],#bottom  right outer starts from here
                            "bottom_right_outer_x2":[d[1]],
                            "bottom_right_outer_y1":[d[2]],
                            "bottom_right_outer_y2":[d[3]],
                            "bottom_right_inner_x1":[d[4]],#bottom right inner starts from here
                            "bottom_right_inner_x2":[d[5]],
                            "bottom_right_inner_y1":[d[6]],
                            "bottom_right_inner_y2":[d[7]],
                            "centre_x1":[e[0]],
                            "centre_x2":[e[1]],
                            "centre_y1":[e[2]],
                            "centre_y2":[e[3]]})

        '''
        df2 = df.append(df1, ignore_index = True)
            df = df2
        print(df2)
        return(df2)
        '''
        #print(df1)
        return df1



    def apppend_dataf(self,som,anil):

        new_data_frame = som.append(anil,ignore_index=True)
        #df2 = som.append(df1, ignore_index = True)
        #print(new_data_frame)
        return new_data_frame

    def convert_into_excel(self,dataframe):
        file_name = 'MarksData.xlsx'
        dataframe.to_excel(file_name)







    def initiate_digit_extraction(self):
        a = digit_extraction().top_left()
        b = digit_extraction().top_right()
        c = digit_extraction().bottom_left()
        d = digit_extraction().bottom_right()
        e = digit_extraction().centre()
        return a,b,c,d,e
        #final_dataframe = digit_extraction(self.ori_df).saving_dataframe(a,b,c,d,self.ori_df)
        #return final_dataframe
        #digit_extraction().convert_into_excel(final_dataframe)

