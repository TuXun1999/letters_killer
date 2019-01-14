import pygame
class Button():
	'''
	The class to represent a button
	'''
	def __init__(self, screen, settings):
		
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		#Load the image of the button
		self.image = pygame.image.load('images/button.bmp')
		self.rect = self.image.get_rect()
		
		#Attributes of the button
		self.txt_color = settings.text_color
		self.button_color = settings.txt_bg_color;
		
		#Assign the position of the button
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery * settings.button_pos_scale
		
		self.font = pygame.font.SysFont(None, 30)
		
		#Build the message shown on the button
		self.prep_msg()
		
		
	def prep_msg(self):
		'''
		Write message on the button
		'''
		self.msg_image = self.font.render("Start", True, self.txt_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		
	
	def draw_button(self):
		'''
		Draw out the button, as well as the text
		'''
		self.screen.blit(self.image, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
