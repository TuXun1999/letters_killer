import pygame
from pygame.sprite import Sprite


class Target(Sprite):
	
	def __init__(self, letter, settings, screen, column):
		'''
		describe the target falling from the top of the screen
		'''
		super(Target, self).__init__()
		
		#Basic part for the screen
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		#Background image
		self.image = pygame.image.load('images/target.bmp')
		self.rect = self.image.get_rect()
		
		#position of the target initially
		self.rect.centerx = column
		self.rect.bottom= 0
		
		#attributes for the letter on the target
		self.letter = letter
		self.text_color = settings.text_color
		self.txt_bg_color = settings.txt_bg_color
		self.font = pygame.font.SysFont(None, 40)
		self.msg_image = self.font.render(letter, True, self.text_color, self.txt_bg_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.centerx = self.rect.centerx
		self.msg_image_rect.centery = self.rect.centery
		
		#attributes for the position
		self.fall_speed = settings.fall_speed
		self.y = self.rect.y
		self.msg_y = self.msg_image_rect.y
	
	def blitme(self):
		'''
		Draw the targe (as well as the letter on it)
		'''
		self.screen.blit(self.image, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
	
	def update(self):
		'''
		Describe the process for the targets to fall
		'''
		self.y += self.fall_speed
		self.msg_y += self.fall_speed
		
		self.rect.y = self.y
		self.msg_image_rect.y = self.msg_y
	
		
