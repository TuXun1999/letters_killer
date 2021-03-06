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
	
				
def check_events(targets, settings, stats, button, aim, sounds, title):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN and stats.game_active:
			check_events_keydown(event, settings, targets, aim, sounds)
		elif event.type == pygame.KEYUP:
			check_events_keyup(aim)
		elif event.type == pygame.MOUSEBUTTONDOWN and not stats.game_active:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(targets, button, stats, mouse_x, mouse_y, title)


def check_play_button(targets, button, stats, mouse_x, mouse_y, title):
	'''
	Update the status if the button is pressed
	'''
	if button.rect.collidepoint(mouse_x, mouse_y):
		pygame.mouse.set_visible(False)
		
		'''stats.reset_stats()'''
		stats.game_active = True
		
		#Clear the targets and start again
		targets.empty()
		
		#Abandon the title and the big man
		del title 
	
	
	
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
		column = game_settings.screen_width * (1 - game_settings.screen_available) * 0.5
		column+= game_settings.screen_width * game_settings.screen_available * (random.random())
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
			
			
def update_screen(screen, game_settings, stats, button, targets, aim, title):
	#Refresh the screen in each loop
	screen.fill(game_settings.bg_color)
	
	#Always targets raining down
	target_list = targets.sprites()
	for target in target_list:
		target.blitme()
		
	targets.update()
	#If the game hasn't started, draw the button; otherwise, draw out the aim
	if not stats.game_active:
		button.draw_button()
		title.draw_title()
		
	else:
		if aim.see_me:
			aim.blitme()
	
	
	pygame.display.flip()
