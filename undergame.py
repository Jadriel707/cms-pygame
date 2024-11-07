# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

PURPLE=pygame.Color(150,30,245)
BLACK= pygame.Color(0,0,0)


class Player:
    def __init__(self, rectangle, image, speed):
        self.rectangle=rectangle
        self.image=pygame.image.load(image)
        self.image=pygame.transform.scale(self.image, (rectangle.width, rectangle.height))
        self.speed = 5

    

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


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # UPDATE

    # DRAW
    screen.fill(PURPLE)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()