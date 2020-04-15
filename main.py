import pygame
import random
import math
#Initialize pygame
pygame.init()

#create the screen

screen = pygame.display.set_mode((800,600))

running = True
#Title
pygame.display.set_caption("Space Raiders")
#Icon
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

#loading the image of the player
playerImage = pygame.image.load('player.png')

#loading background
background = pygame.image.load('background.jpg')
#setting the axes of the player
playerX = 370
playerY = 480
playerX_change = 0

#function to create player
def player(x,y):
    #blit is to draw the image on the screen
    screen.blit(playerImage,(x,y))

alienImage = []
alienX = []
alienY = []
alienX_change = []
alienY_change = []
no_of_aliens = 6

for i in range(no_of_aliens):

    #loading the image of the alien
    alienImage.append(pygame.image.load('alien.png'))

    #setting the axes of the alien
    alienX.append(random.randint(0,735))
    alienY.append(random.randint(50,150))
    alienX_change.append(3)
    alienY_change.append(40)

#function to create alien
def alien(x,y,i):
    #blit is to draw the image on the screen
    screen.blit(alienImage[i],(x,y))

#loading the image of the alien
bulletImage = pygame.image.load('bullet.png')

#setting the axes of the alien
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage,(x + 16, y + 10))

def isCollision(alienX,alienY,bulletX,bulletY):
    distance = math.sqrt(math.pow((bulletX - alienX),2) + math.pow((bulletY - alienY),2))
    if distance < 27:
        return True
    else:
        return False
#score        
score_value = 0

font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score: "+ str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))

#Game Loop

while running:
    #screen update with color
    screen.fill((128,255,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        #To check whether left or right keystroke has been pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #print("Left arrow pressed")
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                #print("Right arrow pressed")
                playerX_change = 4
            if event.key == pygame.K_s:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
        
        #To check when the keystroke has been released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #print("Keystroke has been released")
                playerX_change = 0
    
    playerX += playerX_change  
    #check for boundaries  
    if playerX < 0:
        playerX = 0
    elif playerX > 730:
        playerX = 730
    
    #check boundaries and movement for alien
    for i in range(no_of_aliens):
        alienX[i] += alienX_change[i]
        if alienX[i] < 0:
            alienX_change[i] = 3
            alienY[i] += alienY_change[i]
        elif alienX[i] > 730:
            alienX_change[i] = -3
            alienY[i] += alienY_change[i]
        
           #collision
        collision = isCollision(alienX[i],alienY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            
            alienX[i] = random.randint(0,735)
            alienY[i] = random.randint(50,150)
        
        alien(alienX[i],alienY[i],i)

    #bullet movement
    if bulletY <=0:
        bulletY = 480
        bullet_state = "ready"


    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -=bulletY_change


    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()
