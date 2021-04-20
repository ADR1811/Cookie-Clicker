import pygame
import Data
import math

class Menu:
    def __init__(self):
        pygame.init()
        self.run=True

        #Génération de la fenetre
        pygame.display.set_caption("Cookie Cliker")

            #Dimension de la fenetre
        self.screen = pygame.display.set_mode((Data.WIDTH,Data.HEIGHT))

            #Background
        self.background = pygame.image.load('Python/Cookie Clicker/src/images/bg.jpg').convert()
        self.background = pygame.transform.scale(self.background, (Data.WIDTH,Data.HEIGHT))
        self.centre= self.background.get_rect()
        self.centre.x = math.ceil(self.screen.get_width() / 3)
        self.centre.y = math.ceil(self.screen.get_width() / 5)
        
            #CookieLOGO

        self.cookie_Logo = pygame.image.load('Python/Cookie Clicker/src/images/cookieLOGO.jpg')


            #Play Button

        self.play_button = pygame.image.load('Python/Cookie Clicker/src/images/play.png')
        self.play_button=pygame.transform.scale(self.play_button, (200, 100))
        self.centre_button= self.play_button.get_rect()
        self.centre_button.x = math.ceil(self.screen.get_width()/2.7)
        self.centre_button.y = math.ceil(self.screen.get_width()/2.5)






    def Play(self):
        while self.run:
        
            self.screen.blit(self.background, (0,0)) #On place le background
            self.screen.blit(self.cookie_Logo, self.centre)
            self.screen.blit(self.play_button, self.centre_button)
            pygame.display.flip() #On refresh la page


            #On récupérer tous les events que l'on range dans event
            for event in  pygame.event.get(): 
            
                if event.type == pygame.QUIT: # Si l'event est QUIT
                    #Alors on quitte la boucle et on ferme la fenetre
                    self.run= False
                    pygame.quit()

m=Menu()
m.Play()