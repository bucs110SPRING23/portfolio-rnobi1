import pygame

def threenp1(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

def threenp1range(upper_limit):
    threenplus1_iters_dict = {}
    for n in range(2, upper_limit + 1):
        iters = threenp1(n)
        threenplus1_iters_dict[n] = iters
    return threenplus1_iters_dict

def graph_coordinates(threenplus1_iters_dict):
    pygame.init()
    font = pygame.font.SysFont('arial', 16)
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (0, 0, 255)
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('3n+1 Graph')
    x_scale = width // len(threenplus1_iters_dict)
    y_scale = height // max(threenplus1_iters_dict.values())
    coordinates = [(x * x_scale, height - y * y_scale) for x, y in threenplus1_iters_dict.items()]
    pygame.draw.lines(screen, blue, False, coordinates, 2)
    text_surface = font.render(f'Max iterations: {max(threenplus1_iters_dict.values())}', True, white)
    screen.blit(text_surface, (10, 10))
    pygame.display.flip()
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
    pygame.quit()

def main():
    upper_limit = 20
    threenplus1_iters_dict = threenp1range(upper_limit)
    print(threenplus1_iters_dict)
    graph_coordinates(threenplus1_iters_dict)

if __name__ == '__main__':
    main()
