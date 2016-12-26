import pygame
from pygame.locals import *
pygame.init()
smallfont=pygame.font.SysFont("comicsansms",15)
medfont=pygame.font.SysFont("comicsansms",30)
largefont=pygame.font.SysFont("comicsansms",30)
def text_objects(text,color,size):
	if size=="small":
		textSurface=smallfont.render(text,True,color)
	if size=="medium":
		textSurface=medfont.render(text,True,color)
	if size=="large":
		textSurface=largefont.render(text,True,color)
	return textSurface,textSurface.get_rect()
def message_to_screen(msg,color,display_width,display_height,x_d=0,y_d=0,size="small"):
	textSurf , textRect = text_objects(msg,color,size)
	textRect.center=(display_width / 2)+x_d,(display_height / 2)+y_d
	return textSurf,textRect
