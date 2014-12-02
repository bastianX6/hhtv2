'''
Created on 14-02-2014

@author: bastian
'''
from PyQt4 import QtCore, QtGui
from GUI.UI.Ui_Widget_VideoPreview import Ui_WidgetVideoPreview

class WidgetVideoPreview(QtGui.QMdiSubWindow):
    '''
    classdocs
    '''


    def __init__(self,widget,mdiarea):
        '''
        Constructor
        '''
        
        QtGui.QMdiSubWindow.__init__(self)
        self.__the_widget = Ui_WidgetVideoPreview()
        self.__the_widget.setupUi(self)
        self.video_widget = QtGui.QWidget()
        
        
        self.setWidget(self.video_widget)
        
        self.widget = widget
        self.mdiarea = mdiarea   
        
    def moveEvent(self,e):
        
        
        if self.mdiarea.activeSubWindow()==self:
            print("*** Move event - cambiar slides ***")
            pos = self.mdiarea.activeSubWindow().pos()
            print("pos: "+str(pos.x())+","+str(pos.y()))
            self.widget.change_pos(pos.x(),pos.y())
            
            
    def dropEvent(self,e):
        print("*** Drop Event ***")
        
        
    def mouseReleaseEvent(self,e):
        
        size = self.size()
        print("*** mouseReleaseEvent - cambiar tamaño: "+str(size.width())+","+str(size.height()))
        self.widget.change_size(size.width(),size.height())
        
        
    def set_name(self,name):
        self.setWindowTitle(name)
        
        
    def set_window_size(self,width,height):
        self.resize(width,height)
    
    def set_window_pos(self,xpos,ypos):
        print("*** set window pos **")
        print("xpos,ypos: "+str(xpos)+","+str(ypos))
        self.move(xpos,ypos)
        
    def get_winId(self):
        return self.video_widget.winId()
        
        