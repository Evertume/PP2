# Build a program with pygame where there will be shown window with the name “Mygame” and it need to remain open until you press X button

import pygame

pygame.init()

win_size = (500, 500)

win = pygame.display.set_mode(win_size)

pygame.display.set_caption("My game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
