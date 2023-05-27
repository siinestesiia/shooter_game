import pygame
# Module for system-level operations and interactions.
import sys

from settings import Settings


class Reticle:
    def __init__(self):
        self.cursor_settings = Settings()
        self.cursor_visible = pygame.mouse.set_visible(False) 
        # Converting images is needed to make pygame work more easily.
        self.reticle = pygame.image.load('resources/images/reticle.png').convert_alpha()
    
    def cursor_on_screen(self):
        # gets the reticle rectangle to better handle its position.
        self.reticle_rect = self.reticle.get_rect(center = (pygame.mouse.get_pos()))
        # Draw the reticle on screen.
        self.cursor_settings.screen.blit(self.reticle, self.reticle_rect)
        return self.reticle_rect
            

class Target:
    def __init__(self):
        self.targ_settings = Settings()
        self.target = pygame.image.load('resources/images/target.png').convert_alpha()
        self.pos_x = self.targ_settings.target_pos_x
        self.pos_y = self.targ_settings.target_pos_y
        self.speed = self.targ_settings.target_speed

    def target_on_screen(self):
        self.target_rect = self.target.get_rect(center = (self.pos_x, self.pos_y))
        
        self.pos_x -= self.speed 

        if self.pos_x < -100:
            self.pos_x = self.targ_settings.target_pos_x

        self.targ_settings.screen.blit(self.target, self.target_rect)
        return self.target_rect

class ShooterGame:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('Shooter Game')

        self.settings = Settings()
        self.target = Target()
        self.cursor = Reticle()
        self.screen = self.settings.screen
        self.fps_limit = pygame.time.Clock()
        self.is_running = True
        self.points_gained = 0
        
        # sfx and music.
        self.shot_sound_path = 'resources/sfx_and_music/gun_shot.mp3'
        self.shot_sound = pygame.mixer.Sound(self.shot_sound_path)


    def check_events(self):
        self.point = 0
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
                # Checks if the target has been shot.
                if (self.cursor.cursor_on_screen().colliderect
                    (self.target.target_on_screen())):
                    self.point += 1
                else:
                    pass
            elif event.type == pygame.MOUSEBUTTONUP:
                pass 
        return self.point 

    def scoring(self, score):
        self.points_gained += int(score)
        # Defines the type of font and its size.
        self.font = pygame.font.Font('resources/images/comicz.ttf', 40)
        # Defines the text, the antialiasing and its color.
        self.points = self.font.render(f'Score: {self.points_gained}', True, 'Black')
        self.settings.screen.blit(self.points, (5, 5))

    def run_game(self): 
        while self.is_running:
            pygame.display.update()

            self.screen.fill(self.settings.bg_color)
            self.points = self.check_events()
            self.scoring(self.points)
            self.target.target_on_screen()
            self.cursor.cursor_on_screen()
            

            self.fps_limit.tick(self.settings.fps)

        
        pygame.quit()
        sys.exit()


            
shooter_game = ShooterGame()
shooter_game.run_game()