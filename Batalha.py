import pygame, random, time
import perguntas, StringSplitter

perguntas = perguntas.perguntas
# splitter = StringSplitter.Splitter()
WIDTH, HEIGHT = 1280, 720

# TELA DE BATALHA
class Battle(pygame.sprite.Sprite):
    def __init__(self, capanga: list, pos_x, pos_y, scale, group_btn: list, option_btn: list, screen, materia: list, font, poderes):
        super().__init__()
        self.capanga = capanga
        self.enemyChange = False
        self.group_btn = group_btn
        self.option_btn = option_btn
        self.screen = screen
        self.perguntas = perguntas.copy()
        self.materia = materia
        self.font = font
        self.poderes = poderes
        # self.scale = scale

        self.correct = 0
        self.wrong = 0
        self.perguntaList = []
        self.perguntaJaFeita = []
        self.materiaInimigo = random.sample(self.materia, 3)
        self.materiaEInimigoIndex = -1
        self.battleActive = False
        self.newEnemy = False
        self.state = ''
        self.startTime = 0
        self.tempoMax = 5
        self.powerUpsVerified = False
        self.vida_image = pygame.image.load('sprite/vida.png').convert_alpha()
        self.vida_image = pygame.transform.scale(self.vida_image, (48, 42)) # tamanho real do sprite, divida por 3 os valores

        # self.width = self.capanga[self.materiaEInimigoIndex + 1].get_width()
        # self.height = self.capanga[self.materiaEInimigoIndex + 1].get_height()
        # self.image = pygame.transform.scale(self.capanga[self.materiaEInimigoIndex + 1], (int(self.width * self.scale), int(self.height * self.scale)))

        self.image = pygame.transform.scale(self.capanga[0], (120, 136)) # tamanho real do sprite, divida por 3 os valores
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.splitter = StringSplitter.Splitter(self.screen)

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

        self.splitter.Draw_Text(self.perguntaJaFeita[-1]['pergunta'], self.font, 'Red', WIDTH * 0.08, HEIGHT * 0.15, 640, 240)

        # <==== A button ====>
        self.group_btn[0].update()
        self.group_btn[0].draw(self.screen)
        self.splitter.Draw_Text(self.perguntaList[0], self.font, 'Black', WIDTH * 0.14, HEIGHT * 0.51, WIDTH * 0.35, HEIGHT * 0.18)
        # <==== B button ====>
        self.group_btn[1].update()
        self.group_btn[1].draw(self.screen)
        self.splitter.Draw_Text(self.perguntaList[1], self.font, 'Black', WIDTH * 0.56, HEIGHT * 0.51, WIDTH * 0.35, HEIGHT * 0.18)
        # <==== C button ====>
        self.group_btn[2].update()
        self.group_btn[2].draw(self.screen)
        self.splitter.Draw_Text(self.perguntaList[2], self.font, 'Black', WIDTH * 0.14, HEIGHT * 0.72, WIDTH * 0.35, HEIGHT * 0.18)
        # <==== D button ====>
        self.group_btn[3].update()
        self.group_btn[3].draw(self.screen)
        self.splitter.Draw_Text(self.perguntaList[3], self.font, 'Black', WIDTH * 0.56, HEIGHT * 0.72, WIDTH * 0.35, HEIGHT * 0.18)

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
            'estado': self.state,
            'erros': self.wrong,
            'poder': self.poderes,
        }
  

    def listagemPerguntas(self):
        if self.newEnemy == True:
            self.materiaInimigo = random.sample(self.materia, 3)
            print(self.materiaInimigo)
            self.newEnemy = False

        while True:
            listaPorMateria = perguntas[self.materiaInimigo[self.materiaEInimigoIndex]].copy()
            random.shuffle(listaPorMateria)

            if (listaPorMateria[0] in self.perguntaJaFeita) == False:
                self.perguntaList = listaPorMateria[0]['resposta'].copy()
                random.shuffle(self.perguntaList)

                self.perguntaJaFeita.append(listaPorMateria[0])
                break

        return self.perguntaList

    def verifyAnswer(self, answer):
        if answer == self.perguntaJaFeita[-1]['resposta'][0]:
            print('Acertou')
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
            self.image = pygame.transform.scale(self.capanga[self.materiaEInimigoIndex + 1], (90, 102))
            self.state = 'levelMenu'
        
        if self.wrong == 3:
            # print('Foi de arrasta pra cima')
            print('Game Over')
            self.state = 'mainMenu'
        
        self.startTime = time.time()
    
    def verifyPowerUps(self):
        if self.poderes['vida_extra'] == 1:
            print('-')
            self.poderes['vida_extra'] = 0
        if self.poderes['tempo_extra'] == 1:
            self.tempoMax = 10
            self.poderes['tempo_extra'] = 0
        if self.poderes['dano_extra'] == 1:
            self.correct += 1
            self.poderes['dano_extra'] = 0
        if self.poderes['esquiva'] == 1:
            print('-')
            self.poderes['esquiva'] = 0

    def reset_state(self):
        self.correct = 0
        self.wrong = 0
        self.perguntaList = []
        self.perguntaJaFeita = []
        self.battleActive = False
        self.state = ''
        self.startTime = time.time()
        self.tempoMax = 5
        self.powerUpsVerified = False
    
    def reset_all(self):
        self.correct = 0
        self.wrong = 0
        self.perguntaList = []
        self.perguntaJaFeita = []
        self.materiaEInimigoIndex = -1
        self.battleActive = False
        self.newEnemy = False
        self.state = ''
        self.tempoMax = 5
        self.powerUpsVerified = False
    
    def reset_image(self):
        self.image = pygame.transform.scale(self.capanga[0], (90, 102))
