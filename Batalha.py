import pygame, random, time
import perguntas, Inimigo

perguntas = perguntas.perguntas

# TELA DE BATALHA
class Battle(pygame.sprite.Sprite):
    def __init__(self, capanga: list, pos_x: list, pos_y: list, scale, group_btn: list, option_btn: list, screen, materia: list, font):
        super().__init__()
        width = capanga[0].get_width()
        height = capanga[0].get_height()

        self.image = pygame.transform.scale(capanga[0], (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect(midtop=(pos_x[0], pos_y[0]))

        self.enemyChange = False
        self.group_btn = group_btn
        self.option_btn = option_btn
        self.screen = screen
        self.perguntas = perguntas.copy()
        self.materia = materia
        self.font = font

        self.correct = 0
        self.wrong = 0
        self.perguntaList = []
        self.perguntaJaFeita = []
        self.materiaInimigo = random.sample(self.materia, 3)
        self.materiaIndex = -1
        self.battleActive = False
        self.newEnemy = False
        self.state = ''
        self.startTime = 0

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def battle(self):
        if self.battleActive == False:
            self.listagemPerguntas()
            self.battleActive = True

        currentTime = time.time()

        # aumentar o tempo para responder a pergunta
        if (currentTime - self.startTime) >= 5:
            print('Tempo esgotado')
            self.startTime = time.time()
            self.wrong += 1
            self.battleWonLost()
            self.battleActive = False

        self.draw_text(self.perguntaJaFeita[-1]['pergunta'], self.font, 'Black', 270, 90)

        # A button
        self.group_btn[0].update()
        self.group_btn[0].draw(self.screen)
        self.draw_text(self.perguntaList[0], self.font, 'Black', 180, 365)
        # B button
        self.group_btn[1].update()
        self.group_btn[1].draw(self.screen)
        self.draw_text(self.perguntaList[1], self.font, 'Black', 470, 365)
        # C button
        self.group_btn[2].update()
        self.group_btn[2].draw(self.screen)
        self.draw_text(self.perguntaList[2], self.font, 'Black', 180, 515)
        # D button

        self.group_btn[3].update()
        self.group_btn[3].draw(self.screen)
        self.draw_text(self.perguntaList[3], self.font, 'Black', 470, 515)

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
        return self.state
  

    def listagemPerguntas(self):
        if self.newEnemy == True:
            self.materiaInimigo = random.sample(self.materia, 3)
            print(self.materiaInimigo)
            self.newEnemy = False

        while True:
            listaPorMateria = perguntas[self.materiaInimigo[self.materiaIndex]].copy()
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
            print('Burro')
            self.wrong += 1
            self.battleWonLost()
        
        self.battleActive = False
    
    def battleWonLost(self):
        if self.correct == 2:
            print('Inimigo derrotado')
            self.state = 'levelMenu'
        
        if self.wrong == 3:
            print('Foi de arrasta pra cima')
            self.state = 'mainMenu'
        
        self.startTime = time.time()

    def reset_state(self):
        self.correct = 0
        self.wrong = 0
        self.perguntaList = []
        self.perguntaJaFeita = []
        self.battleActive = False
        self.state = ''
        self.startTime = time.time()
    
    def reset_all(self):
        self.correct = 0
        self.wrong = 0
        self.perguntaList = []
        self.perguntaJaFeita = []
        # self.materiaInimigo = random.sample(self.materia, 3)
        self.materiaIndex = -1
        self.battleActive = False
        self.newEnemy = False
        self.state = ''
