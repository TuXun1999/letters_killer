import pygame


class Man():
	
	def __init__(self, screen, settings):
		
		self.screen = screen 
		self.screen_rect = screen.get_rect()
		
		
		self.image_title = "images/man.bmp"
		self.image = pygame.image.load(self.image_title)
		self.image_rect = self.image.get_rect()
		
		self.image_rect.centerx = self.screen_rect.centerx * settings.man_scale_x
		self.image_rect.centery = self.screen_rect.centery * settings.man_scale_y
	
	def level_change_figure(self, level):
		'''
		Lack the basic operation to store all the figure names in a json file
		'''
		self.image_title = figure_names[level]
	def draw_man(self):
		self.screen.blit(self.image, self.image_rect)
