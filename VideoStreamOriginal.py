from threading import Thread
import cv2

class WebcamVideoStream:
    def __init__(self,src):
        self.stream = self.open_cam_rtsp(src)
        (self.grabbed, self.frame) = self.stream.read()
        
        self.stopped = False
        
    def open_cam_rtsp(self,uri):
        gst_str = f'rtspsrc location={uri} ! rtph264depay ! h264parse ! omxh264dec ! nvvidconv ! video/x-raw, format=(string)BGRx! videoconvert !'
        
        return cv2.VideoCapture(uri, cv2.CAP_FFMPEG)
              

    def start(self):
        Thread(target = self.update, args= ()).start()
        return self
    
    def update(self):
        while True:
            if self.stopped:
                return
            
            (self.grabbed, self.frame) = self.stream.read()
            
    def read(self):	
        return self.grabbed,self.frame
    
    def stop(self):
        self.stopped = True
