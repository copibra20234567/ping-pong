from pygame import *
class Sprite:
    def __init__(self, x, y, filename, speed, w, h):
        self.image = transform.scale(image.load(filename), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, window):
        window.blit(self.image, ( self.rect.x,  self.rect.y))


class Player(Sprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
        if keys[K_d]:
            self.rect.x += self.speed
            

class Bot(Sprite):
    def __init__(self, x, y, filename, speed, w, h, startX, finishX):
        super().__init__(x, y, filename, speed, w, h)
        self.startX = startX
        self.finishX = finishX

    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= self.finishX:
            self.speed *= -1
        if self.rect.x <= self.startX:
            self.speed *= -1

def gameOver(screen, text):
    myfont = font.Font(None, 36).render(text, True, (0, 0, 0))
    clock = time.Clock()
    run = True
    while run:
        #події
        for e in event.get():
            if e.type == QUIT:
                run = False


        #оновлення

        #рендер
        screen.blit(myfont,[250,250])
        display.update()
        clock.tick(60)


class Wall:
    def __init__(self, x, y, w, h, color):
        self.image = Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
init()
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play(-1)
kick = mixer.Sound("kick.ogg")
groshi = mixer.Sound("money.ogg")

window = display.set_mode((700, 500))
clock = time.Clock()

walls = []
walls.append(Wall(90, 137, 100, 10, (255, 255, 0)))
walls.append(Wall(180, 0, 10, 138, (255, 255, 0)))
walls.append(Wall(540,165, 10, 65, (255, 255, 0)))
walls.append(Wall(470,0, 10, 150, (255, 255, 0)))
walls.append(Wall(470,100, 150, 10, (255, 255, 0)))


walls.append(Wall(620,100, 10, 50, (255, 255, 0)))
walls.append(Wall(400, 400, 100, 10, (255, 255, 0)))
walls.append(Wall(490, 300, 10, 100, (255, 255, 0)))
walls.append(Wall(600, 300, 10, 1000, (255, 255, 0)))
walls.append(Wall(90, 137, 10, 100, (255, 255, 0)))
walls.append(Wall(305,100, 10, 200, (255, 255, 0)))
walls.append(Wall(305,100, 100, 10, (255, 255, 0)))
walls.append(Wall(305,300, 76, 10, (255, 255, 0)))
walls.append(Wall(90,230, 10, 80, (255, 255, 0)))
walls.append(Wall(200,226, 500, 10, (255, 255, 0)))
walls.append(Wall(90,300, 110, 10, (255, 255, 0)))
walls.append(Wall(200,300, 10, 110, (255, 255, 0)))
walls.append(Wall(90,400, 110, 10 ,(255, 255, 0)))
walls.append(Wall(0, 0, 700, 1, (255, 255, 0)))
walls.append(Wall(0, 0, 1, 500, (255, 255, 0)))
walls.append(Wall(0, 500, 700, 1, (255, 255, 0)))
walls.append(Wall(700, 0, 1, 500, (255, 255, 0)))
walls.append(Wall(200, 400, 200, 10, (255, 255, 0)))




player = Player(10, 10, "hero.png", 5, 50, 50)
gold = Sprite(600, 10, "treasure.png", 0, 50, 50) 
npc = Bot(400, 250, "cyborg.png", 5, 50, 50, 100, 500)

backround = image.load("background.jpg")
run = True
while run:
    #події
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == MOUSEBUTTONUP:
            print(mouse.get_pos())
    #оновлення
    player.update()
    npc.update()

    if player.rect.colliderect(npc.rect):
        kick.play()
        gameOver(window, "ПРОГРАВ!!")
        run = False
    for wall in walls:
        if player.rect.colliderect(wall.rect):
            kick.play()
            gameOver(window, "ПРОГРАВ!!")
            run = False
    if player.rect.colliderect(gold.rect):
        groshi.play()
        gameOver(window, "ВИГРАВ!!")
        run = False

    #рендер
    window.blit(backround, (0,0))
    player.draw(window)
    npc.draw(window)
    gold.draw(window)
    
    for wall in walls:
        wall.draw(window)
  
    display.update()

    clock.tick(60)


