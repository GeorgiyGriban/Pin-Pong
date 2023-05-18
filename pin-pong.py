import pygame
pygame.init()

#переменные
WIDTH = 500
HEIGHT = 500
game = True
#key = []
margin = 50
speed_paddle = 5
speed_ball_x = 3
speed_ball_y = 3
player1_score = 0
player2_score = 0
winner = 0
pause = True
font1 = pygame.font.Font(None, 25)
#цвета
BG_COLOR = (60, 114, 228)
TEXT_COL = (246, 247, 246)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(BG_COLOR)
clock = pygame.time.Clock()
class PADDLE:
    def __init__(self, x, y, width=20, height=100, color= WHITE):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    def draw(self):
            pygame.draw.rect(window, self.color, self.rect)
    
class BALL():
        def __init__(self, x, y, size = 10):
            self.ball_size = size
            self.rect = pygame.Rect(x, y, self.ball_size, self.ball_size)
        def draw(self):
            pygame.draw.circle(window, WHITE, (self.rect.x + self.ball_size//2, self.rect.y + self.ball_size//2), self.ball_size)
        def colliderect(self, rect_player):
            return self.colliderect(rect_player)
def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        window.blit(img, (x, y))
player1 = PADDLE(20, 200, 20, 100, WHITE)
player2 = PADDLE(460, 200, 20, 100, WHITE)
ball = BALL(250, 250, 10)
while game:
    window.fill(BG_COLOR)
    pygame.draw.line(window, WHITE, (0, margin), (WIDTH, margin), 2)
    draw_text('Игрок 1: ' + str(player1_score), font1, WHITE, 20, 15)
    draw_text('Игрок 2: ' + str(player2_score), font1, WHITE, WIDTH - 140, 15)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN and pause == True:
                pause = False
                ball.rect.x = WIDTH//2
                ball.rect.y = HEIGHT//2
    
    if not pause:
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and player2.rect.top > margin:
            player2.rect.y -= speed_paddle
        if key[pygame.K_DOWN] and player2.rect.bottom < HEIGHT:
            player2.rect.y += speed_paddle
        if key[pygame.K_w] and player1.rect.top > margin:
            player1.rect.y -= speed_paddle
        if key[pygame.K_s] and player1.rect.bottom < HEIGHT:
            player1.rect.y += speed_paddle
        
        
        if ball.rect.top < margin or ball.rect.bottom > HEIGHT:
            speed_ball_y *= -1
        if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
            speed_ball_x *= -1
        ball.rect.x += speed_ball_x
        ball.rect.y += speed_ball_y
        
        if ball.rect.left < 0:
            winner = 2
            player2_score += 1
            pause = True
        if ball.rect.right > WIDTH:
            winner = 1
            player1_score += 1
            pause = True
        ball.draw()
        player1.draw()
        player2.draw()
    
    if pause:
        if winner == 0:
            draw_text('Кликни по экрану, чтобы начать играть', font1, WHITE, 100, HEIGHT // 2 -100)
        if winner == 1:
            draw_text('Игрок 1 выйграл!', font1, WHITE, 150, HEIGHT // 2)
            draw_text('Кликни по экрану', font1, WHITE, 150, HEIGHT // 2 + 40)
        if winner == 2:
            draw_text('Игрок 2 выйграл!', font1, WHITE, 150, HEIGHT//2)
            draw_text('Кликни по экрану', font1, WHITE, 150, HEIGHT // 2 +40)
    pygame.display.update()
    clock.tick(45)