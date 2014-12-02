'''
Created on 13-03-2014

@author: bastian
'''

from PyQt4 import QtCore, QtGui
from os.path import expanduser
from GUI.UI.Ui_Widget_Source_Template import Ui_WidgetSourceTemplate

from GUI.Actions.Dialog_Xorg import Dialog_Xorg
from GUI.Actions.Dialog_Webcam import Dialog_Webcam
from GUI.Actions.Dialog_Microfono import Dialog_Microfono


class WidgetSourceTemplate(QtGui.QWidget):
    '''
    classdocs
    '''


    def __init__(self,source_class):
        '''
        Constructor
        '''
        
        QtGui.QFrame.__init__(self)
        self._the_widget = Ui_WidgetSourceTemplate()
        self._the_widget.setupUi(self)
        self.source_class = source_class
        self.source_type = self.source_class.source_settings["source_type"]
        self.device_name = source_class.source_settings["device_name"]
        self.device = source_class.source_settings["device"]
        self.state = "Verificar Fuente"
        self.ready = False
        self.include_source = True
        
        
        
        self.connect(self._the_widget.CheckBoxIgnoreSource,QtCore.SIGNAL('stateChanged(int)'),self.checkbox_state_changed)
        
        if self.source_type == "Desktop App":
            self.connect(self._the_widget.ToolButtonSelectSource,QtCore.SIGNAL('clicked()'),self.select_desktop_app)
            
        elif self.source_type == "Webcam":
            self.connect(self._the_widget.ToolButtonSelectSource,QtCore.SIGNAL('clicked()'),self.select_webcam)
            
        elif self.source_type == "Pulse":
            self.connect(self._the_widget.ToolButtonSelectSource,QtCore.SIGNAL('clicked()'),self.select_mic)
            
        elif self.source_type == "File":
            self.connect(self._the_widget.ToolButtonSelectSource,QtCore.SIGNAL('clicked()'),self.select_file)
            
        elif self.source_type == "VideoAudioTest":
            self._the_widget.ToolButtonState.setIcon(QtGui.QIcon.fromTheme("dialog-ok-apply"))
            self.state = "Fuente Lista"
            self._the_widget.ToolButtonSelectSource.hide()
            self.ready = True
        
        
        self.set_properies()
        
    def set_properies(self):
        
        self._the_widget.LabelSourceType.setText(self.source_type)
        self._the_widget.LabelSource.setText(self.device_name)
        self._the_widget.LabelState.setText(self.state)
        
        
    def checkbox_state_changed(self):
        if not self._the_widget.CheckBoxIgnoreSource.isChecked():
            self._the_widget.ToolButtonSelectSource.setEnabled(True)
            self._the_widget.ToolButtonState.setEnabled(True)
            self._the_widget.LabelSource.setEnabled(True)
            self._the_widget.LabelSourceType.setEnabled(True)
            self._the_widget.LabelState.setEnabled(True)
            self._the_widget.label.setEnabled(True)
            self._the_widget.label_3.setEnabled(True)
            self._the_widget.label_5.setEnabled(True)
            self.include_source = True
            
            
        else:
            self._the_widget.ToolButtonSelectSource.setEnabled(False)
            self._the_widget.ToolButtonState.setEnabled(False)
            self._the_widget.LabelSource.setEnabled(False)
            self._the_widget.LabelSourceType.setEnabled(False)
            self._the_widget.LabelState.setEnabled(False)
            self._the_widget.label.setEnabled(False)
            self._the_widget.label_3.setEnabled(False)
            self._the_widget.label_5.setEnabled(False)
            self.include_source = False
            
            
    def select_webcam(self):
        dialog = Dialog_Webcam()
        dialog.exec_()
        dialog.show()
        
        if dialog.valid:
            the_tuple = dialog.get_v4l2_device_selected()
            self.device = "v4l2://" + the_tuple[1]
            self.device_name = the_tuple[0]
            self.state = "Fuente Lista"
            self._the_widget.ToolButtonState.setIcon(QtGui.QIcon.fromTheme("dialog-ok-apply"))
            self.set_properies()
            self.ready = True
    
    def select_desktop_app(self):
        dialog = Dialog_Xorg()
        dialog.exec_()
        dialog.show()
        
        if dialog.valid:
            the_tuple = dialog.get_xorg_window_id_selected()
            self.device_name = the_tuple[0]
            self.device = the_tuple[1]
            self.state = "Fuente Lista"
            self._the_widget.ToolButtonState.setIcon(QtGui.QIcon.fromTheme("dialog-ok-apply"))
            self.set_properies()
            self.ready = True
    
    def select_mic(self):
        dialog = Dialog_Microfono()
        dialog.exec_()
        dialog.show()
        
        if dialog.valid:
            the_tuple = dialog.get_pulse_device_selected()
            self.device_name = the_tuple[0]
            self.device = the_tuple[1]
            self.state = "Fuente Lista"
            self._the_widget.ToolButtonState.setIcon(QtGui.QIcon.fromTheme("dialog-ok-apply"))
            self.set_properies()
            self.ready = True
            
            
    def select_file(self):
        filter = "All Compatible media (*.mp4 *.flv *.ogv *.ogg *.mkv *.webm *.avi *.wmv "
        filter += "*.wav *.flac *.oga *.ogg *.mp1 *.mp2 *.mp3 *.wma "
        filter += "*.jpg *.jpeg *.png );;"
        filter += "Video (*.mp4 *.flv *.ogv *.ogg *.mkv *.webm *.avi *.wmv );; "
        filter += "Audio (*.wav *.flac *.oga *.ogg *.mp1 *.mp2 *.mp3 *.wma );;"
        filter += "Images (*.jpg *.jpeg *.png )"
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', expanduser("~"), filter)
        
        if filename:
            
            self.device_name = "Archivo"
            self.device = filename
            self.state = "Fuente Lista"
            self._the_widget.ToolButtonState.setIcon(QtGui.QIcon.fromTheme("dialog-ok-apply"))
            self.set_properies()
            self.ready = True
        