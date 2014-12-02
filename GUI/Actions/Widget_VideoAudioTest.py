'''
Created on 15-12-2013

@author: bastian
'''
from PyQt4 import QtCore, QtGui
from GUI.Actions.Widget_Generic import WidgetGeneric

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

from Containers import Utils
from Containers.Container import Container 
from Containers.SourceContainer import SourceContainer
from Containers.CapsContainer import CapsContainer
from Containers.MixerPreviewContainer import MixerPreviewContainer


from GUI.Actions.Widget_Volume import WidgetVolume
from GUI.Actions.Widget_VideoPreview import WidgetVideoPreview

class WidgetVideoAudioTest(WidgetGeneric):
    '''
    classdocs
    '''


    def __init__(self,main_window,mdiarea,mixer):
        '''
        Constructor
        '''
        super().__init__(main_window,mixer,True,True)
        
        
        self.have_uri = False
        self.is_muted = False
        self.mdiarea = mdiarea
        self.set_name("Audio-Video Test")
        self.create_subwindow_video()
        self.mixer.stop_pipeline()
        self.__create_stream()
        self.mixer.play_pipeline()
        self.__add_combobox_pattern()
        self.__add_slider_frequency()
        
        self.frequency = self._the_widget.SliderFrequency.value()
        self.video_pattern = int(self._the_widget.ComboBoxPattern.currentIndex())
        
        #video elements
        self.connect(self._the_widget.ComboBoxPattern,QtCore.SIGNAL('currentIndexChanged(int)'),self.__change_pattern)
        
        #audio elements
        self.connect(self._the_widget.SliderFrequency,QtCore.SIGNAL('valueChanged(int)'),self.__change_frequency)
    
    
    def __add_combobox_pattern(self):
        self._the_widget.LabelPattern = QtGui.QLabel()
        self._the_widget.LabelPattern.setText("Pattern")
        
        self._the_widget.ComboBoxPattern = QtGui.QComboBox()
        self._the_widget.ComboBoxPattern.setObjectName("ComboBoxPattern")
        
        for i in range(0,23):
            self._the_widget.ComboBoxPattern.addItem("")
        
        self._the_widget.LayoutVideoSettings.addWidget(self._the_widget.LabelPattern,8,0)
        self._the_widget.LayoutVideoSettings.addWidget(self._the_widget.ComboBoxPattern,8,1,)
        
        self._the_widget.ComboBoxPattern.setItemText(0,"(0): Color bars")
        self._the_widget.ComboBoxPattern.setItemText(1, "(1): Random (television snow)")
        self._the_widget.ComboBoxPattern.setItemText(2, "(2): black")
        self._the_widget.ComboBoxPattern.setItemText(3, "(3): white")
        self._the_widget.ComboBoxPattern.setItemText(4, "(4): red")
        self._the_widget.ComboBoxPattern.setItemText(5, "(5): green")
        self._the_widget.ComboBoxPattern.setItemText(6, "(6): blue")
        self._the_widget.ComboBoxPattern.setItemText(7, "(7): Checkers 1px")
        self._the_widget.ComboBoxPattern.setItemText(8, "(8): Checkers 2px")
        self._the_widget.ComboBoxPattern.setItemText(9, "(9): Checkers 4px")
        self._the_widget.ComboBoxPattern.setItemText(10, "(10): Checkers 8px")
        self._the_widget.ComboBoxPattern.setItemText(11, "(11): circular")
        self._the_widget.ComboBoxPattern.setItemText(12, "(12): blink")
        self._the_widget.ComboBoxPattern.setItemText(13, "(13): SMPTE 75% color bars")
        self._the_widget.ComboBoxPattern.setItemText(14, "(14): Zone plate")
        self._the_widget.ComboBoxPattern.setItemText(15, "(15): Gamut checkers")
        self._the_widget.ComboBoxPattern.setItemText(16, "(16): Chroma zone plate")
        self._the_widget.ComboBoxPattern.setItemText(17, "(17): Solid color")
        self._the_widget.ComboBoxPattern.setItemText(18, "(18): Moving ball")
        self._the_widget.ComboBoxPattern.setItemText(19, "(19): SMPTE 100% color bars")
        self._the_widget.ComboBoxPattern.setItemText(20, "(20): Bar")
        self._the_widget.ComboBoxPattern.setItemText(21, "(21): Pinwheel")
        self._the_widget.ComboBoxPattern.setItemText(22, "(22): Spokes")
     
    
    def __add_slider_frequency(self):
        
        
        self._the_widget.LabelFrequency = QtGui.QLabel()
        self._the_widget.LabelFrequency.setObjectName("LabelFrequency")
        self._the_widget.LabelFrequency.setText("Frecuencia")
        self._the_widget.LayoutAudioSettings.addWidget(self._the_widget.LabelFrequency, 3, 0, 1, 1)
        
        self._the_widget.LabelValorFrequency = QtGui.QLabel()
        self._the_widget.LabelValorFrequency.setObjectName("LabelValorFrequency")
        self._the_widget.LabelValorFrequency.setText("440")
        self._the_widget.LayoutAudioSettings.addWidget(self._the_widget.LabelValorFrequency, 3, 4, 1, 1)
        
        self._the_widget.SliderFrequency = QtGui.QSlider()
        self._the_widget.SliderFrequency.setEnabled(True)
        self._the_widget.SliderFrequency.setMaximum(20000)
        self._the_widget.SliderFrequency.setSingleStep(10)
        self._the_widget.SliderFrequency.setProperty("value", 440)
        self._the_widget.SliderFrequency.setOrientation(QtCore.Qt.Horizontal)
        self._the_widget.SliderFrequency.setObjectName("SliderFrequency")
        self._the_widget.LayoutAudioSettings.addWidget(self._the_widget.SliderFrequency, 3, 2, 1, 2)
    
    #video --------------------------------------------------------        
        
    def __change_pattern(self):
        self.video_pattern = int(self._the_widget.ComboBoxPattern.currentIndex())
        print("pattern: "+str(self.video_pattern))
        self.source.set_property("videosrc", "pattern", self.video_pattern)
            
    def __change_frequency(self):
        self.frequency = self._the_widget.SliderFrequency.value()
        self.source.set_property("audiosrc", "freq", float(self.frequency))
        
    #--------------------------------------------------------  
    
    def __create_stream(self):
        
        #CREATE CONTAINERS -------------------------------------------------------------------------
        

        self.source = SourceContainer(self.have_audio,self.have_video,self.have_uri)
        self.source_caps = CapsContainer(self.source.have_audio,self.source.have_video)
        
        self.preview_caps = CapsContainer(False,self.source.have_video)
        self.preview_widget = MixerPreviewContainer(False,self.have_video,self.mixer.bus,self._the_widget.WidgetPreview.winId())
        self.preview_subwindow = MixerPreviewContainer(False,self.have_video,self.mixer.bus,self.subwindow_video.get_winId())

        
        #ADD ELEMENTS ------------------------------------------------------------------------------
        
        self.source.add_element("audiotestsrc", "audiosrc")
        self.source.add_element("videotestsrc", "videosrc")
                
        self.mixer.add_container_to_pipeline(self.source)
        self.mixer.add_container_to_pipeline(self.source_caps)
        
        self.mixer.add_container_to_pipeline(self.preview_caps)
        self.mixer.add_container_to_pipeline(self.preview_widget)
        self.mixer.add_container_to_pipeline(self.preview_subwindow)
        
        #CREATE GHOST PADS -------------------------------------------------------------------------
        self.source.create_ghost_src_pad()

        self.source_caps.create_ghost_sink_pads()
        self.source_caps.create_ghost_src_pads()
        
        self.source.create_ghost_src_pad(None,"video_preview1")
        self.source.create_ghost_src_pad(None,"video_preview2")
        
        self.preview_caps.create_ghost_sink_pads()
        self.preview_caps.create_ghost_src_pads()
        self.preview_widget.create_ghost_sink_pads()
        self.preview_subwindow.create_ghost_sink_pads()
        
        
        #LINK CONTAINERS ELEMENTS-------------------------------------------------------------------
        self.source.link_elements("audiosrc", "audiotee")
        self.source.link_elements("videosrc", "videotee")

        self.source_caps.link_caps_elements()
        self.preview_caps.link_caps_elements()
        
        #LINK CONTAINERS ---------------------------------------------------------------------------
        
        #video
        string_width = "width="+str(self.video_width)
        string_height = "height="+str(self.video_height)
        string_framerate = "framerate="+str(self.video_framerate)+"/1"
        
        self.videocaps_string = "video/x-raw,"+string_width+","+string_height+","+string_framerate
        self.audiocaps_string = "audio/x-raw, format=(string)F32LE, layout=(string)interleaved, rate=(int)44000, channels=(int)2"
            
        #Link containers
        self.source.link_containers("video_src", self.source_caps, "video_sink")
        self.source.link_containers("audio_src", self.source_caps, "audio_sink")
        
        self.source.link_containers("video_preview1", self.preview_caps, "video_sink")     
        self.preview_caps.link_containers("video_src", self.preview_widget, "video_sink")
           
        self.source.link_containers("video_preview2", self.preview_subwindow, "video_sink")
        
        
        #SET ELEMENTS PROPERTIES -------------------------------------------------------------------
        
        self.preview_caps.set_properties()
        self.preview_caps.set_caps("videocaps", self.videocaps_string)
        
        self.source_caps.set_caps("videocaps", self.videocaps_string)
        self.source_caps.set_caps("audiocaps", self.audiocaps_string)
        self.source_caps.set_properties()
        
        self.source_caps.set_property("volume", "volume", 1)
        
        self.source_caps.block_pads(self.link_to_audiomixer,self.link_to_videomixer)
        
        self.source.set_state_playing()
        self.source_caps.set_state_playing()
        self.preview_widget.set_state_playing()
        self.preview_caps.set_state_playing()
        self.preview_subwindow.set_state_playing()
             
    
    def get_caps_container(self):
        return self.source_caps
    
    def create_widget_volume(self):
        self.widget_volume = WidgetVolume(self.get_caps_container())
        self.widget_volume.set_name(self.name)
        
        
    def create_subwindow_video(self):
        self.subwindow_video = WidgetVideoPreview(self,self.mdiarea)
        self.subwindow_video.set_name(self.name)
        
    def set_source_settings(self,source_class):
        data = {"pattern" : self.video_pattern, "frequency" : self.frequency}
        
        source_class.set_source_properties("VideoAudioTest",data,None)
    