import pygame
import os
import sys
import random
import time
from pygame.locals import (
     K_UP,
     RLEACCEL,
     K_DOWN,
     K_LEFT,
     K_RIGHT,
     K_ESCAPE,
     KEYDOWN,
     QUIT,
     K_KP_ENTER,
 ) 
pygame.mixer.init() 
pygame.init()
clock=pygame.time.Clock()
screenx=500
screeny=600
world=pygame.display.set_mode([screenx,screeny])
surf=pygame.Surface((400,400))
running=True
pygame.mixer.music.load("C:\\Users\DELL\\Downloads\\sound.wav")
pygame.mixer.music.play(loops=-1)
clound=pygame.image.load("C:\\Users\\DELL\\Downloads\\cloud.png").convert()
over=pygame.image.load("C:\\Users\\DELL\\Downloads\\game-over.png").convert()
sky=pygame.image.load("C:\\Users\\DELL\\Downloads\\sky.png").convert()
misile=pygame.image.load("C:\\Users\\DELL\\Downloads\\image.png").convert()
misile.set_colorkey((255,255,255),pygame.SRCALPHA)
font1=pygame.font.SysFont("time roman", 30,True,True)
text1=font1.render("1.start(press insert)",True,(12,30,20))
text2=font1.render("2.quite(press q)",True,(12,30,20))
#main loop
def welcome():
    r=True
    world.fill((51, 172, 221))
    #world.blit(sky,(0,0))
    world.blit(clound,(10,20))
    world.blit(clound,(130,150))
    world.blit(clound,(400,30))
    world.blit(clound,(300,200))
    world.blit(clound,(260,20))
    #world.blit(bulite,(0,0))
    player=pygame.image.load("C:\\Users\\DELL\\Downloads\\jet1.png").convert()
    player.set_colorkey((255,255,255),RLEACCEL)

    world.blit(player,(100,300))
    world.blit(misile,(300,320))
    world.blit(misile,(100,100))
    world.blit(misile,(200,200))
    world.blit(misile,(400,150))
    world.blit(misile,(150,400))
    world.blit(text1,(100,450))
    world.blit(text2,(100,480))
    i=True
    while r:
        
        for event in pygame.event.get():
            if(event.type==KEYDOWN):
                if(event.key==pygame.K_INSERT ):
                    r=False

            if (event.type==QUIT):
                r=False
                i=False        
        pygame.display.flip()
    return i                        
class cloud(pygame.sprite.Sprite):
     def __init__(self):
         super(cloud,self).__init__()
         self.surf=pygame.image.load("C:\\Users\\DELL\\Downloads\\cloud.png").convert()
         #self.surf.set_colorkey((0, 0, 0), RLEACCEL)
         self.rect=self.surf.get_rect(
                 center = (random.randint(20+screenx,100+screenx),
             random.randint(0,screeny)
         )
         )
     def update(self):
         self.rect.move_ip(-5, 0)
         if self.rect.right < 0:
             self.kill()
class player(pygame.sprite.Sprite):
    def __init__(self):
        super(player,self).__init__()
        self.surf = pygame.image.load("C:\\Users\\DELL\\Downloads\\jet1.png").convert()
        self.surf.set_colorkey((255,255,255),RLEACCEL)
        self.rect = self.surf.get_rect()
    def update(self,pressed_key):
        if pressed_key[K_UP]:
            self.rect.move_ip(0,-5)
            pygame.display.flip()
        elif pressed_key[K_DOWN]:
            self.rect.move_ip(0,5)
            pygame.display.flip()
        elif pressed_key[K_LEFT]:
            self.rect.move_ip(-5,0)
            pygame.display.flip()
        elif pressed_key[K_RIGHT]:
            self.rect.move_ip(5,0)
            pygame.display.flip()
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>screenx:
            self.rect.right=screenx
        if self.rect.top<=0:
            self.rect.top=0
        if self.rect.bottom>=screeny:
            self.rect.bottom=screeny 
        if self.rect.right==screenx:
            self.rect.right=0       
class enemy(pygame.sprite.Sprite):
     def __init__(self):
         super(enemy,self).__init__()
         self.surf = pygame.image.load("C:\\Users\\DELL\\Downloads\\image.png").convert()
         self.surf.set_colorkey((255, 255, 255),pygame.SRCALPHA)

         self.rect=self.surf.get_rect(
                 center= (random.randint(20+screenx,100+screenx),
             random.randint(0,screeny)
         )
         )             
         self.speed = random.randint(5,20)
     def update(self):
         self.rect.move_ip(-(self.speed),0)
         if self.rect.right<0:
             self.kill()
            
#bullete function
class Bullete_B(pygame.sprite.Sprite):
    def __init__(self,x):
        super(Bullete_B,self).__init__()
        self.surf=pygame.image.load("C:\\Users\\DELL\\Downloads\\b4.png").convert_alpha()
        if self.surf.get_colorkey() is not None:
            self.surf.set_colorkey(self.surf.get_colorkey())
        loadcolor=  self.surf.get_colorkey()
        print(loadcolor)  
        #self.surf.set_colorkey((255,255,255),pygame.SRCALPHA)
        y=x[0]
        k=x[1]
        self.rect=self.surf.get_rect(center=(y+70,k+20))
        self.speed=8
    def update(self):
        self.rect.move_ip(self.speed,0)
        if self.rect.right<0:
            self.kill()    
#all_sprite.add(e) 
def game_over(k):
     t=True
     font=pygame.font.SysFont("bold", 1000)
     text1=font1.render(f"SCORE {k}",True,(12,30,20))
     text2=font1.render(f"MANU",True,(12,30,20))
     while t:
        for event in pygame.event.get():
            if event.type==QUIT:
                t=False
            if event.type==KEYDOWN:
                if event.key==K_UP:
                    t=False     
        world.blit(over,(150,150))
        world.blit(text1,(200,300))
        pygame.display.flip()
    
def main_function(r):
    enimes=pygame.sprite.Group()
    bullets=pygame.sprite.Group()
    all_sprite=pygame.sprite.Group()
    clouds=pygame.sprite.Group() 
    ADDENEMY=pygame.USEREVENT+1
    pygame.time.set_timer(ADDENEMY,250) 
    ADDCLOUD=pygame.USEREVENT+2
    pygame.time.set_timer(ADDCLOUD,1000)
    p=player()
    all_sprite.add(p)
    font=pygame.font.SysFont("Times new Roman", 50)
    i=1
    text=font.render(f"{i}",True,(200,30,20))
    while(r):
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #i=i+1
                text=font.render(f"{i}",True,(200,30,20))
                if(event.key ==pygame. K_ESCAPE):
                    r = False
                if(event.key ==pygame.K_SPACE):
                    print("hello")
                    newbullete=Bullete_B(p.rect)
                    bullets.add(newbullete)
                    all_sprite.add(newbullete)        
            elif event.type == pygame.QUIT:
                r = False
            elif event.type == ADDENEMY:
                newenemy=enemy()
                enimes.add(newenemy)
                all_sprite.add(newenemy)
            elif event.type == ADDCLOUD:
                newcloud=cloud()
                clouds.add(newcloud)
                all_sprite.add(newcloud)         
        pressed_key=pygame.key.get_pressed()
        p.update(pressed_key)    
        enimes.update()    
        clouds.update()
        bullets.update()  
        world.fill((51, 172, 221))
        for entity in all_sprite:

            world.blit(entity.surf,entity.rect)
        if pygame.sprite.spritecollideany(p,enimes):
            p.kill()
            r=False 
        if(pygame.sprite.groupcollide(enimes,bullets,True,True,None)):
            i=i+1        
        world.blit(text,(0,0))      
        pygame.display.flip()
        clock.tick(50)
        pygame.display.flip()
    
    text=font.render(f"{i}",True,(200,30,20))
    world.blit(text,(200,200))    
    time.sleep(1)
    return i       
if __name__ == "__main__":
    pygame.display.set_caption('funbuz')
    while running:
        r=welcome()
        if(r):
            k=main_function(r)
            game_over(k)
        else:
            running=False    
