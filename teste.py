# Pegar o tamanho dos sprites
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

vida = pygame.image.load('sprite/vida.png').convert_alpha()
width = vida.get_width()
height = vida.get_height()

print(width, height)

run = True
while run:
    for event in pygame.event.get():
        if event == pygame.QUIT():
            pygame.quit()
            run = False
        
    