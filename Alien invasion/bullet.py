import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Bullet fired from the ship"""
    
    def __init__(self, ai_game):
        """creat bullet obj"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # Create a bullet rect at (0, 0) and then set correct pos
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # Store the bullet's pos as a float
        self.y = float(self.rect.y)
        
    def update(self):
        """move the bullets up the screen"""
        # Update the exact pos of the bullet
        self.y -= self.settings.bullet_speed
        
        # Update rect pos
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)