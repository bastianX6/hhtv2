'''
Created on 06-10-2013

@author: bastian
'''
from Containers.Container import Container
from Config.GlobalVars import Defaults

import uuid
import gi

gi.require_version('Gst', '1.0')
from gi.repository import Gst

class MixerLink(object):
    
    def __init__(self):
        self.container = None
        self.container_ghost_pad = None
        self.mixer_pad = None
        self.mixer_ghost_pad = None
        

class MixerContainer(Container):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        
        self.pipeline = Gst.Pipeline()
        self.bus = self.pipeline.get_bus()
        
        #self.bus.connect('message', self.__message)
        self.connect_on_error(None)
        
        self.add_element("videomixer", "videomixer")
        self.add_element("adder", "adder")
        self.add_element("tee", "videotee")
        self.add_element("tee", "audiotee")
        self.add_element("videoconvert", "videoconvert")
        self.add_element("audioconvert", "audioconvert")

        self.videomixer_links = dict()
        self.audiomixer_links = dict()
        self.container_list = []
        self.caps_containers_linked = []
        
        self.item_deleted = False
    
        #self.pipeline.set_delay(5)
        
        self.set_property("videomixer", "background", 1)
        self.link_elements("videomixer", "videoconvert")
        self.link_elements("videoconvert", "videotee")
        self.link_elements("adder", "audioconvert")
        self.link_elements("audioconvert", "audiotee")
        
        
    def add_container_to_pipeline(self,container):
        self.container_list.append(container)
        self.pipeline.add(container.the_bin)
        
    def remove_container_from_pipeline(self,container):
        self.container_list.remove(container)
        self.pipeline.remove(container.the_bin)

        
    def play_pipeline(self):
        self.pipeline.set_state(Gst.State.PLAYING)
        
    def stop_pipeline(self):
        '''
            Detiene la reproduccion de un pipeline.
            En caso que se haya eliminado un item mientras se estaba reproduciendo, se eliminan
            todas las fuentes del mixer y se vuelven a agregar.
            Esto incluye el crear nuevos elementos "videmixer" y "adder"
        '''
        self.pipeline.set_state(Gst.State.NULL)
        
        if self.item_deleted:
            
            video_containers = []
            audio_containers = []
            video_pads_properties = []
            
            for videomixer_link in self.videomixer_links.values():
                #Obtener valores pad
                pad_videomixer = videomixer_link.mixer_pad
                
                container = videomixer_link.container
                alpha_value = pad_videomixer.get_property("alpha")
                zorder_value = pad_videomixer.get_property("zorder")
                xpos_value = pad_videomixer.get_property("xpos")
                ypos_value = pad_videomixer.get_property("ypos")
                
                tupla = (container,alpha_value,zorder_value,xpos_value,ypos_value)
                video_pads_properties.append(tupla)
                
                
                video_containers.append(container)
                
            for audiomixer_link in self.audiomixer_links.values():
                audio_containers.append(audiomixer_link.container)
            
            #unlink containers from videomixer
            for video_container in video_containers:
                self.unlink_from_videomixer(video_container)
            
            #unlink containers from adder   
            for audio_container in audio_containers:
                self.unlink_from_audiomixer(audio_container)
                        
                    
                
                
            self.videomixer_links = dict()
            self.audiomixer_links = dict()
            
            self.unlink_elements("videomixer", "videoconvert")
            self.unlink_elements("adder", "audioconvert")
            
            self.remove_element("videomixer")
            self.remove_element("adder")
            
            self.add_element("videomixer", "videomixer")
            self.add_element("adder", "adder")
            
            self.link_elements("videomixer", "videoconvert")
            self.link_elements("adder", "audioconvert")
            
            #link containers to videomixer
            for container in video_containers:
                self.link_to_videomixer(container)
                
            #set videomixer pad's properties
            for tupla in video_pads_properties:
                container = tupla[0]
                alpha_value = tupla[1]
                zorder_value = tupla[2]
                xpos_value = tupla[3]
                ypos_value = tupla[4]
                
                self.set_videomixer_pad_property(container, "alpha", alpha_value)
                self.set_videomixer_pad_property(container, "xpos", xpos_value)
                self.set_videomixer_pad_property(container, "ypos", ypos_value)
                
                if(container.name == Defaults.backgroud_caps_name):
                    self.set_videomixer_pad_property(container, "zorder", 0)
                else:
                    self.set_videomixer_pad_property(container, "zorder", zorder_value)
                
            
            #link containers to adder
            for container in audio_containers:
                self.link_to_audiomixer(container)
            
            
            self.item_deleted = False
            self.set_property("videomixer", "background", 1)
        
        
        
        
    def pause_pipeline(self):
        self.pipeline.set_state(Gst.State.PAUSED)
        
    def pipeline_ready(self):
        self.pipeline.set_state(Gst.State.READY)
        
        for videomixer_link in self.videomixer_links.values():
            success = videomixer_link.mixer_ghost_pad.push_event(Gst.Event.new_reconfigure())
            print("push event videomixer: ",success)
            
        for audiomixer_link in self.audiomixer_links.values():
            success = audiomixer_link.mixer_ghost_pad.push_event(Gst.Event.new_reconfigure())
            print("push event audiomixer: ",success)
        
        
    
    def connect_on_error(self,data):
        self.bus.connect('message::error', self.__on_error,data)
        
        
    def __on_error(self, bus, msg,data):
        print('on_error():', msg.parse_error())
        
        if data == None:
            pass
            
        
        
        
        #self.stop_pipeline()
    
    
    #-----------------------------------------------------------
    
    def link_to_mixer(self,container,have_audio,have_video):
        
        if have_audio:
            self.link_to_audiomixer(container)
            
        if have_video:
            self.link_to_videomixer(container)
            
            
    def unlink_to_mixer(self,container,have_audio,have_video):
        
        if have_audio:
            self.unlink_from_audiomixer(container)
            
        if have_video:
            self.unlink_from_videomixer(container)
    
    
    #-----------------------------------------------------------
        
    def link_to_videomixer(self,source_container,bin_pad_name="video_src"):
        #get ghost pad from source container
        source_bin_pad = source_container.get_bin_pad(bin_pad_name)
            
        #create ghost pad from videomixer pad
        videomixer_pad_name = "sink_%u"
        videomixer = self.element_list["videomixer"]
        videomixer_pad = self.get_pad(videomixer, videomixer_pad_name, True)
        
        pad_name = "video_" + videomixer_pad.get_name()
            
        self.create_ghost_pad_2(videomixer_pad, pad_name)
        mixer_bin_pad = self.get_bin_pad(pad_name, False)
            
        #link source container to videomixer
        source_bin_pad.link(mixer_bin_pad)
        
        videomixer_link = MixerLink()
        
        videomixer_link.container = source_container
        videomixer_link.container_ghost_pad = source_bin_pad
        videomixer_link.mixer_pad = videomixer_pad
        videomixer_link.mixer_ghost_pad = mixer_bin_pad
            
        self.videomixer_links[source_container.name] = videomixer_link
        
        
    def unlink_from_videomixer(self,source_container):
        
        videomixer_link = self.videomixer_links.pop(source_container.name)
        
        
        videomixer_link.container_ghost_pad.push_event(Gst.Event.new_eos())
        #unlink pads
        
        videomixer_link.container_ghost_pad.unlink(videomixer_link.mixer_ghost_pad)
        
        #remove bin pad
        self.remove_ghost_pad2(videomixer_link.mixer_ghost_pad)
        
        #remove videomixer pad
        self.remove_pad("videomixer", videomixer_link.mixer_pad)
        
    #-----------------------------------------------------------
        
    
    def link_to_audiomixer(self,source_container,bin_pad_name="audio_src"):
        #get ghost pad from source container
        source_bin_pad = source_container.get_bin_pad(bin_pad_name)
        
        #create ghost pad from audiomixer pad
        audiomixer_pad_name = "sink_%u"
        audiomixer = self.element_list["adder"]
        audiomixer_pad = self.get_pad(audiomixer, audiomixer_pad_name, True)
        
        pad_name = "audio_" + audiomixer_pad.get_name()
        
        self.create_ghost_pad_2(audiomixer_pad, pad_name)
        mixer_bin_pad = self.get_bin_pad(pad_name, False)
            
        #link source container to audiomixer
            
        source_bin_pad.link(mixer_bin_pad)
        
        audiomixer_link = MixerLink()
        
        audiomixer_link.container = source_container
        audiomixer_link.container_ghost_pad = source_bin_pad
        audiomixer_link.mixer_pad = audiomixer_pad
        audiomixer_link.mixer_ghost_pad = mixer_bin_pad
            
        self.audiomixer_links[source_container.name] = audiomixer_link
        
    def unlink_from_audiomixer(self,source_container):
        
        audiomixer_link = self.audiomixer_links.pop(source_container.name)
        
        audiomixer_link.container_ghost_pad.push_event(Gst.Event.new_eos())
        #unlink pads
        
        audiomixer_link.container_ghost_pad.unlink(audiomixer_link.mixer_ghost_pad)
        
        #remove bin pad
        self.remove_ghost_pad2(audiomixer_link.mixer_ghost_pad)
        
        #remove audiomixer pad
        self.remove_pad("adder", audiomixer_link.mixer_pad)
    
    #-----------------------------------------------------------
        
    def set_videomixer_pad_property(self,source_container,the_property,value):
        videomixer_link = self.videomixer_links[source_container.name]
        pad_videomixer = videomixer_link.mixer_pad
        pad_videomixer.set_property(the_property,value)
        
    #----------------------------------------------------------- 
    
    def create_ghost_src_pads(self,audio_pad_name,video_pad_name):
        self.__create_audio_ghost_src_pad(audio_pad_name)
        self.__create_video_ghost_src_pad(video_pad_name)
        
    
    def __create_audio_ghost_src_pad(self,pad_name):
        self.create_ghost_pad("audiotee", "src_%u", True, pad_name)
        
    def __create_video_ghost_src_pad(self,pad_name):
        self.create_ghost_pad("videotee", "src_%u", True, pad_name)
        
    
        
        
    def __message(self, bus, msg):
        print('-------------------------------------------')
        if msg.type == Gst.MessageType.STATE_CHANGED:
            states = msg.parse_state_changed()
            print('Old State',self.parse_state(states[0])," | New state: ",self.parse_state(states[1])," | State pending: ",self.parse_state(states[2]))
            
        if msg.type == Gst.MessageType.STREAM_STATUS:
            stream_status = msg.parse_stream_status()
            print('Stream Status:',stream_status[0])
            print('Element:',stream_status[1])
            
        if msg.type == Gst.MessageType.WARNING:
            warning = msg.parse_warning()
            print('Error:',warning[0])
            print('Details:',warning[1])
            
        if msg.type == Gst.MessageType.TAG:
            print('Tag:',msg.parse_tag().to_string())
            
        else:
            print("Message: ",msg.type)
            
            
            
    def block_videomixer_src_pad(self,function):
        videomixer = self.element_list["videomixer"]
        pad = videomixer.get_static_pad("src")
        self.videosink_pad_id = pad.add_probe(Gst.PadProbeType.BLOCK_DOWNSTREAM,self.audio_blocked,self)
        
    def block_audiomixer_src_pad(self,function):
        adder = self.element_list["adder"]
        pad = adder.get_static_pad("src")
        self.audiosink_pad_id = pad.add_probe(Gst.PadProbeType.BLOCK_DOWNSTREAM ,self.video_blocked,self)
        
    def unblock_videomixer_src_pad(self):
        videomixer = self.element_list["videomixer"]
        pad = videomixer.get_static_pad("src")
        pad.remove_probe(self.videosink_pad_id)
        
    def unblock_audioomixer_src_pad(self):
        adder = self.element_list["adder"]
        pad = adder.get_static_pad("src")
        pad.remove_probe(self.audiosink_pad_id)
        
    def audio_blocked(self,pad,info,user_data):
        print("audio blocked")
    
    def video_blocked(self,pad,info,user_data):
        print("video blocked")
            
        