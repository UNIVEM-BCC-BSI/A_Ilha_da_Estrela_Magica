import pygame, sys
# pygame.init()
# pygame.font.init()

# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1280, 720))
# font = pygame.font.SysFont('Arial', 20)
# text = "O rompimento pelos nazistas do Pacto Germano-Soviético assinado entre a Alemanha e a União das Repúblicas Socialistas Soviéticas (URSS), no ano de 1939, causou espanto mundial. Em que consistia este acordo?"

class Splitter():
    def __init__(self, screen):
        self.screen = screen

    def Draw_Text(self, text, font, text_col, pos_x, pos_y, rect_width, rect_height):
        text_list = text.split(' ')
        rect = pygame.Rect((pos_x, pos_y), (rect_width, rect_height))
        total_length = 0

        pygame.draw.rect(self.screen, 'Grey', rect)

        for x in text_list:
            image = font.render(x + ' ', True, text_col)
            width = image.get_width()
            total_length += width
            if total_length < rect.right - 30:
                self.screen.blit(image, (rect.x + total_length - width, rect.y))
            else:
                total_length = 0
                total_length += width
                rect.y += 30
                self.screen.blit(image, (rect.x + total_length - width, rect.y))
    

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     screen.fill('Black')
#     Draw_Text(text, font)
#     pygame.display.update()
#     clock.tick(60)
