import pygame

class Sound():
	
	def __init__(self, settings):
		
		self.beep = pygame.mixer.Sound(settings.beep_sound)
