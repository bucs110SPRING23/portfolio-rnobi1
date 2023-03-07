#Visual studio keeps crashing on me for some reason and I just can't get a hold of whats going on. 
#I kept trying to save and update my code but its literally just not working even when the univeristy desktops
#I'm submitting whatever I had before my laptop crahsed because I can't input anything new which means..
#...I'm missing some components of the lab
#...I'll probably need this week to fix whatever issue this is

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

player_one = {
  "Name": "Player 1",
  "Color": "red",
}
player_two = {
  "Name": "Player 2",
  "Color": "Blue",
}
score_board = [0,0]

#random coordinates 
def throw_dart():   
  cord_x = random.randrange(0, 800)
  cord_y = random.randrange(0, 800)
  return (cord_x,cord_y)

#determine if throw is in the circle
def is_in_circle(x,y):
  distance_from_center = math.hypot(400-x, 400-y)
  if distance_from_center < screen_width/2:
    return True 
  else:
    return False

#alternate turns
def player_throws(total_throws):
  total_throws = 0
  if total_throws %2 == 0:
    total_throws += 1
    return player_one
  else:
    return player_two
      
#determines a hit
def play1_move(player):
   x1,y1 = throw_dart()
   if is_in_circle(x1,y1):
       pygame.draw.circle(window, [238,59,59], (x1,y1), 5, 0)
   else:
        pygame.draw.circle(window, [255,255,0], (x1,y1), 5, 0)
   score_board[0] += 1

def play2_move(player):
   x2,y2 = throw_dart()
   if is_in_circle(x2,y2):
        pygame.draw.circle(window, [58,95,205], (x2,y2), 5, 0)
   else:
        pygame.draw.circle(window, [155,48,255], (x2,y2), 5, 0)  
   score_board[1] += 1      
   
#main function 
def main():
  while True: 
    for turns in range(10):
        if player_throws(turns) == player_one:
            play1_move(player_one)
        if player_throws(turns) == player_two:
            play2_move(player_two)

main()
pygame.display.flip()


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()