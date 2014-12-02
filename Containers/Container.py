'''
Created on 22-08-2013

@author: bastian
'''
import sys, uuid
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst

class Container(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        self.element_list= dict()
        self.element_tuple_list = []
        self.the_bin = Gst.Bin()
        self.name= str(uuid.uuid4())
                
    def add_element(self,factory_name,element_name):
        element = Gst.ElementFactory.make(factory_name,None)
        self.element_list[element_name] = element
            
        #Add to bin
        self.the_bin.add(element)
        return True
        
    def remove_element(self,element_name):
        element = self.element_list[element_name]
        self.element_list.pop(element_name)
            
        self.destroy_element_links(element)
            
        #Remove from bin
        self.the_bin.remove(element)
        
    def link_elements(self,source_name,dest_name):
        source = self.element_list[source_name]
        dest = self.element_list[dest_name]
        source.link(dest)
            
        #Add to tuple list
        the_tuple = (source,dest)
        self.element_tuple_list.append(the_tuple)
        
    def unlink_elements(self,source_name,dest_name):
        source = self.element_list[source_name]
        dest = self.element_list[dest_name]
        source.unlink(dest)
            
        #Remove tuple
        the_tuple = (source,dest)
        self.element_tuple_list.remove(the_tuple)
            
        
    def destroy_element_links(self,element):
        for t in self.element_tuple_list:
            source = t[0]
            dest = t[1]
                
            if source == element or dest == element:
                source.unlink(dest)
                self.element_tuple_list.remove(t)
        
    def unlink_all_elements(self):
        for t in self.element_tuple_list:
            source = t[0]
            dest = t[1]
            source.unlink(dest)
            self.element_tuple_list.remove(t)
        
        
    def set_property(self,element_name,the_property,value):
        element = self.element_list[element_name]
        element.set_property(the_property,value)
        
    def set_caps(self,element_name,caps_string):
        element = self.element_list[element_name]
        element.set_property("caps",Gst.Caps.from_string(caps_string))
            
    
    #source_pad_is_request == false --> static pad
    #dest_pad_is_request == false --> static pad    
    
    def link_pads(self,source_name,source_pad_name,dest_name,dest_pad_name,source_pad_is_request,dest_pad_is_request):
        #get elements
        source = self.element_list[source_name]
        dest = self.element_list[dest_name]
            
            
        #get source pad
        source_pad = self.get_pad(source, source_pad_name,source_pad_is_request)
            
        #get dest pad
        dest_pad = self.get_pad(dest, dest_pad_name,dest_pad_is_request)
                
        source_pad.link(dest_pad)
        
        
    def link_containers(self,source_pad_name,dest_container,dest_pad_name):
        source_pad = self.get_bin_pad(source_pad_name)
        dest_pad = dest_container.get_bin_pad(dest_pad_name)
        
        '''print("---------------------")
        print("Container.link_containers()\n")
        print("source pad: "+str(source_pad))
        print("dest pad: "+str(dest_pad))'''
        
        linked = source_pad.link(dest_pad)
        
        #print("linked: ",linked)
    #-----------------------------------------------------------
    
    def get_pad(self,element,pad_name,is_request_pad):
        if is_request_pad:
            return self.__get_request_pad(element, pad_name)
            
        else:
            return self.__get_static_pad(element, pad_name)
        
    def __get_static_pad(self,element,pad_name):
        pad = element.get_static_pad(pad_name)
        return pad
    
    def __get_request_pad(self,element,pad_name):
        pad = element.get_request_pad(pad_name)
        return pad
    
    def remove_pad(self,element_name,pad):
        element = self.element_list[element_name]
        element.remove_pad(pad)
    
    #-----------------------------------------------------------
    
    
    def get_bin_pad(self,pad_name,is_request_pad = False):
        return self.get_pad(self.the_bin, pad_name,is_request_pad)
        
        
    def create_ghost_pad(self,element_name,pad_name,is_request_pad,ghost_pad_name):
        element = self.element_list[element_name]
        pad = self.get_pad(element, pad_name, is_request_pad)
            
        ghost_pad = Gst.GhostPad.new(ghost_pad_name,pad)
        ghost_pad.set_active(True)
        self.the_bin.add_pad(ghost_pad)
        
    def create_ghost_pad_2(self,pad,ghost_pad_name):
        ghost_pad = Gst.GhostPad.new(ghost_pad_name,pad)
        ghost_pad.set_active(True)
        self.the_bin.add_pad(ghost_pad)
    
    def remove_ghost_pad(self,pad_name):
        pad = self.get_bin_pad(pad_name)
        
        if pad.peer:
            self.the_bin.remove_pad(pad.peer)
            
        if pad.peer:
            self.the_bin.remove_pad(pad.pad)
            
            
        self.the_bin.remove_pad(pad)
        
    def remove_ghost_pad2(self,pad):
        if pad.peer:
            self.the_bin.remove_pad(pad.peer)
            
        if pad.peer:
            self.the_bin.remove_pad(pad.pad)
        self.the_bin.remove_pad(pad)
    
    def set_state_playing(self):
        self.the_bin.set_state(Gst.State.PLAYING)
        
        
    def set_state_null(self):
        self.the_bin.set_state(Gst.State.NULL)
        
    def parse_state(self,gst_state):
        
        state = ""
        
        if gst_state == Gst.State.VOID_PENDING:
            state = "VOID_PENDING"
            
        elif gst_state == Gst.State.NULL:
            state = "NULL"
            
        elif gst_state == Gst.State.READY:
            state = "READY"
            
        elif gst_state == Gst.State.PAUSED:
            state = "PAUSED"
            
        elif gst_state == Gst.State.PLAYING:
            state = "PLAYING"
            
        return state
        
        