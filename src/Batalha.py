import pygame, random, time
import perguntas, StringSplitter, Musica

pygame.mixer.pre_init(44100, -16, 2, 512)
perguntas = perguntas.perguntas
socao = pygame.mixer.Sound('sound/socao.mp3')
# splitter = StringSplitter.Splitter()
WIDTH, HEIGHT = 1280, 720

# TELA DE BATALHA
class Battle(pygame.sprite.Sprite):
    def __init__(self, capanga: list, pos_x, pos_y, scale, group_btn: list, option_btn: list, screen, materia: list, font, poderes, music_group: list):
        super().__init__()
        self.capanga = capanga
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.enemyChange = False
        self.group_btn = group_btn
        self.option_btn = option_btn
        self.screen = screen
        self.perguntas = perguntas.copy()
        self.materia = materia
        self.font = font
        self.poderes = poderes
        self.scale = scale
        self.music_group = music_group

        self.correct = 0
        self.wrong = 0
        self.perguntaList = []
        self.perguntaJaFeita = []
        self.materiaInimigo = random.sample(self.materia, k=3)
        self.materiaEInimigoIndex = -1
        self.battleActive = False
        self.musicActice = False
        self.newEnemy = False
        self.state = ''
        self.startTime = 0
        self.tempoMax = 90
        self.powerUpsVerified = False
        self.vidaExtra = False
        self.retornoPorMorteOuNao = False
        self.materiaIndex = {
            'matematica': 0,
            'portugues': 0,
            'historia': 0,
            'geografia': 0,
            'biologia': 0
        }
        self.inimigosDerrotados = 0
        self.vida_image = pygame.image.load('sprite/vida.png').convert_alpha()
        self.vida_image = pygame.transform.scale(self.vida_image, (48, 42)) # tamanho real do sprite, divida por 3 os valores

        self.width = self.capanga[self.materiaEInimigoIndex + 1].get_width()
        self.height = self.capanga[self.materiaEInimigoIndex + 1].get_height()
        self.image = pygame.transform.scale(self.capanga[self.materiaEInimigoIndex + 1], (int(self.width * self.scale), int(self.height * self.scale)))
        self.image = pygame.transform.flip(self.image, True, False)

        # self.image = pygame.transform.scale(self.capanga[0], (120, 136)) # tamanho real do sprite, divida por 3 os valores
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
        self.splitter = StringSplitter.Splitter(self.screen, '#79b0a1', 30)
        self.musica = Musica.BgMusic(self.music_group[self.materiaEInimigoIndex + 1])

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def battle(self):
        if self.powerUpsVerified == False:
            self.verifyPowerUps()
            self.powerUpsVerified = True

        if self.battleActive == False:
            self.listagemPerguntas()
            self.battleActive = True

        currentTime = time.time()

        if self.wrong == 0:
            self.screen.blit(self.vida_image, (35, 20))
            self.screen.blit(self.vida_image, (85, 20))
            self.screen.blit(self.vida_image, (135, 20))
        elif self.wrong == 1:
            self.screen.blit(self.vida_image, (35, 20))
            self.screen.blit(self.vida_image, (85, 20))
        else:
            self.screen.blit(self.vida_image, (35, 20))

        self.screen.blit(self.image, self.rect)
        self.draw_text(str(int((self.tempoMax + 1) - (currentTime - self.startTime))), self.font, 'Blue', 1175, 20)

        # aumentar o tempo para responder a pergunta
        if (currentTime - self.startTime) >= self.tempoMax:
            print('Tempo esgotado')
            self.startTime = time.time()
            self.wrong += 1
            self.battleWonLost()
            self.battleActive = False

        self.splitter.Draw_Text(self.perguntaJaFeita[-1]['pergunta'], self.font, 'Black', WIDTH * 0.08, HEIGHT * 0.1, WIDTH * 0.6, HEIGHT * 0.38)

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
        if self.musicActice == True:
            self.musica.on_start()
            self.musicActice = False

        self.battle()
        return {
            'estado': self.state,
            'erros': self.wrong,
            'poder': self.poderes,
            'morteOuVencedor': self.retornoPorMorteOuNao,
        }

    def listagemPerguntas(self):
        if self.newEnemy == True:
            self.materiaInimigo = random.sample(self.materia, k=3)
            print(self.materiaInimigo)

            for x in self.materiaInimigo:
                random.shuffle(self.perguntas[x])

            self.newEnemy = False
        
        # self.pergunta[matéria][posição da pergunta] >> está difícil de ler, mas é isso, tiramos o loop pelo menos
        self.perguntaJaFeita.append(self.perguntas[self.materiaInimigo[self.materiaEInimigoIndex]][self.materiaIndex[self.materiaInimigo[self.materiaEInimigoIndex]]])
        self.perguntaList = self.perguntaJaFeita[-1]['resposta'].copy()
        random.shuffle(self.perguntaList)

        self.materiaIndex[self.materiaInimigo[self.materiaEInimigoIndex]] += 1

        return self.perguntaList

    def verifyAnswer(self, answer):
        if answer == self.perguntaJaFeita[-1]['resposta'][0]:
            print('Acertou')
            pygame.mixer.Sound.play(socao)
            self.correct += 1
            self.battleWonLost()
        else:
            # print('Burro')
            print('Errou')
            self.wrong += 1
            self.battleWonLost()
        
        self.battleActive = False
    
    def battleWonLost(self):
        if self.correct == 2:
            print('Inimigo derrotado')
            width = self.capanga[self.materiaEInimigoIndex + 1].get_width()
            height = self.capanga[self.materiaEInimigoIndex + 1].get_height()
            self.image = pygame.transform.scale(self.capanga[self.materiaEInimigoIndex + 1], (int(width * self.scale), int(height * self.scale)))
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

            self.musica.on_exit()
            self.musica = Musica.BgMusic(self.music_group[self.materiaEInimigoIndex + 1])
            self.inimigosDerrotados += 1

            self.state = 'levelMenu'
        
        if self.wrong == 3:
            if self.vidaExtra == True:
                print('Vida extra utilizada')
                self.retornoPorMorteOuNao = True
                self.state = 'levelMenu'
                self.poderes['vida_extra'] = 0
                self.musica.on_exit()
            else:
                # print('Foi de arrasta pra cima')
                print('Game Over')
                self.musica.on_exit()
                self.state = 'mainMenu'
        
        self.startTime = time.time()
    
    def verifyPowerUps(self):
        if self.poderes['vida_extra'] == 1:
            self.vidaExtra = True
        if self.poderes['tempo_extra'] == 1:
            self.tempoMax = 150
            self.poderes['tempo_extra'] = 0
        if self.poderes['dano_extra'] == 1:
            self.correct += 1
            self.poderes['dano_extra'] = 0

    def reset_state(self):
        self.correct = 0
        self.wrong = 0
        self.perguntaList = []
        self.perguntaJaFeita = []
        self.battleActive = False
        self.state = ''
        self.perguntas = perguntas.copy()
        self.startTime = time.time()
        self.tempoMax = 90
        self.powerUpsVerified = False
        self.vidaExtra = False
        self.retornoPorMorteOuNao = False
        self.materiaIndex = {
            'matematica': 0,
            'portugues': 0,
            'historia': 0,
            'geografia': 0,
            'biologia': 0
        }
    
    def reset_all(self):
        self.correct = 0
        self.wrong = 0
        self.perguntaList = []
        self.perguntaJaFeita = []
        self.materiaEInimigoIndex = -1
        self.battleActive = False
        self.musicActice = False
        self.newEnemy = False
        self.state = ''
        self.perguntas = perguntas.copy()
        self.tempoMax = 90
        self.powerUpsVerified = False
        self.vidaExtra = False
        self.retornoPorMorteOuNao = False
        self.materiaIndex = {
            'matematica': 0,
            'portugues': 0,
            'historia': 0,
            'geografia': 0,
            'biologia': 0
        }
        self.image = pygame.transform.scale(self.capanga[self.materiaEInimigoIndex + 1], (int(self.width * self.scale), int(self.height * self.scale)))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
        self.musica = Musica.BgMusic(self.music_group[self.materiaEInimigoIndex + 1])

    def reset_image_sound(self):
        self.image = pygame.transform.scale(self.capanga[self.materiaEInimigoIndex + 1], (int(self.width * self.scale), int(self.height * self.scale)))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
        self.musica = Musica.BgMusic(self.music_group[self.materiaEInimigoIndex + 1])
