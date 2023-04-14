import pygame

# initialize pygame
pygame.init()

# set up the screen
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moving Ball")

# set up the ball
ball_color = (255, 0, 0)  # red
ball_radius = 25
ball_position = [225, 225]  # center of the screen
ball_speed = 20

# main game loop
running = True
while running:

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # move the ball in the direction of the arrow key pressed
            if event.key == pygame.K_UP:
                ball_position[1] -= ball_speed
            elif event.key == pygame.K_DOWN:
                ball_position[1] += ball_speed
            elif event.key == pygame.K_LEFT:
                ball_position[0] -= ball_speed
            elif event.key == pygame.K_RIGHT:
                ball_position[0] += ball_speed

    # check if the ball is outside the screen
    if ball_position[0] - ball_radius < 0:
        ball_position[0] = ball_radius
    elif ball_position[0] + ball_radius > 500:
        ball_position[0] = 500 - ball_radius
    if ball_position[1] - ball_radius < 0:
        ball_position[1] = ball_radius
    elif ball_position[1] + ball_radius > 500:
        ball_position[1] = 500 - ball_radius

    # draw the screen
    screen.fill((255, 255, 255))  # white background
    pygame.draw.circle(screen, ball_color, ball_position, ball_radius)
    pygame.display.flip()

# quit pygame
pygame.quit()
