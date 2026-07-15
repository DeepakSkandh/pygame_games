import pygame
import random

pygame.init()
window_width,window_height = 1280,720
display_surface = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("New Game")

player_surf = pygame.image.load("images\player.png").convert_alpha()
player_rect = player_surf.get_frect(center = (window_width/2,(window_height-140)))

star_surf = pygame.image.load("images\star.png").convert_alpha()
star_coordinates = [(random.randint(100,1200), random.randint(100,620)) for _ in range(20)]

metor_surf = pygame.image.load("images\meteor.png").convert_alpha()
metor_rect = metor_surf.get_frect(center = (window_width/2,window_height/2))

laser_surf = pygame.image.load("images\laser.png").convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft=(window_width//2,window_height-200))
x = 0
y = 0
player_direction = pygame.math.Vector2(x,y)
player_speed = 300

running = True
clock = pygame.time.Clock()
while running:
    dt = clock.tick(60) / 1000
    #print(dt)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
         #   print(1 )
        #if event.type == pygame.MOUSEMOTION:
         #   player_rect.center = event.pos
    #print(pygame.mouse.get_pos())
    #print(pygame.mouse.get_pressed())

    keys = pygame.key.get_pressed()
    #if keys[pygame.K_RIGHT]:
        #player_direction.x = 1
        #player_rect.center += player_direction * player_speed * dt
    #if keys[pygame.K_LEFT]:
     #   player_direction.x = -1

    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    player_direction = player_direction.normalize() if player_direction else player_direction

    player_rect.center += player_direction * player_speed * dt
    

    display_surface.fill("gray")
    for position in star_coordinates:
        display_surface.blit(star_surf,position)
        display_surface.blit(metor_surf,metor_rect)
    display_surface.blit(player_surf,player_rect) 
    display_surface.blit(laser_surf,laser_rect)


    pygame.display.update()
#print(clock.get_fps())
    
pygame.quit()

