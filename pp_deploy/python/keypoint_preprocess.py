# Copyright (c) 2021 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
this code is based on https://github.com/open-mmlab/mmpose/mmpose/core/post_processing/post_transforms.py
"""
import cv2
import numpy as np

def expand_crop(images, rect, expand_ratio=0.3):
    imgh, imgw, c = images.shape
    label, conf, xmin, ymin, xmax, ymax = [int(x) for x in rect.tolist()]
    if label != 0:
        return None, None, None
    org_rect = [xmin, ymin, xmax, ymax]
    h_half = (ymax - ymin) * (1 + expand_ratio) / 2.
    w_half = (xmax - xmin) * (1 + expand_ratio) / 2.
    if h_half > w_half * 4 / 3:
        w_half = h_half * 0.75
    center = [(ymin + ymax) / 2., (xmin + xmax) / 2.]
    ymin = max(0, int(center[0] - h_half))
    ymax = min(imgh - 1, int(center[0] + h_half))
    xmin = max(0, int(center[1] - w_half))
    xmax = min(imgw - 1, int(center[1] + w_half))
    return images[ymin:ymax, xmin:xmax, :], [xmin, ymin, xmax, ymax], org_rect
