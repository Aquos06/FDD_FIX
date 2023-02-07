import cv2
import numpy as np
from json.decoder import JSONDecodeError
import json

def specific(coordinate, classes):
    
    result = []
    
    if classes == 1:
        for i in range(len(coordinate)):
            if coordinate[i][5] == 4 or coordinate[i][5] == 5 or coordinate[i][5] == 6 or coordinate[i][5] == 7:
                if coordinate[i][4] >= 0.85:
                    result.append(coordinate[i])
    else:
        for i in range(len(coordinate)):
            if coordinate[i][5] == classes:
                if coordinate[i][4] >= 0.7:
                    result.append(coordinate[i])

    return np.array(result)
    
def drawBbox(img, coordinate,total_channel, fall_coor):
    for coor in coordinate:
        try:
            person_id, x1, y1, x2, y2 = coor

            total_channel.append(int(person_id))
            total_channel = list(set(total_channel))
            if person_id in fall_coor:
                cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0,0,255), 1)
                cv2.putText(img,"Falling", (int(x1), int(y1)-5), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,0,0), 2)
            else:
                cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0,0,255), 1)
            
        except:
            x1,y1,x2,y2,_,_ = coor
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0,0,255), 1)
            cv2.putText(img,"Falling", (int(x1), int(y1)-5), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,0,0), 2)


    return img, len(total_channel), total_channel
    
def NewDraw(img, coordinate, fall):
    for coor in coordinate:
        x1,y1,x2,y2,conf,classId = coor
        cv2.rectangle(img, (int(x1),int(y1)-60), (int(x2),int(y2)-60), color = (255,0,0), thickness = 2)

    for coor in fall:
        id, x1,y1,x2,y2 = coor
        cv2.rectangle(img, (int(x1),int(y1)-60), (int(x2),int(y2)-60), color = (0,0,255), thickness = 2)
        cv2.putText(img, "Falling", (int(x1), int(y1)-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    return img

def openJson(filename):
    try:
        f = open(filename,'r')
        data = json.load(f)
        f.close()
    except JSONDecodeError:
        return 
    return data


def timetoint(hour,minute,second):
    
    return ((hour*3600)+(minute*60)+second) 

