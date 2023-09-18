import os
import pygame
cwd = os.getcwd()


class Theme:
    class Color:
        def __init__(self, name, hexcode, rgb):
            self.name = name
            self.hexcode = hexcode
            self.rgb = rgb

    class Button:  # text_name ex: Load Game, var_name ex: loadgame
        def __init__(self, text, var_name, x, y):
            self.text = text
            self.var_name = var_name
            self.x_coord = x
            self.y_coord = y
            self.coord = (x, y)
            self.area = (x, y, x + 468, y + 88)

            self.default = pygame.image.load(f'{cwd}/Graphics/if_button_{var_name}.png')
            self.clicked = pygame.image.load(f'{cwd}/Graphics/if_button_{var_name}_clicked.png')

    class Icon:
        def __init__(self, name, x, y):
            self.name = name
            self.x_coord = x
            self.y_coord = y
            self.coord = (x, y)
            self.area = (x, y, x + 88, y + 88)

            self.default = pygame.image.load(f'{cwd}/Graphics/if_icon_{name}.png')
            self.clicked = pygame.image.load(f'{cwd}/Graphics/if_icon_{name}_clicked.png')

    class Title:  # pos options: 'left', 'center', 'right', or 'custom #' width and height in pixels
        def __init__(self, text, var_name, x_pos, y, width, height):
            self.text = text
            self.var_name = var_name
            self.y = y

            if x_pos == 'left':
                self.x = 60
            elif x_pos == 'center':
                self.x = 400 - (width / 2)
            elif x_pos == 'right':
                self.x = 740 - width
            else:
                self.x = x_pos

            self.area = (self.x, y, self.x + width, y + height)
            self.coord = (self.x, y)
            self.default = pygame.image.load(f'{cwd}/Graphics/if_title_{var_name}.png')

    class Text:
        def __init__(self, text, var_name, x_pos, y, width, height):
            self.text = text
            self.var_name = var_name
            self.y = y

            if x_pos == 'left':
                self.x = 60
            elif x_pos == 'center':
                self.x = 400 - (width / 2)
            elif x_pos == 'right':
                self.x = 740 - width
            else:
                self.x = x_pos

            self.area = (self.x, y, self.x + width, y + height)
            self.coord = (self.x, y)
            self.white = pygame.image.load(f'{cwd}/Graphics/if_text_{var_name}_white.png')
            self.black = pygame.image.load(f'{cwd}/Graphics/if_text_{var_name}_black.png')

    """INITIATE COLORS"""
    seagreen = Color("seagreen", "077565", (7, 117, 101))
    yellow = Color("yellow", "d9de42", (217, 222, 66))
    purple = Color("purple", "b873e3", (184, 115, 227))
    orange = Color("orange", "ff6b1b", (255, 107, 27))
    midnight = Color("midnight", "541ab7", (84, 26, 183))
    coral = Color("coral", "eb3553", (235, 53, 83))
    pink = Color("pink", "ffcad3", (255, 202, 211))
    aqua = Color("aqua", "24bace", (36, 186, 206))

    """INITIATE BUTTONS"""
    button_newgame = Button('New Game', 'newgame', 166, 400)
    button_loadgame = Button('Load Game', 'loadgame', 166, 480)
    button_savegame = Button('Save Game', 'savegame', 166, 560)
    button_quit = Button('Quit', 'quit', 166, 640)

    """INITIATE ICONS"""
    icon_return = Icon('return', 672, 40)

    """INITIATE TITLES"""
    title_mainmenu = Title('Main Menu', 'mainmenu', 'center', 270, 584, 96)

    """INITIATE TEXTS"""
    text_copyright = Text('Copyright', 'copyright', 'center', 760, 416, 24)

