#!/usr/bin/env python
from contextlib import closing
from socket import socket, AF_INET, SOCK_DGRAM
import struct
from PyQt5.QtCore import QObject
from PyQt5 import QtCore
import json
from time import ctime

class UpdateTime(QObject):
    dateTime = QtCore.pyqtSignal(str)
    fail = QtCore.pyqtSignal(bool)

    def variable(self):
        self.NTP_PACKET_FORMAT = "!12I"
        self.NTP_DELTA = 2208988800  # 1970-01-01 00:00:00
        self.NTP_QUERY = b'\x1b' + 47 * b'\0'  
    
    def ntp_time(self, host="pool.ntp.org", port=123):
        with closing(socket( AF_INET, SOCK_DGRAM)) as s:
            s.sendto(self.NTP_QUERY, (host, port))
            msg, address = s.recvfrom(1024)
        unpacked = struct.unpack(self.NTP_PACKET_FORMAT,
                    msg[0:struct.calcsize(self.NTP_PACKET_FORMAT)])
        return unpacked[10] + float(unpacked[11]) / 2**32 - self.NTP_DELTA

    def run(self):
        self.variable()
        while True:
            try:
                f = open('json/time.json', 'r')
                data = json.load(f)
                f.close()
            except:
                pass
            
            if data['change'] == True:
                servTime = data['server']
                try:
                    a = ctime(self.ntp_time(host=servTime)).replace("  "," ")
                    self.serv = servTime
                    self.fail.emit(False)
                except:
                    self.fail.emit(True)
                    a = ctime(self.ntp_time(host=self.serv)).replace("  "," ")

                data['change'] = False

                f = open('json/time.json', 'w')
                json.dump(data,f,indent=2)
                f.close()
                
            else:
                a = ctime(self.ntp_time(host = self.serv)).replace("  ", " ")
            month = a.split(" ")[1]
            date = a.split(" ")[2]
            year = a.split(" ")[-1] 

            date = date + " " + month + " " + year 
            time = a.split(" ")[3]

            datetime = date + " " + time
            self.dateTime.emit(datetime)
