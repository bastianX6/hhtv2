'''
Created on 11-02-2014

@author: bastian
'''

from PyQt4 import QtCore, QtGui
from GUI.UI.Ui_DockWidget_Streaming import Ui_DockWidgetStreaming

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

from Containers.Container import Container
from Containers.CapsContainer import CapsContainer
from Containers.TcpSinkContainer import TcpSinkContainer
from Containers.RtmpSinkContainer import RtmpSinkContainer
from Containers.TcpSrcContainer import TcpSrcContainer
from Config.GlobalVars import Defaults

class DockWidgetStreaming(QtGui.QDockWidget):
    '''
    classdocs
    '''


    def __init__(self, host_mixer,port_mixer):
        '''
        Constructor
        '''
        
        QtGui.QWidget.__init__(self)
        self.__the_widget = Ui_DockWidgetStreaming()
        self.__the_widget.setupUi(self)
        
        self.host_mixer = host_mixer
        self.port_mixer = port_mixer
        
        self.dot_count = 0
        
        self.__the_widget.ButtonStop.setEnabled(False)
        
        
        
        self.connect(self.__the_widget.ButtonPlay, QtCore.SIGNAL('clicked()'), self.play_streaming)
        self.connect(self.__the_widget.ButtonStop, QtCore.SIGNAL('clicked()'), self.stop_streaming)
        self.connect(self.__the_widget.ButtonDot, QtCore.SIGNAL('clicked()'), self.dot)
        
        
    def __create_streaming(self):
        
        #create containers
        
        self.tcp_mixer =  TcpSrcContainer(True,True,self.host_mixer,self.port_mixer)
        self.caps_container =  CapsContainer(True,True)
        self.rtmp_stream = RtmpSinkContainer(True,True)
        
        
        #add elements to pipeline
        
        self.rtmp_stream.add_container_to_pipeline(self.tcp_mixer)
        self.rtmp_stream.add_container_to_pipeline(self.caps_container)
        self.rtmp_stream.add_container_to_pipeline(self.rtmp_stream)
        
        
        #set elements properties
        
        self.tcp_mixer.set_properties()
        
        self.caps_container.set_caps("videocaps", "video/x-raw,format="+Defaults.video_format)
        self.caps_container.set_caps("audiocaps", "ANY")
        
        #codec
        
        audio_codec = self.__the_widget.ComboBoxAudioCodec.currentText()
        video_codec = self.__the_widget.ComboBoxVideoCodec.currentText()
        
        self.rtmp_stream.add_container_elements(audio_codec, video_codec)
        
        #bitrate 
        audio_bitrate = int(self.__the_widget.ComboBoxAudioBitrate.currentText())
        video_bitrate = self.__the_widget.SpinBoxVIdeoBitrate.value()
        
        #server location
        
        rtmp_location = ""
        location_suf = "live=1 flashver=FME/3.0%20(compatible;%20FMSc%201.0)"
        server_url = self.__the_widget.LineEditServerURL.text()
        server_key = self.__the_widget.LineEditServerKey.text()
        server_type = self.__the_widget.ComboBoxService.currentText()
        
        if server_type == "YouTube":
            rtmp_location += server_url + "/x/" + server_key + " " + location_suf
        
        #Justin.tv - Ustream.tv - Castalba.tv
        else:
            rtmp_location += server_url + "/" + server_key + " " + location_suf
            
        self.rtmp_stream.set_container_properties(audio_bitrate, video_bitrate, rtmp_location)
        
        #Create ghost pads
        
        self.tcp_mixer.create_ghost_src_pad()
        self.rtmp_stream.create_ghost_sink_pads()
        
        self.caps_container.create_ghost_sink_pads()
        self.caps_container.create_ghost_src_pads()
        
        #link containers
        
        self.tcp_mixer.link_containers("video_src", self.caps_container, "video_sink")
        self.tcp_mixer.link_containers("audio_src", self.caps_container, "audio_sink")
        
        self.caps_container.link_containers("video_src", self.rtmp_stream, "video_sink")
        self.caps_container.link_containers("audio_src", self.rtmp_stream, "audio_sink")
        
        self.tcp_mixer.link_container_elements()
        self.rtmp_stream.link_container_elements()
        self.caps_container.link_caps_elements()
        
        
    def play_streaming(self):
        self.__create_streaming()
        self.rtmp_stream.play_pipeline()
        self.__the_widget.ButtonPlay.setEnabled(False)
        self.__the_widget.ButtonStop.setEnabled(True)
        
        self.__the_widget.ProgressBarStream.setRange(0,0)
        
        
        
    
    def stop_streaming(self):
        self.rtmp_stream.stop_pipeline()
        
        #recreate containers
        self.__the_widget.ProgressBarStream.setRange(0,100)
        self.__the_widget.ProgressBarStream.setValue(0)
        
        self.__the_widget.ButtonStop.setEnabled(False)
        self.__the_widget.ButtonPlay.setEnabled(True)
    
    def dot(self):
        Gst.debug_bin_to_dot_file (self.rtmp_stream.pipeline,Gst.DebugGraphDetails.ALL, "rtmp-"+str(self.dot_count))
        self.dot_count = self.dot_count + 1