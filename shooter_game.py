import pygame
# Module for system-level operations and interactions.
import sys

from settings import Settings


class Cursor:
    def __init__(self):
        self.cursor_settings = Settings()
        self.reticle = pygame.image.load('images/reticle.png')
        self.arrow_visible = pygame.mouse.set_visible(self.cursor_settings.cursor_visible) 

    def cursor_on_screen(self):
        # Draw the reticle on screen.
        self.cursor_settings.screen.blit(self.reticle, (pygame.mouse.get_pos()))
            

class Target:
    def __init__(self):
        self.targ_settings = Settings()
        self.size = self.targ_settings.target_size
        self.color = self.targ_settings.target_color

    def target_on_screen(self):
        pygame.draw.rect(self.targ_settings.screen, self.color, 
                         ((self.targ_settings.target_pos), self.size))
        

class ShooterGame:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('Shooter Game')

        self.settings = Settings()
        self.target = Target()
        self.cursor = Cursor()
        self.screen = self.settings.screen
        self.fps_limit = pygame.time.Clock()
        self.is_running = True
        
        # sfx and music.
        self.shot_sound_path = 'sfx_and_music/gun_shot.mp3'
        self.shot_sound = pygame.mixer.Sound(self.shot_sound_path)


    def check_events(self):

        # Checks if Esc is pressed and exits the game.
        for event in pygame.event.get():
            # User clicks the x of the window.
            if event.type == pygame.QUIT:
                self.is_running = False
            elif (event.type == pygame.KEYDOWN 
                  and event.key == pygame.K_ESCAPE):
                self.is_running = False
            
            # Checks for mouse input.
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                self.shot_sound.play()
            elif event.type == pygame.MOUSEBUTTONUP:
                pass

    def scoring(self):
        self.score = 0
        # Defines the type of font and its size.
        self.font = pygame.font.Font('images/comicz.ttf', 40)
        # Defines the text, the antialiasing and its color.
        self.score = self.font.render(f'Score: {self.score}', True, 'Black')
        self.settings.screen.blit(self.score, (5, 5))

    def run_game(self): 
        while self.is_running:
            pygame.display.update()

            self.screen.fill(self.settings.bg_color)
            self.check_events()
            self.scoring()
            self.target.target_on_screen()
            self.cursor.cursor_on_screen()
            

            # pygame.display.flip()
            self.fps_limit.tick(self.settings.fps)

        
        pygame.quit()
        sys.exit()


            
shooter_game = ShooterGame()
shooter_game.run_game()