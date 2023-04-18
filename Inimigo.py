import pygame
import random
import perguntas

perguntas = perguntas.perguntas

class Enemy(pygame.sprite.Sprite):
    def __init__(self):    
        super().__init__()
        # width = capanga.get_width()
        # height = capanga.get_height()
        self.correct = 0
        self.wrong = 0
        self.perguntaList = []
        self.perguntaJaFeita = []

        # self.pos_x = pos_x
        # self.pos_y = pos_y
        # self.image = pygame.transform.scale(capanga, int(width * scale), int(height * scale))
        # self.rect = self.image.get_rect(midtop=(pos_x, pos_y))
        
    def battle(self):
        numList = []

        while True:
            a = random.randint(0, 7)
            if (a in self.perguntaJaFeita) == False:
                while len(self.perguntaList) != 4:
                    num = random.randint(1, 4)

                    if num == 1 and (1 in numList) == False:
                        self.perguntaList.append(perguntas['matematica'][a]['a'])
                    elif num == 2 and (2 in numList) == False:
                        self.perguntaList.append(perguntas['matematica'][a]['b'])
                    elif num == 3 and (3 in numList) == False:
                        self.perguntaList.append(perguntas['matematica'][a]['c'])
                    elif num == 4 and (4 in numList) == False:
                        self.perguntaList.append(perguntas['matematica'][a]['d'])
                    
                    numList.append(num)

                self.perguntaList.append(perguntas['matematica'][a]['pergunta'])
                self.perguntaJaFeita.append(a)
                break
        
        return self.perguntaList, self.perguntaJaFeita


    def verifyAnswer(self, answer, question):
        if answer == perguntas['matematica'][question]['a']:
            print('Acertou')
            self.correct += 1
        else:
            print('Burro')
            self.wrong += 1
        
        return self.correct, self.wrong
