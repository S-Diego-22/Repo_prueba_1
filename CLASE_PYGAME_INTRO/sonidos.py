import pygame

pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)
sonido_fondo_homero = pygame.mixer.Sound("sonido_fondo_homero.mp3")
sonido_fondo_homero.set_volume(0.1)

homero_festeja = pygame.mixer.Sound("homero iuju.mp3")
homero_festeja.set_volume(0.1)