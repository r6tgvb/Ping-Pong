from pygame import *
from random import randint
font.init()
font = font.SysFont(None, 30)

global score
score = str()

class GameSprite(sprite.Sprite):
    def __init__(self, spr_image, spr_x, spr_y, spr_speed):
        super().__init__()
        self.image = transform.scale(image.load(spr_image), (65, 65))
        self.speed = spr_speed
        self.rect = self.image.get_rect()
        self.rect.x = spr_x
        self.rect.y = spr_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, spr_image, spr_x, spr_y, spr_speed):
        GameSprite.__init__(self, spr_image, spr_x, spr_y, spr_speed)
    def move_up(self):
            self.rect.y -= self.speed
    def move_down(self):
            self.rect.y += self.speed

player1 = Player('player1.png', 30, 430, 5)
w_w = 700
w_h = 500
window = display.set_mode((w_w, w_h))

fps = 60
clock = time.Clock()

playing = True
while playing:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            playing = False
    player1.reset()
    display.update()
    clock.tick(fps)