import random 
import math 
import pygame

pygame.init()

#dartboard screen 
screen_width = 800
screen_length = 800
window = pygame.display.set_mode([screen_width, screen_length]) 
window.fill([100,149,237])
pygame.draw.circle(window,[255,181,197],(400,400), 400, 0)
pygame.draw.circle(window,[0,0,0],(400,400), 400, 2)
pygame.draw.line(window, [0,0,0], (0,400), (800,400), 2)
pygame.draw.line(window, [0,0,0], (400,0), (400,800), 2)
pygame.display.flip()

#random coordinates 
def throw_dart():   
  cord_x = random.randrange(0, 800)
  cord_y = random.randrange(0, 800)
  return (cord_x,cord_y)

def is_in_circle(x,y):
  distance_from_center = math.hypot(400-x, 400-y)
  if distance_from_center < screen_width/2:
    return True 
  else:
    return False

turns = 0
for i in range(10):
  x1,y1 = throw_dart()
  if is_in_circle(x1,y1):
    pygame.draw.circle(window, [255,255,255], (x1,y1), 5, 0)
  else:
    pygame.draw.circle(window, [255,255,0], (x1,y1), 5, 0)
  pygame.display.flip()
  turns += 1

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()