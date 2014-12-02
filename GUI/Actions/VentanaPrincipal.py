'''
Created on 17-09-2013

@author: bastian
'''

import os
from os.path import expanduser
from PyQt4 import QtCore, QtGui

#import GUI elements
from GUI.UI.Ui_VentanaPrincipal import Ui_MainWindow 

from GUI.Actions.Dialog_Microfono import Dialog_Microfono 
from GUI.Actions.Dialog_HTTP import Dialog_HTTP
from GUI.Actions.Dialog_Webcam import Dialog_Webcam
from GUI.Actions.Dialog_Xorg import Dialog_Xorg
from GUI.Actions.DockWidget_Fuente import DockWidget_Fuente
from GUI.Actions.Widget_Videotestsrc import Widget_Videotestsrc
from GUI.Actions.Widget_VideoMixer import Widget_VideoMixer
from GUI.Actions.Dialog_Videotestsrc import Dialog_Videotestsrc
from GUI.Actions.Dialog_Add_File import DialogAddFile

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject
from gi.repository import GdkX11, GstVideo

from Containers.MixerContainer import MixerContainer
from Containers.SourceContainer import SourceContainer
from Containers.CapsContainer import CapsContainer
from Containers.TcpSinkContainer import TcpSinkContainer
from Containers.XVideoContainer import XVideoContainer
from Containers.Container import Container



class VentanaPrincipal(QtGui.QMainWindow):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        QtGui.QMainWindow.__init__(self)
        self.__the_window = Ui_MainWindow()
        self.__the_window.setupUi(self)
        
        self.host_mixer = "127.0.0.1"
        self.port_mixer = 60000
        self.current_port = self.port_mixer
        self.current_mixer_sink = 0
        self.preview_number = 0
        self.mixer_have_audio = False
        self.mixer_have_video = True
        self.previews = []
        
        self.mixer = MixerContainer()
        
        self.__init_mixer_widget()
        
        
        self.connect(self.__the_window.ActionArchivo, QtCore.SIGNAL('activated()'), self.__add_file)
        self.connect(self.__the_window.ActionImagen, QtCore.SIGNAL('activated()'), self.__add_image)
        self.connect(self.__the_window.ActionHTTP, QtCore.SIGNAL('activated()'), self.__add_http_stream)
        self.connect(self.__the_window.ActionWebcam, QtCore.SIGNAL('activated()'), self.__add_webcam)
        self.connect(self.__the_window.ActionMicrofono, QtCore.SIGNAL('activated()'), self.__add_microphone)
        self.connect(self.__the_window.ActionVideotest, QtCore.SIGNAL('activated()'), self.add_videotestsrc)
        
    
    def __init_mixer_widget(self):
        widget = Widget_VideoMixer(self,self.__the_window,self.mixer)        
        self.__the_window.LayoutTabMixer.addWidget(widget)
        
    def __init_preview(self):
        self.preview = XVideoContainer(self.mixer_have_audio,self.mixer_have_video,
                                       self.host_mixer,self.port_mixer,
                                       self.__the_window.WidgetVistaPrevia.winId(),False)
        
        Gst.debug_bin_to_dot_file (self.preview.pipeline,Gst.DebugGraphDetails.ALL, "preview_mixer_creado")
        
        self.preview.play_pipeline()
        self.add_preview(self.mixer_have_audio,self.mixer_have_video,
                                       self.host_mixer,self.port_mixer,False)
    
    def add_preview(self,have_audio,have_video,host,port,sync=True):    

        widget = DockWidget_Fuente()
        source_preview = XVideoContainer(have_audio,have_video,host,port,
                                        widget.the_widget.WidgetFuenteVideo.winId(),sync)
        
        self.__the_window.LayoutFuentes.addWidget(widget,0,self.preview_number)
        
              
        source_preview.play_pipeline()
        self.previews.append(source_preview)
        
        Gst.debug_bin_to_dot_file (source_preview.pipeline,Gst.DebugGraphDetails.ALL, 
                                   "preview-"+str(self.preview_number)+"_creado")
        Gst.debug_bin_to_dot_file (self.mixer.pipeline,Gst.DebugGraphDetails.ALL, 
                                   "mixer-preview-"+str(self.preview_number)+"_creado")
        self.preview_number = self.preview_number + 1
    
    def add_videotestsrc(self):
        
        self.current_port = self.current_port+1
        self.current_mixer_sink = self.current_mixer_sink + 1
        
        dialog = Dialog_Videotestsrc(self,self.mixer,self.current_mixer_sink,self.host_mixer,self.current_port)
        dialog.exec_()
        dialog.show()
        
    
    def add_to_tab_widget(self,widget,name):
        self.__the_window.TabWidgetPropiedades.addTab(widget, name)
        
    def closeEvent(self, event):
        Gst.debug_bin_to_dot_file (self.mixer.pipeline,Gst.DebugGraphDetails.ALL, "tcp_mixer_play")
        for preview in self.previews:
            preview.stop_pipeline()
            
    
        
    def __add_file(self):
        self.current_port = self.current_port+1
        self.current_mixer_sink = self.current_mixer_sink + 1
        
        dialog = DialogAddFile(self,self.mixer,self.current_mixer_sink,self.host_mixer,self.current_port)
        
        dialog.set_video_audio_filter()
        dialog.open_file()
        
        '''filter = "Video (*.mp4 *.flv *.ogv *.ogg *.mkv *.webm *.avi *.wmv );; "
        filter += "Audio (*.wav *.flac *.oga *.ogg *.mp1 *.mp2 *.mp3 *.wma )"
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', expanduser("~"), filter)'''
    
    def __add_image(self):
        filter = "Imágenes (*.jpeg *.jpg *.png)"
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', expanduser("~"), filter)
    
    def __add_http_stream(self):
        dialog = Dialog_HTTP()
        dialog.exec_()
        dialog.show()
    
    def __add_webcam(self):
        dialog = Dialog_Webcam()
        dialog.exec_()
        dialog.show()
    
    def __add_microphone(self):
        dialog = Dialog_Microfono()
        dialog.exec_()
        dialog.show()