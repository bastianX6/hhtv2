'''
Created on 11-09-2013

@author: bastian
'''

from PyQt4 import QtCore, QtGui
from GUI.UI.Ui_Dialog_Microfono import Ui_DialogMicrofono
from Containers import Utils

class Dialog_Microfono(QtGui.QDialog):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        QtGui.QDialog.__init__(self)
        self.__the_dialog = Ui_DialogMicrofono()
        self.__the_dialog.setupUi(self)
        self.valid = False
        
        self.pulse_devices = Utils.get_pulse_device_list()
        self.add_pulse_devices()
        self.connect(self.__the_dialog.ButtonBox,QtCore.SIGNAL('accepted()'),self.__accepted)
        self.connect(self.__the_dialog.ButtonBox,QtCore.SIGNAL('rejected()'),self.__reject)
        
    def add_pulse_devices(self):
        
        if self.pulse_devices:
            the_list = []
            for x in self.pulse_devices:
                the_list.append(x[0])
            self.__the_dialog.ComboBoxMicrofono.addItems(the_list)
            
        else:
            self.__the_dialog.ComboBoxMicrofono.addItem("No disponible")
            
    
    def remove_list_elements(self):
        self.__the_dialog.ComboBoxMicrofono.clear()
        
        
    def get_pulse_device_selected(self):
        item_selected = self.__the_dialog.ComboBoxMicrofono.currentIndex()
        device = self.pulse_devices[item_selected]
        return device
    
    def __accepted(self):
        self.valid = True
        self.close()
    
    def __reject(self):
        self.close()