import pygame 
import random
from bullet import Bullet

class AlienBullet(Bullet): #alien bullet - inherits from Bullet class
    
    def __init__(self,x,y):
        super().__init__(x,y)
        self.image = pygame.Surface((10,10), pygame.SRCALPHA)
        pygame.draw.circle(self.image,(165,55,253),(5,5),5) #color purple, 5 x 5, with a 5 radius
        self.get_rect = self.image.get_rect(middlebottom=(x,y))
    
    def update(self, ship_object):
        pygame.sprite.spritecollide(self,ship_object,True) #if alienbullet collides with ship_object == true
        self.rect.y += 10 #moves bullet downwards
        if self.rect.y == 810: #if bullet goes 10px pass 800
            self.kill() #stop instance and delete it

    def shoot_alien_bullet(self):
        can_shoot = random.randint(1,5) #random number between 1 and 5
        if can_shoot == 2: #random shoot number will be == 2
            alien_bullet = AlienBullet(self.rect.x, self.rect.y) #create bullet at the current position of the alien's self
            return alien_bullet



class Alien(pygame.sprite.Sprite): #alien class

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #initializes inherited methods from pygame.sprite.sprite
        self._green_alien = pygame.image.load("assets/GreenAlien.png") #green alien image
        self._red_alien = pygame.image.load("assets/RedAlien.png") #red alien image
        self._yellow_alien = pygame.image.load("assets/YellowAlien.png") #yellow alien image
        self._spawnable_aliens = [self._green_alien,self._red_alien,self._yellow_alien] #list of the images/aliens
        self.image = self._spawnable_aliens[random.randint(0,2)] #randomly selects an alien from self._spawnable_aliens
        self.rect = self.image.get_rect(center=(20,20)) #20 for x, 20 for y
        self._going_right = True #going_right
    
    def update(self):
        if self._going_right == True:
            self.rect.x += 2 #go right
            if self.rect.x == 760: #x max is 800
                self.rect.y += 50 #y max is 800
                self._going_right == False #flips going_right to false
        else:
            self.rect.x -=2 #go left
            if self.rect.x == 10: #x max is 800
                self.rect.y += 50 #x max is 800
                self._going_right == True #flips going_right back to true