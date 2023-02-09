import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random
import numpy as np

from models.experimental import attempt_load
from yolov7Util.general import non_max_suppression, set_logging
from yolov7Util.torch_utils import select_device, TracedModel

import sys


class detect():
    def __init__(self):
        set_logging()
        self.device = select_device('0')
        self.model = attempt_load('best.pt', map_location= self.device)
        self.model(torch.zeros(1, 3, 640, 640).to(self.device).type_as(next(self.model.parameters())))
        # self.model = TracedModel(self.model, self.device, 640)
        self.model.half()

        self.names = self.model.module.names if hasattr(self.model, 'module') else self.model.names
        self.colors = [[random.randint(0,255) for _ in range(3)] for _ in self.names]

    def letterbox(self,img, new_shape=(640, 640), color=(114, 114, 114), auto=True, scaleFill=False, scaleup=True, stride=32): #original 640
        # Resize and pad image while meeting stride-multiple constraints
        shape = img.shape[:2]  # current shape [height, width]
        if isinstance(new_shape, int):
            new_shape = (new_shape, new_shape)

        # Scale ratio (new / old)
        r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
        if not scaleup:  # only scale down, do not scale up (for better test mAP)
            r = min(r, 1.0)

        # Compute padding
        ratio = r, r  # width, height ratios
        new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))
        dw, dh = new_shape[1] - new_unpad[0], new_shape[0] - new_unpad[1]  # wh padding
        if auto:  # minimum rectangle
            dw, dh = np.mod(dw, stride), np.mod(dh, stride)  # wh padding
        elif scaleFill:  # stretch
            dw, dh = 0.0, 0.0
            new_unpad = (new_shape[1], new_shape[0])
            ratio = new_shape[1] / shape[1], new_shape[0] / shape[0]  # width, height ratios

        dw /= 2  # divide padding into 2 sides
        dh /= 2

        if shape[::-1] != new_unpad:  # resize
            img = cv2.resize(img, new_unpad, interpolation=cv2.INTER_LINEAR)
        top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
        left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
        img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border
        return img

    def predict(self, img1):
        img = self.letterbox(img1)
        img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
        self.img = np.ascontiguousarray(img)
        self.img = torch.from_numpy(self.img).to(self.device)
        self.img = self.img.half()
        self.img /= 255.0

        if self.img.ndimension() ==3:
            self.img = self.img.unsqueeze(0)

        with torch.no_grad():
            self.pred = self.model(self.img, augment = False)[0]
            self.pred = non_max_suppression(self.pred, 0.6,0.45,agnostic=True)

        self.pred = self.pred[0].cpu().tolist()

        return self.pred #xcenter, ycenter, width, height, conf, class
    

if __name__ == '__main__':
    sys.path.insert(0,'./FALL_V.5_PP_API')
    detect= detect()
            
            
    
