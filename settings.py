import pygame

class Settings:
    def __init__(self):
        
        # Screen settings.
        self.window_size = (1200, 800)
        self.screen = pygame.display.set_mode((self.window_size))
        self.bg_color = (100, 100, 150)
        self.fps = 60 # Frames per second.

        # Cursor settings.
        self.cursor_visible = pygame.mouse.set_visible(False)
        self.cursor_size = (5, 5)
        self.cursor_color = (255, 255, 255)

        # Target settings.
        self.target_size = (20, 20)
        self.target_color = (255, 0, 0)
        