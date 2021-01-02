import pygame

class Ball:

    RADIUS = 10
    

    def __init__(self, pos_x, pos_y, vel_x, vel_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y

    # show ball on the screen
    def show_ball(self, color, screen):
        
        pygame.draw.circle(screen, color, (self.pos_x, self.pos_y), self.RADIUS)

    # update position's ball
    def updateMove(self, background, ballColor, screen, bgColor):

        # calcualte the new position of the axes
        new_x = self.pos_x + self.vel_x
        new_y = self.pos_y + self.vel_y
        
        # check if ball touches the border
        if new_x < background.BORDER + self.RADIUS:
            self.vel_x = -self.vel_x
        elif new_y < background.BORDER + self.RADIUS or new_y > background.HEIGHT - background.BORDER - self.RADIUS:
            self.vel_y = -self.vel_y
        else:
            
            self.show_ball(bgColor, screen) # re-color the previous position
            self.pos_x += self.vel_x
            self.pos_y += self.vel_y
            self.show_ball(ballColor, screen)

