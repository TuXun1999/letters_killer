import pygame


class Aim():
	'''
	Animate the process for the player to aim by a cursor
	'''
	
	def __init__(self, screen, settings):
		#Initial some basic attributes
		self.screen = screen 
		self.screen_rect = screen.get_rect()
		
		#Load the image
		self.image = pygame.image.load('images/aim.bmp')
		self.rect = self.image.get_rect()
		
		#Initial position: at the center of the bottom of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		self.see_me = True
		
		
	def move(self, x, y):
		'''
		Move the aim to the right position
		'''
		self.centerx = x
		self.centery = y
		
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
		
	
	def blitme(self):
		'''
		Paint the aim on the screen
		'''
		self.screen.blit(self.image, self.rect)
