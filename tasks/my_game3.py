'''
When you press the left key the text with score needs to move to the left,if it exceeds the left side it needs to appear on the right side of the window.
Furthermore, make for the right key similar behavior but conversely text will move to the right.
''' 

import pygame

pygame.init()

win_size = (500, 500)

win = pygame.display.set_mode(win_size)

pygame.display.set_caption("My game")
score = 0
font =pygame.font.Font("fonts\OpenSans.ttf", 36)
score_position = [50, 50]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                score += 1
            elif event.key == pygame.K_DOWN:
                score -= 1
            elif event.key == pygame.K_LEFT:
                score_position[0] -= 10
                if score_position[0] < -130:
                    score_position[0] = win_size[0]
            elif event.key == pygame.K_RIGHT:
                score_position[0] += 10
                if score_position[0] > win_size[0]:
                    score_position[0] = win_size[0] - 630
    # draw the score
    win.fill((0, 0, 0))
    score_text = font.render(f"score: {score}", True, (255, 255, 255))
    win.blit(score_text, score_position)

    pygame.display.update()