import subprocess
import os
from openrgb import OpenRGBClient

class OSController():
    
    #to-do chech if screen mode numbers work as expected, if not change to DisplaySwitch.exe /internal /external /clone /extend
    
    def __init__(self, screen_mode = 3, apps = None, rgb = None):
        self.screen_mode = screen_mode
        self.apps = apps or []
        self.rgb = rgb
    
    def screen_management(self, screen_mode):
        self.screen_mode = screen_mode
        subprocess.Popen(['DisplaySwitch.exe', str(screen_mode)])
    
    
    
    #to-do cange signal rgb to openrgb and add support for prism
        
    def rgb_mode(self, rgb):
        self.rgb = rgb
        client = OpenRGBClient()
        client.load_profile(self.rgb)
        #os.startfile(f'Prism_{rgb}.exe')
  
    def open_apps(self, apps):
        if not apps:
            return
        self.apps = apps
        for i in apps:
            os.startfile(i)
    