import pygame, random, time
import perguntas, StringSplitter, Musica

pygame.mixer.pre_init(44100, -16, 2, 512)
perguntas = perguntas.perguntas
WIDTH, HEIGHT = 1280, 720

class Pedro(pygame.sprite.Sprite):
    def __init__(self, chefe: list, pos_x, pos_y, music_group: dict, group_btn: list, option_btn: list, screen, materia: list, font, poderes):
        super().__init__()
        self.chefe = chefe
        self.enemyChange = False
        self.group_btn = group_btn
        self.option_btn = option_btn
        self.screen = screen
        self.perguntas = perguntas.copy()
        self.materia = materia
        self.font = font
        self.poderes = poderes
        self.music_group = music_group
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.correct = 0
        self.wrong = False
        self.vidaPedro = 5
        self.perguntaList = []
        self.perguntaJaFeita = []
        self.battleActive = False
        self.musicActive = False
        self.state = ''
        self.startTime = time.time()
        self.tempoMax = 90
        self.powerUpsVerified = False
        self.sans = False
        self.instinto = False
        self.materiaIndex = {
            'matematica': 0,
            'portugues': 0,
            'historia': 0,
            'geografia': 0,
            'biologia': 0
        }

        self.image = pygame.transform.scale(self.chefe[0], (114, 204)) # tamanho real do sprite, divida por 6 os valores
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
        self.splitter = StringSplitter.Splitter(self.screen, '#79b0a1', 30)
        self.musica = Musica.BgMusic(self.music_group['pedro'])
    
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def battle(self):
        if self.powerUpsVerified == False:
            self.verifyPowerUps()
            self.powerUpsVerified = True
        
        if self.musicActive == True:
            self.musica.on_start()
            self.musicActive = False

        if self.battleActive == False:
            self.listagemPerguntas()
            self.battleActive = True
        
        currentTime = time.time()

        # imagem do chefe: Pedro, Sans ou Pedro com Instinto
        self.screen.blit(self.image, self.rect)
        self.draw_text(str(int((self.tempoMax + 1) - (currentTime - self.startTime))), self.font, 'Blue', 1175, 20)

        if (currentTime - self.startTime) >= self.tempoMax:
            # print('Tempo esgotado')
            self.wrong = True
            self.battleWonLost()
            self.battleActive = False
        
        self.splitter.Draw_Text(self.perguntaJaFeita[-1]['pergunta'], self.font, 'Red', WIDTH * 0.08, HEIGHT * 0.15, WIDTH * 0.6, 240)

        # <==== A button ====>
        self.group_btn[0].update()
        self.group_btn[0].draw(self.screen)
        self.splitter.Draw_Text(self.perguntaList[0], self.font, 'Black', WIDTH * 0.07, HEIGHT * 0.51, WIDTH * 0.42, HEIGHT * 0.22)
        # <==== B button ====>
        self.group_btn[1].update()
        self.group_btn[1].draw(self.screen)
        self.splitter.Draw_Text(self.perguntaList[1], self.font, 'Black', WIDTH * 0.55, HEIGHT * 0.51, WIDTH * 0.42, HEIGHT * 0.22)
        # <==== C button ====>
        self.group_btn[2].update()
        self.group_btn[2].draw(self.screen)
        self.splitter.Draw_Text(self.perguntaList[2], self.font, 'Black', WIDTH * 0.07, HEIGHT * 0.76, WIDTH * 0.42, HEIGHT * 0.22)
        # <==== D button ====>
        self.group_btn[3].update()
        self.group_btn[3].draw(self.screen)
        self.splitter.Draw_Text(self.perguntaList[3], self.font, 'Black', WIDTH * 0.55, HEIGHT * 0.76, WIDTH * 0.42, HEIGHT * 0.22)

        if self.option_btn[0].mouse_click() == True:
            self.verifyAnswer(self.perguntaList[0])
            self.option_btn[0].reset_state()

        if self.option_btn[1].mouse_click() == True:
            self.verifyAnswer(self.perguntaList[1])
            self.option_btn[1].reset_state()

        if self.option_btn[2].mouse_click() == True:
            self.verifyAnswer(self.perguntaList[2])
            self.option_btn[2].reset_state()

        if self.option_btn[3].mouse_click() == True:
            self.verifyAnswer(self.perguntaList[3])
            self.option_btn[3].reset_state()
    
    def battle_manager(self):
        self.battle()
        return {
            'estado': self.state
        }

    def listagemPerguntas(self):
        materiaPergunta = random.sample(self.materia, k=1)
        # print(materiaPergunta[0])

        self.perguntaJaFeita.append(self.perguntas[materiaPergunta[0]][self.materiaIndex[materiaPergunta[0]]])
        self.perguntaList = self.perguntaJaFeita[-1]['resposta'].copy()
        random.shuffle(self.perguntaList)

        self.materiaIndex[materiaPergunta[0]] += 1


    def verifyAnswer(self, answer):
        if answer == self.perguntaJaFeita[-1]['resposta'][0]:
            # print('\033[96m<===== Acertou =====>\033[00m')
            if self.instinto == True:
                a = random.random()
                if a < 0.25:
                    print('\033[094mMISS\033[00m')
                else:
                    self.correct += 1
            else:
                self.correct += 1
        else:
            # print('\033[91m<===== Errou =====>\033[00m')
            self.wrong = True

        self.battleWonLost()
        self.battleActive = False
    
    def battleWonLost(self):
        if self.correct == self.vidaPedro:
            # print('\033[96m<===== O Mau Foi Erradicado =====>\033[00m')
            self.musica.on_exit()
            self.state = 'win'
        
        if self.wrong == True:
            # print('\033[91m<===== Game Over =====>\033[00m')
            self.musica.on_exit()
            self.state = 'skillIssue'
        
        self.startTime = time.time()
    
    def verifyPowerUps(self):
        if self.poderes['instinto_inferior'] == 1:
            # print('Instinto Inferior')
            self.image = pygame.transform.scale(self.chefe[1], (288, 288))
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
            self.musica = Musica.BgMusic(self.music_group['pedro_instinto'])
            self.instinto = True
        if self.poderes['sans'] == 1:
            # print('Sans')
            self.image = pygame.transform.scale(self.chefe[2], (152, 216))
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
            self.vidaPedro = 10
            self.musica = Musica.BgMusic(self.music_group['pedro_sans'])
            self.sans = True

    def embaralharPerguntas(self):
        random.shuffle(self.perguntas['matematica'])
        random.shuffle(self.perguntas['portugues'])
        random.shuffle(self.perguntas['geografia'])
        random.shuffle(self.perguntas['historia'])
        random.shuffle(self.perguntas['biologia'])
    
    def reset_all(self):
        self.correct = 0
        self.wrong = False
        self.vidaPedro = 5
        self.perguntaList = []
        self.perguntaJaFeita = []
        self.battleActive = False
        self.state = ''
        self.tempoMax = 90
        self.powerUpsVerified = False
        self.sans = False
        self.instinto = False
        self.materiaIndex = {
            'matematica': 0,
            'portugues': 0,
            'historia': 0,
            'geografia': 0,
            'biologia': 0
        }
        self.image = pygame.transform.scale(self.chefe[0], (114, 204)) # tamanho real do sprite, divida por 6 os valores
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
        self.musica = Musica.BgMusic(self.music_group['pedro'])
    