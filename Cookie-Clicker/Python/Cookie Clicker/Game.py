import pygame
import Initialisation

import Data

#Boucle tant que le jeu est lancé
class Game:
    def __init__(self):
        init= Initialisation.Init()
        style=pygame.font.SysFont('Comic Sans MS', 30)
        self.text = style.render(Data.point,1,(255,255,255))
        self.txt_multiplicateur=style.render("X2",1,(0,0,0))
        self.deux_point=style.render(":",1,(0,0,0))

        self.txt_points= (int(Data.multiplicateur)+1)*50
        self.txt_score=style.render(str(self.txt_points),1,(0,0,0))
        
        while init.running:

                    
            init.screen.blit(init.background, (0,0)) #On place le background
            init.screen.blit(init.cookie, (init.centrex,init.centrey)) #On place le cookie
            init.screen.blit(init.fond_score, (0,Data.HEIGHT/5))#Fond Score
            init.screen.blit(self.text, (Data.WIDTH/2,Data.HEIGHT/5.15))#Score
            init.screen.blit(init.bouton, (init.centrex_bouton+300,init.centrey_bouton))
            init.screen.blit(self.txt_multiplicateur, (init.centrex_bouton*1.69,init.centrey_bouton))#multi
            init.screen.blit(self.deux_point, (init.centrex_bouton*1.78,init.centrey_bouton))#deux point
            init.screen.blit(self.txt_score, (init.centrex_bouton*1.8,init.centrey_bouton))#deux point
            pygame.display.flip() #On refresh la page


            #On récupérer tous les events que l'on range dans event
            for event in  pygame.event.get(): 
            
                if event.type == pygame.QUIT: # Si l'event est QUIT
                    #Alors on quitte la boucle et on ferme la fenetre
                    init.running= False
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:# Si un bouton de la souris a été préssé
                    if pygame.mouse.get_focused: # Si il a été préssé dans le screen
                        if init.rect.collidepoint(event.pos): # Si il est dans l'écran
                            if pygame.mouse.get_pressed()==(True,False,False): #Si c'est le bouton droit de la souris qui a été préssé
                                Data.point= int(Data.point)+(1*int(Data.multiplicateur))
                                Data.point=str(Data.point)
                                self.text = style.render(Data.point,1,(255,255,255))
                                
                                
                        if init.rect_bouton.collidepoint(event.pos): # Si il est dans l'écran
                            if pygame.mouse.get_pressed()==(True,False,False): #Si c'est le bouton droit de la souris qui a été préssé
                                if (int(Data.multiplicateur)+1)*50<=int(Data.point):

                                    Data.point=int(Data.point)-(int(Data.multiplicateur)+1)*50
                                    Data.multiplicateur=int(Data.multiplicateur)+1
                                    self.multiplicateur_tampon="X"+str(Data.multiplicateur+1)
                                    Data.point=str(Data.point)

                                    self.text = style.render(Data.point,1,(255,255,255))
                                    self.txt_multiplicateur = style.render(self.multiplicateur_tampon,1,(0,0,0))

                                    self.txt_points= (int(Data.multiplicateur)+1)*50
                                    self.txt_score=style.render(str(self.txt_points),1,(0,0,0))
            init.frame_per_second.tick(Data.FPS)

                                        


                                            
g=Game()