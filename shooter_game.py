import pygame
# Module for system-level operations and interactions.
import sys

from settings import Settings

class Target:
    def __init__(self):
        self.settings = Settings()
        self.size = self.settings.target_size
        self.color = self.settings.target_color

    def show_on_screen(self):
        pygame.draw.rect(self.settings.screen, self.settings.target_color, ((600, 400), self.size))
        


class ShooterGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Shooter Game')

        self.settings = Settings()
        self.target = Target()
        self.screen = self.settings.screen
        self.fps_limit = pygame.time.Clock()
        self.is_running = True
        
        # Cursor not visible.
        self.settings.cursor_visible 

    def exit_events(self):
        # Checks if Esc is pressed and exit the game.
        for event in pygame.event.get():
            # User clicks the x of the window.
            if event.type == pygame.QUIT:
                self.is_running = False
            elif (event.type == pygame.KEYDOWN 
                and event.key == pygame.K_ESCAPE):
                self.is_running = False

    def run_game(self): 
        while self.is_running:
            self.screen
            # Gets the updated position of the cursor and its constant size. 
            self.cursor = pygame.mouse.get_pos(), self.settings.cursor_size
            
            # Draw a target on screen
            self.target.show_on_screen()
            # Draw the cursor on screen.
            pygame.draw.rect(self.screen, self.settings.cursor_color, self.cursor)

            pygame.display.flip()
            self.fps_limit.tick(self.settings.fps)
            self.screen.fill(self.settings.bg_color)

            self.exit_events()    
        
        pygame.quit()
        sys.exit()


            
adventure_game = ShooterGame()
adventure_game.run_game()