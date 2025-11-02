import pygame, sys
from pygame.locals import QUIT
from platformSprite import PlatformSprite
pygame.init()
pygame.font.init() # Initialize the font module
screen = pygame.display.set_mode((1100, 573))
pygame.display.set_caption('Hello World!')
catSprite = pygame.image.load('cat 1.svg')
catWidth, catHeight = 80, 85
catSprite = pygame.transform.scale(catSprite, (catWidth, catHeight))
flippedCatSprite = pygame.transform.flip(catSprite, True, False)
backgroundSprite = pygame.image.load('background 2.jpeg')
platform1 = PlatformSprite('platform1.png', 220, 30, 100, 340, 0.08)
platform2 = PlatformSprite('platform2.png', 220, 30, 270, 220, 0.09)
platform3 = PlatformSprite('platform3.png', 220, 30, 500, 120, -0.06)
platform4 = PlatformSprite('platform2.png', 220, 30, 800, -40, -0.15)
platform5 = PlatformSprite('platform3.png', 220, 30, 900, -180, 0.12)
platformList = [platform1, platform2, platform3, platform4, platform5]
groundLevel = 475
catX, catY = 50, groundLevel - catHeight
catSpeed = 0.15
catYSpeed = 0
jumpTime = 0
catYAcceleration = 0.002
screenYShift = 0
font = pygame.font.SysFont('Arial', 60)
gameover_text = font.render('Game Over :(', True, (255, 255, 255)) # White text
gameover = False
def AOnB(widthA, heightA, posAx, posAy, widthB, heightB, posBx, posBy):
    ## If A is to the right of B, then A not on B
    if posAx > posBx + widthB:
        return False
    ## If A is to the left of B, then A not on B
    if posAx + widthA < posBx:
        return False
    ## Now we know A and B horizontally overlap, if A's bottom surface is the same as B's top surface, then A on B
    if posAy + heightA < posBy + 0.5 and posAy + heightA > posBy - 0.5:
        return True
    return False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           sys.exit()
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_LEFT: 
               catSpeed = -1
           elif event.key == pygame.K_RIGHT:
               catSpeed = 1
           elif event.key == pygame.K_UP and catYSpeed == 0:
              catY = catY - 1
              catYSpeed = 0.8
    screen.fill("white")
    screen.blit(backgroundSprite, (0, -1137 + screenYShift))
    landing = False
    for p in platformList:
        p.move(screen, screenYShift)
        if AOnB(catWidth, catHeight, catX, catY, p.width, p.height, p.x, p.y):
            landing = True
            catYSpeed = 0

    if AOnB(catWidth, catHeight, catX, catY, 9999999, 9999999, 0, groundLevel):
        catYSpeed = 0
        landing = True

    if landing == False:
        catY = catY - catYSpeed
        catYSpeed = catYSpeed - catYAcceleration
    # replace some bottom platforms (outside the screen) with new platforms on the top
    for p in platformList:
        if p.y + screenYShift > 573 + catHeight + 20:
            allPlatformYPos = []
            for pl in platformList:
                allPlatformYPos.append(pl.y)
            topPlatformY = min(allPlatformYPos)
            newPlatformY = topPlatformY - 140
            p.y = newPlatformY
    catX = catX + catSpeed
    if catY + screenYShift > 573:
        gameover = True
    if catX < 0:
        catX = 0    
    if catX > 1100:
        catX = 1100
    if catSpeed < 0:
        if catY + screenYShift < 250:
            screenYShift = 250 - catY
        screen.blit(flippedCatSprite, (catX, catY + screenYShift))
    elif catSpeed > 0:
        if catY + screenYShift < 250:
            screenYShift = 250 - catY
        screen.blit(catSprite, (catX, catY + screenYShift))
    if gameover == True:
        screen.blit(gameover_text, (400, 200))
    pygame.display.update()
