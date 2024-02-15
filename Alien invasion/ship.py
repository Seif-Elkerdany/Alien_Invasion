import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship"""
    
    def __init__(self,ai_game):
        """Initialize the ship and set its starting pos"""
        super().__init__()
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        # Load the ship img and get its rect 
        self.image = pygame.image.load(r"images\ship.bmp")
        self.rect = self.image.get_rect()
        
        # Start with a ship that's not moving 
        self.moving_right = False
        self.moving_left = False
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a float for the ship's exact horizontal pos 
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        
    def update(self):
        """Update the ship's position based on movement flags"""
        # Update the ship's x value not thre rect 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update rect obj from self.x
        self.rect.x = self.x