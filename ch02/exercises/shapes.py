import pygame

White = (255, 255, 255)
Black = (0, 0, 0)
screen = pygame.display.set_mode((700, 700))

def snowman (screen, x, y):
    pygame.draw.circle(screen, White, [60+x, 50+y], 15)
    pygame.draw.circle(screen, White, [60+x, 80+y], 20)
    pygame.draw.circle(screen, White, [60+x, 100+y], 30)

pygame.init()

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
    screen.fill(Black)
    pygame.display.update()
    clock.tick(60)

pygame.quit()