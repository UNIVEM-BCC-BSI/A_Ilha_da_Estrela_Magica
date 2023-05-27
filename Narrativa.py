import pygame, time, StringSplitter

WIDTH, HEIGHT = 1280, 720

class NarrativaText():
    def __init__(self, font, menu_state, screen):
        self.startTime = 0
        self.font = font
        self.menu_state = menu_state
        self.screen = screen

        self.state = ''

        self.splitter = StringSplitter.Splitter(self.screen)
    
    def historia(self):
        self.splitter.Draw_Text('Em uma galáxia muito muito distante, havia uma estrela e acabou que ela caiu na Terra, formou uma ilha e agora um vilão quer usar seu poder para o mau (o que mais seria?) e você, na pele de João, deve derrotá-lo', self.font, 'Black', WIDTH * 0.15, HEIGHT * 0.2, WIDTH * 0.65, HEIGHT * 0.4)
    
    def vencedor(self):
        self.splitter.Draw_Text('Parabéns, Pedro foi derrotado', self.font, 'Black', WIDTH * 0.33, HEIGHT * 0.45, WIDTH * 0.2, HEIGHT * 0.2)
    
    def skillIssue(self):
        self.splitter.Draw_Text('Game Over', self.font, 'Black', WIDTH * 0.43, HEIGHT * 0.45, WIDTH * 0.2, HEIGHT * 0.2)
        # self.splitter.Draw_Text('Skill Issue', self.font, 'Black', WIDTH * 0.43, HEIGHT * 0.45, WIDTH * 0.2, HEIGHT * 0.2)
    
    def manager(self):
        if self.menu_state == 'story':
            self.historia()
        elif self.menu_state == 'win':
            self.vencedor()
        elif self.menu_state == 'skillIssue':
            self.skillIssue()
    
        currentTime = time.time()

        if (currentTime - self.startTime) >= 5:
            if self.menu_state == 'story':
                self.state = 'map'
            elif self.menu_state == 'win' or self.menu_state == 'skillIssue':
                self.state = 'mainMenu'
            
        return {
            'estado': self.state
        }
    
    def reset_state(self):
        self.state = ''


