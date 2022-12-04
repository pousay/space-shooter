#import
import random
import pygame
from pygame import mixer
import math
#start the pygame
init = pygame.init()


#make the screen
#window height,width
screen = pygame.display.set_mode((800,600))
#window name,icon , ...
pygame.display.set_caption("HeHe")
icon = pygame.image.load("photos\spaceship.png")
pygame.display.set_icon(icon)

#add background image
bg = pygame.image.load("photos\Bg.png")
#player
playerimg = pygame.image.load("photos\spaceship1.png")
playerx = 370
playery = 510
playerx_change = 0 
playery_change = 0



#sounds
    #bg sounds
mixer.music.load("sounds\Background.wav")
mixer.music.play(-1)


#enemy
#multiply enemies
enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 10

for i in range(num_of_enemies) :
#one enemy
    enemyimg.append(pygame.image.load("photos\enemy.png"))
    enemyx.append(random.randint(5,730))
    enemyy.append(random.randint(20,160))
    enemyx_change.append(2)
    enemyy_change.append(45)


#bullet
bulletimg = pygame.image.load("photos\Bullet.png")
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 10
bullet_state = "Ready"


#score
score = 0
font = pygame.font.Font("font\FreeSansBold.ttf",15)
textX = 10
textY = 10

#show score
def showScore(x,y) :
    scored = font.render(f"score : {str(score)}",True,(255,255,255))
    screen.blit(scored,(x,y))

#gameover text
GO = pygame.font.Font("font\FreeSansBold.ttf",70)

#gameover

def GameOver() :
    gameover = GO.render("GAME OVER",True,(255,255,255))
    screen.blit(gameover,(180,250))


#player function
def player(x,y):
    screen.blit(playerimg,(x,y))
    
#enemy func
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

def bullet(x,y) :
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg,(x + 16, y + 10))

def iscol(enemyx, enemyy, bulletx , bullety):
    distance = math.sqrt((math.pow(enemyx - bulletx , 2))+ (math.pow(enemyy- bullety,2)))
    if distance < 27 :
        return True
    else: 
        return False
#infinity running 
#point    all things might be called or written in this 
gotext = True
run = True
while run :
    
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                playerx_change = -4
            elif event.key == pygame.K_RIGHT :
                playerx_change = 4
            if event.key ==  pygame.K_SPACE :
                if bullet_state is "Ready" :
                    bulletsound = mixer.Sound("sounds\Laser.wav")
                    bulletsound.play()
                    bulletx = playerx
                    bullet(playerx,bullety)   
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT :
                playerx_change = 4
            elif event.key == pygame.K_LEFT :
                playerx_change = -4

            
    # change colors by RGB (Red  Green  Blue)
    screen.blit(bg,(0,0))
    
    #get the keys
        
    
    #enemy movement
    for i in range(num_of_enemies):
        if enemyy[i] > 440 :
            if gotext :
                
                goSound = mixer.Sound("sounds\gameover.wav")
                goSound.play()
                mixer.music.stop()
                
                gotext = False
            for j in range(num_of_enemies):
                enemyy[j] = 2000
                   
            GameOver()
            
        
    
                        

        enemyx[i] += enemyx_change[i]
        if enemyx[i] <=  5 :
            enemyx_change[i] = random.randint(1,3)
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 730:
            enemyx_change[i] = random.randint(-3,-1)
            enemyy[i] += enemyy_change[i]

        #col
        colis = iscol(enemyx[i],enemyy[i],bulletx,bullety)
        if colis : 
            expSound = mixer.Sound("sounds\Explosion.wav")
            expSound.play()
            score += 1
            enemyx[i] = random.randint(5,730)
            enemyy[i] = random.randint(20,160)


        enemy(enemyx[i],enemyy[i],i)



    #add  player movement
    playerx += playerx_change
    if playerx <= 0 :
        playerx = 0
    elif playerx >= 735:
        playerx = 735
        #call a func
    player(playerx,playery)
    
    

    #bullet movement
    if bullety <= 0 :
        bullety = 550
        bullet_state = "Ready"
    if bullet_state is "fire" :
        bullet(bulletx,bullety)
        bullety -= bullety_change
    
    showScore(textX,textY)


    # #col
    # colis = iscol(enemyx,enemyy,bulletx,bullety)
    # if colis :
    #     score += 1
    #     print(score)
    #     enemyx = random.randint(5,730)
    #     enemyy = random.randint(20,160)
    #after every update need to call this to set new thing
    #point   its better to call it at the end 
    pygame.display.update()