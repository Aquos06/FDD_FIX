# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
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

import os
import yaml
import glob
import cv2
import numpy as np
import math
import paddle
import sys
import copy
import threading
import queue
import time
from pp_deploy.pipeline.datacollector import Result

parent_path = os.path.abspath(os.path.join(__file__, *(['..'] * 2)))
sys.path.insert(0, parent_path)
from pp_deploy.pipe_utils import crop_image_with_det
from pp_deploy.python.preprocess import decode_image
from pp_deploy.python.infer import Detector

from pp_deploy.pipeline.attr_infer import AttrDetector


class PipePredictor(object):

    def __init__(self):
        # general module for pphuman
        self.with_human_attr = True

        self.det_predictor = Detector(model_dir='pp_deploy/output_inference_human/mot_ppyoloe_s_36e_pipeline/', device='GPU', run_mode='paddle')

        self.attr_predictor = AttrDetector.init_with_cfg()

        self.timing_fall = dict()
        self.frame_id = 0
        self.attr_res = dict()
        self.fps = 10

        self.pipeline_res = Result()

    def visualize_image(self, result):
        fall_coor = list()
        det_res = result.get('det')
        human_attr_res = result.get('attr')
        human_attr_list = list()

        for i in range(len(det_res['boxes'])):
            human_attr = tuple(list(det_res['boxes'][i][2:].astype(float))+[det_res['boxes'][i][1].astype(float)]+[det_res['boxes'][i][0].astype(int)])
            human_attr_list.append(tuple(human_attr))

            # if ((human_attr_res['output'])[i][0] == True) and ((human_attr[2]-human_attr[0])*1.5 > (human_attr[3]-human_attr[1])):
            if (human_attr_res['output'])[i][0] == True:
                fall_coor.append(human_attr)

        return human_attr_list, fall_coor

    def predict_image_2(self, input):
        # det
        # det -> attr
        batch_loop_cnt = math.ceil(
            float(len(input)) / self.det_predictor.batch_size)
        fall_coor = list()

        for i in range(batch_loop_cnt):
            start_index = i * self.det_predictor.batch_size
            end_index = min((i + 1) * self.det_predictor.batch_size, len(input))
            batch_file = input[start_index:end_index]
            batch_input = [decode_image(f, {})[0] for f in batch_file]


            # det output format: class, score, xmin, ymin, xmax, ymax
            det_res = self.det_predictor.predict_image(batch_input, visual=False)

            det_res = self.det_predictor.filter_box(det_res,0.5)
            self.pipeline_res.update(det_res, 'det')

            if self.with_human_attr:
                crop_inputs = crop_image_with_det(batch_input, det_res)
                attr_res_list = []

                for crop_input in crop_inputs:
                    self.attr_res = self.attr_predictor.predict_image(
                        crop_input, visual=False)
                    attr_res_list.extend(self.attr_res['output'])

                self.attr_res = {'output': attr_res_list}
                self.pipeline_res.update(self.attr_res, 'attr')

            human_attr_list, fall_coor = self.visualize_image(self.pipeline_res)

        return human_attr_list, fall_coor