import pygame
pygame.init()

monitor = pygame.display.set_mode((1280,720))

pygame.display.set_caption("PP2 pygame")

pygame.display.set_icon(pygame.image.load("white_walker.png"))
check = True

#square = pygame.Surface((60, 200))

#font =pygame.font.Font("Lobster-Regular.ttf", 25)
#text = font.render('PP2 game', False, 'Red')

background = pygame.image.load("game_of_thrones.png").convert_alpha()
background = pygame.transform.smoothscale(background, (1280,720))

sound = pygame.mixer.Sound("light_of_the_seven.mp3")
sound.play()

while check:
    monitor.fill((177, 252, 3))
    #monitor.blit(square,(50, 50))
    #pygame.draw.circle(monitor, 'Blue', (100, 100), 40)
    #monitor.blit(text, (300, 100))
    monitor.blit(background, (0, 0))
    pygame.display.update()
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()