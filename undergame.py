# Example file showing a basic pygame "game loop"
import pygame
import random
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
running = True

PURPLE = pygame.Color(150,30,245)
BLACK = pygame.Color(0,0,0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
GREEN = pygame.Color(0,255,0)
YELLOW = pygame.Color(255,255,0)



allThings = []

class Player:
    def __init__(self, rectangle, image, speed):
        allThings.append(rectangle)
        self.rectangle=rectangle
        self.image=pygame.image.load(image)
        self.image=pygame.transform.scale(self.image, (rectangle.width, rectangle.height))
        self.speed = speed
        self.color=PURPLE
        self.colliding=False

    def collidingWith(self, rect2):
        rect=self.rectangle
        if rect.x<=(rect2.x+rect2.width) and (rect.x+rect.width)>=rect2.x and rect.y<=(rect2.y+rect2.height) and (rect.y+rect.height)>=rect2.y:
            return True
            

    def move_left(self):
        self.rectangle.x-=self.speed
    def move_right(self):
        self.rectangle.x+=self.speed
    def move_up(self):
        self.rectangle.y-=self.speed
    def move_down(self):
        self.rectangle.y+=self.speed
        
    def move(self):
        keys_down=pygame.key.get_pressed()

        if keys_down[pygame.K_LEFT]:
            self.move_left()
        if keys_down[pygame.K_RIGHT]:
            self.move_right()
        if keys_down[pygame.K_UP]:
            self.move_up()
        if keys_down[pygame.K_DOWN]:
            self.move_down()
            
        self.colliding=False
        for r in allThings:
            if r!=self.rectangle and self.collidingWith(r):
                self.colliding=True

    def move2(self):
        keys_down=pygame.key.get_pressed()

        if keys_down[pygame.K_a]:
            self.move_left()
        if keys_down[pygame.K_d]:
            self.move_right()
        if keys_down[pygame.K_w]:
            self.move_up()
        if keys_down[pygame.K_s]:
            self.move_down()

        self.colliding=False
        for r in allThings:
            if r!=self.rectangle and self.collidingWith(r):
                self.colliding=True

    def draw(self, screen):
        rect=self.rectangle
        if self.colliding:
            color=YELLOW
        else:
            color=PURPLE
        pygame.draw.rect(screen, color, rect)
        screen.blit(self.image, (rect.x, rect.y))

class Enemy:
    boxes=[]
    def __init__(self,x,y,size, image):
        self.x=x
        self.y=y
        self.size=size
        self.waitTime=50
        self.image=pygame.image.load(image)
        self.image=pygame.transform.scale(self.image, (self.size, self.size))

    def attack(self):
        boxes=[]
        start=["LEFT", "UP", "RIGHT", "DOWN"]
        if self.waitTime>0:
            self.waitTime-=1
            return
        else:
            self.waitTime=50
        
        num=random.randint(1,4)
        if num==1:
            print(num)
        if num==2:
            print(num)
        if num==3:
            print(num)
        if num==4:
            print(num)
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    
            

class Box:
    def __init__(self, x, y):
        self.damage=5

    def go_up(self):
    def go_down(self):
    def go_left(self):
    def go_right(self):

    
    

enemy = Enemy(300,400,200,"assets/EnemyBox4.png")   
    


player1= Player(pygame.Rect(100,100,25,25), "assets/blueSOUL.png", 4)
player2= Player(pygame.Rect(400,100,25,25), "assets/redSOUL.png", 4)
allThings.append(pygame.Rect(300,200,100,100))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # UPDATE
    player1.move2()
    player2.move()
    enemy.attack()
    
    # DRAW
    screen.fill(BLACK)

    pygame.draw.rect(screen, GREEN, allThings[2])
    player1.draw(screen)
    player2.draw(screen)
    enemy.draw(screen)
    
    
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()