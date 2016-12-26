import pygame
import time
from pygame.locals import *
pygame.init()
beep=pygame.mixer.Sound('pickup.wav')
def control(event,px,py,pc):
	if event.type==QUIT:
		time.sleep(1)
		quit()
	if event.type==pygame.KEYDOWN:
		if event.key==K_q:
			beep.play()
			time.sleep(1)
			quit()
		if event.key==K_RETURN:
			beep.play()
			time.sleep(1)
		if event.key==K_a:
			if px>-387:
				beep.play()
				pc=-10
		if event.key==K_d:
			if px<383:
				beep.play()
				pc=10
	if event.type==pygame.KEYUP:
		if event.key==K_a or event.key==K_d:
			pc=0
	return px,py,pc
def qcontrol(event):
	if event.type==QUIT:
		time.sleep(1)
		quit()
	if event.type==pygame.KEYDOWN:
		if event.key==K_q:
			beep.play()
			time.sleep(1)
			quit()
		if event.key==K_RETURN:
			beep.play()
			time.sleep(1)