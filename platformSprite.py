import pygame, sys
class PlatformSprite:
    def __init__(self, imageUrl, width, height, x, y, xSpeed):
        self.imageUrl = imageUrl
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.xSpeed = xSpeed
        self.sprite = pygame.image.load(imageUrl)
        self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))
    
    def move(self, screen, screenYShift):
        self.x = self.x + self.xSpeed
        if self.x > 890:
            if self.xSpeed > 0:
                self.xSpeed = -self.xSpeed
        elif self.x < 0:
            if self.xSpeed < 0:
                self.xSpeed = -self.xSpeed
        screen.blit(self.sprite, (self.x, self.y + screenYShift))