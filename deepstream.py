import pyds
import numpy as np
from PyQt5.QtGui import QImage , QPixmap
from PyQt5.QtWidgets import QMainWindow
from gi.repository import GObject
import sys
sys.settrace
sys.path.append('../')
import gi
import configparser

gi.require_version('Gst', '1.0')
from gi.repository import GLib, Gst
from ctypes import *
import time
import sys
import math
import platform
from common.is_aarch_64 import is_aarch64
from common.bus_call import bus_call
from common.FPS import PERF_DATA
import numpy as np
import pyds
import cv2
import os
#from dsl import *
import os.path
from os import path
from PyQt5.QtCore import QObject
from PyQt5 import QtCore, QtGui

perf_data = None
frame_count = {}
saved_count = {}


MAX_DISPLAY_LEN = 64

global PGIE_CLASS_ID_VEHICLE
PGIE_CLASS_ID_VEHICLE=0

global PGIE_CLASS_ID_PERSON
PGIE_CLASS_ID_PERSON=2
MAX_DISPLAY_LEN=64
PGIE_CLASS_ID_VEHICLE = 0
PGIE_CLASS_ID_BICYCLE = 1
PGIE_CLASS_ID_PERSON = 2
PGIE_CLASS_ID_ROADSIGN = 3
MUXER_OUTPUT_WIDTH=1920
MUXER_OUTPUT_HEIGHT=1080
MUXER_BATCH_TIMEOUT_USEC=4000000
TILED_OUTPUT_WIDTH=1920
TILED_OUTPUT_HEIGHT=1080
GST_CAPS_FEATURES_NVMM="memory:NVMM"
#
pgie_classes_str= ["Vehicle", "TwoWheeler", "Person","RoadSign"]
#pgie_classes_str= ["Person"]

MIN_CONFIDENCE = 0.3
MAX_CONFIDENCE = 1

class Deep(QObject):

    image = QtCore.pyqtSignal(np.ndarray)
    reconnect = QtCore.pyqtSignal(bool)

    def display_frame_2(self, flag, buff, b_id, obj_meta):
        rgbImage=pyds.get_nvds_buf_surface(hash(buff),b_id)
        #convert python array into numy array format.
        self.frame_image=np.ascontiguousarray(rgbImage,dtype = np.uint8)	
        self.image.emit(self.frame_image)

	
    def tiler_sink_pad_buffer_probe(self,pad,info,u_data):
        #num_rects = 0
        gst_buffer = info.get_buffer()

        if not gst_buffer:
            print("Unable to get GstBuffer")
            return

        batch_meta = pyds.gst_buffer_get_nvds_batch_meta(hash(gst_buffer))

        l_frame = batch_meta.frame_meta_list
        while l_frame is not None:
            try:
                frame_meta = pyds.NvDsFrameMeta.cast(l_frame.data)
            except StopIteration:
                break
                print("stopped")
            else:	
                self.display_frame_2(0, gst_buffer, frame_meta.batch_id,0)

            try:
                l_frame=l_frame.next
            except StopIteration:
                break

        return Gst.PadProbeReturn.OK

    def cb_newpad(self,decodebin, decoder_src_pad,data):
        print("In cb_newpad\n")
        caps=decoder_src_pad.get_current_caps()
        gststruct=caps.get_structure(0)
        gstname=gststruct.get_name()
        source_bin=data
        features=caps.get_features(0)

        # Need to check if the pad created by the decodebin is for video and not
        # audio.
        if(gstname.find("video")!=-1):
            # Link the decodebin pad only if decodebin has picked nvidia
            # decoder plugin nvdec_*. We do this by checking if the pad caps contain
            # NVMM memory features.
            if features.contains("memory:NVMM"):
                # Get the source bin ghost pad
                bin_ghost_pad=source_bin.get_static_pad("src")
                if not bin_ghost_pad.set_target(decoder_src_pad):
                    sys.stderr.write("Failed to link decoder src pad to source bin ghost pad\n")
            else:
                sys.stderr.write(" Error: Decodebin did not pick nvidia decoder plugin.\n")

    def decodebin_child_added(self,child_proxy,Object,name,user_data):
        print("Decodebin child added:", name, "\n")
        if(name.find("decodebin") != -1):
            Object.connect("child-added",self.decodebin_child_added,user_data)   
        if(is_aarch64() and name.find("nvv4l2decoder") != -1):
            print("Seting bufapi_version\n")
            Object.set_property("bufapi-version",True)

    def create_source_bin(self,index,uri):
        print("Creating source bin")

        # Create a source GstBin to abstract this bin's content from the rest of the
        # pipeline
        bin_name="source-bin-%02d" %index
        print(bin_name)
        nbin=Gst.Bin.new(bin_name)
        if not nbin:
            sys.stderr.write(" Unable to create source bin \n")

        # Source element for reading from the uri.
        # We will use decodebin and let it figure out the container format of the
        # stream and the codec and plug the appropriate demux and decode plugins.
        uri_decode_bin=Gst.ElementFactory.make("uridecodebin", "uri-decode-bin")
        if not uri_decode_bin:
            sys.stderr.write(" Unable to create uri decode bin \n")
        # We set the input uri to the source element
        uri_decode_bin.set_property("uri",uri)
        # Connect to the "pad-added" signal of the decodebin which generates a
        # callback once a new pad for raw data has beed created by the decodebin
        uri_decode_bin.connect("pad-added",self.cb_newpad,nbin)
        uri_decode_bin.connect("child-added",self.decodebin_child_added,nbin)

        # We need to create a ghost pad for the source bin which will act as a proxy
        # for the video decoder src pad. The ghost pad will not have a target right
        # now. Once the decode bin creates the video decoder and generates the
        # cb_newpad callback, we will set the ghost pad target to the video decoder
        # src pad.
        Gst.Bin.add(nbin,uri_decode_bin)
        bin_pad=nbin.add_pad(Gst.GhostPad.new_no_target("src",Gst.PadDirection.SRC))
        if not bin_pad:
            sys.stderr.write(" Failed to add ghost pad in source bin \n")
            return None
        return nbin

    def draw_bounding_boxes(self,image,obj_meta,confidence):
        rect_params=obj_meta.rect_params
        top=int(rect_params.top)
        left=int(rect_params.left)
        width=int(rect_params.width)
        height=int(rect_params.height)
        image=cv2.rectangle(image,(left,top),(left+width,top+height),(0,0,255,0),2)

        return image

    def img2pyqt(self,img,label):
        '''
        convert the opencv format to pyqt format color
        '''
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        temp = QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1]*3, QImage.Format_RGB888)
        return QPixmap.fromImage(temp).scaled(label.width(), label.height())

    def run(self):

        # Check input arguments

        args = ['deepstream_imagedata-multistream.py','rtsp://admin:ai123456@192.168.0.51/cam/realmonitor?channel=1&subtype=1', 'frames22']

        number_sources=len(args)-2

        # Standard GStreamer initialization
        Gst.init(None)

        # Create gstreamer elements */
        # Create Pipeline element that will form a connection of other elements
        print("Creating Pipeline \n ")
        self.pipeline = Gst.Pipeline()
        is_live = False

        if not self.pipeline:
            sys.stderr.write(" Unable to create Pipeline \n")
        print("Creating streamux \n ")

        # Create nvstreammux instance to form batches from one or more sources.
        streammux = Gst.ElementFactory.make("nvstreammux", "Stream-muxer")
        if not streammux:
            sys.stderr.write(" Unable to create NvStreamMux \n")

        self.pipeline.add(streammux)
        for i in range(number_sources):
        #    os.mkdir(folder_name+"/stream_"+str(i))
            frame_count["stream_"+str(i)]=0
            saved_count["stream_"+str(i)]=0
            print("Creating source_bin ",i," \n ")
            uri_name=args[i+1]
            if uri_name.find("rtsp://") == 0 :
                is_live = True
            source_bin=self.create_source_bin(i, uri_name)
            if not source_bin:
                sys.stderr.write("Unable to create source bin \n")
            self.pipeline.add(source_bin)
            padname="sink_%u" %i
            sinkpad= streammux.get_request_pad(padname) 
            if not sinkpad:
                sys.stderr.write("Unable to create sink pad bin \n")
            srcpad=source_bin.get_static_pad("src")
            if not srcpad:
                sys.stderr.write("Unable to create src pad bin \n")
            srcpad.link(sinkpad)

        print("Creating Pgie \n ")
        pgie = Gst.ElementFactory.make("nvinfer", "primary-inference")
        if not pgie:
            sys.stderr.write(" Unable to create pgie \n")

        print("Creating nvvidconv1 \n ")
        nvvidconv1 = Gst.ElementFactory.make("nvvideoconvert", "convertor1")
        if not nvvidconv1:
            sys.stderr.write(" Unable to create nvvidconv1 \n")
        print("Creating filter1 \n ")

        caps1 = Gst.Caps.from_string("video/x-raw(memory:NVMM), format=RGBA")
        filter1 = Gst.ElementFactory.make("capsfilter", "filter1")
        if not filter1:
            sys.stderr.write(" Unable to get the caps filter1 \n")
        filter1.set_property("caps", caps1)
        print("Creating tiler \n ")
        tiler=Gst.ElementFactory.make("nvmultistreamtiler", "nvtiler")
        if not tiler:
            sys.stderr.write(" Unable to create tiler \n")
        print("Creating nvvidconv \n ")
        nvvidconv = Gst.ElementFactory.make("nvvideoconvert", "convertor")
        if not nvvidconv:
            sys.stderr.write(" Unable to create nvvidconv \n")
        print("Creating nvosd \n ")
        nvosd = Gst.ElementFactory.make("nvdsosd", "onscreendisplay")
        if not nvosd:
            sys.stderr.write(" Unable to create nvosd \n")


        #sink = Gst.ElementFactory.make("nveglglessink", "nvvideo-renderer")
        #if not sink:
        #    sys.stderr.write(" Unable to create egl sink \n")

        print('creating fake sink')
        sink = Gst.ElementFactory.make("fakesink","fakesink")
        sink.set_property('enable-last-sample',0)
        sink.set_property('sync',0)

        if is_live:
            print("Atleast one of the sources is live")
            streammux.set_property('live-source', 1)

        streammux.set_property('width', self.lchannel.width())
        streammux.set_property('height', self.lchannel.height())
        streammux.set_property('batch-size', number_sources)
        streammux.set_property('batched-push-timeout', 1/30)
        pgie.set_property('config-file-path', "config_deepstream.txt")
        
        pgie_batch_size=pgie.get_property("batch-size")
        if(pgie_batch_size != number_sources):
            print("WARNING: Overriding infer-config batch-size",pgie_batch_size," with number of sources ", number_sources," \n")
            pgie.set_property("batch-size",number_sources)
        tiler_rows=int(math.sqrt(number_sources))
        tiler_columns=int(math.ceil((1.0*number_sources)/tiler_rows))
        tiler.set_property("rows",tiler_rows)
        tiler.set_property("columns",tiler_columns)
        tiler.set_property("width", self.lchannel.width())
        tiler.set_property("height", self.lchannel.height())

        sink.set_property("qos", 0)

        if not is_aarch64():
            # Use CUDA unified memory in the pipeline so frames
            # can be easily accessed on CPU in Python.
            mem_type = int(pyds.NVBUF_MEM_CUDA_UNIFIED)
            streammux.set_property("nvbuf-memory-type", mem_type)
            nvvidconv.set_property("nvbuf-memory-type", mem_type)
            nvvidconv1.set_property("nvbuf-memory-type", mem_type)
            tiler.set_property("nvbuf-memory-type", mem_type)
            
        print("Adding elements to Pipeline \n")
        self.pipeline.add(pgie)
        # self.pipeline.add(tracker)
        #self.pipeline.add(sgie1)
        self.pipeline.add(tiler)
        self.pipeline.add(nvvidconv)
        self.pipeline.add(filter1)
        self.pipeline.add(nvvidconv1)
        self.pipeline.add(nvosd)
        self.pipeline.add(sink)
        #self.pipeline.add(self.returnConnect())

        print("Linking elements in the Pipeline \n")
        streammux.link(pgie)  
        pgie.link(nvvidconv1)
        nvvidconv1.link(filter1)
        filter1.link(tiler)
        tiler.link(nvvidconv)
        nvvidconv.link(nvosd)
        nvosd.link(sink)

        # create an event loop and feed gstreamer bus mesages to it
        loop = GLib.MainLoop()
        bus = self.pipeline.get_bus()
        bus.add_signal_watch()
        bus.connect ("message", bus_call, loop)
        tiler_sink_pad=tiler.get_static_pad("sink")
        if not tiler_sink_pad:
            sys.stderr.write(" Unable to get src pad \n")
        else:

            tiler_sink_pad.add_probe(Gst.PadProbeType.BUFFER, self.tiler_sink_pad_buffer_probe, 0)
        # List the sources
        print("Now playing...")
        print("Starting pipeline \n")
        # start play back and listed to events		
        self.pipeline.set_state(Gst.State.PLAYING)
        
        try:
            loop.run()
        except:
            pass
        # cleanup
        print("Exiting app\n")
        
        self.pipeline.set_state(Gst.State.NULL)
