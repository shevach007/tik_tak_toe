import pygame
from time import sleep
import random
pygame.init()
win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("first game")

walkRight = [pygame.image.load('viking run_run_0.png'), pygame.image.load('viking run_run_1.png'),
             pygame.image.load('viking run_run_2.png'), pygame.image.load('viking run_run_3.png'),
             pygame.image.load('viking run_run_4.png'), pygame.image.load('viking run_run_5.png')]
walkLeft = [pygame.image.load('viking run_run_left_0.png'), pygame.image.load('viking run_run_left_1.png'),
            pygame.image.load('viking run_run_left_2.png'), pygame.image.load('viking run_run_left_3.png'),
            pygame.image.load('viking run_run_left_4.png'), pygame.image.load('viking run_run_left_5.png')]
bg = pygame.image.load('maxresdefault.jpg')
idleStand = [pygame.image.load('viking idle_idle_0.png'), pygame.image.load('viking idle_idle_1.png'),
             pygame.image.load('viking idle_idle_2.png'), pygame.image.load('viking idle_idle_0.png'),
             pygame.image.load('viking idle_idle_1.png'), pygame.image.load('viking idle_idle_2.png'),
             pygame.image.load('viking idle_idle_0.png'), pygame.image.load('viking idle_idle_1.png'),
             pygame.image.load('viking idle_idle_2.png'), pygame.image.load('viking idle_idle_0.png'),
             pygame.image.load('viking idle_idle_1.png'),pygame.image.load('viking idle_idle_2.png')]
idleStandLeft = [pygame.image.load('viking idle_idle_left_0.png'), pygame.image.load('viking idle_idle_left_1.png'),
                 pygame.image.load('viking idle_idle_left_2.png'), pygame.image.load('viking idle_idle_left_0.png'),
                 pygame.image.load('viking idle_idle_left_1.png'), pygame.image.load('viking idle_idle_left_2.png'),
                 pygame.image.load('viking idle_idle_left_0.png'), pygame.image.load('viking idle_idle_left_1.png'),
                 pygame.image.load('viking idle_idle_left_2.png'), pygame.image.load('viking idle_idle_left_0.png'),
                 pygame.image.load('viking idle_idle_left_1.png'),pygame.image.load('viking idle_idle_left_2.png')]
bulletSound = pygame.mixer.Sound('bullet.wav')
hit = pygame.mixer.Sound('hit.wav')
jump = pygame.mixer.Sound('jump.wav')
running = pygame.mixer.Sound('run.wav')
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

class Projectile:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * self.facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y + 20), self.radius)

class Enemy():
    walkRightEnemy = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                 pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                 pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),
                 pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeftEnemy = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),
                pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.path = (self.x, self.end)
        self.vel = 3
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.health = 9
        self.visable = True

    def draw(self, win):
        self.move()
        if self.visable:
            if self.walkCount + 1 > 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRightEnemy[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeftEnemy[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            self.hitbox = (self.x + 20, self.y, 28, 60)
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 20, 55 - (5 * (10 - self.health)), 10))
            #pygame.draw.rect(win, (255, 0, 0), (self.x + 20, self.y, 28, 60), 2)
        else:
            self.health = 10
            self.x = random.randint(200, 1000)
            self.visable = True



    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x -self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
            if self.health > 0:
                self.health -= 1
            else:
                self.visable = False
            print("hit")



clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.val = 5
        self.jumpCount = 10
        self.isJmp = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standCounter = 0
        self.flag = True
        self.flag1 = False
        self.hitbox = (self.x + 20, self.y, 28, 30)

    def draw(self, win):

        if self.flag and not self.right:
            win.blit(idleStand[self.standCounter // 6], (self.x, self.y))
            self.standCounter += 1
            if self.standCounter == 11:
                self.standCounter = 0

        elif self.flag1 and not self.left:
            win.blit(idleStandLeft[self.standCounter // 6], (self.x, self.y))
            self.standCounter += 1
            if self.standCounter == 11:
                self.standCounter = 0

        elif self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            if self.walkCount == 5:
                self.walkCount = 0

        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            if self.walkCount == 5:
                self.walkCount = 0

        self.hitbox = (self.x + 15, self.y + 35, 28, 30)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        self.x = random.randint(0, 1200)
        #self.y = 600
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255, 0, 0))
        win.blit(text, (250 - (text.get_width() / 2), 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
class Surface:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x + self.width, self.height + self.y, 200, 30)
    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 255), self.hitbox, 10)

def redrawGameWindow():
    win.blit(bg, (0, 0))
    text = font.render('score: ' + str(score), True, (0, 0, 0))
    win.blit(text, (1150, 30))
    surf1.draw(win)
    surf2.draw(win)
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


font = pygame.font.SysFont('comicsans', 30, True)
man = Player(0, 600, 64, 64)
surf1 = Surface(100, 500, 200, 30)
surf2 = Surface(400, 200, 100, 30)
goblin = Enemy(200, 610, 64, 64, 800)
bullets = []
shootloop = 1
score = 0
run = True
while run:
    clock.tick(27)
    man.left = False
    man.right = False
    if goblin.visable:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score -= 5

    if shootloop > 0:
        shootloop += 1
    if shootloop > 3:
        shootloop = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if goblin.visable:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    goblin.hit()
                    hit.play()
                    score += 1
                    bullets.pop(bullets.index(bullet))

        if 1280 > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootloop == 0:
        if man.left or man.flag1:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bulletSound.play()
            bullets.append(Projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0),
                                      facing))
        shootloop = 1

    if keys[pygame.K_LEFT]:
        man.left = True
        man.right = False
        man.flag1 = True
        man.flag = False
        if man.x >= 0:
            #running.play()
            man.x -= man.val

    elif keys[pygame.K_RIGHT]:
        man.right = True
        man.left = False
        man.flag = True
        man.flag1 = False
        if man.x <= 1240:
            #running.play()
            man.x += man.val
    else:
        man.walkCount = 0






    if not man.isJmp:

        if keys[pygame.K_UP]:
            jump.play()
            man.isJmp = True
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= neg * (man.jumpCount ** 2) * 0.5
            man.jumpCount -= 1
        else:
            man.isJmp = False
            man.jumpCount = 10


    redrawGameWindow()

pygame.quit()
