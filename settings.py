import pygame
from random import randint

class Settings:
    def __init__(self):
        
        # Screen settings.
        self.window_width = 1200
        self.window_height = 800
        self.window_size = (self.window_width, self.window_height)
        self.screen = pygame.display.set_mode((self.window_size))
        self.bg_color = (140, 140, 80)
        self.fps = 60 # Frames per second.


        # Target settings.
        self.target_pos_x = 1250
        self.target_pos_y = 400
        self.target_speed = 4
        