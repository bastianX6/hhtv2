'''
Created on 17-09-2013

@author: Bastian Veliz Vega
'''


import sys,os
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

from GUI.Actions.MainWindow import MainWindow

from PyQt4 import QtCore, QtGui

if __name__ == '__main__':
    
    
    os.putenv('GST_DEBUG_DUMP_DOT_DIR',os.getcwd()+'/dot')
    os.putenv('GST_DEBUG', '1')
    GObject.threads_init()
    Gst.init(None)
    
    
    app = QtGui.QApplication(sys.argv)
    prueba = MainWindow()
    prueba.show();
    sys.exit(app.exec_())