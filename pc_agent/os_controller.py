import subprocess
import os
from openrgb import OpenRGBClient
import time

TV = "GSM84C5"
MONITOR = "SAM711A"

class OSController():
    
    #to-do chech if screen mode numbers work as expected, if not change to DisplaySwitch.exe /internal /external /clone /extend
    
    def __init__(self, screen_mode = 'both', apps = None, rgb = None):
        self.screen_mode = screen_mode
        self.apps = apps or []
        self.rgb = rgb
        self.mmt = 'C:/Dev/Python-remote-app/pc_agent/Multimonitortool/MultiMonitorTool.exe'
    
    def screen_management(self, screen_mode):
        self.screen_mode = screen_mode
        if screen_mode == 'tv':
            subprocess.run([self.mmt, '/enable', TV], check=True)
            subprocess.run([self.mmt, '/SetPrimary', TV], check=True)
            subprocess.run([self.mmt, '/disable', MONITOR], check=True)
        elif screen_mode == 'both':
            subprocess.run([self.mmt, '/enable', MONITOR], check=True)
            subprocess.run([self.mmt, '/enable', TV], check=True)
            subprocess.run([self.mmt, '/SetPrimary', MONITOR], check=True)
        else:
            print(f'Unknown screen mode: {screen_mode!r} | file: {__file__}')
            return
        time.sleep(2)
    
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
    