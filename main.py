import pygame 

pygame.init()
back = (0,255,255)
mw = pygame.display.set_mode((500,500))
mw.fill((back))

clock = pygame.time.Clock()

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color
 
    def color(self, new_color):
        self.fill_color = new_color
 
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
 
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)       
 
    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        super().__init__(x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
      
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


start_x = 5
start_y = 5
c_enemy = 9
l_enemy = []

for row in range(3):
    x = start_x + 27.5 * row
    y = start_y + 55 * row
    for n_enemy in range(c_enemy):
        l_enemy.append(Picture('enemy.png', x,y,50,50))
        x += 55
    c_enemy -= 1

platform_x = 200
platform_y = 330

platform = Picture('platform.png', platform_x,platform_y,100,30)
ball = Picture('ball.png', 160,200,50,50)


dx = 3
dy = 3

move_right = False
move_left = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    move_right = False
                if event.key == pygame.K_LEFT:
                    move_left = False
    if move_left:
        platform_x -= 5
    
    if move_right:
        platform_x += 5

    platform.rect.x = platform_x

    ball.rect.x += dx
    ball.rect.y += dy

    if ball.colliderect(platform.rect):
        dy *= -1

    if ball.rect.y < 0:
        dy *= -1

    if ball.rect.x > 450 or ball.rect.x < 0:
        dx *= -1

    mw.fill((back))

    for enemy in l_enemy:
        enemy.draw()
        if enemy.colliderect(ball.rect):
            l_enemy.remove(enemy)


    platform.draw()
    ball.draw()


    pygame.display.update()
    clock.tick(30)
