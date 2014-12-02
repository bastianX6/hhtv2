'''
Created on 22-07-2014

@author: usuario
'''

from enum import Enum


class PluginXV(Enum):
    '''
    classdocs
    '''
    xvimagesink = 1
    ximagesink = 2
    
class VideoFormat(object):
    
    I420 = "(string)I420"
    YUY2 = "(string)YUY2"
    AYUV = "(string)AYUV"
    
class Defaults(object):
    video_format = VideoFormat.I420
    backgroud_caps_name = "background_caps_container"
    

        