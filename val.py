
import easyocr
reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
result = reader.readtext('/home/anil/Videos/work/extraction/split_image/top_left.png')

#im1 = result.save("geeks.jpg")
#print(result)
#print(result[0])

values = []
for i in range(len(result)):
    indi_value = result[i][1]
    #print(result[i][1])
    values.append(indi_value)

print(values)

#top left first mapping
top_left_outer_y1 = values[0]
top_left_outer_x1 = values[1]
top_left_outer_x2 = values[2]
top_left_outer_y2 = values[4]

#top left second mapping
top_left_inner_y1 = values[3]
top_left_inner_x1 = values[5]
top_left_inner_x2 = values[6]
top_left_inner_y2 = values[7]


#print(result[0][1])
#print(len(result))


import pandas as pd

'''
#df = pd.DataFrame(columns=["top_left","top_right"])
data = [{'top_left_outer_x1': top_left_outer_x1 , 'top_left_outer_x2': top_left_outer_x2,
         'top_left_outer_y1': top_left_outer_y1,'top_left_outer_y2': top_left_outer_y2,
         'top_left_inner_x1': top_left_inner_x1 , 'top_left_inner_x2': top_left_inner_x2,
         'top_left_inner_y1': top_left_inner_y1,'top_left_inner_y2': top_left_inner_y2,
         }]
'''
df = pd.DataFrame()
for i in range(2):

    df1 = pd.DataFrame({"top_left_outer_x1":[top_left_outer_x1],
                      "top_left_outer_y1":[top_left_outer_y1]})

    df2 = df.append(df1, ignore_index = True)
    df = df2

print(df2)



                    '''                                                                                                                       
                                "top_left_inner_x1":[self.top_left_inner_x1],#top left inner starts from here                                 
                                "top_left_inner_x2":[self.top_left_inner_x2],                                                                 
                                "top_left_inner_y1":[self.top_left_inner_y1],                                                                 
                                "top_left_inner_y2":[self.top_left_inner_y2],                                                                 
                                "top_right_outer_x1":[self.top_right_outer_x1],#top right outer starts from here                              
                                "top_right_outer_x2":[self.top_right_outer_x2],                                                               
                                "top_right_outer_y1":[self.top_right_outer_y1],                                                               
                                "top_right_outer_y2":[self.top_right_outer_y2],                                                               
                                "top_right_inner_x1":[self.top_right_inner_x1],#top right inner starts from here                              
                                "top_right_inner_x2":[self.top_right_inner_x2],                                                               
                                "top_right_inner_y1":[self.top_right_inner_y1],                                                               
                                "top_right_inner_y2":[self.top_right_inner_y2],                                                               
                                "bottom_left_outer_x1":[self.bottom_left_outer_x1],#bottom left outer starts from here                        
                                "bottom_left_outer_x2":[self.bottom_left_outer_x2],                                                           
                                "bottom_left_outer_y1":[self.bottom_left_outer_y1],                                                           
                                "bottom_left_outer_y2":[self.bottom_left_outer_y2],                                                           
                                "bottom_left_inner_x1":[self.bottom_left_inner_x1],#bottom left inner starts from here                        
                                "bottom_left_inner_x2":[self.bottom_left_inner_x2],                                                           
                                "bottom_left_inner_y1":[self.bottom_left_inner_y1],                                                           
                                "bottom_left_inner_y2":[self.bottom_left_inner_y2],                                                           
                                "bottom_right_outer_x1]":[self.bottom_right_outer_x1],#bottom  right outer starts from here                   
                                "bottom_right_outer_x2":[self.bottom_right_outer_x2],                                                         
                                "bottom_right_outer_y1":[self.bottom_right_outer_y1],                                                         
                                "bottom_right_outer_y2":[self.bottom_right_outer_y2],                                                         
                                "bottom_right_inner_x1":[self.bottom_right_inner_x1],#bottom right inner starts from here                     
                                "bottom_right_inner_x2":[self.bottom_right_inner_x2],                                                         
                                "bottom_right_inner_y1":[self.bottom_right_inner_y1],                                                         
                                "bottom_right_inner_y2":[self.bottom_right_inner_y2]})                                                        
    '''
