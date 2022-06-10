import pygame

pygame.mixer.init()
pygame.mixer.music.load('wii.ogg')
pygame.mixer.music.play()
input('agora voce escuta?')
pygame.event.wait()
