from dispatcher import ModeMapper
from os_controller import OSController

controller = OSController()
disp = ModeMapper()

while True:
    mode = input('Please enter desired mode or help for available modes: ')
    
    if mode == 'help':
        print(f"Available modes: {disp.available_modes()}")
    elif mode in disp.available_modes():
        config = disp.get_config(mode)
        controller.screen_management(config[0])
        controller.open_apps(config[1])
        controller.rgb_mode(config[2])
        
    else:
        print('Please enter a valid argument.')