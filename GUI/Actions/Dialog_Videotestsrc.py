'''
Created on 11-09-2013

@author: bastian
'''
from PyQt4 import QtCore, QtGui
from GUI.UI.Ui_Dialog_Videotestsrc import Ui_DialogVideotestsrc
from GUI.Actions.Widget_Videotestsrc import Widget_Videotestsrc
from Containers import Utils

class Dialog_Videotestsrc(QtGui.QDialog):
    '''
    classdocs
    '''


    def __init__(self,ventana_principal,mixer,mixer_sink,host,port):
        '''
        Constructor
        '''
        QtGui.QDialog.__init__(self)
        self.__the_dialog = Ui_DialogVideotestsrc()
        self.__the_dialog.setupUi(self)
        
        self.ventana_principal = ventana_principal
        self.mixer = mixer
        self.mixer_sink = mixer_sink
        self.host_mixer = host
        self.port = port
        
        self.connect(self.__the_dialog.ButtonBox,QtCore.SIGNAL('accepted()'),self.__add_videotestsrc)
        self.connect(self.__the_dialog.ButtonBox,QtCore.SIGNAL('rejected()'),self.__close_dialog)
            
        
    def __add_videotestsrc(self):
        
        width = self.__the_dialog.SpinBoxWidth.value()
        height = self.__the_dialog.SpinBoxHeight.value()
        
        alpha = self.__the_dialog.SpinBoxAlpha.value()
        
        framerate = self.__the_dialog.SpinBoxFramerate.value()
        pattern = self.__the_dialog.ComboBoxPattern.currentIndex()
        
        videotest_widget = Widget_Videotestsrc(self.mixer,self.mixer_sink,self.host_mixer,self.port,width,height,alpha,framerate,pattern)
        videotest_widget.add_videotest()
        
        self.ventana_principal.add_to_tab_widget(videotest_widget,"Source - Port: "+str(self.port))
        self.ventana_principal.add_preview(videotest_widget.have_audio, videotest_widget.have_video, self.host_mixer, self.port)
        self.close()
        
    def __close_dialog(self):
        self.ventana_principal.current_port = self.ventana_principal.current_port+1
        self.ventana_principal.current_mixer_sink = self.ventana_principal.current_mixer_sink + 1
        self.close()
        