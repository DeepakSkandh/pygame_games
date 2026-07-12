import pygame
import random

pygame.init()
window_width,window_height = 1280,720
display_surface = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("New Game")

surf = pygame.Surface((100,200))
surf.fill("red")
x = 590
y = 260
player_surf = pygame.image.load("images\player.png").convert_alpha()
star_surf = pygame.image.load("images\star.png").convert_alpha()
star_coordinates = [(random.randint(100,1200), random.randint(100,620)) for _ in range(20)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_surface.fill("gray")
    for position in star_coordinates:
        display_surface.blit(star_surf,position)
    display_surface.blit(player_surf,(x,y))
    
    x += 0.1
    y += 0.1
    pygame.display.update()
    
pygame.quit()

