import cv2
import time
import os
import json
from datetime import date,datetime
import shutil

class Fallutil():

    def __init__(self):
        self.today = date.today()
        self.today = str(self.today)

        self.today= self.editdate()
        
    def final_fall(self,fall_coor,image,channel,delay):
        self.channel = channel
        ratio = open('./json/ratio.json','r')
        self.fallRatio = json.load(ratio)
        ratio.close()
        
        if channel == 1:
            f = open('./temp_falldown/fall_store.json', 'r')
        elif channel == 2:
            f = open('./temp_falldown/fall_store2.json', 'r')
        elif channel == 3:
            f = open('./temp_falldown/fall_store3.json', 'r')
        else:
            f = open('./temp_falldown/fall_store4.json', 'r')
            
        self.fall_store = json.load(f)
        f.close()    
            
        self.checkInBox(fall_coor,image,channel)
        fallname = self.check_VFall(delay)
        
        
        if channel == 1:
            f = open('temp_falldown/fall_store.json', 'w')
        elif channel == 2:
            f = open('temp_falldown/fall_store2.json','w')
        elif channel == 3:
            f = open('temp_falldown/fall_store3.json', 'w')
        else:
            f = open('temp_falldown/fall_store4.json','w')
        json.dump(self.fall_store, f, indent= 2)
        f.close()
        
        return fallname
        
    def editdate(self):
        strtoday =""
        for i in self.today:
            if i != "-":
                strtoday += i
                
        return strtoday
    
    def checkKey(self,id,channel):
        for key in self.fall_store:
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
                self.fall_store[self.key]['time'] = time_now[:2] + ":" + time_now[2:4] + ":" + time_now[-2:]
                self.fall_store[self.key]['counter'] += 1
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
                self.fall_store.update(new_data)

     
    def timetoint(self,hour,minute,second):
        
        return ((hour*3600)+(minute*60)+second) 
                        
    def check_VFall(self,delay):
        time_now = datetime.now()
        time_now_seconds = self.timetoint(time_now.hour, time_now.minute, time_now.second)
        self.deleteKey = []
        for key in self.fall_store:
            key_time_seconds = self.timetoint(int(self.fall_store[key]['time'][:2]), int(self.fall_store[key]['time'][3:5]), int(self.fall_store[key]['time'][-2:]))    
            print(f"{time_now_seconds-key_time_seconds} < {delay}")
            if (time_now_seconds - key_time_seconds) < delay:
                if int(self.fall_store[key]['counter']) >= (delay*int(2*float(self.fallRatio['ratio']))):
                # if self.fall_store[key]['counter'] > 1:
                    print(f"{int(self.fall_store[key]['counter'])} delay: {delay * int(2*float(self.fallRatio['ratio']))}")
                    self.fall_store[key]['pass'] = True
                
        fallname = self.SaveFall()

        return fallname
    
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
                
                # self.falldown += 1

        # for key in key_temp:
        #     del self.fall_store[key]
        
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

        return key_temp