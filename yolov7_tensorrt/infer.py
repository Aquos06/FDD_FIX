import cv2
import tensorrt as trt
import torch
import numpy as np
from collections import OrderedDict,namedtuple
import time
import os

class TRT_engine():
    def __init__(self, weight) -> None:
        self.imgsz = [640,640]
        self.weight = weight
        self.device = torch.device('cuda:0')
        self.init_engine()

    def init_engine(self):
        # Infer TensorRT Engine
        self.Binding = namedtuple('Binding', ('name', 'dtype', 'shape', 'data', 'ptr'))
        self.logger = trt.Logger(trt.Logger.INFO)
        trt.init_libnvinfer_plugins(self.logger, namespace="")
        with open(self.weight, 'rb') as self.f, trt.Runtime(self.logger) as self.runtime:
            self.model = self.runtime.deserialize_cuda_engine(self.f.read())
        self.bindings = OrderedDict()
        self.fp16 = False
        for index in range(self.model.num_bindings):
            print(index)
            self.name = self.model.get_binding_name(index)
            self.dtype = trt.nptype(self.model.get_binding_dtype(index))
            self.shape = tuple(self.model.get_binding_shape(index))
            self.data = torch.from_numpy(np.empty(self.shape, dtype=np.dtype(self.dtype))).to(self.device)
            self.bindings[self.name] = self.Binding(self.name, self.dtype, self.shape, self.data, int(self.data.data_ptr()))
            if self.model.binding_is_input(index) and self.dtype == np.float16:
                self.fp16 = True
        self.binding_addrs = OrderedDict((n, d.ptr) for n, d in self.bindings.items())
        self.context = self.model.create_execution_context()

    def letterbox(self,im,color=(114, 114, 114), auto=False, scaleup=True, stride=32):
        # Resize and pad image while meeting stride-multiple constraints
        shape = im.shape[:2]  # current shape [height, width]
        new_shape = self.imgsz
        if isinstance(new_shape, int):
            new_shape = (new_shape, new_shape)
        # Scale ratio (new / old)
        self.r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
        if not scaleup:  # only scale down, do not scale up (for better val mAP)
            self.r = min(self.r, 1.0)
        # Compute padding
        new_unpad = int(round(shape[1] * self.r)), int(round(shape[0] * self.r))
        self.dw, self.dh = new_shape[1] - new_unpad[0], new_shape[0] - new_unpad[1]  # wh padding
        if auto:  # minimum rectangle
            self.dw, self.dh = np.mod(self.dw, stride), np.mod(self.dh, stride)  # wh padding
        self.dw /= 2  # divide padding into 2 sides
        self.dh /= 2
        if shape[::-1] != new_unpad:  # resize
            im = cv2.resize(im, new_unpad, interpolation=cv2.INTER_LINEAR)
        top, bottom = int(round(self.dh - 0.1)), int(round(self.dh + 0.1))
        left, right = int(round(self.dw - 0.1)), int(round(self.dw + 0.1))
        self.img = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border
        return self.img,self.r,self.dw,self.dh

    def preprocess(self,image):
        self.img,self.r,self.dw,self.dh = self.letterbox(image)
        self.img = self.img.transpose((2, 0, 1))
        self.img = np.expand_dims(self.img,0)
        self.img = np.ascontiguousarray(self.img)
        self.img = torch.from_numpy(self.img).to(self.device)
        self.img = self.img.float()
        return self.img

    def predict(self,img,threshold):
        img = self.preprocess(img)
        self.binding_addrs['images'] = int(img.data_ptr())
        self.context.execute_v2(list(self.binding_addrs.values()))
        nums = self.bindings['num_dets'].data[0].tolist()
        boxes = self.bindings['det_boxes'].data[0].tolist()
        scores =self.bindings['det_scores'].data[0].tolist()
        classes = self.bindings['det_classes'].data[0].tolist()
        num = int(nums[0])
        # num = sum(i!=0 for i in scores)
        new_bboxes = []
        for i in range(num):
            if(scores[i] < threshold):
                continue
            xmin = (boxes[i][0] - self.dw)/self.r
            ymin = (boxes[i][1] - self.dh)/self.r
            xmax = (boxes[i][2] - self.dw)/self.r
            ymax = (boxes[i][3] - self.dh)/self.r
            new_bboxes.append([classes[i],scores[i],xmin,ymin,xmax,ymax])
        return new_bboxes

def visualize(img,bbox_array):
    for temp in bbox_array:
        xmin = int(temp[2])
        ymin = int(temp[3])
        xmax = int(temp[4])
        ymax = int(temp[5])
        clas = int(temp[0])
        score = temp[1]
        cv2.rectangle(img,(xmin,ymin),(xmax,ymax), (105, 237, 249), 3)
        img = cv2.putText(img, "class:"+str(clas)+" "+str(round(score,2)), (xmin,int(ymin)-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (105, 237, 249), 1)
    return img

# import threading
# import time
# import cv2
# import numpy as np
# import pycuda.driver as cuda
# import tensorrt as trt
# import torch
# import torchvision

# CONF_THRESH = 0.5
# IOU_THRESHOLD = 0.4

# class YoLov5TRT(object):
#     """
#     description: A YOLOv5 class that warps TensorRT ops, preprocess and postprocess ops.
#     """

#     def __init__(self, engine_file_path):
#         # Create a Context on this device,
#         self.ctx = cuda.Device(0).make_context()
#         stream = cuda.Stream()
#         TRT_LOGGER = trt.Logger(trt.Logger.INFO)
#         runtime = trt.Runtime(TRT_LOGGER)

#         # Deserialize the engine from file
#         with open(engine_file_path, "rb") as f:
#             engine = runtime.deserialize_cuda_engine(f.read())
#         context = engine.create_execution_context()

#         host_inputs = []
#         cuda_inputs = []
#         host_outputs = []
#         cuda_outputs = []
#         bindings = []

#         for binding in engine:
#             print('bingding:', binding, engine.get_binding_shape(binding))
#             size = trt.volume(engine.get_binding_shape(binding)) * engine.max_batch_size
#             dtype = trt.nptype(engine.get_binding_dtype(binding))
#             # Allocate host and device buffers
#             host_mem = cuda.pagelocked_empty(size, dtype)
#             cuda_mem = cuda.mem_alloc(host_mem.nbytes)
#             # Append the device buffer to device bindings.
#             bindings.append(int(cuda_mem))
#             # Append to the appropriate list.
#             if engine.binding_is_input(binding):
#                 self.input_w = engine.get_binding_shape(binding)[-1]
#                 self.input_h = engine.get_binding_shape(binding)[-2]
#                 host_inputs.append(host_mem)
#                 cuda_inputs.append(cuda_mem)
#             else:
#                 host_outputs.append(host_mem)
#                 cuda_outputs.append(cuda_mem)

#         # Store
#         self.stream = stream
#         self.context = context
#         self.engine = engine
#         self.host_inputs = host_inputs
#         self.cuda_inputs = cuda_inputs
#         self.host_outputs = host_outputs
#         self.cuda_outputs = cuda_outputs
#         self.bindings = bindings
#         self.batch_size = engine.max_batch_size
        
#     def infer(self, raw_image_generator):
#         threading.Thread.__init__(self)
#         # Make self the active context, pushing it on top of the context stack.
#         self.ctx.push()
#         # Restore
#         stream = self.stream
#         context = self.context
#         engine = self.engine
#         host_inputs = self.host_inputs
#         cuda_inputs = self.cuda_inputs
#         host_outputs = self.host_outputs
#         cuda_outputs = self.cuda_outputs
#         bindings = self.bindings
#         # Do image preprocess
#         batch_image_raw = []
#         batch_origin_h = []
#         batch_origin_w = []
#         batch_input_image = np.empty(shape=[self.batch_size, 3, self.input_h, self.input_w])
#         for i, image_raw in enumerate(raw_image_generator):
#             input_image, image_raw, origin_h, origin_w = self.preprocess_image(image_raw)
#             batch_image_raw.append(image_raw)
#             batch_origin_h.append(origin_h)
#             batch_origin_w.append(origin_w)
#             np.copyto(batch_input_image[i], input_image)
#         batch_input_image = np.ascontiguousarray(batch_input_image)

#         # Copy input image to host buffer
#         np.copyto(host_inputs[0], batch_input_image.ravel())
#         start = time.time()
#         # Transfer input data  to the GPU.
#         cuda.memcpy_htod_async(cuda_inputs[0], host_inputs[0], stream)
#         # Run inference.
#         context.execute_async(batch_size=self.batch_size, bindings=bindings, stream_handle=stream.handle)
#         # Transfer predictions back from the GPU.
#         cuda.memcpy_dtoh_async(host_outputs[0], cuda_outputs[0], stream)
#         # Synchronize the stream
#         stream.synchronize()
#         end = time.time()
#         # Remove any context from the top of the context stack, deactivating it.
#         self.ctx.pop()
#         # Here we use the first row of output in that batch_size = 1
#         output = host_outputs[0]
#         # Do postprocess
#         res = []
#         #[(0, [1704, 680, 1914, 880], 0.2763671875), (0, [1238, 666, 1512, 1077], 0.75244140625)]
#         #[(class,bbox,conf),(class,bbox,conf),(class,bbox,conf),...]
#         for i in range(self.batch_size):
#             result_boxes, result_scores, result_classid = self.post_process(
#                 output[i * 6001: (i + 1) * 6001], batch_origin_h[i], batch_origin_w[i]
#             )

#             # Draw rectangles and labels on the original image
#             for j in range(len(result_boxes)):
#                 res.append((int(result_classid[j]),result_boxes[j].tolist(),result_scores[j].item()))
                
#         return batch_image_raw ,res, end - start

#     def destroy(self):
#         # Remove any context from the top of the context stack, deactivating it.
#         self.ctx.pop()
        
#     def get_raw_image(self, image_path_batch):
#         """
#         description: Read an image from image path
#         """
#         for img_path in image_path_batch:
#             yield cv2.imread(img_path)
        
#     def get_raw_image_zeros(self, image_path_batch=None):
#         """
#         description: Ready data for warmup
#         """
#         for _ in range(self.batch_size):
#             yield np.zeros([self.input_h, self.input_w, 3], dtype=np.uint8)

#     def preprocess_image(self, raw_bgr_image):
#         """
#         description: Convert BGR image to RGB,
#                      resize and pad it to target size, normalize to [0,1],
#                      transform to NCHW format.
#         param:
#             input_image_path: str, image path
#         return:
#             image:  the processed image
#             image_raw: the original image
#             h: original height
#             w: original width
#         """
#         image_raw = raw_bgr_image
#         h, w, c = image_raw.shape
#         image = cv2.cvtColor(image_raw, cv2.COLOR_BGR2RGB)
#         # Calculate widht and height and paddings
#         r_w = self.input_w / w
#         r_h = self.input_h / h
#         if r_h > r_w:
#             tw = self.input_w
#             th = int(r_w * h)
#             tx1 = tx2 = 0
#             ty1 = int((self.input_h - th) / 2)
#             ty2 = self.input_h - th - ty1
#         else:
#             tw = int(r_h * w)
#             th = self.input_h
#             tx1 = int((self.input_w - tw) / 2)
#             tx2 = self.input_w - tw - tx1
#             ty1 = ty2 = 0
#         # Resize the image with long side while maintaining ratio
#         image = cv2.resize(image, (tw, th))
#         # Pad the short side with (128,128,128)
#         image = cv2.copyMakeBorder(
#             image, ty1, ty2, tx1, tx2, cv2.BORDER_CONSTANT, (128, 128, 128)
#         )
#         image = image.astype(np.float32)
#         # Normalize to [0,1]
#         image /= 255.0
#         # HWC to CHW format:
#         image = np.transpose(image, [2, 0, 1])
#         # CHW to NCHW format
#         image = np.expand_dims(image, axis=0)
#         # Convert the image to row-major order, also known as "C order":
#         image = np.ascontiguousarray(image)
#         return image, image_raw, h, w

#     def xywh2xyxy(self, origin_h, origin_w, x):
#         """
#         description:    Convert nx4 boxes from [x, y, w, h] to [x1, y1, x2, y2] where xy1=top-left, xy2=bottom-right
#         param:
#             origin_h:   height of original image
#             origin_w:   width of original image
#             x:          A boxes tensor, each row is a box [center_x, center_y, w, h]
#         return:
#             y:          A boxes tensor, each row is a box [x1, y1, x2, y2]
#         """
#         y = torch.zeros_like(x) if isinstance(x, torch.Tensor) else np.zeros_like(x)
#         r_w = self.input_w / origin_w
#         r_h = self.input_h / origin_h
#         if r_h > r_w:
#             y[:, 0] = x[:, 0] - x[:, 2] / 2
#             y[:, 2] = x[:, 0] + x[:, 2] / 2
#             y[:, 1] = x[:, 1] - x[:, 3] / 2 - (self.input_h - r_w * origin_h) / 2
#             y[:, 3] = x[:, 1] + x[:, 3] / 2 - (self.input_h - r_w * origin_h) / 2
#             y /= r_w
#         else:
#             y[:, 0] = x[:, 0] - x[:, 2] / 2 - (self.input_w - r_h * origin_w) / 2
#             y[:, 2] = x[:, 0] + x[:, 2] / 2 - (self.input_w - r_h * origin_w) / 2
#             y[:, 1] = x[:, 1] - x[:, 3] / 2
#             y[:, 3] = x[:, 1] + x[:, 3] / 2
#             y /= r_h

#         return y

#     def post_process(self, output, origin_h, origin_w):
#         """
#         description: postprocess the prediction
#         param:
#             output:     A tensor likes [num_boxes,cx,cy,w,h,conf,cls_id, cx,cy,w,h,conf,cls_id, ...] 
#             origin_h:   height of original image
#             origin_w:   width of original image
#         return:
#             result_boxes: finally boxes, a boxes tensor, each row is a box [x1, y1, x2, y2]
#             result_scores: finally scores, a tensor, each element is the score correspoing to box
#             result_classid: finally classid, a tensor, each element is the classid correspoing to box
#         """
#         # Get the num of boxes detected
#         num = int(output[0])
#         # Reshape to a two dimentional ndarray
#         pred = np.reshape(output[1:], (-1, 6))[:num, :]
#         # to a torch Tensor
#         pred = torch.Tensor(pred).cuda()
#         # Get the boxes
#         boxes = pred[:, :4]
#         # Get the scores
#         scores = pred[:, 4]
#         # Get the classid
#         classid = pred[:, 5]
#         # Choose those boxes that score > CONF_THRESH
#         si = scores > CONF_THRESH
#         boxes = boxes[si, :]
#         scores = scores[si]
#         classid = classid[si]
#         # Trandform bbox from [center_x, center_y, w, h] to [x1, y1, x2, y2]
#         boxes = self.xywh2xyxy(origin_h, origin_w, boxes)
#         # Do nms
#         indices = torchvision.ops.nms(boxes, scores, iou_threshold=IOU_THRESHOLD).cpu()
#         result_boxes = boxes[indices, :].cpu()
#         result_scores = scores[indices].cpu()
#         result_classid = classid[indices].cpu()
#         return result_boxes, result_scores, result_classid


class Predictor:
    def __init__(self):
        self.trt_engine = TRT_engine("./fall_infer/best.engine")

    def fallPredict(self, image):
        results = self.trt_engine.predict(image, threshold=0.4)
        image= visualize(image, results)
        return image


def main():
    dir = 'outset4.mp4'
    yolo_trt = Predictor()

    video = cv2.VideoCapture(dir)
    while video.isOpened():

        start = time.time()
        ret, image = video.read()
        image = cv2.resize(image,(640,640), interpolation = cv2.INTER_AREA)
        image = yolo_trt.fallPredict(image)
        cv2.imshow('video', image)
        print(f'FPS : {1/(time.time() - start)})')

        if cv2.waitKey(1)& 0xFF == ord('q'):
            break

    # for i in os.listdir(dir):
    #     img = cv2.imread(dir+i)
    #     yolo_trt.fallPredict(img)
    #     # save ori img if det
    #     cv2.imwrite(i, img)


if __name__ == "__main__":
    main()
