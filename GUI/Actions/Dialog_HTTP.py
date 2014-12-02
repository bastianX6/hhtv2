'''
Created on 11-09-2013

@author: bastian
'''
from PyQt4 import QtCore, QtGui
from GUI.UI.Ui_Dialog_HTTP import Ui_DialogHTTP

class Dialog_HTTP(QtGui.QDialog):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        QtGui.QDialog.__init__(self)
        self.__the_dialog = Ui_DialogHTTP()
        self.__the_dialog.setupUi(self)
        self.valid = False
        self.audio_selected = False
        self.video_selected = True
        
        self.connect(self.__the_dialog.CheckBoxHTTPAudio, QtCore.SIGNAL('clicked()'), self.http_checkbox_audio_action)
        self.connect(self.__the_dialog.CheckBoxHTTPVideo, QtCore.SIGNAL('clicked()'), self.http_checkbox_video_action)
        self.connect(self.__the_dialog.ButtonBox,QtCore.SIGNAL('accepted()'),self.__accepted)
        self.connect(self.__the_dialog.ButtonBox,QtCore.SIGNAL('rejected()'),self.__reject)
        
        
    def set_http_checkbox_checked(self,audio,video):
        self.__the_dialog.CheckBoxHTTPAudio.setChecked(audio)
        self.__the_dialog.CheckBoxHTTPVideo.setChecked(video)
        
    def http_checkbox_audio_action(self):      
        self.__the_dialog.CheckBoxHTTPAudio.setChecked(True)
        self.__the_dialog.CheckBoxHTTPVideo.setChecked(False)
        
        self.__the_dialog.LineEditAddressAudio.setText("")
        self.__the_dialog.LineEditAddressVideo.setText("")
        self.__the_dialog.LineEditPortAudio.setText("")
        self.__the_dialog.LineEditPortVideo.setText("")
        
        self.__the_dialog.LineEditAddressAudio.setEnabled(True)
        self.__the_dialog.LineEditPortAudio.setEnabled(True)
        self.__the_dialog.LineEditAddressVideo.setEnabled(False)
        self.__the_dialog.LineEditPortVideo.setEnabled(False)
        
        self.audio_selected = True
        self.video_selected = False
        
    
    def http_checkbox_video_action(self):      
        self.__the_dialog.CheckBoxHTTPAudio.setChecked(False)
        self.__the_dialog.CheckBoxHTTPVideo.setChecked(True)
        
        self.__the_dialog.LineEditAddressAudio.setText("")
        self.__the_dialog.LineEditAddressVideo.setText("")
        self.__the_dialog.LineEditPortAudio.setText("")
        self.__the_dialog.LineEditPortVideo.setText("")
        
        self.__the_dialog.LineEditAddressAudio.setEnabled(False)
        self.__the_dialog.LineEditPortAudio.setEnabled(False)
        self.__the_dialog.LineEditAddressVideo.setEnabled(True)
        self.__the_dialog.LineEditPortVideo.setEnabled(True)
        
        self.audio_selected = False
        self.video_selected = True
        
    def __accepted(self):
        self.valid = True
        self.close()
        
    def __reject(self):
        self.close()
        
    def get_http_link(self):
        
        link = ""
        
        if self.__the_dialog.CheckBoxHTTPAudio.isChecked():
            link= "http://" + self.__the_dialog.LineEditAddressAudio.text() + ":"
            link+= self.__the_dialog.LineEditPortAudio.text() + self.__the_dialog.LabelAudio.text()
        
        if self.__the_dialog.CheckBoxHTTPVideo.isChecked():
            link= "http://" + self.__the_dialog.LineEditAddressVideo.text() + ":"
            link+= self.__the_dialog.LineEditPortVideo.text() + self.__the_dialog.LabelVideo.text()
        
        return link