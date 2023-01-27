import pygame
import random
import os

done = False
while not done:
    WINDOW_WIDTH = random.randint(500, 1500)
    WINDOW_HEIGHT = random.randint(300, 900)
    PERIM_WIDTH = 20
    WEIGHT = 1.2

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    RAND_COLOR = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    RAND_COLOR2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    pygame.init()
    pygame.display.set_caption("Polygon Sheet Music")

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    current_path = os.path.dirname(__file__)

    ball_x = int(WINDOW_WIDTH / 2) # initial LOC = CENTER of screen
    ball_y = int(WINDOW_HEIGHT / 2)
    ball_size = random.randint(30,75) # radius of ball
    # BALL SPEED!!!!!!!!!!! CHANGE TO YOUR LIKING
    ball_dx = random.randint(-30,30) # velocity x
    ball_dy = random.randint(-30,30) # velocity y
    temp_dx = 0
    temp_dy = 0

    C = pygame.mixer.Sound(os.path.join(current_path, 'C.wav'))
    E_flat = pygame.mixer.Sound(os.path.join(current_path, 'Eb.wav'))
    G_flat = pygame.mixer.Sound(os.path.join(current_path, 'Gb.wav'))
    A = pygame.mixer.Sound(os.path.join(current_path, 'A.wav'))

    reset = False
    while not reset:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                reset = True
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if ball_dx != 0 and ball_dy != 0:
                        temp_dx = ball_dx
                        temp_dy = ball_dy
                        ball_dx = 0
                        ball_dy = 0
                    elif ball_dx == 0 and ball_dy == 0:
                        ball_dx = temp_dx
                        ball_dy = temp_dy
            if keys[pygame.K_ESCAPE]:
                done = True
                reset = True
            if keys[pygame.K_RETURN]:
                reset = True


        ball_x += ball_dx #location updated every frame
        ball_y += ball_dy

        if (ball_x + ball_size) > WINDOW_WIDTH - PERIM_WIDTH*WEIGHT:
            ball_dx = ball_dx * -1
            E_flat.play()
        if (ball_x - ball_size) < 0 + PERIM_WIDTH*WEIGHT: #center of ball + radius, center of ball - radius
            ball_dx = ball_dx * -1
            A.play()
        if (ball_y + ball_size) > WINDOW_HEIGHT - PERIM_WIDTH*WEIGHT:
            ball_dy = ball_dy * -1 
            C.play()
        if (ball_y - ball_size) < 0 + PERIM_WIDTH*WEIGHT:
            ball_dy = ball_dy * -1
            G_flat.play()

        screen.fill(BLACK)

        pygame.draw.rect(screen, RAND_COLOR2, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT), PERIM_WIDTH)
        pygame.draw.circle(screen, RAND_COLOR, [ball_x, ball_y], ball_size, 0)

        pygame.display.flip()

        clock.tick(60) # 60 frames per sec
                    # ball dx = 4 
                    # ball velocity = 4 pixels per frame, so 240 frames per second

pygame.quit()