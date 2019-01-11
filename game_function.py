import pygame

import sys
import string
import random

from targets import Target
from get_key import get_key as get_key

		
def check_events_keydown(event, settings, targets, aim, sounds):
	letter = get_key(event)
	for target in targets.copy():
		if target.letter == letter:
			aim.move(target.rect.centerx, target.rect.centery)
			aim.see_me = True
			sounds.beep.play()
			targets.remove(target)
			break
			
def check_events_keyup( aim):
	aim.see_me = False
				
def check_events(targets, settings, aim, sounds):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_events_keydown(event, settings, targets, aim, sounds)
		elif event.type == pygame.KEYUP:
			check_events_keyup(aim)
	
	
def create_targets(screen, game_settings, targets):
	target_list = targets.sprites()
	if targets:
		bottom = target_list[-1].rect.bottom
		
	check = False
	if not targets:
		check = True
	elif bottom >= target_list[-1].rect.height:
		check = True
	
	if check == True:
		letter = string.ascii_letters[int(26 * random.random())]
		column = game_settings.screen_width * game_settings.screen_available * (random.random())
		target = Target(letter, game_settings, screen, column)
		targets.add(target)


def update_targets(screen, game_settings, targets):
	'''
	Update the status of the targets
	'''
	#Update the position of the targets
	targets.update()
	
	#Remove the targets beyond the region
	for target in targets.copy():
		if target.rect.bottom >= game_settings.screen_height:
			targets.remove(target)
			
			
def update_screen(screen, game_settings, targets, aim):
	#Refresh the screen in each loop
	screen.fill(game_settings.bg_color)
	
	update_targets(screen, game_settings, targets)
	target_list = targets.sprites()
	for target in target_list:
		target.blitme()
	
	if aim.see_me:
		aim.blitme()
		
	pygame.display.flip()
