from pygame import *
from random import randint

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Pym pam')
background = transform.scale(image.load('bg.jpg'), (win_width, win_height))

mixer.init()
font.init()

game = True
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_height, player_width, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

lost = 0


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

player = Player('rok.png', 0, 250, 100, 150, 10)
player2 = Player2('rok.png', 550, 250, 100, 150, 10)
bullets = sprite.Group()



font1 = font.Font(None, 36)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
    window.blit(background, (0, 0))
    if lost == 3:
        game = False
    player.reset()
    player.update()
    player2.reset()
    player2.update()
    display.update()
    clock.tick(60)