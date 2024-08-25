import pygame 
from sys import exit
from random import randint
import math

def time():
    thoigian_hientai = int((pygame.time.get_ticks() / 1000) - thoigian_batdau)
    thoigian = text.render(f"Score: {thoigian_hientai}" , False, (64,64,64) ) 
    thoigian_rect = thoigian.get_rect(center = (400 , 50))
    screen.blit(thoigian , thoigian_rect)
    return thoigian_hientai

def obstacle_movement(ob_list): 
    if ob_list:
        for ob_rect in ob_list:
            ob_rect.x -= 10
            if ob_rect.bottom == 350 :
                screen.blit(chicken_surf , ob_rect )
            else:
                screen.blit(bird_surf, ob_rect )

        ob_list = [ob for ob in ob_list if ob.x > -100]
    

        return ob_list
    else:
        return []

def va_cham(char , ob):
    if ob:
        for ob_rect in ob:
            if char.colliderect(ob_rect):
                return False
    return True

def char_animation():
    global character_surf , character_index

    if character_rect.bottom < 350:
        character_surf = character_jump1
    else:
        character_index += 0.14
        if character_index >= len(character_run):
            character_index = 0
        character_surf = character_run[int(character_index)]

def speed_up (x):
    if x:
        for ob_rect in x:
            ob_rect.x -= 5

pygame.init()

widght = 800
height = 400
scroll = 0
scroll_ground = 0
bien_spam = 0
dem_menu = 0

screen = pygame.display.set_mode((widght , height))
icon = pygame.image.load("./img/gà1.png")
pygame.display.set_icon(icon)
title = pygame.display.set_caption('Infinite Escape')

bg_screen = screen.get_width()
bg_titles = math.ceil(widght / bg_screen) + 1

bg_ground = screen.get_width()
ground_title = math.ceil(widght / bg_ground) + 1

menu_screen = pygame.image.load ("Menu.png")

clock = pygame.time.Clock()
game_bgm = pygame.mixer.Sound("./img/BGM.wav")
j_s = pygame.mixer.Sound("./img/jump_sound.wav")
game_bgm.play( loops = -1 )
game_bgm.set_volume(0.1)
j_s.set_volume(0.4)

gravity = 0

hdonggame = False

text = pygame.font.Font( "pixel_font.ttf" , 23)
surface_screen = pygame.image.load("./img/bg.png").convert()
ground_screen = pygame.image.load ("./img/ground2.jpg").convert()


chicken_1 = pygame.image.load ("./img/gà1.png").convert_alpha()
chicken_2 = pygame.image.load ("./img/gà2.png").convert_alpha()
chicken_3 = pygame.image.load ("./img/gà3.png").convert_alpha()
chicken_4 = pygame.image.load ("./img/gà4.png").convert_alpha()
chicken_run = [chicken_1,chicken_2,chicken_3,chicken_4]
chicken_index = 0
chicken_surf = chicken_run[chicken_index]
chicken_rect = chicken_surf.get_rect (midbottom = ( 600 , 338))

character_1 = pygame.image.load("./img/char.png").convert_alpha()
character_2 = pygame.image.load("./img/char2.png").convert_alpha()
character_3 = pygame.image.load("./img/char3.png").convert_alpha()
character_4 = pygame.image.load("./img/char4.png").convert_alpha()
character_5 = pygame.image.load("./img/char5.png").convert_alpha()
character_6 = pygame.image.load("./img/char6.png").convert_alpha()
character_run = [character_1,character_2,character_3,character_4,character_5,character_6]
character_jump1 = pygame.image.load("./img/charjump.png").convert_alpha()
character_jump2 = pygame.image.load("./img/charjump2.png").convert_alpha()
character_index = 0
character_surf = character_run[character_index]
character_rect = character_surf.get_rect (midbottom = (100,360) )

bird_1 = pygame.image.load("./img/bird1.png").convert_alpha()
bird_2 = pygame.image.load("./img/bird2.png").convert_alpha()
bird_3 = pygame.image.load("./img/bird3.png").convert_alpha()
bird_index = 0
bird_list = [bird_1,bird_2,bird_3]

bird_surf = bird_list[bird_index]
bird_rect = bird_surf.get_rect (midbottom = (600 , 200)) 


obstacle_rect_list = []

thoigian_batdau  = 0
my_score = 0

again_text = text.render("Click to run" , False , (64,64,64))
again_text_rect = again_text.get_rect(center = (400 , 200))

obstacle_timer = pygame.USEREVENT + 1 
pygame.time.set_timer(obstacle_timer , 1000 - bien_spam )

chicken_ani_timer = pygame.USEREVENT + 2
pygame.time.set_timer(chicken_ani_timer , 160 )

bird_ani_timer = pygame.USEREVENT + 3
pygame.time.set_timer(bird_ani_timer , 180 )

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()
        if hdonggame is False:
            if ev.type == pygame.MOUSEBUTTONUP:
                hdonggame = True
                chicken_rect.left = 800 
        if ev.type == pygame.KEYDOWN:
            if ev.key  == pygame.K_SPACE:
                if character_rect.bottom == 350:
                    gravity = -18
                    if hdonggame is True:
                        j_s.play()
 
        if hdonggame:
            if ev.type == obstacle_timer and hdonggame:
                if randint(0,2):
                    obstacle_rect_list.append(chicken_surf.get_rect (bottomright = (randint(900 , 1100), 350)))
                else:
                    obstacle_rect_list.append(bird_surf.get_rect (midbottom = (randint(900 , 1000) , 200 )))
            if ev.type == chicken_ani_timer:
                chicken_index += 1 
                if chicken_index >= len(chicken_run):
                    chicken_index == 0
                chicken_surf = chicken_run[int(chicken_index) % len(chicken_run)]

            if ev.type == bird_ani_timer:
                bird_index += 1
                if bird_index >= len(bird_list):
                    bird_index = 0
                bird_surf = bird_list[int(bird_index) % len(bird_list)]

    new_ground = pygame.transform.scale ( ground_screen , (800 , 50))

    if hdonggame is True:   
        
        for i in range (0, bg_titles):
            screen.blit( surface_screen , (i*widght + scroll , -50))
            scroll -= 3
            if abs(scroll) > widght:
                scroll = 0
        for i_ground in range (0, ground_title):
            screen.blit( new_ground , (i_ground*widght + scroll_ground , 350))
            scroll_ground -= 4.5
            if abs(scroll_ground) > widght:
                scroll_ground = 0  

        my_score = time()

        if my_score >= 15:
            speed_up(obstacle_rect_list)
        if my_score >= 30:
            speed_up(obstacle_rect_list)
        if my_score >= 50:
            speed_up(obstacle_rect_list)
        if my_score >= 60:
            speed_up(obstacle_rect_list)

        gravity += 1
        character_rect.bottom += gravity
        if character_rect.bottom >= 350 :
            character_rect.bottom = 350
        char_animation()
        screen.blit( character_surf , character_rect )
        
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        hdonggame = va_cham(character_rect, obstacle_rect_list)
   
    else:
        
        screen.blit(menu_screen , (0,0))

        thoigian_batdau = int(pygame.time.get_ticks() / 1000)
        score = text.render(f"Your Score: {my_score}", False , (64, 64 , 64))
        score_rect = score.get_rect(center  = (400 , 200))
        
        if my_score == 0:
            screen.blit(again_text , again_text_rect)
        else:
            
            screen.blit(score , score_rect)
      
        obstacle_rect_list.clear()
        character_rect.midbottom = (100,350)
        gravity = 0

    clock.tick(60)
    pygame.display.update()