import pygame
from random import randint

class Settings:
    def __init__(self):
        
        # Screen settings.
        self.window_width = 1200
        self.window_height = 800
        self.window_size = (self.window_width, self.window_height)
        self.screen = pygame.display.set_mode((self.window_size))
        self.bg_color = (100, 100, 150)
        self.fps = 60 # Frames per second.

        # Cursor settings.
        self.cursor_visible = False

        # Target settings.
        self.target_size = (20, 20)
        self.target_color = (255, 0, 0)
        self.target_pos_x = randint(10, self.window_width - 10)
        self.target_pos_y = randint(50, self.window_height - 10)
        self.target_pos = self.target_pos_x, self.target_pos_y
        