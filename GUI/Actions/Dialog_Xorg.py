'''
Created on 11-09-2013

@author: bastian
'''
from PyQt4 import QtCore, QtGui
from GUI.UI.Ui_Dialog_Xorg import Ui_DialogXorg
from Containers import Utils

class Dialog_Xorg(QtGui.QDialog):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        QtGui.QDialog.__init__(self)
        self.__the_dialog = Ui_DialogXorg()
        self.__the_dialog.setupUi(self)
        self.xorg_list = Utils.get_x11_windows_id_list()
        self.add_xorg_windows()
        
        self.valid = False
        
        self.connect(self.__the_dialog.ButtonBox,QtCore.SIGNAL('accepted()'),self.__accepted)
        self.connect(self.__the_dialog.ButtonBox,QtCore.SIGNAL('rejected()'),self.__reject)
        
    def add_xorg_windows(self):
        
        
        if self.xorg_list:
            the_list = []
            for x in self.xorg_list:
                the_list.append(x[0])
            self.__the_dialog.ComboBoxXorg.addItems(the_list)
            
        else:
            self.__the_dialog.ComboBoxXorg.addItem("No disponible")
            
    def remove_list_elements(self):
        self.__the_dialog.ComboBoxXorg.clear()
        
    def get_xorg_window_id_selected(self):
        item_selected = self.__the_dialog.ComboBoxXorg.currentIndex()
        xid = self.xorg_list[item_selected][1]
        
        if xid!=0:
            xid = int(xid,0)
        
        return (self.xorg_list[item_selected][0],xid)
    
    
    def __accepted(self):
        self.valid = True
        self.close()
    
    def __reject(self):
        self.close()
        
        