'''
Created on 23-08-2013

@author: bastian
'''

import gi,subprocess
gi.require_version('Gst', '1.0')
from gi.repository import Gst,GstPbutils


def uri_discoverer(the_uri):
    '''
    returns (have_audio,have_video) tuple 
    '''
    discoverer = GstPbutils.Discoverer()
    discoverer_info = discoverer.discover_uri(the_uri)
    stream_list = discoverer_info.get_stream_list()
    
    have_audio = False
    have_video = False
    is_image = False
    
    for stream in stream_list:
        caps = stream.get_caps().to_string()
        print("caps")
        
        if caps.startswith('audio/'):
            have_audio = True
        
        elif caps.startswith('video/'):
            have_video = True            
        
        elif caps.startswith('image/'):
            is_image = True
            have_video = True
            
            
    return (have_audio,have_video,is_image)

def get_v4l2_device_list():
    
    #http://stackoverflow.com/questions/2502833/python-store-output-of-subprocess-popen-call-in-a-string
    command = ["v4l2-ctl","--list-devices"]
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    out, err = p.communicate()
    
    the_out = str(out,"utf-8")
    the_out = the_out.replace("\t", "")
    split_devices = the_out.split("\n")
    
    
    list_devices = []
    
    for x in range(0,len(split_devices),3):
        if split_devices[x] == "":
            break
        
        device = (split_devices[x],split_devices[x+1])
        
        list_devices.append(device)
        
    return list_devices
        

def get_pulse_device_list():
    #http://stackoverflow.com/questions/2502833/python-store-output-of-subprocess-popen-call-in-a-string
    
    #get human names
    command = ["pactl","list","sources"]
    
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    out, err = p.communicate()
    p1_out = str(out,"utf-8")
    
    p1_out = p1_out.replace("\t", "")
    split_list = p1_out.rsplit("\n")
    
    list_temp = []
    list_devices_name = []
    
    for x in split_list:
        if x.startswith("device.description"):
            list_temp.append(x)
            
    for x in list_temp:
        aux = x.split(" = ")
        device = aux[1].replace("\"","")
        list_devices_name.append(device)
        
    #print("device human names: "+str(list_devices_name))
    
    #get device names
    
    command2 = ["pactl","list","short","sources"]
    p = subprocess.Popen(command2, stdout=subprocess.PIPE)
    out, err = p.communicate()
    
    p2_out = str(out,"utf-8")
    
    split_list = p2_out.rsplit("\n")
    list_devices = []
    
    for x in split_list:
        if x:
            y = x.split("\t")
            list_devices.append(y[1])
            
    #print("device names: "+str(list_devices))
            
    #create list of tuples (device human name, device name)
    tuple_list = []
    for x in range(0,len(list_devices_name)):
        the_tuple = (list_devices_name[x],list_devices[x])
        tuple_list.append(the_tuple)
    
    
    
    #print("tuple_list: "+str(tuple_list))    
    return tuple_list

def get_x11_windows_id_list():
     
    #http://stackoverflow.com/questions/2502833/python-store-output-of-subprocess-popen-call-in-a-string
    command = ["wmctrl","-l"]
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    out, err = p.communicate()
    
    the_out = str(out,"utf-8")
    the_out = the_out.replace("\t", "")
    split_list = the_out.split("\n")
    
    
    list_windows_id = []
    tuple_temp = ("Escritorio",0)
    list_windows_id.append(tuple_temp)
    
    for x in split_list:
        win_element = x.split(" ")
        win_id = win_element[0]
        nombre = ""
        
        if len(win_element) <=4:
            continue
        
        for y in range(4,len(win_element)):
            nombre += " " + win_element[y]
            
        the_tuple = (nombre,win_id)
        list_windows_id.append(the_tuple)
        
    return list_windows_id