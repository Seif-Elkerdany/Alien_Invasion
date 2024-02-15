class Settings:
    """A class to store all settings for alien invasion"""
    
    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        
        # Alien settings
        self.fleet_drop_speed = 10
        
        # How quickly the game speed up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
        
        self.initialization_dynamic_settings()
        
    def initialization_dynamic_settings(self):
        # Bullet settings
        self.bullet_speed = 2.5
        
        # Ship settings
        self.ship_speed = 1.5
        
        # Alien settings.
        self.alien_speed = 1.0
        self.alien_points = 50
        
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        # Scoring settings
        self.alien_points = int(self.alien_points * self.score_scale)