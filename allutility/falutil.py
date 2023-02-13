import cv2
import time
import os
import json
from datetime import date,datetime
import shutil
import sqlite3

class Fallutil():

    def __init__(self):
        self.today = date.today()
        self.today = str(self.today)
        self.today= self.editdate()
        self.store = {
            "Camera1": {},
            "Camera2": {},
            "Camera3": {},
            "Camera4": {}
        }
        
        self.con = sqlite3.connect("fall_database.db")
        self.database = self.con.cursor()
        
    def final_fall(self,fall_coor,image,channel,delay):
        self.channel = channel
        ratio = open('./json/ratio.json','r')
        self.fallRatio = json.load(ratio)
        ratio.close()
        
        if channel == 1:
            self.kunci = "Camera1"
        elif channel == 2:
            self.kunci = "Camera2"
        elif channel == 3:
            self.kunci = "Camera3"
        else:
            self.kunci = "Camera4"
            
        self.checkInBox(fall_coor,image,channel)
        fallname = self.check_VFall(delay)
        
        return fallname
        
    def editdate(self):
        strtoday =""
        for i in self.today:
            if i != "-":
                strtoday += i
                
        return strtoday
    
    def checkKey(self,id,channel):
        for key in self.store[self.kunci]:
            if key[27:] == str(id) and key[25] == str(channel):
                self.key = key
                return True
        
    def drawredbox(self,img,coor):
        _,x1,y1,x2,y2= coor
        
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0,0,255), 2)
        
        return img

    def checkInBox(self,fall_coor,img,channel):
        path = './temp_falldown/cut'
        path_ss = './temp_falldown/screenshot'
            
        for coor in fall_coor:
            personId,x1,y1,x2,y2 = coor
            time_now = time.strftime('%H:%M:%S')
            
            if self.checkKey(int(personId),channel):
                time_now = time.strftime("%H%M%S")
                self.store[self.kunci][self.key]['time'] = time_now[:2] + ":" + time_now[2:4] + ":" + time_now[-2:]
                self.store[self.kunci][self.key]['counter'] += 1
            else:
                new_data = {
                    f"{self.today}_{time_now}_channel{channel}_{int(personId)}" :{
                        "counter" : 1,
                        "event": "fall down",
                        "pass":  False,
                        "saved": False,
                        "date" : self.today[:4] + "-" + self.today[4:6] + "-" + self.today[-2:],
                        "time" : time_now[:2] + ":" + time_now[3:5] + ":" + time_now[-2:],
                        "channel": channel,
                    }
                }
                filename = f"{self.today}_{time_now}_channel{channel}_{int(personId)}" + ".jpg"
                img = self.drawredbox(img,coor)
                try:
                    cv2.imwrite(os.path.join(path_ss,filename),img)
                    cv2.imwrite(os.path.join(path,filename),img[int(y1):int(y2),int(x1):int(x2)])
                except:
                    print('Failed to Save Falldown Image...')
                else:
                    print('Saving FallDown Image: Sucess...')
                self.store[self.kunci].update(new_data)

     
    def timetoint(self,hour,minute,second):
        
        return ((hour*3600)+(minute*60)+second) 
                        
    def check_VFall(self,delay):
        time_now = datetime.now()
        time_now_seconds = self.timetoint(time_now.hour, time_now.minute, time_now.second)
        self.deleteKey = []
        for key in self.store[self.kunci]:
            key_time_seconds = self.timetoint(int(self.store[self.kunci][key]['time'][:2]), int(self.store[self.kunci][key]['time'][3:5]), int(self.store[self.kunci][key]['time'][-2:]))    
            if (time_now_seconds - key_time_seconds) < delay:
                if int(self.store[self.kunci][key]['counter']) >= (delay*int(2*float(self.fallRatio['ratio']))):
                    self.store[self.kunci][key]['pass'] = True
                
        fallname = self.SaveFall()

        return fallname
    
    def SaveFall(self):
        temp_path = './temp_falldown/cut'
        temp_path_ss = './temp_falldown/screenshot'
        
        fixed_path = './falldown/cut'
        fixed_path_ss = './falldown/screenshot'
        
        key_temp = []
        
        for key in self.store[self.kunci]:
            if self.store[self.kunci][key]['pass'] == True and self.store[self.kunci][key]['saved'] == False:
                self.store[self.kunci][key]['saved'] = True
                key = key + ".jpg"
                
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
                
                event = self.store[self.kunci][key]["event"]
                tanggal =  self.store[self.kunci][key]["date"]
                waktu =  self.store[self.kunci][key]["time"]
                dateTime = tanggal + " " +waktu
                channel = self.store[self.kunci][key]["channel"]
            
                query = f"""
                INSERT INTO fall (FileName, Event, DateTime, channel)
                VALUES ('{key}', '{event}', '{dateTime}', '{channel}')
                """
                
                self.database.execute(query)
                self.database.commit()
            
                key_temp.append(key)

        for key in key_temp:
            del self.store[self.kunci][key]

        return key_temp