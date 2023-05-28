import pygame, time, StringSplitter, Musica

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
WIDTH, HEIGHT = 1280, 720

class NarrativaText():
    def __init__(self, font, menu_state, screen, music_group: dict):
        self.font = font
        self.menu_state = menu_state
        self.screen = screen
        self.music_group = music_group
        self.musicActive = False

        self.state = ''

        self.splitter = StringSplitter.Splitter(self.screen, 'White', 45)
        self.musica = Musica.BgMusic(self.music_group['vencedor'])
    
    def historia(self):
        self.splitter.Draw_Text('Em uma quarta-feira à noite, João se encontrava num churrasco de família, quando ele vê uma estrela cair do céu, em direção à praia. No próximo dia, durante a aula, ele escuta Pedro cochichando sobre esta estrela, de acordo com Pedro a estrela tem um poder magico que realizara o desejo de qualquer um que obtiver seu núcleo... João escuta também sobre as intenções de Pedro e seus colegas. Intenções essas de cunho ganancioso e maligno, algumas ideias poderiam até mesmo ser consideradas terroristas. João então se prepara ao longo do dia, para assim que a noite chegasse, ele sair de casa escondido e "roubar" a estrela para si, evitando que Pedro colocasse suas mãos sujas em um objeto tão poderoso. ', 
                                self.font, 'Black', WIDTH * 0.15, HEIGHT * 0.1, WIDTH * 0.65, HEIGHT * 0.4)
    
    def vencedor(self):
        self.splitter.Draw_Text('João conseguiu! Provou a Pedro que ele é burro e não é apto a segurar tal poder, após derrotá-lo e pegar o tesouro, João decidiu que era melhor usá-lo para, apagar cujo objeto, já que tal poder seria demais até mesmo para o mais puro dos humanos...Certo ou errado, então ele retorna a sua casa, estava tarde. Ao chegar ele toma uma bronca de sua mãe, que o lembra que as provas são na semana que vem e que ele precisa recuperar as notas... ', 
                                self.font, 'Black', WIDTH * 0.15, HEIGHT * 0.2, WIDTH * 0.65, HEIGHT * 0.4)
    
    def skillIssue(self):
        self.splitter.Draw_Text('Você não conseguiu parar Pedro, que pena..., o lado bom é que você não vai presenciar as atrocidades feitas por ele. c:', 
                                self.font, 'Black', WIDTH * 0.15, HEIGHT * 0.35, WIDTH * 0.65, HEIGHT * 0.4)
    
    def manager(self):
        if self.menu_state == 'story':
            self.historia()
        elif self.menu_state == 'win':
            self.musica = Musica.BgMusic(self.music_group['vencedor'])
            if self.musicActive == True:
                self.musica.on_start()
                self.musicActive = False
            self.vencedor()
        elif self.menu_state == 'skillIssue':
            self.musica = Musica.BgMusic(self.music_group['game_over'])
            if self.musicActive == True:
                self.musica.on_start()
                self.musicActive = False
            self.skillIssue()

        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN) or (event.type == pygame.MOUSEBUTTONDOWN):
                if self.menu_state == 'story':
                    self.state = 'map'
                elif self.menu_state == 'win' or self.menu_state == 'skillIssue':
                    self.state = 'mainMenu'

        return {
            'estado': self.state
        }
    
    def reset_state(self):
        self.state = ''
        self.musicActive = False


