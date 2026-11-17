class ModeMapper():
    
    def __init__(self):
        self.modes = {
            'cinema' : [4, None, 'dark'],
            'game' : [4, ["steam://open/bigpicture"], 'cyanred'],
            'work' : [3, None, 'cyanred']
            }
    
    def available_modes(self):
        return list(self.modes)
    
    def get_config(self, mode):
        try:
            return self.modes[mode.lower()]    
        except KeyError:
            return 'unidentified_mode'
