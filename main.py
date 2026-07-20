import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self,image_path,groups):
        super().__init__(groups)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_frect(center = (window_width/2,(window_height-140)))
        self.speed = 300
        self.direction = pygame.math.Vector2()

    def update(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt


pygame.init()

window_width,window_height = 1280,720
display_surface = pygame.display.set_mode((window_width,window_height))
image_pth = "images\player.png"
all_sprites = pygame.sprite.Group()
player = Player(image_pth,all_sprites)
pygame.display.set_caption("New Game")


all_sprites.add(player)

background = pygame.image.load("images/background.jpeg").convert()
background = pygame.transform.scale(background, (window_width, window_height))

#player_surf = pygame.image.load("images\player.png").convert_alpha()
#player_rect = player_surf.get_frect(center = (window_width/2,(window_height-140)))

star_surf = pygame.image.load("images\star.png").convert_alpha()
star_coordinates = [(random.randint(100,1200), random.randint(100,620)) for _ in range(20)]

metor_surf = pygame.image.load("images\meteor.png").convert_alpha()
metor_rect = metor_surf.get_frect(center = (window_width/2,window_height/2))

laser_surf = pygame.image.load("images\laser.png").convert_alpha()
#laser_rect = laser_surf.get_frect(midbottom = player_rect.midtop)
#x,y = 0,0
#player_direction = pygame.math.Vector2(x,y)
#player_speed = 300

x1,y1 = 0,0
laser_direction = pygame.math.Vector2(x1,y1)
laser_speed = 450
laser_activate = False
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

    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_RIGHT]:
        #player_direction.x = 1
        #player_rect.center += player_direction * player_speed * dt
    #if keys[pygame.K_LEFT]:
     #   player_direction.x = -1

    #player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    #player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    #player_direction = player_direction.normalize() if player_direction else player_direction

   # player_rect.center += player_direction * player_speed * dt
   # if not laser_activate:
       # laser_rect.midbottom = player_rect.midtop

    all_sprites.update()
    #laser_keys = pygame.key.get_pressed()
    #if laser_keys[pygame.K_SPACE]:
     #   laser_activate = True
      #  laser_direction.y = -1
    #if laser_activate:
      #  laser_rect.center += laser_direction * laser_speed * dt
    #if laser_rect.bottom < 0:
       # laser_activate = False
    

    display_surface.fill("gray")
    display_surface.blit(background, (0, 0))
    for position in star_coordinates:
        display_surface.blit(star_surf,position)
    display_surface.blit(metor_surf,metor_rect)
    #display_surface.blit(player_surf,player_rect) 
    #display_surface.blit(laser_surf,laser_rect)
    #display_surface.blit(player.image,player.rect)
    all_sprites.draw(display_surface)

    pygame.display.update()
#print(clock.get_fps())
    
pygame.quit()

