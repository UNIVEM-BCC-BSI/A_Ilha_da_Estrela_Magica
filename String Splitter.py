import pygame, sys
pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont('Arial', 20)
text = "O rompimento pelos nazistas do Pacto Germano-Soviético assinado entre a Alemanha e a União das Repúblicas Socialistas Soviéticas (URSS), no ano de 1939, causou espanto mundial. Em que consistia este acordo?"

def Draw_Text(text, font):
    text = text
    font = font
    text_list = text.split(' ')
    rect = pygame.Rect(100, 50, 600, 500)
    total_length = 100

    pygame.draw.rect(screen, (255, 0, 0), rect)

    for x in text_list:
        image = font.render(x + ' ', True, (255, 255, 255))
        width = image.get_width()
        total_length += width
        if total_length < rect.right - 30:
            screen.blit(image, (total_length - width + 20, rect.y + 20))
        else:
            total_length = 100
            total_length += width
            rect.y += 20
            screen.blit(image, (total_length - width + 20, rect.y + 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('Black')
    Draw_Text(text, font)
    pygame.display.update()
    clock.tick(60)
