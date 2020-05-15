import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((700,700))
image = pygame.image.load('skull.png').convert_alpha()
image = pygame.transform.scale(image,(100,100))
image2 = pygame.image.load('arrow.png').convert_alpha()
image2 = pygame.transform.scale(image2,(200,100)) 
image3 = pygame.image.load('coin.png').convert_alpha()
image3 = pygame.transform.scale(image3,(75,75))
image4 = pygame.image.load('coins.png').convert_alpha()
image4 = pygame.transform.scale(image4,(100,100))

done = False
x = 30
y = 30
pygame.mixer.music.load('pirates_of_caribbean.mp3')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms",25)

def Score(score):
	text = smallfont.render("Score: "+str(score), True, (0,0,0))
	screen.blit(text, [0,0] )

def my_function():
        rect_y = random.randrange(150,550) 
        rect_x = 800
        return [rect_x,rect_y] 

bool1 = True
timer = 0
bool2 = False
[a,b] = my_function()
c = 800
d = 0 
obstable_speed = 2
object_speed = 3

def text_objects(text, font):
	textSurface = font.render(text, True,(0,0,0))
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = (350,350)
	screen.blit(TextSurf, TextRect)
	Score(score)
	pygame.display.flip()
	time.sleep(5)

def crash():
	message_display('You crashed')

timer_for_coin = 0
timer_for_coins = 0
x_coin = random.randrange(50,650)
y_coin = random.randrange(50,650)
x_coins = random.randrange(50,650)
y_coins = random.randrange(50,650)
coins = False
coin = False
score =0 

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                         done = True
        timer_for_coin+=1
        timer_for_coins+=1
        if timer <= 150:
                timer+=1
        if timer > 150: 
                bool2 = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
        	if y-object_speed>=0:
        		y-= object_speed  
        if pressed[pygame.K_DOWN]: 
        	if y+object_speed+100<=700:  
        		y += object_speed
        if pressed[pygame.K_LEFT]: 
        	if x-object_speed>=0:
        		x -= object_speed
        if pressed[pygame.K_RIGHT]: 
        	if x+object_speed+100<=700:
        		x += object_speed

        screen.fill((255, 255, 255))

        if timer_for_coin == 100:
        	coin = True
        	x_coin = random.randrange(50,650)
        	y_coin = random.randrange(50,650)

        if timer_for_coin <= 300 and coin == True:
        	screen.blit(image3,(x_coin,y_coin,100,100))
        	if timer_for_coin == 300:
        		coin = False
        		timer_for_coin = 0
        
        if timer_for_coins == 400:
        	coins = True
        	x_coins = random.randrange(100,600)
        	y_coins = random.randrange(100,600)

        if timer_for_coins <= 600 and coins == True:
        	screen.blit(image4,(x_coins,y_coins,100,100))
        	if timer_for_coins == 600:
        		coins = False
        		timer_for_coins = 0

        screen.blit(image,(x,y,10,10))

        if (abs(x_coins - x) <= 30 and abs(y_coins - y) <= 30 and coins ==True and timer_for_coins<=600):
	       	coins = False
	       	timer_for_coins = -100
	       	score+=5
	        
        if ( abs(x_coin - x) <= 30 and abs(y_coin-y) <= 30 and coin == True and timer_for_coin <=300):
	       	coin = False
	       	timer_for_coin = -50
	       	score+=1

        if bool1:
                while (a<=-200):
                	[a,b] = my_function()
                screen.blit(image2,(a,b,100,100))
                a-=obstable_speed
        if bool2:
                while (c<=-200):
                        [c,d] = my_function()
                screen.blit(image2,(c,d,100,100))
                c-=obstable_speed
      
        if ((( abs(x-c)<80 or  (x-c<180 and x>c) )  and abs(y-d)<40 ) or (  ( abs(x-a) <80 or (x -a < 180 and x > a) ) and abs(y-b)<40)):
        	crash()
        	done = True

        if obstable_speed < 8:
        	obstable_speed+=0.002
        if object_speed < 8.5:
        	object_speed+=0.002
        
        Score(score)
        pygame.display.flip()
        clock.tick(60)
