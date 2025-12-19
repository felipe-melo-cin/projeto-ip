import pygame
import Constantes as k
from random import shuffle

class Playlist:

    def __init__(self, playlist):
        pygame.mixer.music.set_endevent(k.MUSIC_END)
        self.playlist = playlist
        self.music_pointer = 0
        self.current_music = None

    @staticmethod
    def set_volume(volume):
        pygame.mixer.music.set_volume(volume)

    def start(self):
        self.current_music = self.playlist[self.music_pointer]
        pygame.mixer.music.load(self.current_music)
        pygame.mixer.music.play()

    @staticmethod
    def stop(time_seconds):
        pygame.mixer.music.fadeout(time_seconds * 1000)

    def next(self):
        self.music_pointer = (self.music_pointer + 1) % len(self.playlist)

    def queue_shuffle(self):
        shuffle(self.playlist)

class SFX(pygame.mixer.Sound):

    def __init__(self, source, volume):
        super().__init__(source)
        self.set_volume(volume)