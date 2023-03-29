import pygame, random, sys, os, time
from pygame.locals import *

windowwidth = 800
windowheight = 600
textcolor = (255, 255, 255)
backgroundcolor = (0, 0, 0)
fps = 40
baddieminsize = 10
baddiemaxsize = 40
baddieminspeed = 5
baddiemaxspeed = 15
addnewbaddierate = 4
playermoverate = 6
count = 3

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                terminate()
                return
    
def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, textcolor)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
# set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption('car race')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 30)

gameOverSound = pygame.mixer.Sound