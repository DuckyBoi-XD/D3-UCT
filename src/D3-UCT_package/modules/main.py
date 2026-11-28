import pygame
import platform
import random
import json
import os
import math
from pathlib import Path
from pygame.locals import *

import setting
import crypto
from scenes import index

class game_variable:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((setting.displaywidth, setting.displayheight), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = False

GV = game_variable()

class game_objects:
    def __init__(self):
        pass
    def on_init(self):
        pass
GO = game_objects()


class pygame_function:
    def __init__(self):
        self.FPS = pygame.time.Clock()
        pygame.display.set_caption("D3 - UCT")
        GV._running = False

    def on_init(self):
        GV._running = True

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GV._running = False
        index.game_option_buttons_hover()

    def on_render(self):
        GV.display.fill(setting.table_colour)
        index.game_option_buttons(GV.display)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.on_init()
        while(GV._running):
            self.FPS.tick(setting.fps)
            self.event_handler()
            self.on_render()
        self.on_cleanup()

PF = pygame_function()

if __name__ == "__main__":
    PF.on_execute()