import pygame

# Initialize Pygame
pygame.init()

# Set screen size
screen_size = (400, 400)
screen = pygame.display.set_mode(screen_size)

# Set screen color
blue_color = (0, 0, 255)

# Set the window title
pygame.display.set_caption("The Maze Game")

# Importing images
player = pygame.image.load('player.png')
enemy1 = pygame.image.load('enermy.png')
enemy2 = pygame.image.load('enermy.png')
wall = pygame.image.load('wall.png')

# Resizing the images
player = pygame.transform.scale(player, (30, 30))
enemy1 = pygame.transform.scale(enemy1, (30, 30))
enemy2 = pygame.transform.scale(enemy2, (30, 30))
wall = pygame.transform.scale(wall, (50, 50))

# Player position
player_x, player_y = 200, 300
player_speed = 0.1

# Enemy positions
enemy1_x, enemy1_y = 350, 100
enemy2_x, enemy2_y = 50, 50

# Enemy movement directions
enemy1_direction = 'left'
enemy2_direction = 'down'
enemy_speed = 0.1

# Walls positions
walls = [
    pygame.Rect(100, 100, 50, 50),
    pygame.Rect(150, 100, 50, 50),
    pygame.Rect(200, 100, 50, 50),
    pygame.Rect(250, 100, 50, 50),
    pygame.Rect(300, 100, 50, 50),
    pygame.Rect(100, 150, 50, 50),
    pygame.Rect(300, 150, 50, 50),
    pygame.Rect(100, 200, 50, 50),
    pygame.Rect(150, 200, 50, 50),
    pygame.Rect(300, 200, 50, 50),
    pygame.Rect(300, 250, 50, 50),
    pygame.Rect(150, 300, 50, 50),
    pygame.Rect(200, 300, 50, 50),
    pygame.Rect(250, 300, 50, 50),
]

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Update player rectangle for collision detection
    player_rect = pygame.Rect(player_x, player_y, player.get_width(), player.get_height())

    # Check for collision with walls
    for wall_rect in walls:
        if player_rect.colliderect(wall_rect):
            if keys[pygame.K_LEFT]:
                player_x += player_speed
            if keys[pygame.K_RIGHT]:
                player_x -= player_speed
            if keys[pygame.K_UP]:
                player_y += player_speed
            if keys[pygame.K_DOWN]:
                player_y -= player_speed

    # Enemy 1 horizontal movement
    if enemy1_direction == "left":
        enemy1_x -= enemy_speed
        if enemy1_x <= 200:
            enemy1_direction = "right"
    else:
        enemy1_x += enemy_speed
        if enemy1_x >= 350:
            enemy1_direction = "left"

    # Enemy 2 vertical movement
    if enemy2_direction == "down":
        enemy2_y += enemy_speed
        if enemy2_y >= 350:
            enemy2_direction = "up"
    else:
        enemy2_y -= enemy_speed
        if enemy2_y <= 50:
            enemy2_direction = "down"

    # Fill the screen with blue color
    screen.fill(blue_color)

    # Draw walls
    for wall_rect in walls:
        screen.blit(wall, wall_rect)

    # Positioning the images
    screen.blit(player, (player_x, player_y))
    screen.blit(enemy1, (enemy1_x, enemy1_y))
    screen.blit(enemy2, (enemy2_x, enemy2_y))

    # Update the display
    pygame.display.flip()

    # Create Rect objects for collision detection with enemies
    enemy1_rect = pygame.Rect(enemy1_x, enemy1_y, enemy1.get_width(), enemy1.get_height())
    enemy2_rect = pygame.Rect(enemy2_x, enemy2_y, enemy2.get_width(), enemy2.get_height())

    # Check for collision with enemies
    if player_rect.colliderect(enemy1_rect) or player_rect.colliderect(enemy2_rect):
        print("Game Over! You collided with an enemy.")
        running = False

# Quit Pygame
pygame.quit()
