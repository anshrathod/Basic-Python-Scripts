# import phue library
from phue import Bridge
import time

# add ip address of your router
ip_address = ''

#establishing connection
connection = Bridge(ip_address)
list_of_lights = connection.lights


#Switch on all lights
def switch_on():
    for light in list_of_lights:
        light.on  = True
        light.hue = 15000
        light.saturation = 120

#Switch of all lights
def switch_of():
    for light in list_of_lights:
        light.on = False


#Toggle specific light
def toggle_light(name):
    light = connection.get_light(name)
    if light.on:
        light.on = True
    else:
        light.on = False


#Set Timer to on or off
def setTime(hour,minute,On):
    T = time.localtime()
    curr_hour,curr_minute = T[3],T[4]

    if curr_hour >= hour and curr_minute:
        if On:
            for light in list_of_lights:
                light.on = False
        else:
            for light in list_of_lights:
                light.on = False


#Dim light according to the time of day
def naturalLight():
    T = time.localtime()
    curr_hour = T[3]

    if curr_hour >= 6 and curr_hour <= 18:
        for light in list_of_lights:
            light.on  = True
            light.hue = 15000
            light.saturation = 120
    else:
        for light in list_of_lights:
            light.on  = True
            light.hue = 150
            light.saturation = 50
