import pygame
pygame.init()

window = pygame.display.set_mode((500,500))

done = False
secs = 0
mins = 0
hours = 0

font = pygame.font.Font('OpenSansItalic.ttf', 80)
text = font.render("{}:{}:{}".format(hours, mins, secs), True, (255, 255, 255), (0, 0, 0))
textRect = text.get_rect()
textRect.center = 500 // 2, 500 // 2

clock = pygame.time.Clock()

while not done:
    clock.tick(1)
    secs += 1
    window.blit(text, textRect)
    if secs == 60:
        secs = 0
        mins +=1
    if mins == 60:
        mins = 0
        hours +=1
    text = font.render("{}:{}:{}".format(hours, mins, secs), True, (255, 255, 255), (0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        pygame.display.update()