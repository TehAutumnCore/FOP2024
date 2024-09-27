import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self) #similar to using super()
        self.image = pygame.Surface((10,10), pygame.SRCALPHA)
        pygame.draw.circle(self.image,(255,0,0), (5,5), 5) #Image/shape -> Creates color,and shape of projectile
        self.rect = self.image.get_rect(midbottom=(x,y))
        self._shoot_sound = pygame.mixer.music.load("sounds/shoot1.mp3")
        pygame.mixer.music.play()

    def update(self,alien_group):
        self.rect.y -= 20
        pygame.sprite.spritecollide(self,alien_group) #checks 2 sprite groups to see if they collided (bullet(self), alien group)
        if self.rect.y == -50: #if bullet reaches 50px out of border
            self.kill() #sprite method - stops the instance and deletes it