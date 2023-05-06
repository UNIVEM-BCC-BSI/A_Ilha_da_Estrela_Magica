import pygame

class Map():
    def __init__(self, group_btn: list, option_btn: list, screen):
        self.map_state = 'level_1'
        self.group_btn = group_btn
        self.option_btn = option_btn
        self.screen = screen
        # self.levelList = levelList

        self.menu_state = ''
    
    def map_manager(self):
        if self.map_state == 'level_1':
            self.level_1()
        
        if self.map_state == 'level_2':
            self.level_2()
        
        if self.map_state == 'level_3':
            self.level_3()
        
        if self.map_state == 'boss':
            self.boss()
    
        return self.menu_state

    def reset_state(self):
        self.menu_state = ''

    def level_1(self):
        # store button
        self.group_btn[11].update()
        self.group_btn[11].draw(self.screen)

        # level 1 button
        self.group_btn[0].update()
        self.group_btn[0].draw(self.screen)

        # level 2 button disabled
        self.group_btn[8].update()
        self.group_btn[8].draw(self.screen)

        # level 3 button disabled
        self.group_btn[9].update()
        self.group_btn[9].draw(self.screen)

        # boss button disabled
        self.group_btn[10].update()
        self.group_btn[10].draw(self.screen)

        if self.option_btn[0].mouse_click() == True:
            self.menu_state = 'levelMenu'
            self.option_btn[0].reset_state()
        
        if self.option_btn[11].mouse_click() == True:
            self.menu_state = 'store'
            self.option_btn[11].reset_state()

    def level_2(self):
        # store button
        self.group_btn[11].update()
        self.group_btn[11].draw(self.screen)

        # level 1 button disabled
        self.group_btn[4].update()
        self.group_btn[4].draw(self.screen)

        # level 2 button
        self.group_btn[1].update()
        self.group_btn[1].draw(self.screen)

        # level 3 button disabled
        self.group_btn[9].update()
        self.group_btn[9].draw(self.screen)

        # boss button disabled
        self.group_btn[10].update()
        self.group_btn[10].draw(self.screen)

        if self.option_btn[1].mouse_click() == True:
            self.menu_state = 'levelMenu'
            self.option_btn[1].reset_state()

        if self.option_btn[11].mouse_click() == True:
            self.menu_state = 'store'
            self.option_btn[11].reset_state()
        
    def level_3(self):
        # store button
        self.group_btn[11].update()
        self.group_btn[11].draw(self.screen)

        # level 1 button disabled
        self.group_btn[4].update()
        self.group_btn[4].draw(self.screen)

        # level 2 button disabled
        self.group_btn[5].update()
        self.group_btn[5].draw(self.screen)

        # level 3 button
        self.group_btn[2].update()
        self.group_btn[2].draw(self.screen)

        # boss button disabled
        self.group_btn[10].update()
        self.group_btn[10].draw(self.screen)

        if self.option_btn[2].mouse_click() == True:
            self.menu_state = 'levelMenu'
            self.option_btn[2].reset_state()

        if self.option_btn[11].mouse_click() == True:
            self.menu_state = 'store'
            self.option_btn[11].reset_state()
        
    def boss(self):
        # store button
        self.group_btn[11].update()
        self.group_btn[11].draw(self.screen)

        # level 1 button disabled
        self.group_btn[4].update()
        self.group_btn[4].draw(self.screen)

        # level 2 button disabled
        self.group_btn[5].update()
        self.group_btn[5].draw(self.screen)

        # level 3 button disabled
        self.group_btn[6].update()
        self.group_btn[6].draw(self.screen)

        # boss button
        self.group_btn[3].update()
        self.group_btn[3].draw(self.screen)

        if self.option_btn[3].mouse_click() == True:
            self.menu_state = 'battle'
            self.option_btn[3].reset_state()
        
        if self.option_btn[11].mouse_click() == True:
            self.menu_state = 'store'
            self.option_btn[11].reset_state()
        