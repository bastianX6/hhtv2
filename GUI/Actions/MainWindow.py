'''
Created on 15-12-2013

@author: bastian
'''

from PyQt4 import QtCore, QtGui
from os.path import expanduser

from GUI.UI.Ui_MainWindow import Ui_MainWindow
from GUI.Actions.Widget_VideoAudioTest import WidgetVideoAudioTest
from GUI.Actions.Widget_File import WidgetFile
from GUI.Actions.Widget_V4L2 import WidgetV4L2
from GUI.Actions.Widget_HTTP import WidgetHTTP
from GUI.Actions.Widget_Mic import WidgetMic
from GUI.Actions.Widget_Mixer import WidgetMixer
from GUI.Actions.Widget_DesktopApp import WidgetDesktopApp

from GUI.Actions.DockArea import DockArea
from GUI.Actions.DockWidget_Preview import DockWidgetPreview
from GUI.Actions.DockWidget_Streaming import DockWidgetStreaming
from GUI.Actions.DockWidget_VolumeControl import DockWidgetVolumeControl
from GUI.Actions.DockWidget_Videos import DockWidgetVideos


from GUI.Actions.Dialog_Webcam import Dialog_Webcam
from GUI.Actions.Dialog_HTTP import Dialog_HTTP
from GUI.Actions.Dialog_Microfono import Dialog_Microfono
from GUI.Actions.Dialog_Xorg import Dialog_Xorg
from GUI.Actions.Dialog_Import_Template import DialogImportTemplate

from Containers.MixerContainer import MixerContainer
from Config.ConfigFile import ConfigFile
from Config.ConfigFile import SourceClass

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

class MainWindow(QtGui.QMainWindow):
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
        
        self.setTabPosition( QtCore.Qt.TopDockWidgetArea , QtGui.QTabWidget.North )
        
        self.host_mixer = "127.0.0.1"
        self.port_mixer = 60000
        self.current_port = self.port_mixer + 1
        self.mixer_have_audio = False
        self.mixer_have_video = True
        self.sources = []
        self.primera_vez = True
        
        self.mixer = MixerContainer()
        #self.__create_dock_area()
        
        
        self.setWindowIcon(QtGui.QIcon("GUI/Resources/hhtv-studio.png"))
        self.__the_window.ActionVideoAudiotest.setIcon(QtGui.QIcon("GUI/Resources/SMPTE_Color_Bars.png"))
        self.__the_window.centralwidget.hide()
        self.__init_dock_widgets()
        
        
        
        
        self.connect(self.__the_window.ActionFile, QtCore.SIGNAL('activated()'), self.__action_file)
        self.connect(self.__the_window.ActionAndroid, QtCore.SIGNAL('activated()'), self.__action_android)
        self.connect(self.__the_window.ActionWebcam, QtCore.SIGNAL('activated()'), self.__action_webcam)
        self.connect(self.__the_window.ActionMic, QtCore.SIGNAL('activated()'), self.__action_microphone)
        self.connect(self.__the_window.ActionVideoAudiotest, QtCore.SIGNAL('activated()'), self.add_videoaudiotest)
        self.connect(self.__the_window.ActionDesktopApp, QtCore.SIGNAL('activated()'), self.__action_desktop_app)
        self.connect(self.__the_window.ActionQuit, QtCore.SIGNAL('activated()'), self.close_window)
        self.connect(self.__the_window.actionTemplateExport, QtCore.SIGNAL('activated()'), self.export_template)
        self.connect(self.__the_window.actionTemplateImport, QtCore.SIGNAL('activated()'), self.import_template)
    
    
    def closeEvent(self, event):
        self.close_window()
        
        
    def close_window(self):
        self.mixer.stop_pipeline()
        self.close()
    
    def __create_dock_area(self):
        self.Dock_Area = DockArea()
        self.__the_window.LayoutWidgetRight.addWidget(self.Dock_Area)
    
    
    def __init_dock_widgets(self):
        
        #dockwidget_preview
        self.dockwidget_preview = DockWidgetPreview(self.host_mixer,self.port_mixer)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dockwidget_preview)
        
        #widget_streaming
        self.widget_streaming = DockWidgetStreaming(self.host_mixer,self.port_mixer)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.widget_streaming)
        
        #widget_volume_control
        
        self.widget_volume_contol = DockWidgetVolumeControl()
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.widget_volume_contol)
        
        #widget_videos
        self.widget_videos = DockWidgetVideos()
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.widget_videos)
        
        
        #widget mixer
        self.widget_mixer = WidgetMixer(self,self.mixer,self.widget_videos.get_mdiarea(),self.dockwidget_preview)
        self.add_to_layout_sources(self.widget_mixer)
        
        
        #add widget volume from mixer
        self.widget_mixer.create_widget_volume()
        self.widget_volume_contol.add_volume_widget(self.widget_mixer.widget_volume)
        
        #create tabs
        self.tabifyDockWidget(self.dockwidget_preview,self.widget_streaming)
        self.widget_mixer.widget_streaming = self.widget_streaming
        self.widget_streaming.setEnabled(False)
        
        self.tabifyDockWidget(self.widget_streaming,self.widget_volume_contol)
        self.tabifyDockWidget(self.__the_window.DockWidgetSources,self.widget_videos)
        
        self.__the_window.DockWidgetSources.raise_()
        self.dockwidget_preview.raise_()
        
        self.widget_mixer.play_mixer()
        
        print("Cantidad de fuentes agregadas: "+str(len(self.sources)))
    
    def add_to_layout_sources(self,widget):
        self.__the_window.LayoutSources.addWidget(widget)
        
    def remove_from_layout_sources(self,widget):
        self.__the_window.LayoutSources.removeWidget(widget)
        
    #-----------------------------------------------------    
        
    def add_videoaudiotest(self):
        
        widget = WidgetVideoAudioTest(self,self.widget_videos.get_mdiarea(),self.mixer)
        self.sources.append(widget)
        self.add_to_layout_sources(widget)
        
        widget.create_widget_volume()
        self.widget_volume_contol.add_volume_widget(widget.widget_volume)
        self.widget_videos.add_subwindow(widget.subwindow_video)
        
        print("Cantidad de fuentes agregadas: "+str(len(self.sources)))
        
        
    def add_file(self,the_uri):
        
        widget = WidgetFile(self,self.widget_videos.get_mdiarea(),self.mixer,the_uri)
        self.sources.append(widget)
        self.add_to_layout_sources(widget)
        
        
        if widget.have_audio:
            widget.create_widget_volume()
            self.widget_volume_contol.add_volume_widget(widget.widget_volume)
    
        if widget.have_video:
            self.widget_videos.add_subwindow(widget.subwindow_video)
            
        print("Cantidad de fuentes agregadas: "+str(len(self.sources)))
            
            
    def add_android_stream(self,audio_selected,video_selected,the_uri):
        
        widget = WidgetHTTP(self,self.widget_videos.get_mdiarea(),self.mixer,audio_selected,video_selected,the_uri)
        self.sources.append(widget)
        self.add_to_layout_sources(widget)
        
        if widget.have_audio:
            widget.create_widget_volume()
            self.widget_volume_contol.add_volume_widget(widget.widget_volume)
    
        if widget.have_video:
            self.widget_videos.add_subwindow(widget.subwindow_video)
            
        print("Cantidad de fuentes agregadas: "+str(len(self.sources)))
            
    def add_webcam_v4l2(self,device,device_name):
        widget = WidgetV4L2(self,self.widget_videos.get_mdiarea(),self.mixer,device_name,device)
        self.sources.append(widget)
        self.add_to_layout_sources(widget)
        self.widget_videos.add_subwindow(widget.subwindow_video)
        
        print("Cantidad de fuentes agregadas: "+str(len(self.sources)))
        
        
    def add_microphone_pulse(self,device,device_name):
        widget = WidgetMic(self,self.widget_videos.get_mdiarea(),self.mixer,device_name,device)
        self.sources.append(widget)
        self.add_to_layout_sources(widget)
        
        widget.create_widget_volume()
        self.widget_volume_contol.add_volume_widget(widget.widget_volume)
        
        print("Cantidad de fuentes agregadas: "+str(len(self.sources)))
        
    def add_desktop_app_xorg(self,window_name,xid):
        widget = WidgetDesktopApp(self,self.widget_videos.get_mdiarea(),self.mixer,window_name,xid)
        self.sources.append(widget)
        self.add_to_layout_sources(widget)

        self.widget_videos.add_subwindow(widget.subwindow_video)
        
        print("Cantidad de fuentes agregadas: "+str(len(self.sources)))

    def __action_file(self):
        filter = "All Compatible media (*.mp4 *.flv *.ogv *.ogg *.mkv *.webm *.avi *.wmv "
        filter += "*.wav *.flac *.oga *.ogg *.mp1 *.mp2 *.mp3 *.wma "
        filter += "*.jpg *.jpeg *.png );;"
        filter += "Video (*.mp4 *.flv *.ogv *.ogg *.mkv *.webm *.avi *.wmv );; "
        filter += "Audio (*.wav *.flac *.oga *.ogg *.mp1 *.mp2 *.mp3 *.wma );;"
        filter += "Images (*.jpg *.jpeg *.png )"
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', expanduser("~"), filter)
        
        if filename:
            self.add_file(filename)
    

    def __action_android(self):
        dialog = Dialog_HTTP()
        dialog.exec_()
        dialog.show()
        
        if dialog.valid:
            the_uri = dialog.get_http_link()
            self.add_android_stream(dialog.audio_selected,dialog.video_selected,the_uri)
            
    def __action_webcam(self):
        
        dialog = Dialog_Webcam()
        dialog.exec_()
        dialog.show()
            
        if dialog.valid:
            the_tuple = dialog.get_v4l2_device_selected()
            device = "v4l2://" + the_tuple[1]
            device_name = the_tuple[0]
            self.add_webcam_v4l2(device, device_name)
            
            
            
    def __action_desktop_app(self):

        dialog = Dialog_Xorg()
        dialog.exec_()
        dialog.show()
        
        if dialog.valid:
            the_tuple = dialog.get_xorg_window_id_selected()
            window_name = the_tuple[0]
            xid = the_tuple[1]
            self.add_desktop_app_xorg(window_name, xid)                
                
    
    def __action_microphone(self):
        
        dialog = Dialog_Microfono()
        dialog.exec_()
        dialog.show()
            
        if dialog.valid:
            the_tuple = dialog.get_pulse_device_selected()
            device = the_tuple[1]
            device_name = the_tuple[0]
            self.add_microphone_pulse(device, device_name)

    def remove_source(self,widget):
        
        #stop pipeline and previews
        
        #remove widgets
        self.sources.remove(widget)
        self.remove_from_layout_sources(widget)
        
        if widget.have_video:
            self.widget_videos.remove_subwindow(widget.subwindow_video)
            
        if widget.have_audio:
            self.widget_volume_contol.remove_volume_widget(widget.widget_volume)
        
        print("remove_source | Cantidad de fuentes agregadas: "+str(len(self.sources)))
        
        widget.close()
        widget.destroy()
        self.repaint()
        
    
    def export_template(self):
        
        
        try:
            template = ConfigFile()
        
            template.add_source(self.widget_mixer.get_source_class())
            
                
            for source in self.sources:
                print("source: ",source)
                source_class = source.get_source_class()
                source.set_source_settings(source_class)
                if source.widget_volume:
                    source_class.set_audio_properties(source.widget_volume.get_volume())
                template.add_source(source_class)
                    
            filename = QtGui.QFileDialog.getSaveFileName(self, "Save Template", expanduser("~"), "JSON (*.json)")
            
            success = False
            if filename:
                success = template.write_to_file(filename)
                
            
            if not success:
                raise Exception   
        except:
            print("Error")
            
    def import_template(self):
        filename = QtGui.QFileDialog.getOpenFileName(None, 'Open File', expanduser("~"), "JSON (*.json)")
    
        if filename:
            config_file = ConfigFile()
            if not config_file.read_from_file(filename):
                raise Exception 
        
        
            dialog = DialogImportTemplate(config_file)
            dialog.exec_()
            dialog.show()
            
            if dialog.valid:
                
                self.mixer.stop_pipeline()
                #delete all sources
                
                
                while len(self.sources) > 0:
                
                    print("antes de eliminar | Cantidad de fuentes agregadas: "+str(len(self.sources)))
                    the_source = self.sources[0]
                    the_source.remove_from_mixer() 

                self.sources = []
                temp_sources = []
                
                self.mixer.play_pipeline()
                   
                #create new sources and add them to pipeline
                
                for widget_template in dialog.widget_list:
                    source_class = widget_template.source_class
                    device = widget_template.device
                    device_name = widget_template.device_name
                    
                    if widget_template.include_source:
                    
                        if widget_template.source_type == "Desktop App":
                            self.add_desktop_app_xorg(device_name, device)
                            
                        elif widget_template.source_type == "Webcam":
                            self.add_webcam_v4l2(device, device_name)
                        
                        elif widget_template.source_type == "Pulse":
                            self.add_microphone_pulse(device, device_name)
                        
                        elif widget_template.source_type == "File":
                            self.add_file(device)
                        
                        elif widget_template.source_type == "VideoAudioTest":
                            self.add_videoaudiotest()
                        
                        
                        widget = self.sources[len(self.sources)-1]
                        have_video = source_class.general_settings["have_video"]
                        have_audio = source_class.general_settings["have_audio"]
                        is_image = source_class.general_settings["is_image"]
                        textoverlay = source_class.general_settings["textoverlay"]
                        
                        
                        #set video properties
                        if have_video:
                            width = source_class.video_settings["width"]
                            height = source_class.video_settings["height"]
                            xpos = source_class.video_settings["xpos"]
                            ypos = source_class.video_settings["ypos"]
                            zorder = source_class.video_settings["zorder"]
                            alpha = source_class.video_settings["alpha"]
                            widget.change_size(width,height)
                            
                            the_tuple = (widget,xpos,ypos,zorder,alpha)
                            temp_sources.append(the_tuple)
                        
                        
                        
                        #set audio properties
                        if have_audio:
                            volume = source_class.audio_settings["volume"]
                            widget.widget_volume.set_volume(volume)
                        
                        #set textoverlay properties
                        if textoverlay:
                            text = source_class.textoverlay_settings["text"]
                            xpos = source_class.textoverlay_settings["xpos"]
                            ypos = source_class.textoverlay_settings["ypos"]
                            font_settings = source_class.textoverlay_settings["font_settings"]
                            widget.change_text(text,xpos,ypos,font_settings)
                       
                
                #apply video properties
                if len(temp_sources)>0:
                    for the_tuple in temp_sources:
                        
                        try:
                            widget = the_tuple[0]
                            xpos = the_tuple[1]
                            ypos = the_tuple[2]
                            zorder = the_tuple[3]
                            alpha = the_tuple[4]
                         
                            widget.change_pos(xpos,ypos)
                            widget.change_zorder(zorder)
                            widget.change_alpha(alpha)
                        except:
                            print("Error al aplicar propiedades de video")
        
        