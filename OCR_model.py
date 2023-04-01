import numpy as np
import keras_ocr
import sys # to access the system
import cv2
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



def detect_w_keras(pipeline,image_path):
    """Function returns detected text from image"""

    read_image = keras_ocr.tools.read(image_path)

    prediction_groups = pipeline.recognize([read_image])
    return prediction_groups

def isOnSameLine(boxOne, boxTwo):
    boxOneStartY = boxOne[0,1]
    boxOneEndY = boxOne[2,1]
    boxTwoStartY = boxTwo[0,1]
    boxTwoEndY = boxTwo[2,1]
    if((boxTwoStartY <= boxOneEndY and boxTwoStartY >= boxOneStartY)
    or(boxTwoEndY <= boxOneEndY and boxTwoEndY >= boxOneStartY)
    or(boxTwoEndY >= boxOneEndY and boxTwoStartY <= boxOneStartY)):
        return True
    else:
        return False

def segmentLines(box_group):
    import numpy as np

    box_group = box_group[np.argsort(box_group[:, 0, 1])]

    lined_box_group = np.zeros(box_group.shape)
    sorted_box_group = np.zeros(box_group.shape)

    temp = []
    i = 0
    lines_list = []

    if len(box_group) > 1:
        while i < len(box_group):
            for j in range(i + 1, len(box_group)):
                if(isOnSameLine(box_group[i],box_group[j])):

                    if i not in temp:
                        temp.append(i)
                    if j not in temp:
                        temp.append(j)

            if len(temp) == 0:
                temp.append(i)

            lined_box_group = box_group[np.array(temp)]
            t = np.argsort(lined_box_group[:, 0, 0])
            lines_list.append([x+i for x in t])
            lined_box_group = lined_box_group[t]
            sorted_box_group[i:temp[-1]+1] = lined_box_group
            i = temp[-1] + 1

            temp = []
    else:
        sorted_box_group = box_group
  
    return sorted_box_group,lines_list

def load_model():
    return keras_ocr.pipeline.Pipeline()
def get_text(pipeline):

    res_pred = []



    root = tk.Tk()
    root.withdraw()

    image_path = filedialog.askopenfilename()

    pred = detect_w_keras(pipeline,image_path)

    pred = pred[0]

    box_group = np.array([x[1] for x in pred])

    s,l = segmentLines(box_group)

    for i in range(len(l)):
        l[i].sort()


    # image = mpimg.imread(image_path)
    # plt.imshow(image)
    # plt.show()

    import os
    clear = lambda: os.system('cls')
    clear()

    for ran in l:
        s_sub = s[ran[0]:ran[-1]+1]
        #print(s_sub)
        
        for x in s_sub:
            
            for text,box in pred:

                if int(x[0][0]) == int(box[0][0]) and int(x[0][1]) == int(box[0][1]):
                    res_pred.append(text)
                    break
    return res_pred            
