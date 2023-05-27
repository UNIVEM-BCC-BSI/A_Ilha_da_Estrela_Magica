import pygame, StringSplitter, Musica

pygame.mixer.init()
store_sound = pygame.mixer.Sound('sound/wii_shop.mp3')
WIDTH, HEIGHT = 1280, 720

class Store():
    def __init__(self, dinheiros, group_btn: list, option_btn: list, font, screen, poderes):
        self.dinheiros = dinheiros
        self.group_btn = group_btn
        self.option_btn = option_btn
        self.font = font
        self.screen = screen
        self.compras = poderes

        self.musicActive = False
        self.state = ''
        self.musica = Musica.BgMusic(store_sound)
    
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))
    
    def itens(self):
        # explicar que os poderes comprados serão utilizados sem falta na próxima batalha, ou seja,
        # não há um seletor para o jogador escolher que poder ele quer usar =P

        self.group_btn[4].update()
        self.group_btn[4].draw(self.screen)

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
        self.draw_text('??? - --- 27 Dinheiros', self.font, 'White', WIDTH * 0.23, HEIGHT * 0.62)

        if self.option_btn[0].mouse_click() == True:
            if self.compras['vida_extra'] == 1:
                print('Parece que você já possui uma VIDA EXTRA, não é possível comprar outra no momento')
            elif (self.dinheiros - 7) < 0:
                print('Você não possui DINHEIROS suficiente para adquirir este item')
            else:
                print('Comprou a VIDA EXTRA')
                print(f'{self.dinheiros} - 7')
                self.compras['vida_extra'] = 1
                self.dinheiros -= 7
            print('<' + '=' * 50 + '>')
            self.option_btn[0].reset_state()
        
        if self.option_btn[1].mouse_click() == True:
            if self.compras['tempo_extra'] == 1:
                print('Parece que você já possui uma DILATAÇÃO TEMPORAL, não é possível comprar outra no momento')
            elif (self.dinheiros - 7) < 0:
                print('Você não possui DINHEIROS suficiente para adquirir este item')
            else:
                print('Comprou a DILATAÇÃO TEMPORAL')
                print(f'{self.dinheiros} - 7')
                self.compras['tempo_extra'] = 1
                self.dinheiros -= 7
            print('<' + '=' * 50 + '>')
            self.option_btn[1].reset_state()
        
        if self.option_btn[2].mouse_click() == True:
            if self.compras['dano_extra'] == 1:
                print('Parece que você já possui um DIÁLOGO, não é possível comprar outro no momento')
            elif (self.dinheiros - 4) < 0:
                print('Você não possui DINHEIROS suficiente para adquirir este item')
            else:
                print('Comprou o DIÁLOGO')
                print(f'{self.dinheiros} - 4')
                self.compras['dano_extra'] = 1
                self.dinheiros -= 4
            print('<' + '=' * 50 + '>')
            self.option_btn[2].reset_state()

        if self.option_btn[3].mouse_click() == True:
            if (self.dinheiros - 27) < 0:
                print('Você não possui DINHEIROS suficiente para adquirir este item')
            else:
                print('Comprou o ???')
                print(f'{self.dinheiros} - 27')
                self.compras['sans'] = 1
                self.dinheiros -= 27
            print('<' + '=' * 50 + '>')
            self.option_btn[3].reset_state()
        
        if self.option_btn[4].mouse_click() == True:
            self.musica.on_exit()
            self.state = 'map'
            self.option_btn[4].reset_state()
        
        # print(self.compras)

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
