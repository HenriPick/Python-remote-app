class ModeMapper():
    
    def __init__(self):
        self.modes = {
            'cinema' : [1, None, 'dark'],
            'game' : [1, ["steam://open/bigpicture"], 'cyan'],
            'work' : [3, None, 'cyan']
            }
    
    def available_modes(self):
        return list(self.modes)
    
    def get_config(self, mode):
        try:
            return self.modes[mode.lower()]    
        except KeyError:
            return 'unidentified_mode'
