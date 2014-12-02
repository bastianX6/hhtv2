'''
Created on 06-12-2013

@author: bastian
'''
from PyQt4 import QtCore, QtGui
from os.path import expanduser

class DialogAddFile(object):
    '''
    classdocs
    '''


    def __init__(self,ventana_principal,mixer,mixer_sink,host,port):
        '''
        Constructor
        '''
        self.filter = ""
        self.ventana_principal = ventana_principal
        self.mixer = mixer
        self.mixer_sink = mixer_sink
        
        self.host_mixer = host
        self.port = port
        
        
    
    def set_video_audio_filter(self):
        self.filter = "Video (*.mp4 *.flv *.ogv *.ogg *.mkv *.webm *.avi *.wmv );; "
        self.filter += "Audio (*.wav *.flac *.oga *.ogg *.mp1 *.mp2 *.mp3 *.wma )"
        
        
    def set_image_filter(self):
        filter = "Imágenes (*.jpeg *.jpg *.png)"
        
        
    def open_file(self):
        filename = QtGui.QFileDialog.getOpenFileName(self.ventana_principal, 'Open File', expanduser("~"), self.filter)
        if filename:
            print("filename: "+filename)
            width = 400
            height = 300
            alpha = 10
            framerate = 30
            self.the_uri = "file://"+filename
            file_widget = Widget_AddFile(self.mixer,self.mixer_sink,self.host_mixer,self.port,width,height,alpha,framerate,self.the_uri)
            file_widget.add_file()
            
            self.ventana_principal.add_to_tab_widget(file_widget,"Source - Port: "+str(self.port))
            self.ventana_principal.add_preview(file_widget.have_audio, file_widget.have_video, self.host_mixer, self.port)
        
        else:
            mensaje = "Error al abrir el archivo"
            msgBox = QtGui.QMessageBox(self.ventana_principal);
            msgBox.setText(mensaje)
            msgBox.exec_()