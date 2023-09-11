import pygame
import random
from sys import exit
pygame.init()

WIDTH = 800
HEIGHT = 400

my_font = pygame.font.Font(r'C:\Users\sohai\OneDrive\Desktop\All About Programming\Pygame Course\UltimatePygameIntro-main\font\Pixeltype.ttf',50)

player1_score = 0
player2_score = 0
def display():
    global ball_speed
    global player1_score
    global player2_score
    player1_score_text = my_font.render(f"{player1_score}",False,'green')
    player2_score_text = my_font.render(f"{player2_score}",False,'green')
    screen.blit(player1_score_text,(200,50))
    screen.blit(player2_score_text,(600,50))
    if ball.x > 810:
            ball.x = WIDTH//2 - 9
            ball.y = HEIGHT//2
            ball_speed = -5
            player1_score +=1
            player1_score_text = my_font.render(f"{player1_score}",False,'green')
            screen.blit(player1_score_text,(200,50))
    if ball.x < -5:
        ball.x = WIDTH//2 - 9
        ball.y = HEIGHT//2
        ball_speed = 5
        player2_score +=1
        player2_score_text = my_font.render(f"{player2_score}",False,'green')
        screen.blit(player2_score_text,(600,50))
    
    


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

player_1 = pygame.Rect(100, 150, 10, 100)

player_2 = pygame.Rect(700, 150, 10, 100)

ball = pygame.Rect(WIDTH//2 - 9, HEIGHT//2, 20, 20)

player1_win_screen = my_font.render("Player One Wins",False,"White")
player2_win_screen = my_font.render("Player Two Wins",False,"White")

clock = pygame.time.Clock()

start_screen_text1 = my_font.render("My Ping Pong Game",False,'White')
start_screen_text2 = my_font.render("Press 'Space' To Start ",False,'White')
move_up = False
move_down = False

move_W = False
move_S = False

running = False

ball_moving = False

# Adjust the speed for smoother movement
speed = 8
ball_y = 0
ball_speed = 5
ball_start_direction = random.choice([ball_speed,ball_speed * -1])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if running == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_up = True
                if event.key == pygame.K_DOWN:
                    move_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    move_up = False
                if event.key == pygame.K_DOWN:
                    move_down = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    move_W = True
                if event.key == pygame.K_s:
                    move_S = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    move_W = False
                if event.key == pygame.K_s:
                    move_S = False
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = True
                ball.x += ball_start_direction
                ball_moving = True
                player2_score = 0
                player1_score = 0
    
    if running:
        
        if move_up and player_2.top > 0:
            player_2.y -= speed
        if move_down and player_2.bottom < 400 :
            player_2.y += speed

        if move_W and player_1.top > 0:
            player_1.y -= speed
        if move_S and player_1.bottom < 400 :
            player_1.y += speed
        
        
        
        if player_1.colliderect(ball):
            ball_speed = 11
            ball_y = random.choice([-5,5])
        if player_2.colliderect(ball):
            ball_speed = -11
            ball_y = random.choice([-5,5])
        
        if ball.y > 380:
            ball_y = -5
        if ball.y < 5 : 
            ball_y = 5
        
        screen.fill('blue')
        display()
        pygame.draw.line(screen, 'green', (400, 0), (400, 400), width=4)
        pygame.draw.rect(screen, 'red', player_1)
        pygame.draw.rect(screen,'red', player_2)
        
        pygame.draw.ellipse(screen, pygame.Color('red'), ball)
        
        if player1_score == 11:
            running = False
            screen.fill('Blue')
            screen.blit(player1_win_screen,(WIDTH//4 + 40,HEIGHT//4))
            screen.blit(start_screen_text2,(WIDTH//4 + 30,HEIGHT//4 + 150)) 
        elif player2_score == 11:
            running = False
            screen.fill('Black')
            screen.blit(player2_win_screen,(WIDTH//4 + 40,HEIGHT//4))
            screen.blit(start_screen_text2,(WIDTH//4 + 30,HEIGHT//4 + 150)) 
        
        
        if ball_moving:
            ball.x += ball_speed
            ball.y += ball_y
            
    elif running == False and player1_score == 0 and player2_score == 0:
        screen.fill('Black')
        screen.blit(start_screen_text1,(WIDTH//4 + 40,HEIGHT//4))
        screen.blit(start_screen_text2,(WIDTH//4 + 30,HEIGHT//4 + 150))    
    
    pygame.display.update()
    clock.tick(60)


