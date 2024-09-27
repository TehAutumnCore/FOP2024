import pygame

class SpaceShip(pygame.sprite.Sprite):

    def __init__(self,image,x,y):
        pygame.sprite.Sprite.__init__(self)
        self._space_space_surface = pygame.image.load(image) #will load its image into its surface
        self.rect = self._space_space_surface.get_rect(midbottom=(x,y))#spaceship will start in the middle at the bottom located at x,y
    
    def get_position(self):
        return (self.rect.x, self.rect.y)

    def get_surface(self):
        return self._space_space_surface

    def move(self,direction): #movement
        if direction == "d":
            if self.rect.x <= 700: #sets a limit/border for the right side
                self.rect.x += 5
        elif direction == "a":
            if self.rect.x >= 20: #sets a limit/border for the left side
                self.rect.x -= 5
        elif direction == "s":
            if self.rect.y <= 700: #sets a limit/border for the bottom side
                self.rect.y += 5
        elif direction == "w":
            if self.rect.y >= 300: #sets a limit/border for the top side
                self.rect.y -= 5
