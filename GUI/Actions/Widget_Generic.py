'''
Created on 25-12-2013

@author: bastian
'''

from PyQt4 import QtCore, QtGui

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject
from Config.ConfigFile import SourceClass
from GUI.UI.Ui_Widget_Generic import Ui_WidgetGeneric
import uuid

class WidgetGeneric(QtGui.QFrame):
    '''
    classdocs
    '''


    def __init__(self,main_window,mixer,have_audio,have_video):
        '''
        Constructor
        '''
        
        QtGui.QFrame.__init__(self)
        self._the_widget = Ui_WidgetGeneric()
        self._the_widget.setupUi(self)
        self.id = str(uuid.uuid4())
        
        
        self.main_window = main_window
        self.mixer = mixer
        self.have_video = have_video
        self.have_audio = have_audio
        self.dot_count = 0
        self.name = ""
        
        self.widget_volume = None
        self.subwindow_video = None
        
        
        self.video_width = self._the_widget.SliderWidth.value()
        self.video_height = self._the_widget.SliderHeight.value()
        self.video_alpha = self._the_widget.SliderAlpha.value()
        self.video_framerate = self._the_widget.SpinBoxFramerate.value()
        
        self._the_widget.TabWidget.removeTab(3)
        self._the_widget.TabWidget.setCurrentIndex(0)
        self._the_widget.WidgetButtons.hide()
        
        debug_enabled = False
        if not debug_enabled:
            self._the_widget.ButtonDot.hide()
        
        #connect's
        
        #video elements
        self.connect(self._the_widget.SliderWidth,QtCore.SIGNAL('sliderReleased()'),self.__change_width_height_framerate)
        self.connect(self._the_widget.SliderHeight,QtCore.SIGNAL('sliderReleased()'),self.__change_width_height_framerate)
        self.connect(self._the_widget.SpinBoxFramerate,QtCore.SIGNAL('valueChanged(int)'),self.__change_width_height_framerate)
        self.connect(self._the_widget.SliderAlpha ,QtCore.SIGNAL('valueChanged(int)'),self.__change_alpha)
        
        #videomixer elements
        self.connect(self._the_widget.SliderXpos ,QtCore.SIGNAL('valueChanged(int)'),self.__change_xpos_ypos)
        self.connect(self._the_widget.SliderYpos ,QtCore.SIGNAL('valueChanged(int)'),self.__change_xpos_ypos)
        self.connect(self._the_widget.SpinBoxZpos ,QtCore.SIGNAL('valueChanged(int)'),self.__change_zpos)
        
        self.connect(self._the_widget.CheckBoxText ,QtCore.SIGNAL('stateChanged(int)'),self.__set_textoverlay)
        self.connect(self._the_widget.SliderXposText ,QtCore.SIGNAL('valueChanged(int)'),self.__apply_text_settings)
        self.connect(self._the_widget.SliderYposText ,QtCore.SIGNAL('valueChanged(int)'),self.__apply_text_settings)
        self.connect(self._the_widget.SpinBoxTextSize ,QtCore.SIGNAL('valueChanged(int)'),self.__apply_text_settings)
        self.connect(self._the_widget.ComboBoxStyle ,QtCore.SIGNAL('currentIndexChanged(int)'),self.__apply_text_settings)
        self.connect(self._the_widget.FontComboBox ,QtCore.SIGNAL('currentIndexChanged(int)'),self.__apply_text_settings)
        self.connect(self._the_widget.LineEditText ,QtCore.SIGNAL('textChanged(QString)'),self.__apply_text_settings)
        
        
        self.connect(self._the_widget.ToolButtonEditName ,QtCore.SIGNAL('clicked()'),self.__change_name)
        self.connect(self._the_widget.ButtonDelete ,QtCore.SIGNAL('clicked()'),self.remove_from_mixer)
    
    
    def __set_textoverlay(self):
        
        if self._the_widget.CheckBoxText.isChecked():
            self.__set_groupbox_text_enabled(True)
            
            self.__apply_text_settings()
            
        elif not self._the_widget.CheckBoxText.isChecked():
            self.__set_groupbox_text_enabled(False)   
            self.source_caps.set_property("textoverlay", "text", "")
            self.preview_caps.set_property("textoverlay", "text", "")
            
            
    def __apply_text_settings(self):
        
        if self.have_video:
            self.source_caps.set_property("textoverlay", "text", self._the_widget.LineEditText.text())
            self.source_caps.set_property("textoverlay", "font-desc", self.__get_font_description())
            
            self.preview_caps.set_property("textoverlay", "text", self._the_widget.LineEditText.text())
            self.preview_caps.set_property("textoverlay", "font-desc", self.__get_font_description()) 
            
            xpos = self._the_widget.SliderXposText.value()
            self.source_caps.set_property("textoverlay", "xpos", float(xpos/100))
            self.preview_caps.set_property("textoverlay", "xpos", float(xpos/100))
            self._the_widget.LabelXposValueText.setText(str(xpos))
            
            ypos = self._the_widget.SliderYposText.value()
            self.source_caps.set_property("textoverlay", "ypos", float(ypos/100))
            self.preview_caps.set_property("textoverlay", "ypos", float(ypos/100))
            self._the_widget.LabelYposValueText.setText(str(ypos))  
            
    def change_text(self,text,xpos,ypos,font_description):
        if self.have_video:
            self.__set_groupbox_text_enabled(True)
            self._the_widget.CheckBoxText.setChecked(True)
            
            
            self._the_widget.LineEditText.setText(text)
            self.source_caps.set_property("textoverlay", "text", self._the_widget.LineEditText.text())
            try:
                self.source_caps.set_property("textoverlay", "font-desc", font_description)
            except:
                self.source_caps.set_property("textoverlay", "font-desc", self.__get_font_description())
            
            self.preview_caps.set_property("textoverlay", "text", self._the_widget.LineEditText.text())
            
            try:
                self.preview_caps.set_property("textoverlay", "font-desc", font_description)
            except:
                self.preview_caps.set_property("textoverlay", "font-desc", self.__get_font_description()) 
            
            self.source_caps.set_property("textoverlay", "xpos", float(xpos/100))
            self.preview_caps.set_property("textoverlay", "xpos", float(xpos/100))
            self._the_widget.LabelXposValueText.setText(str(xpos))
            self._the_widget.SliderXposText.setValue(xpos)
            
            self.source_caps.set_property("textoverlay", "ypos", float(ypos/100))
            self.preview_caps.set_property("textoverlay", "ypos", float(ypos/100))
            self._the_widget.LabelYposValueText.setText(str(ypos))
            self._the_widget.SliderYposText.setValue(ypos)
            
    #textoverlay --------------------------------------------------                
                
    def __set_groupbox_text_enabled(self,enabled):
        
        if self.have_video:
            self._the_widget.LineEditText.setEnabled(enabled)
            self._the_widget.SliderXposText.setEnabled(enabled)
            self._the_widget.SliderYposText.setEnabled(enabled)
            self._the_widget.FontComboBox.setEnabled(enabled)
            self._the_widget.SpinBoxTextSize.setEnabled(enabled)
            self._the_widget.ComboBoxStyle.setEnabled(enabled)
        

        
    def __get_font_description(self):
        
        string_font = self._the_widget.FontComboBox.currentText()
        string_size = str(self._the_widget.SpinBoxTextSize.value())
        
        index = self._the_widget.ComboBoxStyle.currentIndex()
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
    
    #video --------------------------------------------------------
    
    def change_size(self,width,height):
        if self.have_video:
            self.video_width = width
            self.video_height = height
            
            string_width = "width="+str(self.video_width)
            string_height = "height="+str(self.video_height)
            #string_framerate = "framerate="+str(self.video_framerate)+"/1"
            
            #self.videocaps_string = "video/x-raw,"+string_width+","+string_height+","+string_framerate
            self.videocaps_string = "video/x-raw,"+string_width+","+string_height
            self.source_caps.set_caps("videocaps", self.videocaps_string)
            
            self._the_widget.SliderWidth.setValue(self.video_width)
            self._the_widget.SliderHeight.setValue(self.video_height)
            
            self._the_widget.LabelWidthValue.setText(str(self.video_width))
            self._the_widget.LabelHeightValue.setText(str(self.video_height))
            
    def __change_width_height_framerate(self):
        
        if self.have_video:
        
            self.video_width = self._the_widget.SliderWidth.value()
            self.video_height = self._the_widget.SliderHeight.value()
            self.video_framerate = self._the_widget.SpinBoxFramerate.value()
            
            string_width = "width="+str(self.video_width)
            string_height = "height="+str(self.video_height)
            #string_framerate = "framerate="+str(self.video_framerate)+"/1"
            
            self.videocaps_string = "video/x-raw,"+string_width+","+string_height
            #self.videocaps_string = "video/x-raw,"+string_width+","+string_height+","+string_framerate
            self.source_caps.set_caps("videocaps", self.videocaps_string)
            
            self._the_widget.LabelWidthValue.setText(str(self.video_width))
            self._the_widget.LabelHeightValue.setText(str(self.video_height))
            
            if self.subwindow_video:
                self.subwindow_video.set_window_size(self.video_width,self.video_height)
        
    
    #videomixer ---------------------------------------------------
    
    def __change_alpha(self):
        if self.have_video:
            self.alpha = self._the_widget.SliderAlpha.value()
            alpha_float = float(self.alpha/100)
            self._the_widget.LabelAlphaValue.setText(str(self.alpha))
            
            self.mixer.set_videomixer_pad_property(self.source_caps, "alpha", alpha_float)
            
            
    def change_alpha(self,alpha_float):
        if self.have_video:
            self.mixer.set_videomixer_pad_property(self.source_caps, "alpha", alpha_float)
            self.alpha = alpha_float * 100
            self._the_widget.SliderAlpha.setValue(self.alpha)
            self._the_widget.LabelAlphaValue.setText(str(self.alpha))
            
            
            
            
    def change_pos(self,xpos,ypos):
        if self.have_video:
            
            try:
                self._the_widget.SliderXpos.setValue(xpos)
                self._the_widget.SliderYpos.setValue(ypos)
                
                self.mixer.set_videomixer_pad_property(self.source_caps, "xpos", xpos)
                self._the_widget.LabelXposValue.setText(str(xpos))
                
                self.mixer.set_videomixer_pad_property(self.source_caps, "ypos", ypos)
                self._the_widget.LabelYposValue.setText(str(ypos))
                
            except:
                print("This container is not linked with pipeline")
    
    def __change_xpos_ypos(self):
        if self.have_video:
            print("nombre: "+self.name)
            
            xpos = self._the_widget.SliderXpos.value()
            ypos = self._the_widget.SliderYpos.value()
            
            print("xpos,ypos: "+str(xpos)+","+str(ypos))
            
            self.mixer.set_videomixer_pad_property(self.source_caps, "xpos", xpos)
            self._the_widget.LabelXposValue.setText(str(xpos))
            
            self.mixer.set_videomixer_pad_property(self.source_caps, "ypos", ypos)
            self._the_widget.LabelYposValue.setText(str(ypos))
            
            if self.subwindow_video:
                self.subwindow_video.set_window_pos(xpos,ypos)
    
    def change_zorder(self,zorder):
        if self.have_video:
            self.mixer.set_videomixer_pad_property(self.source_caps, "zorder", zorder)
            self._the_widget.SpinBoxZpos.setValue(zorder)
                   
                
    def __change_zpos(self):
        
        if self.have_video:
            zpos = self._the_widget.SpinBoxZpos.value()
            self.mixer.set_videomixer_pad_property(self.source_caps, "zorder", zpos)
            
            
    def set_tabs_enabled(self,audio_enabled,video_enabled):
        self._the_widget.TabAudio.setEnabled(audio_enabled)
        self._the_widget.TabVideo.setEnabled(video_enabled)
        
        
    def hide_tabs(self,hide_audio,hide_video,hide_text=False):
        
        if hide_audio == True:
            self._the_widget.TabWidget.removeTab(1)
            
        if hide_video == True:
            self._the_widget.TabWidget.removeTab(0)
            
        if hide_text == True:
            self._the_widget.TabWidget.removeTab(0)
            
    def set_name(self,name):
        self.name = name   
        self._the_widget.LineEditName.setText(self.name)     
            
    def __change_name(self):
        if not self._the_widget.ToolButtonEditName.isChecked():
            self._the_widget.LineEditName.setReadOnly(True)
            self.name = self._the_widget.LineEditName.text()
            
            if self.widget_volume:
                self.widget_volume.set_name(self.name)
            
            if self.subwindow_video:
                self.subwindow_video.set_name(self.name)
            
            self._the_widget.ToolButtonEditName.setText("Editar")
            
        if self._the_widget.ToolButtonEditName.isChecked():
            self._the_widget.LineEditName.setReadOnly(False)
            self._the_widget.ToolButtonEditName.setText("Finalizar Edición")
        
        
    #----------------------------------------------

    def link_to_videomixer(self,pad,info,caps_container):
        #print("Link to videomixer "+self.name)
        self.mixer.link_to_videomixer(caps_container)
        caps_container.unblock_videosink_pad()
        #Gst.debug_bin_to_dot_file (self.mixer.pipeline,Gst.DebugGraphDetails.ALL,"LinkVideomixer-"+self.name)
        
        
    def link_to_audiomixer(self,pad,info,caps_container):
        #print("Link to audiomixer - "+self.name)
        self.mixer.link_to_audiomixer(caps_container)
        caps_container.unblock_audiosink_pad()
        #Gst.debug_bin_to_dot_file (self.mixer.pipeline,Gst.DebugGraphDetails.ALL,"LinkAudiomixer"+self.name)
    

    def remove_source(self):
        #remove all widgets
        self.main_window.remove_source(self)
        
    def remove_from_mixer(self):
        #self.mixer.stop_pipeline()
        #remove containers
        
        self.mixer.item_deleted = True
        print("\n---Eliminando fuente---")
        if self.have_video:
            print("Fuente tiene video")
            self.preview_widget.set_state_null()
            self.preview_subwindow.set_state_null()
            self.preview_caps.set_state_null()
            self.mixer.unlink_from_videomixer(self.source_caps)
            self.mixer.remove_container_from_pipeline(self.preview_widget)
            self.mixer.remove_container_from_pipeline(self.preview_subwindow)
            self.mixer.remove_container_from_pipeline(self.preview_caps)
            
            
        if self.have_audio:
            print("Fuente tiene audio")
            self.mixer.unlink_from_audiomixer(self.source_caps)


        self.source.set_state_null()
        self.source_caps.set_state_null()
        
        self.mixer.remove_container_from_pipeline(self.source)
        self.mixer.remove_container_from_pipeline(self.source_caps)
        self.remove_source() 
        #self.mixer.play_pipeline()
        
        
    def get_source_class(self):
        
        have_text = self._the_widget.CheckBoxText.isChecked()
        source = SourceClass(self.id,self.have_video,self.have_audio, textoverlay=have_text )
        
        if self.have_video:
            xpos = self._the_widget.SliderXpos.value()
            ypos = self._the_widget.SliderYpos.value()
            zorder = self._the_widget.SpinBoxZpos.value()
            alpha_float = float(self.video_alpha/100)
            self.video_framerate = self._the_widget.SpinBoxFramerate.value()
            source.set_video_properties(self.video_width, self.video_height, xpos, ypos, zorder, alpha_float)
            
            
        if have_text:
            text = self._the_widget.LineEditText.text()
            xpos = self._the_widget.SliderXposText.value()
            ypos = self._the_widget.SliderYposText.value()
            font_settings = self.__get_font_description()
            source.set_textoverlay_properties(text, xpos, ypos, font_settings)
                
        return source
        