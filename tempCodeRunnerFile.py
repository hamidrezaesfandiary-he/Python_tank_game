import pygame
import random


pygame.init()

font = pygame.font.SysFont(None, 40)

#creat main screen
screen = pygame.display.set_mode((1200 , 800))
#change titel, icon and back ground
pygame.display.set_caption("...tank...")
icon = pygame.image.load("tank6.png")
pygame.display.set_icon(icon)
back_ground = pygame.image.load("images_sky.jfif")
back_ground = pygame.transform.scale(back_ground, (1200, 800))


#icon tank
player_img = pygame.image.load("tank6.png")
player_img = pygame.transform.scale(player_img,(100, 100))
player_x = 100
player_y = 0
player_spead = 1

#icon soldier
player_soldier = pygame.image.load("images _1.jfif")
player_soldier = pygame.transform.scale(player_soldier ,(20, 20))
soldier_x = -20
soldier_y = -20
soldier_spead = 1

rain_soldier = []
for _ in range(4):
    rain_soldier_x = random.randint(0, 1180)
    rain_soldier_y = 0
    rain_soldier_speed = random.uniform(0.1 , 0.4)
    rain_soldier.append([rain_soldier_x, rain_soldier_y, rain_soldier_speed])


#icon bullet
bullet_img = pygame.image.load("bullet.png")
bullet_img = pygame.transform.scale(bullet_img,(40, 40))
bullet_x = -100
bullet_y = -100
bullet_speed = 0.5
bullet_active = True
score = 0

#loop 
runing = True
while runing:
    event = pygame.event.get()
    for e in event:
        if e.type == pygame.QUIT:
            runing = False


    #move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_x += player_spead
    if keys[pygame.K_LEFT]:
        player_x -= player_spead
    if keys[pygame.K_UP]:
        player_y -= player_spead
    if keys[pygame.K_DOWN]:
        player_y += player_spead
    
    if keys[pygame.K_SPACE]:
        bullet_speed = 1
        if bullet_active:
            bullet_x = player_x + 50
            bullet_y = player_y
            bullet_active = False
        bullet_y -= bullet_speed



    #bundrary chek
    if player_x < 0:
        player_x = 0
    if player_x > 1100:
        player_x = 1100
    if player_y < 0:
        player_y = 0
    if player_y > 650:
        player_y = 650

        
#move bullet
    bullet_y -= bullet_speed
    if not bullet_active:
        if bullet_y < -20:
            bullet_active = True
    bullet_rect = bullet_img.get_rect(topleft=(bullet_x, bullet_y))
        
    for i in rain_soldier:
        i[1] += i[2]
        rain_rect = player_soldier.get_rect(topleft = (i[0] , i[1]))
        if bullet_rect.colliderect(rain_rect):
            i[0] = random.randint(0, 1180)
            i[1] = 0
            bullet_active = True
            bullet_x = -100
            bullet_y = -100
            score += 1
            break
           
    player_rect = player_img.get_rect(topleft = (player_x , player_y))
    for i in rain_soldier:
        rain_rect = player_soldier.get_rect(topleft = (i[0] , i[1]))
        if rain_rect.colliderect(player_rect):
            score -= 1
            i[0] = random.randint(0, 1180)
            i[1] = 0

        if i[1] > 800:
            score -= 1
            i[0] =random.randint(0, 1180)
            i[1] = 0

    score_text = font.render(f"score : {score}", True, (244, 255 ,255))  


    for i in rain_soldier:
        i[1] += i[2]
        if i[1] > 800:
            i[1] = 0
            i[0] = random.randint(0, 1180) 
        
        
   

    screen.blit(back_ground, (0, 0))
    screen.blit(player_img, (player_x, player_y))
    for i in rain_soldier:
        screen.blit(player_soldier, (i[0], i[1]))
    screen.blit(bullet_img, (bullet_x, bullet_y))
    screen.blit(score_text, (1000, 10))

    pygame.display.update()