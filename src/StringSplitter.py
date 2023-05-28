import pygame
# pygame.init()
# pygame.font.init()

# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1280, 720))
# font = pygame.font.SysFont('Arial', 20)
# text = "O rompimento pelos nazistas do Pacto Germano-Soviético assinado entre a Alemanha e a União das Repúblicas Socialistas Soviéticas (URSS), no ano de 1939, causou espanto mundial. Em que consistia este acordo?"

class Splitter():
    def __init__(self, screen, bgColor, lineHeight):
        self.screen = screen
        self.color = bgColor
        self.lineHeight = lineHeight

    def Draw_Text(self, text, font, text_col, pos_x, pos_y, rect_width, rect_height):
        text_list = text.split(' ')
        rect = pygame.Rect((pos_x, pos_y), (rect_width, rect_height))
        total_length = 0

        pygame.draw.rect(self.screen, self.color, rect)

        for x in text_list:
            image = font.render(x + ' ', True, text_col)
            width = image.get_width()
            total_length += width
            # if total_length < rect.right - 30:
            if total_length < rect_width:
                self.screen.blit(image, (rect.x + total_length - width, rect.y))
            else:
                total_length = 0
                total_length += width
                rect.y += self.lineHeight
                self.screen.blit(image, (rect.x + total_length - width, rect.y))

# splitter = Splitter(screen)
# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     screen.fill('White')
#     splitter.Draw_Text(text, font, 'Black', 100, 100, 350, 250)
#     pygame.display.update()
#     clock.tick(60)
