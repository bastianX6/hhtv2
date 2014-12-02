'''
Created on 18-02-2014

@author: bastian
'''
from PyQt4 import QtCore, QtGui
from GUI.UI.Ui_Widget_Mixer import Ui_WidgetMixer

import gi,os
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

from Containers.Container import Container
from Containers.CapsContainer import CapsContainer
from Containers.TcpSinkContainer import TcpSinkContainer
from Containers.SourceContainer import SourceContainer
from Containers.MixerPreviewContainer import MixerPreviewContainer
from Config.ConfigFile import SourceClass
from Config.GlobalVars import Defaults

from GUI.Actions.Widget_Volume import WidgetVolume

class WidgetMixer(QtGui.QFrame):
    '''
    classdocs
    '''


    def __init__(self,main_window,mixer,mdiarea,dockwidget_preview):
        '''
        Constructor
        '''
        
        QtGui.QFrame.__init__(self)
        self.__the_widget = Ui_WidgetMixer()
        self.__the_widget.setupUi(self)
        
        self.main_window = main_window
        self.mixer = mixer
        self.mixer_have_audio = True
        self.mixer_have_video = True
        self.host_mixer = "0.0.0.0"
        self.port_mixer = 60000
        self.widget_streaming = None
        self.is_muted = False
        self.is_playing = False
        self.name = "Mixer"
        
        
        #self.__init_preview()
        
        self.mixer_count = 0
        self.widget_volume = None
        self.widget_text = None
        self.mdiarea = mdiarea
        self.dockwidget_preview = dockwidget_preview
        
        self.__init_mixer()
        
        self.connect(self.__the_widget.ButtonPlay, QtCore.SIGNAL('clicked()'), self.play_mixer)
        self.connect(self.__the_widget.ButtonPause, QtCore.SIGNAL('clicked()'), self.pause_mixer)
        self.connect(self.__the_widget.ButtonStop, QtCore.SIGNAL('clicked()'), self.stop_mixer)
        self.connect(self.__the_widget.ButtonDot, QtCore.SIGNAL('clicked()'), self.dot)
        
        
        self.connect(self.__the_widget.CheckBoxText ,QtCore.SIGNAL('stateChanged(int)'),self.__set_textoverlay)
        self.connect(self.__the_widget.SliderXposText ,QtCore.SIGNAL('valueChanged(int)'),self.__apply_text_settings)
        self.connect(self.__the_widget.SliderYposText ,QtCore.SIGNAL('valueChanged(int)'),self.__apply_text_settings)
        self.connect(self.__the_widget.SpinBoxTextSize ,QtCore.SIGNAL('valueChanged(int)'),self.__apply_text_settings)
        self.connect(self.__the_widget.ComboBoxStyle ,QtCore.SIGNAL('currentIndexChanged(int)'),self.__apply_text_settings)
        self.connect(self.__the_widget.FontComboBox ,QtCore.SIGNAL('currentIndexChanged(int)'),self.__apply_text_settings)
        self.connect(self.__the_widget.LineEditText ,QtCore.SIGNAL('textChanged(QString)'),self.__apply_text_settings)
        
        self.connect(self.__the_widget.SliderAlpha ,QtCore.SIGNAL('valueChanged(int)'),self.__change_alpha)
        
        self.connect(self.__the_widget.ComboBoxVideoSize ,QtCore.SIGNAL('currentIndexChanged(int)'),self.__change_videomixer_size)
        self.connect(self.__the_widget.SpinBoxFramerate ,QtCore.SIGNAL('valueChanged(int)'),self.__change_videomixer_size)
        
        
    #textoverlay --------------------------------------------------   
        
    def __set_textoverlay(self):
        
        if self.__the_widget.CheckBoxText.isChecked():
            self.__set_groupbox_text_enabled(True)
            
            self.__apply_text_settings()
            
        elif not self.__the_widget.CheckBoxText.isChecked():
            self.__set_groupbox_text_enabled(False)   
            self.mixer_caps.set_property("textoverlay", "text", "")
            self.tcp_caps.set_property("textoverlay", "text", "")
            
            
    def __apply_text_settings(self):
        
        
        self.mixer_caps.set_property("textoverlay", "text", self.__the_widget.LineEditText.text())
        self.mixer_caps.set_property("textoverlay", "font-desc", self.__get_font_description()) 
        
        self.tcp_caps.set_property("textoverlay", "text", self.__the_widget.LineEditText.text())
        self.tcp_caps.set_property("textoverlay", "font-desc", self.__get_font_description()) 
        
        xpos = self.__the_widget.SliderXposText.value()
        self.mixer_caps.set_property("textoverlay", "xpos", float(xpos/100))
        self.tcp_caps.set_property("textoverlay", "xpos", float(xpos/100))
        self.__the_widget.LabelXposValueText.setText(str(xpos))
        
        ypos = self.__the_widget.SliderYposText.value()
        self.mixer_caps.set_property("textoverlay", "ypos", float(ypos/100))
        self.tcp_caps.set_property("textoverlay", "ypos", float(ypos/100))
        self.__the_widget.LabelYposValueText.setText(str(ypos)) 
                
                
    def __set_groupbox_text_enabled(self,enabled):
        
        self.__the_widget.LineEditText.setEnabled(enabled)
        self.__the_widget.SliderXposText.setEnabled(enabled)
        self.__the_widget.SliderYposText.setEnabled(enabled)
        self.__the_widget.FontComboBox.setEnabled(enabled)
        self.__the_widget.SpinBoxTextSize.setEnabled(enabled)
        self.__the_widget.ComboBoxStyle.setEnabled(enabled)
        
    def __get_font_description(self):
        
        string_font = self.__the_widget.FontComboBox.currentText()
        string_size = str(self.__the_widget.SpinBoxTextSize.value())
        
        index = self.__the_widget.ComboBoxStyle.currentIndex()
        string_style = ""
        if index == 0:
            string_style = "Normal"
            
        elif index == 1:
            string_style = "Bold"
            
        elif index == 2:
            string_style = "Italic"
            
        elif index == 3:
            string_style = "Bold Italic"
            
        return string_font + " " + string_style + " " + string_size
    
    
    def __change_alpha(self):
        self.alpha = self.__the_widget.SliderAlpha.value()
        alpha_float = float(self.alpha/100)
        self.background_caps
        self.mixer.set_videomixer_pad_property(self.background_caps, "alpha", alpha_float)
        self.__the_widget.LabelAlphaValue.setText(str(self.alpha))
        
        
    def __change_videomixer_size(self):
        index = self.__the_widget.ComboBoxVideoSize.currentIndex()
        framerate = self.__the_widget.SpinBoxFramerate.value()
        
        #640x480
        if index == 0:
            self.__set_video_caps(640, 480, framerate)
        
        #800x600
        elif index == 1:
            self.__set_video_caps(800, 600, framerate)
        
        #1024x768
        elif index == 2:
            self.__set_video_caps(1024, 768, framerate)
        
        #1024x576
        elif index == 3:
            self.__set_video_caps(1024, 576, framerate)
        
        #1280x720
        elif index == 4:
            self.__set_video_caps(1280, 720, framerate)
        
  
  
    def __set_video_caps(self,width,height,framerate):
        
        self.mixer.stop_pipeline()
        videomixer_caps_string = "video/x-raw,width="+str(width)+",height="+str(height)+",framerate="+str(framerate)+"/1"
        
        if self.background:
            image_path = ""
            if width == 640 and height == 480: 
                image_path = os.getcwd()+"/GUI/Resources/640x480.jpg"
                
            elif width == 800 and height == 600: 
                image_path = os.getcwd()+"/GUI/Resources/800x600.jpg"
                
            elif width == 1024 and height == 768: 
                image_path = os.getcwd()+"/GUI/Resources/1024x768.jpg"
                
            elif width == 1024 and height == 576: 
                image_path = os.getcwd()+"/GUI/Resources/1024x576.jpg"
                
            elif width == 1280 and height == 720: 
                image_path = os.getcwd()+"/GUI/Resources/1280x720.jpg"
            
            the_uri = "file://" + image_path
            self.background.set_property("uridecodebin", "uri", the_uri)
        
        if self.background_caps:
            self.background_caps.set_caps("videocaps", videomixer_caps_string)
            
        if self.mixer_caps:
            self.mixer_caps.set_caps("videocaps", videomixer_caps_string) 
            
        
        self.mixer.play_pipeline()
        if self.mdiarea:
            self.mdiarea.setMinimumSize(width, height)
            self.mdiarea.setMaximumSize(width, height) 
            self.mdiarea.repaint()
            
    #------------------------------------------------------------------       
            
    def __init_mixer(self):
        
        videomixer_caps_string = "video/x-raw,width=1280,height=720,framerate=15/1,format="+Defaults.video_format
        audiomixer_caps_string = "audio/x-raw, format=(string)F32LE, layout=(string)interleaved, rate=(int)44000, channels=(int)2"
        #CREATE CONTAINERS -------------------------------------------------------------------------
        
        background_have_audio = True
        background_have_video = True
        
        image_path = os.getcwd()+"/GUI/Resources/640x480.jpg"
        the_uri = "file://" + image_path
        
        self.background= SourceContainer(background_have_audio,background_have_video)
        
        self.background_caps = CapsContainer(background_have_audio,background_have_video,True)
        self.background_caps.name = Defaults.backgroud_caps_name
        
        self.mixer_caps = CapsContainer(self.mixer_have_audio,self.mixer_have_video)
        
        
        self.mixer_preview_sink = MixerPreviewContainer(True,True,self.mixer.bus,self.dockwidget_preview.get_winId())
        self.mixer_preview_sink2 = MixerPreviewContainer(False,True,self.mixer.bus,self.__the_widget.WidgetPreview.winId())
        
        self.tcp_caps = CapsContainer(self.mixer_have_audio,self.mixer_have_video)
        self.tcp_sink = TcpSinkContainer(self.mixer_have_audio,self.mixer_have_video,self.host_mixer,self.port_mixer)
        
        #ADD ELEMENTS ------------------------------------------------------------------------------
        
        self.background.add_element("audiotestsrc", "audiosrc")
        
        self.mixer.add_container_to_pipeline(self.background)
        self.mixer.add_container_to_pipeline(self.background_caps)
        self.mixer.add_container_to_pipeline(self.mixer_caps)
        
        self.mixer.add_container_to_pipeline(self.mixer)
        self.mixer.add_container_to_pipeline(self.mixer_preview_sink)
        self.mixer.add_container_to_pipeline(self.mixer_preview_sink2)
        
        self.mixer.add_container_to_pipeline(self.tcp_sink)
        self.mixer.add_container_to_pipeline(self.tcp_caps)
        
        #CREATE GHOST PADS -------------------------------------------------------------------------
        
        #self.background.create_ghost_pad("videosrc", "src", False, "video_src")
        #self.background.create_ghost_pad("audiosrc", "src", False, "audio_src")
        
        self.background.create_ghost_src_pad()
        self.background_caps.create_ghost_sink_pads()
        self.background_caps.create_ghost_src_pads()
        self.mixer.create_ghost_src_pads("audio_preview1","video_preview1")
        self.mixer.create_ghost_src_pads("audio_preview2","video_preview2")
        self.mixer.create_ghost_src_pads("audio_tcp_src","video_tcp_src")
        self.mixer_caps.create_ghost_sink_pads()
        self.mixer_caps.create_ghost_src_pads()
        self.mixer_preview_sink.create_ghost_sink_pads()
        self.mixer_preview_sink2.create_ghost_sink_pads()
        
        self.tcp_caps.create_ghost_sink_pads()
        self.tcp_caps.create_ghost_src_pads()
        
        self.tcp_sink.create_ghost_sink_pads()
        
        
        #LINK CONTAINERS ELEMENTS-------------------------------------------------------------------
        
        self.background.link_elements("audiosrc", "audiotee")
        self.background_caps.link_caps_elements()
        self.mixer_caps.link_caps_elements()
        self.tcp_caps.link_caps_elements()
        self.tcp_sink.link_tcp_elements()
        
        #LINK CONTAINERS ---------------------------------------------------------------------------
        
        #self.background --> self.background_caps
        self.background.link_containers("video_src", self.background_caps, "video_sink")
        self.background.link_containers("audio_src", self.background_caps, "audio_sink")
        
        #self.background_caps --> mixer
        self.mixer.link_to_mixer(self.background_caps,self.background_caps.have_audio,self.background_caps.have_video)
        
        #mixer --> mixer_caps
        self.mixer.link_containers("video_preview1", self.mixer_caps, "video_sink")
        self.mixer.link_containers("audio_preview1", self.mixer_caps, "audio_sink")
        
        self.mixer.link_containers("video_preview2", self.mixer_preview_sink2, "video_sink")
        
        self.mixer.link_containers("video_tcp_src", self.tcp_caps, "video_sink")
        self.mixer.link_containers("audio_tcp_src", self.tcp_caps, "audio_sink")
        
        #mixer_caps --> mixer_preview_sink
        self.mixer_caps.link_containers("video_src", self.mixer_preview_sink, "video_sink")
        self.mixer_caps.link_containers("audio_src", self.mixer_preview_sink, "audio_sink")
        
        self.tcp_caps.link_containers("video_src", self.tcp_sink, "video_sink")
        self.tcp_caps.link_containers("audio_src", self.tcp_sink, "audio_sink")
        
        
        #SET ELEMENTS PROPERTIES -------------------------------------------------------------------
        
        self.background.set_property("uridecodebin", "uri", the_uri)
        self.mixer_caps.set_properties()
        self.background_caps.set_properties()
        self.tcp_sink.set_tcp_properties()
    
        #mixer
        self.mixer.set_videomixer_pad_property(self.background_caps, "alpha", 0.0)
        
        self.mixer_preview_sink.set_sync(False, False)
        self.mixer_preview_sink2.set_sync(False, True)
        
        #self.background_caps
        self.background_caps.set_caps("videocaps", videomixer_caps_string)
        self.background_caps.set_caps("audiocaps", audiomixer_caps_string)
        
        self.background_caps.set_property("volume", "volume", 0)
        self.mixer_caps.set_caps("videocaps", videomixer_caps_string)
        
        self.tcp_caps.set_caps("videocaps", videomixer_caps_string)
        self.tcp_caps.set_caps("audiocaps", audiomixer_caps_string)
        
    def play_mixer(self):
        self.mixer.play_pipeline()
        if self.widget_streaming:
            self.widget_streaming.setEnabled(True)
                    
    def stop_mixer(self):
        self.mixer.stop_pipeline()
        if self.widget_streaming:
            self.widget_streaming.setEnabled(False)

    def pause_mixer(self):
        self.mixer.pipeline_ready()
        
    def dot(self):
        Gst.debug_bin_to_dot_file (self.mixer.pipeline,Gst.DebugGraphDetails.ALL, 
                                   "Mixer-"+str(self.mixer_count))
        
        self.mixer_count = self.mixer_count + 1
        
    def reconfigure_videosink(self):
        self.mixer_preview_sink.send_event()
        self.mixer_preview_sink2.send_event()
        
        
    def get_source_class(self):
        
        have_text = self.__the_widget.CheckBoxText.isChecked()
        source = SourceClass("Mixer",have_video=True,have_audio=True, textoverlay=have_text )
        
        
        xpos = 0
        ypos = 0
        width = 0
        height = 0
        zorder = 0
        
        index = self.__the_widget.ComboBoxVideoSize.currentIndex()
        
        #640x480
        if index == 0:
            width,height = 640,480
        
        #800x600
        elif index == 1:
            width,height = 800,600
        
        #1024x768
        elif index == 2:
            width,height = 1024,768
        
        #1024x576
        elif index == 3:
            width,height = 1024,576
        
        #1280x720
        elif index == 4:
            width,height = 1280,720
        
        
        
        
        alpha_float = float(self.__the_widget.SliderAlpha.value()/100)
        self.video_framerate = self.__the_widget.SpinBoxFramerate.value()
        source.set_video_properties(width,height, xpos, ypos, zorder, alpha_float)
        source.set_audio_properties(self.widget_volume.get_volume())
            
            
        if have_text:
            text = self.__the_widget.LineEditText.text()
            xpos = self.__the_widget.SliderXposText.value()
            ypos = self.__the_widget.SliderYposText.value()
            font_settings = self.__get_font_description()
            source.set_textoverlay_properties(text, xpos, ypos, font_settings)
            
        return source
        
        
    def get_caps_container(self):
        return self.mixer_caps
        
    def get_preview(self):
        return self.preview
        
        
    def create_widget_volume(self):
        self.widget_volume = WidgetVolume(self.get_caps_container())
        self.widget_volume.set_name(self.name)
        
    def __message(self, bus, msg):
        print('-------------------------------------------')
        if msg.type == Gst.MessageType.STATE_CHANGED:
            states = msg.parse_state_changed()
            print('Old State',self.parse_state(states[0])," | New state: ",self.parse_state(states[1])," | State pending: ",self.parse_state(states[2]))
            
        if msg.type == Gst.MessageType.STREAM_STATUS:
            stream_status = msg.parse_stream_status()
            print('Stream Status:',stream_status[0])
            print('Element:',stream_status[1])
            
        if msg.type == Gst.MessageType.WARNING:
            warning = msg.parse_warning()
            print('Error:',warning[0])
            print('Details:',warning[1])
            
        if msg.type == Gst.MessageType.TAG:
            print('Tag:',msg.parse_tag().to_string())
            
        else:
            print("Message: ",msg.type)
    
    
        