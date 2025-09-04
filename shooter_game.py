import pygame
from sys import exit
from random import randint


class ShooterGame:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        
        # Display settings --------------------------------------------------------
        self.window_size = (1500, 800)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption('Shoot the targets!')
        self.bg_color = (120, 120, 100) # Temporary
        self.clock = pygame.time.Clock()

        # Cursor:
        self.cursor_visible = pygame.mouse.set_visible(False)
        self.reticle_surf = pygame.image.load(Reticle().sprite).convert_alpha()
        self.reticle_rescaled = pygame.transform.scale_by(self.reticle_surf, .07)
        
        # Target:
        self.target_surf = pygame.image.load(Target().sprite).convert_alpha()
        self.target_rescaled = pygame.transform.scale_by(self.target_surf, .10)
        
        # Font:
        self.font = pygame.font.Font('resources/fonts/arcadeclassic.ttf', 35)
        self.game_over_font = pygame.font.Font('resources/fonts/arcadeclassic.ttf', 60)

        # Score and tries values:
        self.init_score = 0
        self.init_tries = 3
        
        # Init target pos.
        self.target_pos = [-50, 400]
        
        self.run_game()


    def run_game(self):
        while True:
            # Events -----------------------------------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # Collision and mouse clicks
                if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                    if self.reticle_rect.colliderect(self.target_rect):
                        self.target_pos[0] = -50
                        self.target_pos[1] = randint(50, 700)
                        self.init_score += 1
            
            # Main Logic ---------------------------------------------------------
            if self.init_score == 0:
                self.target_pos[0] +=  .5
            elif self.init_score > 0:
                self.target_pos[0] += self.init_score
            
            if self.target_pos[0] > 1050:
                self.target_pos[1] = randint(80, 750)
                self.init_tries -= 1
                self.target_pos[0] = -50
            
            elif self.init_tries <= 0:
                print('Game Over!')
                break
            
            # Update Section -----------------------------------------------------
            pygame.display.update()
            self.clock.tick(60)

            self.target_rect = self.target_rescaled.get_rect(center=self.target_pos)
            
            # Font Related.            
            self.score_mssg = self.font.render(f'Score {self.init_score}', True, 'Black')
            # Improve font position based on window size - - - - - !
            self.score_rect = self.score_mssg.get_rect(topleft=(5, 0))
            self.chances_mssg = self.font.render(f'Tries {self.init_tries}', True, 'Black')
            # Improve font position based on window size - - - - - !
            self.chances_rect = self.chances_mssg.get_rect(topright=(995, 0))

            # Updating surfaces on screen.
            self.screen.fill((self.bg_color))
            self.screen.blit(self.score_mssg, self.score_rect)
            self.screen.blit(self.chances_mssg, self.chances_rect)
            
            # Target
            self.screen.blit(self.target_rescaled, self.target_rect)
            # Cursor
            self.reticle_rect = self.reticle_rescaled.get_rect(center=pygame.mouse.get_pos())
            self.screen.blit(self.reticle_rescaled, self.reticle_rect)


# -----------------------------------------------------------------------------
class Reticle:
    def __init__(self):
        self.sprite = 'resources/sprites/reticle.png'


# --------------------------------------------------------------------------------
class Target:
    def __init__(self):
        self.sprite = 'resources/sprites/round_target.png'


# ===================================================================================
if __name__ == '__main__':
    game = ShooterGame()
