import pygame
from sys import exit
from random import randint


class ShooterGame:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        
        # Display settings --------------------------------------------------------
        self.window_size = (1000, 800)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption('Shoot the targets!')
        self.bg_color = (120, 120, 100) # Temporary
        self.clock = pygame.time.Clock()

        # Cursor:
        self.cursor_visible = pygame.mouse.set_visible(False)
        self.reticle = pygame.image.load('resources/images/reticle.png').convert_alpha()
        
        # Target:
        self.target = pygame.image.load('resources/images/target.png').convert_alpha()
        
        self.run_game()


    def run_game(self):
        # Font:
        self.font = pygame.font.Font('resources/fonts/arcadeclassic.ttf', 35)
        self.game_over_font = pygame.font.Font('resources/fonts/arcadeclassic.ttf', 60)
            
        # Score and tries values:
        self.init_score = 0
        self.init_tries = 3
        
        self.target_pos = [-50, 400]

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

            self.target_rect = self.target.get_rect(center=self.target_pos)
            
            # Font Related.            
            self.score_mssg = self.font.render(f'Score {self.init_score}', True, 'Black')
            self.score_rect = self.score_mssg.get_rect(topleft=(5, 0))
            self.chances_mssg = self.font.render(f'Tries {self.init_tries}', True, 'Black')
            self.chances_rect = self.chances_mssg.get_rect(topright=(995, 0))

            # Updating surfaces on screen.
            self.screen.fill((self.bg_color))
            self.screen.blit(self.score_mssg, self.score_rect)
            self.screen.blit(self.chances_mssg, self.chances_rect)
            
            # Target
            self.screen.blit(self.target, self.target_rect)
            # Cursor
            self.reticle_rect = self.reticle.get_rect(center=pygame.mouse.get_pos())
            self.screen.blit(self.reticle, self.reticle_rect)



# ===================================================================================
if __name__ == '__main__':
    game = ShooterGame()