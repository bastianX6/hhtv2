'''
Created on 13-03-2014

@author: bastian
'''

from PyQt4 import QtCore, QtGui
from os.path import expanduser

from GUI.UI.Ui_Dialog_Import_Template import Ui_DialogImportTemplate
from GUI.Actions.Widget_Source_Template import WidgetSourceTemplate

class DialogImportTemplate(QtGui.QDialog):
    '''
    classdocs
    '''


    def __init__(self, conf_file):
        '''
        Constructor
        '''
        
        QtGui.QDialog.__init__(self)
        self.__the_dialog = Ui_DialogImportTemplate()
        self.__the_dialog.setupUi(self)
        self.valid = False
        self.conf_file = conf_file
        self.widget_list = []
        self.add_widgets()
        
        
        self.connect(self.__the_dialog.ButtonBox,QtCore.SIGNAL('accepted()'),self.__accepted)
        self.connect(self.__the_dialog.ButtonBox,QtCore.SIGNAL('rejected()'),self.__reject)
        
    def __accepted(self):
        pass
    
    def accept(self):
        
        self.valid = True
        
        for widget in self.widget_list:
            if widget.include_source and not widget.ready:
                self.valid = False
        
        if self.valid:
            self.close()
            
        else:
            QtGui.QMessageBox.warning(self, "Alerta", "Una o mas fuentes no se encuentran listas")
    
    def __reject(self):
        self.close()
        
    def add_widgets(self):
        
        for source_class in self.conf_file.source_list.values():
            
            if source_class.id == "Mixer":
                continue
            
            widget = WidgetSourceTemplate(source_class)
            self.__the_dialog.LayoutSources.addWidget(widget)
            self.widget_list.append(widget)
        