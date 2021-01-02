import pygame

class Paddle:

    HEIGHT = 60
    WIDTH = 15

    def __init__(self, y_pos):
        self.y_pos = y_pos
    
    def show_paddle(self, color, screen, background):

        print("Y = ")
        print(self.y_pos)

        pygame.draw.rect(screen, color, pygame.Rect(background.WIDTH-self.WIDTH-10, self.y_pos, self.WIDTH, self.HEIGHT)) # left, top, width, height
    
    def updateMove(self, screen, background):
        
        self.show_paddle(pygame.Color("black"), screen, background)
        self.y_pos = self.y_pos - pygame.mouse.get_pos()[1] # take the y position, not x
        self.show_paddle(pygame.Color("white"), screen, background)