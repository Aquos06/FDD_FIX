import requests
from requests.auth import HTTPDigestAuth
import os

def setTime(date,time):
    link = f"http://192.168.0.21/cgi-bin/global.cgi?action=setCurrentTime&time={date}%20{time}"
    res = requests.post(link, auth = HTTPDigestAuth("admin", "ai123456"))
    print(res.status_code)

def getTime():
    link = "http://192.168.0.21/cgi-bin/global.cgi?action=getCurrentTime"
    res = requests.get(link, auth = HTTPDigestAuth("admin", "ai123456"))
    print(res.status_code)
    dateTime = res.text.split("=")[-1]
    date = dateTime.split(" ")[0]
    time = dateTime.split(" ")[-1]
    dateTime = date + " " +  time[:-2]
    cmd = f'timedatectl set-time "{dateTime}"'
    os.system(cmd)

if __name__ == "__main__":
    getTime()