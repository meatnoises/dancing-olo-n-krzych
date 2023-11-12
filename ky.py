import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1200, 1000
win = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Two Dumbasses Krzysiu And Olus Dancing")



# Load the dancer images
dancer_img1 = pygame.image.load('dancer1.png')
dancer_img1 = pygame.transform.scale(dancer_img1, (300, 300))  # Adjust the size if needed

dancer_img2 = pygame.image.load('dancer2.png')
dancer_img2 = pygame.transform.scale(dancer_img2, (300, 300))  # Adjust the size if needed

# Object attributes
radius1, radius2 = 150, 200  # Adjust the radius for the dance patterns
speed1, speed2 = 0.05, 0.03  # Adjust the speed of the dance

clock = pygame.time.Clock()

# Main loop
running = True
while running:
    win.fill((15, 15, 15))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update dancers' positions in circular motions
    dancer_x1 = WIDTH // 2 + int(radius1 * math.cos(speed1))
    dancer_y1 = HEIGHT // 2 + int(radius1 * math.sin(speed1))

    dancer_x2 = WIDTH // 2 + int(radius2 * math.cos(speed2))
    dancer_y2 = HEIGHT // 2 + int(radius2 * math.sin(speed2))

    speed1 += 0.05  # Increment speed for animation effect
    speed2 += 0.03  # Increment speed for animation effect

    # Draw the dancer images
    win.blit(dancer_img1, (dancer_x1, dancer_y1))
    win.blit(dancer_img2, (dancer_x2, dancer_y2))

    pygame.display.update()
    clock.tick(60)
   
pygame.quit()
sys.exit()
