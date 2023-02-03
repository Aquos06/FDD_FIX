import cv2
import time
import os
import json
from datetime import date,datetime
from calculate import calculate
import shutil

class Fallutil():

    def __init__(self,channel):
        self.channel = channel
        if self.channel == 1:
            f = open('./temp_falldown/fall_store.json', 'r')
        elif self.channel == 2:
            f = open('./temp_falldown/fall_store2.json', 'r')
        elif self.channel == 3:
            f = open('./temp_falldown/fall_store3.json', 'r')
        elif self.channel == 4:
            f = open('./temp_falldown/fall_store4.json', 'r')
            
        self.fall_id = []
    
        self.fall_store = json.load(f)
        f.close()
        
        self.calculate = calculate()
        
        self.list_fd = []
        self.falldown = 0
        self.today = date.today()
        self.today = str(self.today)

        self.today= self.editdate()
        
    def final_fall(self,fall_coor,person_coor,image,channel, ROI,delay):
        self.checkInBox(fall_coor,person_coor,image,channel, ROI)
        fallname,total = self.check_VFall(delay)
        f = open('temp_falldown/fall_store.json', 'w')
        json.dump(self.fall_store, f, indent= 2)
        f.close()
        
        return fallname, total
        
    def editdate(self):
        strtoday =""
        for i in self.today:
            if i != "-":
                strtoday += i
                
        return strtoday
    
    def checkKey(self,id,channel):
        for key in self.fall_store:
            if key[25:] == str(id) and key[23] == str(channel):
                self.key = key
                return True

    def translateClass(self, classes):
        if classes == 4:
            classes = "chk"
            return  classes
            
        if classes == 5:
            classes = "Sit"
            return  classes
            
        if classes == 6:
            classes = "Lie Down"
            return  classes
             
        if classes == 7:
            classes = "Squat"
            return  classes
        
    def drawredbox(self,img,coor):
        x1,y1,x2,y2,_,_= coor
        
        cv2.rectangle(img.copy(), (int(x1), int(y1)), (int(x2), int(y2)), (0,0,255), 3)
        
        return img

    def checkInBox(self,fall_coor,person_coor,img,channel,ROI):
        path = './temp_falldown/cut'
        path_ss = './temp_falldown/screenshot'
        
        if channel == 1:
            mask_img = cv2.imread('./ROI/Camera1/fall_down.jpg')
        if channel == 2:
            mask_img = cv2.imread('./ROI/Camera2/fall_down.jpg')
        if channel == 3:
            mask_img = cv2.imread('./ROI/Camera3/fall_down.jpg')
        if channel == 4:
            mask_img = cv2.imread('./ROI/Camera4/fall_down.jpg')
            
        for i in person_coor:
            person_id,x1,y1,x2,y2 = i
            person_id = int(person_id)
            for j in fall_coor:
                x11,y11,x22,y22,confidence,classes= j
                CenterXX, CenterYY = (x22 + x11) / 2, (y22 + y11) / 2
                classes = self.translateClass(classes)
                if x1 < CenterXX < x2 and y1 < CenterYY <y2: 
                    if int(y11) < int(y22) and int(x11) < int(x22) :
                        if int(y11) > 5 and int(y22) > 5 and int(x11) > 5 and int(x22) > 5:
                            if self.calculate.find(mask_img, i) == 1 and ROI == True:
                                if self.checkKey(person_id,channel):
                                    time_now = time.strftime("%H%M%S")
                                    self.fall_store[self.key]['time'] = time_now[:2] + ":" + time_now[2:4] + ":" + time_now[-2:]
                                    self.fall_store[self.key]['counter'] += 1
                                else:
                                    time_now = time.strftime("%H:%M:%S")
                                    new_data = {
                                        f"{self.today}_{time_now}_channel{channel}_{person_id}" :{
                                            "counter" : 1,
                                            "event": "fall down", 
                                            "pass":  False,
                                            "saved": False,
                                            "date" : self.today[:4] + "-" + self.today[4:6] + "-" + self.today[-2:],
                                            "time" : time_now[:2] + ":" + time_now[2:4] + ":" + time_now[-2:],
                                            "channel": channel,
                                        }
                                    }
                                    filename = f"{self.today}_{time_now}_channel{channel}_{person_id}" + ".jpg"
                                    try:
                                        cv2.imwrite(os.path.join(path,filename),img[int(y11):int(y22),int(x11):int(x22)])
                                        cv2.imwrite(os.path.join(path_ss,filename),img)
                                    except:
                                        print('Failed to Save Falldown Image...')
                                    else:
                                        print('Saving FallDown Image: Sucess...')
                                    self.fall_store.update(new_data)
                                    img = self.drawredbox(img, j)
                            elif ROI == False:
                                time_now = time.strftime('%H:%M:%S')
                                if self.checkKey(person_id,channel):
                                    time_now = time.strftime("%H%M%S")
                                    self.fall_store[self.key]['time'] = time_now[:2] + ":" + time_now[2:4] + ":" + time_now[-2:]
                                    self.fall_store[self.key]['counter'] += 1
                                else:
                                    new_data = {
                                        f"{self.today}_{time_now}_channel{channel}_{person_id}" :{
                                            "counter" : 1,
                                            "event": "fall down",
                                            "pass":  False,
                                            "saved": False,
                                            "date" : self.today[:4] + "-" + self.today[4:6] + "-" + self.today[-2:],
                                            "time" : time_now[:2] + ":" + time_now[2:4] + ":" + time_now[-2:],
                                            "channel": channel,
                                        }
                                    }
                                    filename = f"{self.today}_{time_now}_channel{channel}_{person_id}" + ".jpg"
                                    try:
                                        cv2.imwrite(os.path.join(path_ss,filename),img)
                                        cv2.imwrite(os.path.join(path,filename),img[int(y11):int(y22),int(x11):int(x22)])
                                    except:
                                        print('Failed to Save Falldown Image...')
                                    else:
                                        print('Saving FallDown Image: Sucess...')
                                    self.fall_store.update(new_data)
                                    img = self.drawredbox(img,j)
                
     
    def timetoint(self,hour,minute,second):
        
        return ((hour*3600)+(minute*60)+second) 
                        
    def check_VFall(self,delay):
        time_now = datetime.now()
        time_now_seconds = self.timetoint(time_now.hour, time_now.minute, time_now.second)
        deleteFall = []
        for key in self.fall_store:
            
            key_time_seconds = self.timetoint(int(self.fall_store[key]['time'][:2]), int(self.fall_store[key]['time'][3:5]), int(self.fall_store[key]['time'][-2:]))    
            if time_now_seconds - key_time_seconds > delay:
                if self.fall_store[key]['counter'] > 3:
                    self.fall_store[key]['pass'] = True
                
        fallname,total = self.SaveFall()
            
        return fallname, total
    
    def SaveFall(self):
        temp_path = './temp_falldown/cut'
        temp_path_ss = './temp_falldown/screenshot'
        
        fixed_path = './falldown/cut'
        fixed_path_ss = './falldown/screenshot'
        
        if self.channel == 1:
            self.path = 'falldown/all_falldown.json' 
        elif self.channel == 2:
            self.path = 'falldown/all_falldown2.json'
        elif self.channel == 3:
            self.path = 'falldown/all_falldown3.json'
        elif self.channel == 4:
            self.path = 'falldown/all_falldown4.json'  

        with open(self.path, 'r') as j:
            self.fall_data = json.loads(j.read())
        
        key_temp = []
        
        for key in self.fall_store:
            if self.fall_store[key]['pass'] == True and self.fall_store[key]['saved'] == False:
                self.fall_store[key]['saved'] = True
                self.falldown += 1
                key = key + ".jpg"
                self.list_fd.append(key)
                
                if shutil.disk_usage("./falldown").free < 1000:
                    if self.config["utils"]["storageMethod"] == True:
                        return
                    else:
                        for filename in reversed(os.listdir("./falldown")):
                            if filename[:-4] == ".jpg":
                                os.remove(filename)
                                break
                
                shutil.move(os.path.join(temp_path,key), os.path.join(fixed_path,key), copy_function= shutil.copy2)
                shutil.move(os.path.join(temp_path_ss,key), os.path.join(fixed_path_ss,key), copy_function= shutil.copy2)
                
                key = key[:-4]
                
                newdata = {
                    key : {
                        "event": self.fall_store[key]["event"],
                        "date" : self.fall_store[key]["date"],
                        "time" : self.fall_store[key]["time"],
                        "channel": self.fall_store[key]["channel"]
                    }
                }    
            
                self.fall_data.update(newdata)
                key_temp.append(key)
                
                self.falldown += 1

        for key in key_temp:
            del self.fall_store[key]
        
        if self.channel == 1:
            f = open('./falldown/all_falldown.json', "w")
        elif self.channel == 2:
            f = open('./falldown/all_falldown2.json', 'w')
        elif self.channel == 3:
            f = open('./falldown/all_falldown3.json', 'w')
        elif self.channel == 4:
            f = open('./falldown/all_falldown4.json', 'w')   
            
        json.dump(self.fall_data, f, indent=2)
        f.close()

        return key_temp, self.falldown
    
        
