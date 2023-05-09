import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors for players
player1_color = (255, 0, 0)  # red
player2_color = (0, 0, 255)  # blue

# Set up game window
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dart Game")

# Set up font for displaying winner/tie message
font = pygame.font.SysFont("Arial", 50)

# Set up squares for player selection
player1_box = pygame.Rect(50, 400, 100, 100)
player2_box = pygame.Rect(350, 400, 100, 100)

# Set up variables to keep track of player scores and user selection
player1_score = 0
player2_score = 0
user_selection = None

# Define function to simulate one round of the game
def play_round():
  global player1_score, player2_score
  player1_dirt = (random.randint(50, 200), random.randint(50, 200))
  player2_dirt = (random.randint(300, 450), random.randint(50, 200))
  if player1_dirt[1] > player2_dirt[1]:
    player1_score += 1
    return "Player 1 wins!"
  elif player2_dirt[1] > player1_dirt[1]:
    player2_score += 1
    return "Player 2 wins!"
  else:
    return "Tie!"

# Set up main game loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if player1_box.collidepoint(event.pos):
        user_selection = "Player 1"
      elif player2_box.collidepoint(event.pos):
        user_selection = "Player 2"

# Clear screen
screen.fill((255, 255, 255))

# Draw player boxes
pygame.draw.rect(screen, player1_color, player1_box)
pygame.draw.rect(screen, player2_color, player2_box)

# Draw text on boxes
player1_text = font.render("Player 1", True, (255, 255, 255))
player2_text = font.render("Player 2", True, (255, 255, 255))
screen.blit(player1_text, (60, 430))
screen.blit(player2_text, (360, 430))

# Check if user has made a selection
while user_selection is None:
  pygame.display.update()
  continue

# Play 10 rounds of the game
for i in range(10):
  round_result = play_round()
  print(round_result)

# Determine winner or tie
if player1_score > player2_score:
  winner_text = "Player 1 wins!"
elif player2_score > player1_score:
  winner_text = "Player 2 wins!"
else:
  winner_text = "Tie!"

# Draw winner/tie message on screen
winner_display = font.render(winner_text, True, (0, 0, 0))
screen.blit(winner_display, (50, 200))

# Draw user selection and check if it was correct
if user_selection == "Player 1":
  player1_box


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()