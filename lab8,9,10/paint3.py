import pygame, math

pygame.init()
sc = pygame.display.set_mode((800, 450))
sc.fill((255, 255, 255))
pygame.display.flip()

color = (0, 0, 0)
radius = 10
Draw = False
spos = None
tool = 3

f1 = pygame.font.SysFont(None, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                radius -= 2
            elif event.key == pygame.K_p:
                radius += 2
            elif event.key == pygame.K_r:
                color = (255, 0, 0)
            elif event.key == pygame.K_b:
                color = (0, 0, 255)
            elif event.key == pygame.K_q:
                color = (0, 0, 0)
            elif event.key == pygame.K_g:
                color = (0, 255, 0)
            elif event.key == pygame.K_1:
                tool = 1
            elif event.key == pygame.K_2:
                tool = 2
            elif event.key == pygame.K_3:
                tool = 3
            elif event.key == pygame.K_4:
                tool = 4
            elif event.key == pygame.K_5:
                tool = 5
            elif event.key == pygame.K_6:
                tool = 6
            elif event.key == pygame.K_7:
                tool = 7
            elif event.key == pygame.K_8:
                tool = 8
            elif event.key == pygame.K_a:
                sc.fill((255, 255, 255))
                pygame.display.update()
        
        if tool == 2:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                layer2 = sc
                Draw = True
                spos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if Draw:
                    pos = event.pos

                    w = pos[0] - spos[0]
                    h = pos[1] - spos[1]
                    
                    pygame.draw.rect(sc, color, (spos[0], spos[1], w, h))
                    pygame.display.update()
                Draw = False
                
        if tool == 5:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Draw = True
                spos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if Draw:
                    pos = event.pos
                    w = pos[0] - spos[0]
                    h = pos[1] - spos[1]
                    

                    pygame.draw.rect(sc, color, (spos[0], spos[1], min(w, h), min(w, h)))
                    pygame.display.update()
                Draw = False
        if tool == 6:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Draw = True
                spos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if Draw:
                    pos = event.pos
                    w1, h1 = spos
                    w2, h2 = pos

                    pygame.draw.polygon(sc, color, [(w1, h1), (w1, h2), (w2, h2)], 0)
                    pygame.display.update()
                Draw = False
        if tool == 7:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Draw = True
                spos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if Draw:
                    pos = event.pos
                    w1, h1 = spos
                    w2, h2 = pos
                    w3, h3 = (w1 + w2) // 2, h1 - int((w2 - w1) * math.sqrt(3) / 2)

                    pygame.draw.polygon(sc, color, [(w1, h1), (w2, h2), (w3, h3)], 0)
                    pygame.display.update()
                Draw = False
        if tool == 8:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Draw = True
                spos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if Draw:
                    pos = event.pos
                    w1, h1 = spos
                    w2, h2 = pos
                    w3, h3 = (w1 + w2) // 2, (h1 + h2) // 2

                    pygame.draw.polygon(sc, color, [(w1, h3), (w3, h2), (w2, h3), (w3, h1)], 0)
                    pygame.display.update()

                Draw = False
        if tool == 1:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Draw = True
                spos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if Draw:
                    pos = event.pos

                    w = pos[0] - spos[0]
                    h = pos[1] - spos[1]

                    pygame.draw.circle(sc, color, (spos[0], spos[1]), w//2)
                    pygame.display.update()
                Draw = False

        if tool == 3:
            mouse_press = pygame.mouse.get_pressed()
            if mouse_press[0]:
                mPos = pygame.mouse.get_pos()
                pygame.draw.circle(sc, color, mPos, radius)
                pygame.display.flip()

        if tool == 4:
            mouse_press = pygame.mouse.get_pressed()
            if mouse_press[0]:
                mPos = pygame.mouse.get_pos()
                pygame.draw.circle(sc, (255, 255, 255), mPos, radius)
                pygame.display.flip()


        pygame.display.update()
