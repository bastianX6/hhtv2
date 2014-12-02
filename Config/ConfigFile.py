'''
Created on 08-03-2014

@author: bastian
'''

import json,sys
from pprint import pprint


class SourceClass(object):
    '''
    classdocs
    '''
    
    def __init__(self,the_id,have_video,have_audio,is_image=False,textoverlay=False):
        '''
        Constructor
        '''
        
        self.id = the_id
        self.general_settings = {}
        self.audio_settings = {}
        self.video_settings = {}
        self.textoverlay_settings = {}
        self.source_settings = {}
        
        self.general_settings["have_audio"] = have_audio
        self.general_settings["have_video"] = have_video
        self.general_settings["is_image"] = is_image  
        self.general_settings["textoverlay"] = textoverlay      
        
    def set_video_properties(self,width,height,xpos,ypos,zorder,alpha):
        self.video_settings["width"] = width
        self.video_settings["height"] = height
        self.video_settings["xpos"] = xpos
        self.video_settings["ypos"] = ypos
        self.video_settings["zorder"] = zorder
        self.video_settings["alpha"] = alpha
        
    def set_textoverlay_properties(self,text,xpos,ypos,font_settings):
        self.textoverlay_settings["text"] = text
        self.textoverlay_settings["xpos"] = xpos
        self.textoverlay_settings["ypos"] = ypos
        self.textoverlay_settings["font_settings"] = font_settings
    
    
    def set_source_properties(self,source_type,device,device_name):
        self.source_settings["source_type"] = source_type
        self.source_settings["device"] = device
        self.source_settings["device_name"] = device_name
        
    def set_audio_properties(self,volume):
        self.audio_settings["volume"] = volume
    
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)    

class ConfigFile(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        self.source_list = {}

    def add_source(self,source):
        self.source_list[source.id] = source
        
    def remove_source(self,source):
        self.source_list.pop(source.id)
        
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
    
    def read_from_file(self,file_path):
        
        
        json_data = open(file_path)
        data = json.load(json_data)
        #pprint(data)
        json_data.close()
        
        #print("data: ",data)
        #print("source_list",data["source_list"])
        
        for key,value in data["source_list"].items():
            #print("value: ",value)
            general_settings = value["general_settings"]
            have_video = general_settings["have_video"]
            have_audio = general_settings["have_audio"]
            is_image = general_settings["is_image"]
            textoverlay = general_settings["textoverlay"]
            
            source_class = SourceClass(key,have_video,have_audio,is_image,textoverlay)
            source_class.audio_settings = value["audio_settings"]
            source_class.video_settings = value["video_settings"]
            source_class.textoverlay_settings = value["textoverlay_settings"]
            source_class.source_settings = value["source_settings"]
            
            self.add_source(source_class)
        
        return True
        
        
    def write_to_file(self,file_path):
        try:
            
            json_data = open(file_path,"w")
            json_data.write(self.to_JSON())
            json_data.close()
            return True
        except :
            return False
        
        