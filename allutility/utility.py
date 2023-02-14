import json
import csv
from datetime import datetime

def text(Event,time,channel):
    text =  f'Event: {Event} ' + \
            f'<br />Time: {time}' + \
            f'<br />Channel: {channel} '
    
    return text

def textforstat(Event,time,date,channel):
    text =  f'Event: {Event} ' + \
            f'<br />Time: {time}' + \
            f'<br />Date: {date}' + \
            f'<br />Channel: {channel} '
    
    return text 

def timetoint(hour,minute,second):
        
    return ((hour*3600)+(minute*60)+second) 

def setupLogin():
    f = open('json/personal.json', 'w')
    data = {
        "loggedIn": False
            }
    json.dump(data,f,indent=2)
    f.close()
    
    
    f = open('json/config2Channels.json', 'r')
    data = json.load(f)
    f.close()
    
    data['channel1']['change'] = False
    data['channel2']['change'] = False
    data['channel3']['change'] = False
    data['channel4']['change'] = False
    
    f = open('json/config2Channels.json', 'w')
    json.dump(data,f,indent=2)
    f.close()

def toLog(activity):
    with open('./settings/log.csv', 'a', newline ='') as file:
        writer = csv.writer(file)
        now = datetime.now()
        writer.writerow([now.strftime("%Y-%m-%d %H:%M"), "admin", activity])
        file.close()   

