import pygame
import Data

class Init:
    def __init__(self):
        pygame.init()

        #Génération de la fenetre
        pygame.display.set_caption("Cookie Cliker")

            #Dimension de la fenetre
        self.screen = pygame.display.set_mode((Data.WIDTH,Data.HEIGHT))

            #Background
        self.background = pygame.image.load('Python/Cookie Clicker/src/images/bg.jpg').convert()
        self.background = pygame.transform.scale(self.background, (Data.WIDTH,Data.HEIGHT))

        

            #Cookie
        self.cookie = pygame.image.load('Python/Cookie Clicker/src/images/cookie.svg')
        self.cookie = pygame.transform.scale(self.cookie, (200, 200))

        self.centre_cookie=self.cookie.get_size()

        self.centrex= Data.WIDTH/2-self.centre_cookie[0]/2
        self.centrey= self.background.get_height()/2-self.centre_cookie[1]/2

        self.rect = self.cookie.get_rect() #rect lié  au cookie pour pourvoir cliquer
        self.rect.x=self.centrex
        self.rect.y=self.centrey
       
            #Score
        self.fond_score = pygame.image.load('Python/Cookie Clicker/src/images/fondnoir.png')
        self.fond_score = pygame.transform.scale(self.fond_score, (Data.WIDTH,35))
        self.fond_score.fill((0, 0, 0, 120))

            #Bouton
        self.bouton = pygame.image.load('Python/Cookie Clicker/src/images/bouton.png')
        self.centre_bouton=self.bouton.get_size()
        self.centrex_bouton= Data.WIDTH/2-self.centre_bouton[0]/2
        self.centrey_bouton= Data.HEIGHT/2-self.centre_bouton[1]/2
        self.rect_bouton = self.cookie.get_rect() #rect lié  au cookie pour pourvoir cliquer
        self.rect_bouton.x=self.centrex_bouton+300
        self.rect_bouton.y=self.centrey_bouton

        self.frame_per_second = pygame.time.Clock()

        
       

        
        #Boucle tant que le jeu est lancé
        self.running = True
        