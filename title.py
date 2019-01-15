import pygame
class Title():

	def __init__(self, screen, settings):
		
		self.screen = screen 
		self.screen_rect = screen.get_rect()
		
		self.font = pygame.font.SysFont("Times New Roman", 64);
		self.msg = settings.title
		
		self.txt_color = settings.text_color
		self.txt_bg_color = settings.txt_bg_color
		
		
		self.msg_image = self.font.render(self.msg, True, self.txt_color, self.txt_bg_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.centerx = self.screen_rect.centerx
		self.msg_image_rect.centery = self.screen_rect.centery * settings.title_scale
		
	def draw_title(self):
		self.screen.blit(self.msg_image, self.msg_image_rect)
