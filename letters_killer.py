import sys

import pygame
from pygame.sprite import Group
from settings import Settings
import game_function as gf

from targets import Target
from aim import Aim
from sound import Sound

def run_game():
	#Initialize the game and create a screen object
	pygame.init()
	game_settings = Settings()
	screen = pygame.display.set_mode(
			(game_settings.screen_width, game_settings.screen_height))
	pygame.display.set_caption('Letters Killer')
	
	#Initialize all the sounds in need
	sounds = Sound(game_settings)
	
	#Initialize the falling targets
	targets = Group()
	
	#Initialize an aim
	aim = Aim(screen, game_settings)
	while True:
		#Create a target with random value
		gf.create_targets(screen, game_settings, targets)
		
		
		#Check the events and responds
		gf.check_events(targets, game_settings, aim, sounds)
		
		
		
		#Update the screen
		gf.update_screen(screen, game_settings, targets, aim)

	
run_game()
		
		
