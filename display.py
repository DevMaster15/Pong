import pygame
from ball import Ball
from paddle import Paddle

class Display:

    def __init__(self, WIDTH, HEIGHT, BORDER):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.BORDER = BORDER

    def create_display(self):

        # Variables
        screenColor = "white"
        ballColor = "red"
        bgColor = "black"
        velocityOfBall = 5
        
        
        # Draw the main scenario 

        pygame.init()
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT)) # initialize the display 

        # Draw borders
        pygame.draw.rect(screen, pygame.Color(screenColor), pygame.Rect((0,0), (self.WIDTH, self.BORDER)) )
        pygame.draw.rect(screen, pygame.Color(screenColor), pygame.Rect(0, 0, self.BORDER, self.HEIGHT))
        pygame.draw.rect(screen, pygame.Color(screenColor), pygame.Rect(0, self.HEIGHT-self.BORDER, self.WIDTH, self.BORDER))
        pygame.draw.rect(screen, pygame.Color(screenColor), pygame.Rect((0, self.WIDTH), (self.WIDTH, self.BORDER)))
        
        # Draw ball
        gameBall = Ball(self.WIDTH-Ball.RADIUS, self.HEIGHT//2, -velocityOfBall, -velocityOfBall) 
        gameBall.show_ball(ballColor, screen)
        
        # Draw paddle
        gamePaddle = Paddle(100)
        gamePaddle.show_paddle("white", screen, self)
        
        # pygame.display.flip()

        clock = pygame.time.Clock()    # Determine FPS (frames-per-second)

        crashed = False

        # Game loop
        while not crashed:

            for event in pygame.event.get(): # controls movement of the user on the screen
                if event.type == pygame.QUIT:
                    crashed = True

                print(event)

            pygame.display.flip()
            gameBall.updateMove(self, ballColor, screen, bgColor)
            gamePaddle.updateMove(screen, self)

            pygame.display.update()
            clock.tick(60)

        pygame.quit()

    
        