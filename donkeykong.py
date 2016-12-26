import pygame
import sys
from pygame.locals import *
pygame.init()
import layout
import colors
import message
import controls
import random
from time import sleep

class board:
	def __init__(self):
		self.score=0
		self.count_time=0
		self.lives=3
		self.level=0
	def start_screen(self):
		display_width=800
		display_height=300
		background_color=colors.red
		caption='Donkey Kong'
		border=layout.s_layout(display_width,display_height,background_color,caption)
		surf,rect=message.message_to_screen('Donkey Kong',colors.green,display_width,display_height,0,-100,"large")
		border.blit(surf,rect)
		surf,rect=message.message_to_screen('Controls',colors.blue,display_width,display_height,0,-50,"medium")
		border.blit(surf,rect)
		surf,rect=message.message_to_screen('Move Left                    a',colors.yellow,display_width,display_height,-20,-20,"small")
		border.blit(surf,rect)
		surf,rect=message.message_to_screen('Move Right                   d',colors.pink,display_width,display_height,-20,5,"small")
		border.blit(surf,rect)
		surf,rect=message.message_to_screen('Move Up                        w',colors.lightblue,display_width,display_height,-20,30,"small")
		border.blit(surf,rect)
		surf,rect=message.message_to_screen('Move Down                   s',colors.purple,display_width,display_height,-20,55,"small")
		border.blit(surf,rect)
		surf,rect=message.message_to_screen('     Jump                           Space',colors.navyblue,display_width,display_height,-20,80,"small")
		border.blit(surf,rect)
		surf,rect=message.message_to_screen('QUIT                           q',colors.black,display_width,display_height,-20,105,"small")
		border.blit(surf,rect)
		surf,rect=message.message_to_screen('Press Enter Key to Start',colors.navyblue,display_width,display_height,0,140,"small")
		border.blit(surf,rect)
		while True:
			for event in pygame.event.get():
				controls.qcontrol(event)
				if event.type==pygame.KEYDOWN:
					if event.key==K_RETURN:
						self.game()
			pygame.display.update()
	def game(self):
		self.level=self.level+1
		display_width=800
		display_height=300
		background_color=colors.white
		caption='Donkey Kong'
		border=layout.s_layout(display_width,display_height,background_color,caption)
		#Background music
		"""pygame.mixer.music.load('background.mid') # Change .mid to mp3 format as it is playable on most of the environments
		pygame.mixer.music.play(-1,0.0)""" # Uncomment this in case .mid files are playable 
		px=-380#Player's x-coordinate
		rdx=-200#Donkey's x-coordinate
		py=135#Player's x-coordinate
		pcx=0#Player's position change
		rx=[]#List of x-coordinates of coins
		ry=[]#List of y-coordinates of coins
		fx=[]#List of x-coordinates of fireballs
		fy=[]#List of y-coordinates of fireballs
		lx=[]#List of x-coordinates of ladders
		ly=[]#List of y-coordinates of ladders
		rcy=135#Floor position
		control=2#For jump-ability
		flag=0#For jump-ability
	# For creating positons of 20 random coins
		for i in range(20):
			if i%4==0:
				rcy=rcy-40
			if rcy==95:
				temp=random.randrange(-76,25)
			if rcy==55:
				temp=random.randrange(-38,77)
			if rcy==15:
				temp=random.randrange(-76,39)
			if rcy==-25:
				temp=random.randrange(-56,77)
			if rcy==-65:
				temp=random.randrange(-76,9)
			temp=temp*5
			rx.append(temp)
			ry.append(rcy)
			t=95
	# For creating positions of 5 random fireballs
		for i in range(5):
			if t==95:
				temp=random.randrange(-76,25)
			if t==55:
				temp=random.randrange(-38,77)
			if t==15:
				temp=random.randrange(-76,39)
			if t==-25:
				temp=random.randrange(-56,77)
			if t==-65:
				temp=random.randrange(-76,9)
			temp=temp*5
			fx.append(temp)
			fy.append(t)
			t=t-40
	#For creating positions of ladders
		rcy=135
		for i in range(5):
			if rcy==135:
				temp=random.randrange(-16,24)
			if rcy==95:
				temp=random.randrange(-38,25)
			if rcy==55:
				temp=random.randrange(-38,41)
			if rcy==15:
				temp=random.randrange(-59,41)
			if rcy==-25:
				temp=random.randrange(-59,11)
			temp=temp*5
			lx.append(temp)
			ly.append(rcy)
			rcy=rcy-40
		# Frames per second
		clock=pygame.time.Clock()
		count_ms=0
		# BEEP Sound
		beep=pygame.mixer.Sound('pickup.wav')
		while True:
			for event in pygame.event.get():
				if event.type==QUIT:
					beep.play()
					time.sleep(1)
					quit()
				if event.type==pygame.KEYDOWN:
					if event.key==K_a:
						if px>-383:
							pcx=-5
					if event.key==K_d:
						if px<383:
							pcx=5
					if event.key==K_w:
						for i in range(5):
							if (px==lx[i] and py==ly[i]) or(px==-120 and py==-65):
								py=py-40#Comparision for ladder position
					if event.key==K_s:
						for i in range(5):
							if (px==lx[i] and py==ly[i]-40):
								py=py+40#Comparision for ladder position
					if event.key==K_SPACE:#For jump-ability
						if flag==0:
							control=-2
							flag=-1
				if event.type==pygame.KEYUP:
					if event.key==K_a or event.key==K_d:
						pcx=0
			px+=pcx
			if (px>=130 and py==95) or (px<=-195 and py==55) or (px<=-300 and py==-25) or (px>=210 and py==15) or (px>=60 and py==-65):
					py=py+40#The Comparisions are done so that the player falls off the floor crossing the edge
			if px>=383 or px<=-383:#So that the player does not cross the wall boundaries
				pcx=0
		#To check for players collision with coins
			for i in range(20):
				if (px==rx[i]) and (py==ry[i]):
					self.score=self.score+5
					beep.play()
					rx[i]=None
					ry[i]=None
		#SETTING THE BACKGROUND
			#Background color
			border.fill(colors.white)
			#WALLS
			c=143
			while c>-151:
				surf,rect=message.message_to_screen('x',colors.black,display_width,display_height,395,c,"small")
				border.blit(surf,rect)
				c=c-8
			c=395
			while c>-403:
				surf,rect=message.message_to_screen('x',colors.black,display_width,display_height,c,143,"small")
				border.blit(surf,rect)
				c=c-8
			c=387
			while c>-403:
				surf,rect=message.message_to_screen('x',colors.black,display_width,display_height,c,-143,"small")
				border.blit(surf,rect)
				c=c-8
			c=135
			while c>-143:
				surf,rect=message.message_to_screen('x',colors.black,display_width,display_height,-397,c,"small")
				border.blit(surf,rect)
				c=c-8
			c=125
			while c>-395:
				surf,rect=message.message_to_screen('x',colors.black,display_width,display_height,c,103,"small")
				border.blit(surf,rect)
				c=c-8
			c=387
			while c>-200:
				surf,rect=message.message_to_screen('x',colors.black,display_width,display_height,c,63,"small")
				border.blit(surf,rect)
				c=c-8
			c=200
			while c>-395:
				surf,rect=message.message_to_screen('x',colors.black,display_width,display_height,c,23,"small")
				border.blit(surf,rect)
				c=c-8
			c=387
			while c>-300:
				surf,rect=message.message_to_screen('x',colors.black,display_width,display_height,c,-18,"small")
				border.blit(surf,rect)
				c=c-8
			c=50
			while c>-395:
				surf,rect=message.message_to_screen('x',colors.black,display_width,display_height,c,-58,"small")
				border.blit(surf,rect)
				c=c-8
			c=-300
			while c<-100:
				surf,rect=message.message_to_screen('x',colors.black,display_width,display_height,c,-100,"small")
				border.blit(surf,rect)
				c=c+8
			#PRINCESS(On Screen)
			surf,rect=message.message_to_screen('Q',colors.black,display_width,display_height,-150,-110,"small")
			border.blit(surf,rect)
			#LADDERS
			c=-95
			while c!=-55:
				surf,rect=message.message_to_screen('H',colors.black,display_width,display_height,-120,c,"small")
				border.blit(surf,rect)
				c=c+10
			for i in range(5):
				c=ly[i]
				while c!=ly[i]-35:
					surf,rect=message.message_to_screen('H',colors.black,display_width,display_height,lx[i],c,"small")
					border.blit(surf,rect)		
					c=c-5
	#----------------------------------------------------------------------------------#
			#For jump-ability
			if control==-2 or control==-1:
				control=control+1
				py=py-20
			if	control==0 or control==1:
				control=control+1
				py=py+20
			if control==2:
				flag=0
			surf,rect=message.message_to_screen('P',colors.navyblue,display_width,display_height,px,py,"small")
			border.blit(surf,rect)
			rd=random.randrange(-3,3)
			rd=rd*5
			rdx=rdx+rd
			if (px==-120 and py==-105):#Checking if player has reached final position
				self.score=self.score+50#Awarding 50 points for successful completion
				self.game()
			if (rdx<-383) or (rdx>47):#Boundaries for Donkey
				rdx=rdx-rd
			if (rdx==px) and (py==-65):#For Collision with Donkey
				self.lives=self.lives-1
				self.score=self.score-25
				px=-380
				py=135
				if self.lives==0:
					self.lives=3
					self.level=0
					self.gameover()
			surf,rect=message.message_to_screen('D',colors.navyblue,display_width,display_height,rdx,-65,"small")
			border.blit(surf,rect)#Donkey on screen
			#For Coins on screen
			for i in range(20):
				if (rx[i]!=None) and (ry[i]!=None):
					surf,rect=message.message_to_screen('C',colors.navyblue,display_width,display_height,rx[i],ry[i],"small")
					border.blit(surf,rect)
			#For Fireballs on screen
			for i in range(5):
				fl=random.randint(0,1)#Random Flag
				#RANDOMISING FALL OF FIREBALLS THROUGH LADDER OR EDGE OF FLOOR BY CREATING A RANDOM FLAG
				if fy[i]==135:
					fx[i]=fx[i]-5
					if fx[i]<-385:
						fy[i]=-65
				if fy[i]==95:
					fx[i]=fx[i]+5
					if fx[i]==lx[0]:
						if fl==1:
							fy[i]=fy[i]+40
					if fx[i]>130:
						fy[i]=fy[i]+40
				if fy[i]==55:
					fx[i]=fx[i]-5
					if fx[i]==lx[1]:
						if fl==1:
							fy[i]=fy[i]+40
					if fx[i]<-195:
						fy[i]=fy[i]+40
				if fy[i]==15:
					fx[i]=fx[i]+5
					if fx[i]==lx[2]:
						if fl==1:
							fy[i]=fy[i]+40
					if fx[i]>205:
						fy[i]=fy[i]+40
				if fy[i]==-25:
					fx[i]=fx[i]-5
					if fx[i]==lx[3]:
						if fl==1:
							fy[i]=fy[i]+40
					if fx[i]<-290:
						fy[i]=fy[i]+40
				if fy[i]==-65:
					fx[i]=fx[i]+5
					if fx[i]==lx[4]:
						if fl==1:
							fy[i]=fy[i]+40
					if fx[i]>60:
						fy[i]=fy[i]+40
			#FOR COLLISIONS WITH FIREBALLS
				if (fx[i]==px) and (fy[i]==py):
					self.lives=self.lives-1
					self.score=self.score-25
					px=-380
					py=135
					if self.lives==0:
						self.lives=3
						self.level=0
						self.gameover()
				surf,rect=message.message_to_screen('O',colors.navyblue,display_width,display_height,fx[i],fy[i],"small")
				border.blit(surf,rect)#FOR FIREBALLS ON SCREEN
			surf,rect=message.message_to_screen('Score:'+str(self.score),colors.navyblue,display_width,display_height,330,-125,"small")
			border.blit(surf,rect)#SCORE ON SCREEN
			surf,rect=message.message_to_screen('Lives:'+str(self.lives),colors.navyblue,display_width,display_height,-330,-125,"small")
			border.blit(surf,rect)#LIVES ON SCREEN
			surf,rect=message.message_to_screen('Level:'+str(self.level),colors.navyblue,display_width,display_height,-250,-125,"small")
			border.blit(surf,rect)#LEVEL ON SCREEN
			time_string='Time:'+str(self.count_time)#Variable calculating time
			if count_ms==1000:
				self.count_time=self.count_time+1
				count_ms=0
			surf,rect=message.message_to_screen(time_string+"s",colors.navyblue,display_width,display_height,200,-125,"small")
			border.blit(surf,rect)#TIME ON SCREEN
			pygame.display.update()
			clock.tick(10)#FPS
			count_ms=count_ms+100
	def gameover(self):
		display_width=800
		display_height=300
		background_color=colors.red
		caption='Donkey Kong'
		border=layout.s_layout(display_width,display_height,background_color,caption)
		pygame.mixer.music.load('gameover.wav')
		pygame.mixer.music.play(0,0.0)
		surf,rect=message.message_to_screen('Your Score',colors.green,display_width,display_height,-20,-100,"large")
		border.blit(surf,rect)
		surf,rect=message.message_to_screen(str(self.score),colors.yellow,display_width,display_height,-25,-25,"large")
		border.blit(surf,rect)
		if self.count_time>=60:
			surf,rect=message.message_to_screen('Time Taken:'+'  '+str(self.count_time/60)+'min'+'  '+str(self.count_time%60)+'s',colors.navyblue,display_width,display_height,-10,10,"small")
			border.blit(surf,rect)
		else:
			surf,rect=message.message_to_screen('Time Taken:'+'  '+str(self.count_time%60)+'s',colors.navyblue,display_width,display_height,-10,10,"small")
			border.blit(surf,rect)
		surf,rect=message.message_to_screen('Press Enter Key to Start',colors.navyblue,display_width,display_height,0,40,"medium")
		border.blit(surf,rect)
		surf,rect=message.message_to_screen('Press q to quit',colors.black,display_width,display_height,-20,90,"medium")
		border.blit(surf,rect)
		while True:
			for event in pygame.event.get():
				controls.qcontrol(event)
				if event.type==pygame.KEYDOWN:
					if event.key==K_RETURN:
						self.score=0
						self.count_time=0
						self.game()
			pygame.display.update()

ok=board()
ok.start_screen()
