import pygame

pygame.mixer.pre_init(44100, -16, 2, 512)

class BgMusic():
    def __init__(self, music):
        self.music = music
        self.channel = pygame.mixer.Channel(0)
    
    def on_start(self):
        self.channel.play(self.music, loops=-1)
    
    def on_exit(self):
        self.channel.stop()
