import json
import os
import struct
import shutil

from .timeAPI import setTime
from contextlib import closing
from socket import socket, AF_INET, SOCK_DGRAM
from time import ctime
from utility import toLog

def setWaktu(server):

    NTP_PACKET_FORMAT = "!12I"
    NTP_DELTA = 2208988800  # 1970-01-01 00:00:00
    NTP_QUERY = b'\x1b' + 47 * b'\0'  

    with closing(socket( AF_INET, SOCK_DGRAM)) as s:
        s.sendto(NTP_QUERY, (server, 123))
        msg, address = s.recvfrom(1024)
    unpacked = struct.unpack(NTP_PACKET_FORMAT,
                msg[0:struct.calcsize(NTP_PACKET_FORMAT)])
    return unpacked[10] + float(unpacked[11]) / 2**32 - NTP_DELTA

def realMonth(month):
    monthlist = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Des']
    monthint = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    return monthint[monthlist.index(month)]

def returnTime():
    a = ctime(setWaktu("pool.ntp.org")).replace("  "," ")
    date = a.split(' ')[-1] + "-" + realMonth(a.split(' ')[1]) + "-" + a.split(' ')[2]
    time = a.split(' ')[3]
    
    dateTime = date + " " + time

    setTime(date,time)
    cmd = f'timedatectl set-time "{dateTime}"'
    os.system(cmd)

def resetIP():
    ip = "192.168.0.10"
    cmd = f'sudo ifconfig eth0 {ip} netmask 255.255.255.0'

    os.system(cmd)

def resetROI():
    onePath = '/home/nvidia/Desktop/fall_v.5_pp_API/ROI/Camera1/blank.jpg'
    Path1 = '/home/nvidia/Desktop/fall_v.5_pp_API/ROI/Camera1'
    shutil.copyfile(onePath, os.path.join(Path1, 'fall_down.jpg'))
    shutil.copyfile(onePath, os.path.join(Path1, 'person.jpg'))
    shutil.copyfile(onePath, os.path.join(Path1, 'PPE.jpg'))

    Path2 = '/home/nvidia/Desktop/fall_v.5_pp_API/ROI/Camera2'
    shutil.copyfile(onePath, os.path.join(Path2, 'fall_down.jpg'))
    shutil.copyfile(onePath, os.path.join(Path2, 'person.jpg'))
    shutil.copyfile(onePath, os.path.join(Path2, ' PPE.jpg'))

def FactoryReset():
    f = open('factoryreset/AiSettings.json', 'r')
    data = json.load(f)
    f.close()
    f = open('AiSettings.json', 'w')
    json.dump(data,f,indent=2)
    f.close()

    f = open('factoryreset/config2Channels.json','r')
    data = json.load(f)
    f.close()
    f = open('config2Channels.json', 'w')
    json.dump(data,f,indent=2)
    f.close()

    f = open('factoryreset/function.json', 'r')
    data = json.load(f)
    f.close()
    f = open('function.json', 'w')
    json.dump(data,f,indent=2)
    f.close()

    f = open('factoryreset/loggin.json', 'r')
    data =json.load(f)
    f.close()
    f = open('output/loggin.json', 'w')
    json.dump(data,f,indent=2)
    f.close()

    f = open('factoryreset/nxconfig.json', 'r')
    data = json.load(f)
    f.close()
    f = open('json/nxconfig.json', 'w')
    json.dump(data,f,indent=2)
    f.close()

    f = open('factoryreset/time.json', 'r')
    data = json.load(f)
    f.close()
    f = open('json/time.json' , 'w')
    json.dump(data,f,indent=2)

    f = open('factoryreset/timeTable.json', 'r')
    data = json.load(f)
    f.close()
    f = open('json/timeTable.json', 'w')
    json.dump(data,f,indent=2)
    f.close()

    returnTime()
    resetIP()
    resetROI()
    toLog("All Settings are reseted")

