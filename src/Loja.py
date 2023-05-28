import pygame, StringSplitter, Musica

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.font.init()
fontDinheiro = pygame.font.SysFont('comicsansms', 30)
store_sound = pygame.mixer.Sound('sound/wii_shop.mp3')
item_comprado = pygame.mixer.Sound('sound/item_comprado.wav')
WIDTH, HEIGHT = 1280, 720

class Store():
    def __init__(self, dinheiros, group_btn: list, option_btn: list, font, screen, poderes, image):
        self.dinheiros = dinheiros
        self.group_btn = group_btn
        self.option_btn = option_btn
        self.font = font
        self.screen = screen
        self.compras = poderes
        self.vendedor = image
        self.textoAlerta = {
            'entrada': 'Os poderes comprados serão utilizados automaticamente na próxima batalha.',
            'pobre': 'Você não possui DINHEIROS suficiente para adquirir este item.',
            'item_duplicado': 'Use seu item antes de comprar outro.',
            'item_comprado': 'Obrigado pela compra.'
        }

        self.musicActive = False
        self.falaVendedor = 'entrada'
        self.state = ''
        self.musica = Musica.BgMusic(store_sound)
        self.splitter = StringSplitter.Splitter(self.screen, '#506773', 30)

        self.width = self.vendedor.get_width()
        self.height = self.vendedor.get_height()
        self.image = pygame.transform.scale(self.vendedor, (int(self.width * 5), int(self.height * 5)))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect(center=(1011, HEIGHT * 0.6))
    
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def itens(self):
        # falas do vendedor
        self.screen.blit(self.image, self.rect)
        self.splitter.Draw_Text(self.textoAlerta[self.falaVendedor], self.font, 'White', WIDTH*0.7, HEIGHT*0.3, WIDTH*0.2, HEIGHT*0.175)

        self.draw_text(f'Dinheiro: {str(self.dinheiros)}', fontDinheiro, 'White', WIDTH * 0.15, HEIGHT * 0.05)

        self.group_btn[5].update()
        self.group_btn[5].draw(self.screen)

        if self.musicActive == True:
            self.musica.on_start()
            self.musicActive = False

        self.group_btn[0].update()
        self.group_btn[0].draw(self.screen)
        self.draw_text('VIDA EXTRA --- 7 Dinheiros', self.font, 'White', WIDTH * 0.23, HEIGHT * 0.32)
    
        self.group_btn[1].update()
        self.group_btn[1].draw(self.screen)
        self.draw_text('DILATAÇÃO TEMPORAL --- 7 Dinheiros', self.font, 'White', WIDTH * 0.23, HEIGHT * 0.42)

        self.group_btn[2].update()
        self.group_btn[2].draw(self.screen)
        self.draw_text('DIÁLOGO --- 4 Dinheiros', self.font, 'White', WIDTH * 0.23, HEIGHT * 0.52)

        self.group_btn[3].update()
        self.group_btn[3].draw(self.screen)
        self.draw_text('??? --- 27 Dinheiros', self.font, 'White', WIDTH * 0.23, HEIGHT * 0.62)

        self.group_btn[4].update()
        self.group_btn[4].draw(self.screen)
        self.draw_text('??? --- 27 Dinheiros', self.font, 'White', WIDTH * 0.23, HEIGHT * 0.72)

        if self.option_btn[0].mouse_click() == True:
            if self.compras['vida_extra'] == 1:
                self.falaVendedor = 'item_duplicado'
            elif (self.dinheiros - 7) < 0:
                self.falaVendedor = 'pobre'
            else:
                pygame.mixer.Sound.play(item_comprado)
                self.falaVendedor = 'item_comprado'
                self.compras['vida_extra'] = 1
                self.dinheiros -= 7
            self.option_btn[0].reset_state()
        
        if self.option_btn[1].mouse_click() == True:
            if self.compras['tempo_extra'] == 1:
                self.falaVendedor = 'item_duplicado'
            elif (self.dinheiros - 7) < 0:
                self.falaVendedor = 'pobre'
            else:
                pygame.mixer.Sound.play(item_comprado)
                self.falaVendedor = 'item_comprado'
                self.compras['tempo_extra'] = 1
                self.dinheiros -= 7
            self.option_btn[1].reset_state()
        
        if self.option_btn[2].mouse_click() == True:
            if self.compras['dano_extra'] == 1:
                self.falaVendedor = 'item_duplicado'
            elif (self.dinheiros - 4) < 0:
                self.falaVendedor = 'pobre'
            else:
                pygame.mixer.Sound.play(item_comprado)
                self.falaVendedor = 'item_comprado'
                self.compras['dano_extra'] = 1
                self.dinheiros -= 4
            self.option_btn[2].reset_state()

        if self.option_btn[3].mouse_click() == True:
            if self.compras['sans'] == 1:
                self.falaVendedor = 'item_duplicado'
            elif (self.dinheiros - 27) < 0:
                self.falaVendedor = 'pobre'
            else:
                pygame.mixer.Sound.play(item_comprado)
                self.falaVendedor = 'item_comprado'
                self.compras['sans'] = 1
                self.dinheiros -= 27
            self.option_btn[3].reset_state()

        if self.option_btn[4].mouse_click() == True:
            if self.compras['instinto_inferior'] == 1:
                self.falaVendedor = 'item_duplicado'
            elif (self.dinheiros - 27) < 0:
                self.falaVendedor = 'pobre'
            else:
                pygame.mixer.Sound.play(item_comprado)
                self.falaVendedor = 'item_comprado'
                self.compras['instinto_inferior'] = 1
                self.dinheiros -= 27
            self.option_btn[4].reset_state()
        
        if self.option_btn[5].mouse_click() == True:
            self.musica.on_exit()
            self.state = 'map'
            self.option_btn[5].reset_state()

    def store_manager(self):
        self.itens()
        return {
            'compras': self.compras,
            'dinheiros': self.dinheiros,
            'estado': self.state,
        }

    def reset_state(self):
        self.state = ''
        self.musicActive = False
