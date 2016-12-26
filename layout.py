import pygame
from pygame.locals import *
pygame.init()
def s_layout(display_width,display_height,background_color,caption):
	background=pygame.display.set_mode((display_width,display_height))
	background.fill(background_color)
	pygame.display.set_caption(caption)
	pygame.display.update()
	return background