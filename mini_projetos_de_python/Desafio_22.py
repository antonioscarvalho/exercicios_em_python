#Tocar música dentro do python
import pygame
pygame.init()
pygame.mixer.music.load('Desafio22.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()