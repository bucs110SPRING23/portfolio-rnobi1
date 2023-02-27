import pygame

pygame.init()

White = (255, 255, 255)
Black = (0, 0, 0)
screen = pygame.display.set_mode((700, 700))

screen.fill(Black)
def snowman (screen, x, y):
    pygame.draw.circle(screen, White, [100+x, 30+y], 40, 0)
    pygame.draw.circle(screen, White, [100+x, 90+y], 55, 0)
    pygame.draw.circle(screen, White, [100+x, 150+y], 70, 0)

snowman(screen, 100, 120)
pygame.display.flip()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()