import pygame

pygame.mixer.init()
click_sound = pygame.mixer.Sound('sound/mouse_click.wav')

class Button(pygame.sprite.Sprite):
    def __init__(self, image_unp, image_pressed, pos_x, pos_y, scale):
        super().__init__()
        width_unp = image_unp.get_width()
        height_unp = image_unp.get_height()
        width_pressed = image_pressed.get_width()
        height_pressed = image_pressed.get_height()

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.mouse_is_down = False
        self.image_list = []
        self.image_list.append(pygame.transform.scale(image_unp, (int(width_unp * scale), int(height_unp * scale))))
        self.image_list.append(pygame.transform.scale(image_pressed, (int(width_pressed * scale), int(height_pressed * scale))))
        self.image = self.image_list[0]
        self.rect = self.image.get_rect(midtop = (pos_x, pos_y))

        self.scale = scale
        self.action = False

    def mouse_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.image = self.image_list[1]
                self.rect.y = self.pos_y + (self.scale * 2)
                if self.mouse_is_down == False:
                    self.mouse_is_down = True
            elif pygame.mouse.get_pressed()[0] == False and self.mouse_is_down == True:
                pygame.mixer.Sound.play(click_sound)
                self.mouse_is_down = False
                self.image = self.image_list[0]
                self.rect.y = self.pos_y

                if self.action == False:
                    self.action = True
                else:
                    self.action = False

                
        else:
            self.image = self.image_list[0]
            self.rect.y = self.pos_y
        
        return self.action

    def reset_state(self):
        self.action = False

    def update(self):
        self.mouse_click()
    
class Button_Enemy(Button):
    def __init__(self, image_unp, image_pressed, pos_x, pos_y, scale, id):
        super().__init__(image_unp, image_pressed, pos_x, pos_y, scale)
        self.id = id

    def mouse_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.image = self.image_list[1]
                self.rect.y = self.pos_y + (self.scale * 2)
                if self.mouse_is_down == False:
                    self.mouse_is_down = True
            elif pygame.mouse.get_pressed()[0] == False and self.mouse_is_down == True:
                pygame.mixer.Sound.play(click_sound)
                self.mouse_is_down = False
                self.image = self.image_list[0]
                self.rect.y = self.pos_y

                if self.action == False:
                    self.action = True
                else:
                    self.action = False
                
        else:
            self.image = self.image_list[0]
            self.rect.y = self.pos_y
        
        return self.action