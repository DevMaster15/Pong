import pygame

class Paddle:

    HEIGHT = 80
    WIDTH = 20

    def __init__(self, y_pos):
        self.y_pos = y_pos
    
    def show_paddle(self, color, screen, background):
        pygame.draw.rect(screen, color, pygame.Rect((background.WIDTH-self.WIDTH, self.y-self.HEIGHT/2)))
    
    def updateMove(self):
        self.show_paddle(pygame.Color("black"), screen, background)
        self.y = pygame.mouse.get_pos()[1] # take the y position, not x
        self.show_paddle(pygame.Color("white"), screen, background)