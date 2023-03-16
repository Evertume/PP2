# Add in your program on the top left score text starting from 0. When you press up key the score needs to increase, while the down key decreases respectively.
import pygame

pygame.init()

win_size = (500, 500)

win = pygame.display.set_mode(win_size)

pygame.display.set_caption("My game")
score = 0
font =pygame.font.Font("OpenSans.ttf", 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                score += 1
            elif event.key == pygame.K_DOWN:
                score -= 1
    # draw the score
    win.fill((0, 0, 0))
    score_text = font.render(f"score: {score}", True, (255, 255, 255))
    win.blit(score_text, (10, 10))

    pygame.display.update()