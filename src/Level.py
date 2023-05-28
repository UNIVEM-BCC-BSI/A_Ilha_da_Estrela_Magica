# ENEMY SELECTION
import pygame
import perguntas, Musica

pygame.mixer.pre_init(44100, -16, 2, 512)
perguntas = perguntas.perguntas

class LevelState():
    def __init__(self, group_btn: list, option_btn: list, screen, music_group: dict):
        self.level_state = 'level_1' # which level the user is
        self.group_btn = group_btn
        self.option_btn = option_btn
        self.screen = screen
        self.music_group = music_group

        self.state = ''
        self.musicActive = False
        self.musica = Musica.BgMusic(self.music_group['level_selection'])

    def level_1(self):
        # Enemy 1 button
        self.group_btn[0].update()
        self.group_btn[0].draw(self.screen)

        # Enemy 2 button disabled
        self.group_btn[7].update()
        self.group_btn[7].draw(self.screen)


        # Enemy 3 button disabled
        self.group_btn[8].update()
        self.group_btn[8].draw(self.screen)

        # Option enemy 1 button
        if self.option_btn[0].mouse_click() == True:
            self.state = 'battle'
            self.option_btn[0].reset_state()
            self.musica.on_exit()
    
    def level_2(self):
        # level 1 disabled
        self.group_btn[3].update()
        self.group_btn[3].draw(self.screen)

        # level 2
        self.group_btn[1].update()
        self.group_btn[1].draw(self.screen)

        # Enemy 3 button disabled
        self.group_btn[8].update()
        self.group_btn[8].draw(self.screen)

        if self.option_btn[1].mouse_click() == True:
            self.state = 'battle'
            self.option_btn[1].reset_state()
            self.musica.on_exit()
        
    def level_3(self):
        # level 1 disabled
        self.group_btn[3].update()
        self.group_btn[3].draw(self.screen)

        # level 2 disabled
        self.group_btn[4].update()
        self.group_btn[4].draw(self.screen)
    
        # level 3
        self.group_btn[2].update()
        self.group_btn[2].draw(self.screen)

        if self.option_btn[2].mouse_click() == True:
            self.state = 'battle'
            self.option_btn[2].reset_state()
            self.musica.on_exit()

    def level_manager(self):
        if self.musicActive == True:
            self.musica.on_start()
            self.musicActive = False

        if (self.level_state == 'level_1'):
            self.level_1()
        
        if (self.level_state == 'level_2'):
            self.level_2()
        
        if (self.level_state == 'level_3'):
            self.level_3()
        
        return self.state

    def reset_state(self):
        self.state = ''
        self.musicActive = False
