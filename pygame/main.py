import pygame #importing the library
import sys #manipulates stuff on desktop
from bullet import Bullet
from space_ship import SpaceShip
from alien import Alien
class Game:

    def __init__(self):

        #creates the main window
        pygame.init() #initializing the module
        self._display = pygame.display.set_mode((800,800)) #creates the window and sets its size
        self._clock = pygame.time.Clock() #creates a clock
        #line 15, mixer not initialized
        self._channels = pygame.mixer.set_num_channels(2) #like the radio, every channel only plays one song at a time, so multiple channels multiple sounds. Creates 2 channels
        self._background_music = pygame.mixer.Sound(file ="sounds/retro-background-music.mp3") #creates background music
        pygame.display.set_caption('Space Invaders') #allows us to change the text of the window
        pygame.mixer.Channel(0).play(self._background_music)

        #creates a surface - like creating a table
        self._space_surface = pygame.Surface((800,800)) #want the surface to be the full window

        #create spaceship
        self._space_ship = SpaceShip("assets/DurrrSpaceShip.png", 400, 800) #takes (image,x,y)
        self.ship_sprite_group = pygame.sprite.GroupSingle() #GroupSingle() being unique, only holds one thing
        self.ship_sprite_group.add(self._space_ship)

        # print(self._space_ship)

        #Create sprite groups - dictionary of all bullets and all aliens
        self._all_bullet = pygame.sprite.Group()
        self._all_aliens = pygame.sprite.Group()
        self._all_alien_bullets = pygame.sprite.Group()

        #Create timer for user events
        self._alien_spawn_event = pygame.USEREVENT + 1 #creating an event
        pygame.time.set_timer(self._alien_spawn_event, 1000) #timer isn't visible, uses the alien spawn timer events every 1000 milli seconds

        self._alien_shoot_event = pygame.USEREVENT + 1 #creates alien shoot event
        pygame.time.set_timer(self.alien_shoot_event, 1000) #timer for this event to occur every 1000ms ######

    def run(self): #function to run the game
        while True: #game will run in a large while loop

            #CHECKS FOR EVENTS - loops through dictionary of events to see if the game is quit or not
            for event in pygame.event.get(): #returns a dictionary of all events in the game whether game is closed, exited, etc
                if event.type == pygame.QUIT: #if event occurs
                    pygame.quit() #stop pygame
                    sys.exit() #closes the window

                if event.type == pygame.MOUSEBUTTONDOWN: #will shoot using mousebutton
                    current_ship_location = self._space_ship.get_position() #grabs ship current location
                    # print(current_ship_location)
                    bullet_object = Bullet(current_ship_location[0] + 40, current_ship_location[1] + 10) #takes in x and y coordinate
                    self._all_bullet.add(bullet_object) #adds the bullet object to bullet dictionary
                    # print(self._all_bullet)

                if event.type == self._alien_spawn_event:
                    alien_object = Alien()
                    self._all_aliens.add(alien_object)
                    # print(self._all_aliens)

                if event.type == self._alien_shoot_event:
                    alien.list = self._all_aliens.sprites()
                    # print(alien_list)
                    for alien in alien_list: #for every alien in the alien group, call the alien shoot object
                        alien_bullet_object = alien.shoot_alien_bullet()
                        if alien_bullet_object is not None: #if alien_bullet object exist
                            self._all_alien_bullets.add(alien_bullet_object)
                        else:
                            pass #then dont need to do anything
                    # print self._all_alien_bullets

            
            keys = pygame.key.get_pressed() #prints the status of every key, whether it is being pressed
            if keys[pygame.K_d]:
                self._space_ship.move("d")
                # print(keys[pygame.K_d])
            if keys[pygame.K_a]:
                self._space_ship.move("a")
                # print(keys[pygame.K_a])
            if keys[pygame.K_w]:
                self._space_ship.move("w")
                # print(keys[pygame.K_w])
            if keys[pygame.K_s]:
                self._space_ship.move("s")
                # print(keys[pygame.K_s])
            # print(keys)


            self._display.blit(self._space_surface,(0,0)) #allows to place surface -like paper on table
            self._space_surface.blit(pygame.image.load("assets/OuterSpace.png"), (0,0)) #Places on surface - like drawing on paper
            self._space_surface.blit(self._space_ship.get_surface(), self._space_ship.get_position()) #place ship on surface
            self._all_bullet.draw(self._space_surface) #draw the bullets onto the screen 
            self._all_bullet.update(self,_all_aliens) #checks the status of every bullet in the dictionary
            self._all_aliens.draw(self._space_surface)#draws the aliens onto the screen
            self._all_aliens.update()#Checks the status of every alien
            if self._all_alien_bullets is not None: #if bullet exist
                self._all_alien_bullets.draw(self._space_surface) #draw the bullets onto the screen
                self._all_alien_bullets.update(self.ship_sprite_group) #checks the status of the alien bullets 
            
            if pygame.sprite.spritecollide(self._space_ship, self._all_aliens, False): #if spaceship and alien collide
                pygame.quit() #quits the game
                sys.exit() #closes the window

            #updates window
            pygame.display.update() #updates the screen
            self._clock.tick(60) #sets to 60fps

my_game = Game()
my_game.run()



# https://www.pygame.org/docs/ref/key.html