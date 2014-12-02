'''
Created on 11-09-2013

@author: bastian
'''
from PyQt4 import QtCore, QtGui
from GUI.UI.Ui_Dialog_Webcam import Ui_DialogWebcam
from Containers import Utils

class Dialog_Webcam(QtGui.QDialog):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        QtGui.QDialog.__init__(self)
        self.__the_dialog = Ui_DialogWebcam()
        self.__the_dialog.setupUi(self)
        self.valid = False
        
        self.v4l2_devices = Utils.get_v4l2_device_list()
        self.add_v4l2_devices()
        
        self.connect(self.__the_dialog.ButtonBox,QtCore.SIGNAL('accepted()'),self.__accepted)
        self.connect(self.__the_dialog.ButtonBox,QtCore.SIGNAL('rejected()'),self.__reject)
        
    def add_v4l2_devices(self):
        
        
        if self.v4l2_devices:
            the_list = []
            for x in self.v4l2_devices:
                the_list.append(x[0])
            
            self.__the_dialog.ComboBoxWebcam.addItems(the_list)
            
        else:
            self.__the_dialog.ComboBoxWebcam.addItem("No disponible")
            
    def remove_list_elements(self):
        self.__the_dialog.ComboBoxWebcam.clear()
        
    def get_v4l2_device_selected(self):
        item_selected = self.__the_dialog.ComboBoxWebcam.currentIndex()
        device = self.v4l2_devices[item_selected]
        return device
    
    def __accepted(self):
        self.valid = True
        self.close()
    
    def __reject(self):
        self.close()