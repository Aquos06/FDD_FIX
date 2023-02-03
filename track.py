# limit the number of cpus used by high performance libraries
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import sys
from pathlib import Path
import torch
import numpy as np

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # yolov5 strongsort root directory
WEIGHTS = ROOT / 'weights'

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
if str(ROOT / 'yolov5') not in sys.path:
    sys.path.append(str(ROOT / 'yolov5'))  # add yolov5 ROOT to PATH
if str(ROOT / 'trackers' / 'strong_sort') not in sys.path:
    sys.path.append(str(ROOT / 'trackers' / 'strong_sort'))  # add strong_sort ROOT to PATH
if str(ROOT / 'trackers' / 'ocsort') not in sys.path:
    sys.path.append(str(ROOT / 'trackers' / 'ocsort'))  # add strong_sort ROOT to PATH
if str(ROOT / 'trackers' / 'strong_sort' / 'deep' / 'reid' / 'torchreid') not in sys.path:
    sys.path.append(str(ROOT / 'trackers' / 'strong_sort' / 'deep' / 'reid' / 'torchreid'))  # add strong_sort ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

import logging

from trackers.ocsort.ocsort import OCSort




class Trackker:
    def __init__(self):
        self.nr_sources = 1
        self.pred_thresh = 0.45
        self.iou_threshold = 0.2
        self.use_byte = False 
        self.deleted_id = []

    # Create as many strong sort instances as there are video sources
    def preparation(self):
        
        self.tracker_list = []
        for i in range(self.nr_sources):
            self.tracker = OCSort(
                det_thresh=0.45,
                iou_threshold=0.2,
                use_byte=False 
            )
            self.tracker_list.append(self.tracker, )
            if hasattr(self.tracker_list[i], 'model'):
                if hasattr(self.tracker_list[i].model, 'warmup'):
                    self.tracker_list[i].model.warmup()
        self.outputs = [None] * self.nr_sources

    # Run tracking
        self.dt, self.seen = [0.0, 0.0, 0.0, 0.0], 0
        
    def xyxy2xywh(self,x):
        # Convert nx4 boxes from [x1, y1, x2, y2] to [x, y, w, h] where xy1=top-left, xy2=bottom-right
        y = x.clone() if isinstance(x, torch.Tensor) else np.copy(x)
        y[:, 0] = (x[:, 0] + x[:, 2]) / 2  # x center
        y[:, 1] = (x[:, 1] + x[:, 3]) / 2  # y center
        y[:, 2] = x[:, 2] - x[:, 0]  # width
        y[:, 3] = x[:, 3] - x[:, 1]  # height
        
        return y
    
    def tracking(self, pred, img):
        self.return_res = []
        
        #pred = yolov5_engine [xmin, ymin, xmax, ymax, conf, id]
        self.seen += 1
        
        if pred is not None and len(pred):
            # Print results
            xywhs = torch.from_numpy(self.xyxy2xywh(pred[:,:4]))
            confs = torch.from_numpy(pred[:, 4])
            clss = torch.from_numpy(pred[:, 5])

            # pass predections to strongsort
            self.outputs[0] = self.tracker_list[0].update(xywhs.cpu(), confs.cpu(), clss.cpu(), img)


            # draw boxes for visualization
            if len(self.outputs[0]) > 0:
                for j, (output, conf) in enumerate(zip(self.outputs[0], confs)):

                    bboxes = output[0:4]
                    person_id = output[4]
                    cls = output[5]


                    bbox_left = output[0]
                    bbox_top = output[1]
                    bbox_w = output[2] 
                    bbox_h = output[3] 
                    
                    # Write MOT compliant results to file
                    self.return_res.append([person_id, bbox_left,bbox_top, bbox_w, bbox_h])
            self.deleted_id = self.tracker.deleted_id.copy()

        else:
            return self.return_res, self.deleted_id
        
        return self.return_res,self.deleted_id

