import pygame, os
import time
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'

display_width = 1000
display_height = 536
black = (0,0,0)
white = (255,255,255)
red = (250,0,0)
grey = (166,175,179)
green = (0, 250, 0)
brightred = (255,0,0)
brightgreen = (0,255,0)
car_width = 150
thing_height = 300
thing_width = 150

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Fast N Furious')
clock = pygame.time.Clock()

carImg = pygame.image.load('Player.png')
car2Img = pygame.image.load('Enemy.png')
back = pygame.image.load('back.jpg').convert()
gameDisplay.blit(back, (0, 0))
def things_dodged(count):
    font = pygame.font.SysFont(None,40)
    text = font.render("Score : "+str(count),True,red)
    gameDisplay.blit(text,(10,10))

def things(thingx,thingy):
    gameDisplay.blit(car2Img,(thingx,thingy))
def carDisplay(x,y):
    gameDisplay.blit(carImg,(x,y))
def text_objects(text,font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1.5)
    game_loop()
def crash():
    message_display('You Crashed!')

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(back, (0, 0))
        largeText = pygame.font.Font('freesansbold.ttf',90)
        TextSurf, TextRect = text_objects("FAST N FURIOUS", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.draw.rect(gameDisplay,red,(675,400,100,60))
        mouse = pygame.mouse.get_pos()
        if 225+100 > mouse[0] > 225 and 400+60 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay,brightgreen,(225,400,100,60))
        else:
            pygame.draw.rect(gameDisplay,green,(225,400,100,60))

        pygame.display.update()
        clock.tick(15)

def game_loop():
    x= (display_width*0.45)
    y= (display_height*0.73)
    x_change = 0
    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 10
    gameExit = False
    dodged = 0
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -20
                elif event.key == pygame.K_RIGHT:
                    x_change = 20
                elif event.key == pygame.K_LEFT and event.key == pygame.K_RIGHT:
                    x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    x_change=0
        x = x + x_change
        ##gameDisplay.fill(grey)
        gameDisplay.blit(back, (0, 0))

        things(thing_startx, thing_starty)
        thing_starty = thing_starty + thing_speed
        carDisplay(x,y)
        things_dodged(dodged)
        if x>display_width - car_width or x<=0:
                crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(30,(display_width-150))
            dodged = dodged +1
            if dodged % 10 == 0:
                thing_speed=thing_speed + 2

        if y < thing_starty+thing_height: #y crossover
            if thing_startx < x + car_width and thing_startx + thing_width > x:
                crash()
            #if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                #x crossover
        pygame.display.update()
        clock.tick(30)
#game_intro()
game_loop()
pygame.quit()
quit()
