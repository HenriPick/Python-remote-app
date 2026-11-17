class ModeMapper():
    
    def __init__(self):
        self.modes = {
            'cinema' : ['tv', None, 'dark'],
            'game' : ['tv', ["steam://open/bigpicture"], 'cyanred'],
            'work' : ['both', None, 'cyanred']
            }
    
    def available_modes(self):
        return list(self.modes)
    
    def get_config(self, mode):
        try:
            return self.modes[mode.lower()]    
        except KeyError:
            return 'unidentified_mode'
