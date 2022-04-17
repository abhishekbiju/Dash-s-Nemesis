import pygame
import random
import time
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.mixer.pre_init()
pygame.init()
pygame.mixer.init()

# clock

surface = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)
w,h = size = surface.get_width(), surface.get_height()
infoObject = pygame.display.Info()

print(w,h)

# self.screen.blit(pygame.transform.flip(self.image, False, True))

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

															 	  #========#
#-----------------------------------------------------------------# COLORS #----------------------------------------------------------------------------------------------------------------------------------
																  #========#

# Function: These varibales are used to store some common colors in the RGB format.

red=(255,0,0)
green=(0,255,0)
yellow=(255,255,0)
blue=(0,255,255)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



left=False
right=False
stand=False
walkCount=0
walkCountDio=0
isJump=False
standDio=False
jumpCount=10
punch=False
dioHurt=False
dioRight=False
dioLeft=False
dioPunch=False
kick=False

dioPunchCount=0

PunchCount=0
gameRun=True
render=True	
x=w//2
y=h//2-100
xD=400
yD=y

power_move1_frame=2
power_move2_frame=0
power_move3_frame=0
power_move4_frame=0

dio_power_move1_frame=0
dio_power_move2_frame=0
dio_power_move3_frame=0
dio_power_move4_frame=0

dio_punch_frame=0

dio_frame_count=0

playerkick_frame=0
playerpunch_frame=0
dioHurt_frame=0
walk_frame=0
xB=-1000
yB=0
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

															 	  #=======================#
#-----------------------------------------------------------------# POWER MOVES VARIABLES #----------------------------------------------------------------------------------------------------------------------------------
																  #=======================#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Function: These variable store boolean values for the player so as to enable the player to use "power moves" once they have enough "power points".

power_move1=False
power_move2=False
power_move3=False
power_move4=False

dio_power_move1=False
dio_power_move2=False
dio_power_move3=False
dio_power_move4=False

frame_count=0
dio_move= "1"
power_move=False

minDis=185

dio_pause=False
dio_pause_frame_count=0
dio_pause_real=False

player_pause=False
player_pause_frame_count=0
player_pause_real=False

dio_power_move1_damage=0.2
dio_power_move2_damage=0.3
dio_power_move3_damage=0.4
dio_power_move4_damage=0

player_power_move1_damage=0.2
player_power_move2_damage=0.3
player_power_move3_damage=0.4
player_power_move4_damage=0

dio_projectile_attack=False

xK=xD+10
yK=yD+90
vK=70

Right=False
Left=False

dio_RIGHT=False
dio_LEFT=False

Za_Worldo_Sound=0
dio_muda_Sound=0
dio_roadrollar_Sound=0
dio_knifethrow_Sound=0
dio_attack_Sound=0
dio_hurt_Sound=0
jotaro_attack_Sound=0
jotaro_attack2_Sound=0
jotaro_ora_Sound=0
jotaro_oraoraend_Sound=0
jotaro_power1_Sound=0
background_count=0

background_check=False
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

															 	  #========================#
#-----------------------------------------------------------------# ATTACK REWARD VARIABLE #----------------------------------------------------------------------------------------------------------------------------------
																  #========================#

# Function: This varibale is used to store the pixels that are added to the player and enemny power bars. 
#		    In a way this helps establish a point/score system which awards the player/enemy with points each time they carry out a succecful attack 
#           These points can then be used to unlock extra attack moves.

attack_reward=0.18
attack_damage=0.17

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


															 	  #=======================#
																  # STATUS BARS VARIABLES #
																  #=======================#

# Function: These lines of code are used to store the starting values of the power and health bars for both the enemy and the player.
#  		   These varibales are then used to draw the bar on the screen.

#                                                                  #=============#
#------------------------------------------------------------------# HEALTH BARS #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#																   #=============#

# Function: To store the "health" status bar variables for both the enemy and player.

player_health=100
enemy_health=100

#                                                                  #============#
#------------------------------------------------------------------# POWER BARS #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#																   #============#

# Function: To store the "power" status bar varibales for both the enemy and player.

player_power=0
enemy_power=0
load_bar=0

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def gameloop():

#                                                                 #======================#
#-----------------------------------------------------------------# WOW I GOTTA FIX THIS #----------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                 #======================#
	global walkCount
	global x
	global xy
	global jumpCount
	global isJump
	global left
	global right
	global punch
	global stand
	global dioHurt
	global xD
	global dioRight
	global dioLeft
	global kick
	global dioPunchCount
	global dioPunch
	global green
	global yellow
	global red
	global enemy_health
	global player_health
	global enemy_power
	global player_power
	global PunchCount
	global gameRun
	global render
	global blue
	global power_move1
	global power_move2
	global power_move3
	global power_move4
	global power_move1_frame,power_move2_frame,power_move3_frame,power_move4_frame
	global xB,yB
	global playerkick_frame
	global playerpunch_frame
	global dioHurt_frame
	global walk_frame



	global dio_power_move1
	global dio_power_move2
	global dio_power_move4
	global dio_power_move3



	global dio_power_move1_frame
	global dio_power_move2_frame
	global dio_power_move3_frame
	global dio_power_move4_frame

	global dio_move

	global frame_count
	global power_move
	global dio_punch_frame
	global dio_frame_count
	global minDis

	global dio_pause
	global dio_pause_frame_count
	global dio_pause_real

	

	global player_pause

	global player_pause_frame_count
	global player_pause_real

	global dio_power_move1_damage
	global dio_power_move2_damage
	global dio_power_move3_damage
	global dio_power_move4_damage

	global player_power_move1_damage
	global player_power_move2_damage
	global player_power_move3_damage
	global player_power_move4_damage

	global dio_projectile_attack 
	global xK,yK,vK

	global Left,Right

	global Za_Worldo_Sound
	global dio_RIGHT,dio_LEFT
	global dio_muda_Sound
	global dio_roadrollar_Sound
	global dio_knifethrow_Sound
	global dio_attack_Sound
	global dio_hurt_Sound
	global jotaro_attack_Sound
	global jotaro_attack2_Sound
	global jotaro_ora_Sound
	global jotaro_oraoraend_Sound
	global jotaro_power1_Sound
	global background_count
	global background_check
	global load_bar




#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Images
	load_screen=pygame.image.load("load_screen.png")
	load_screen = pygame.transform.scale(load_screen, (400,400))
	
	loading=pygame.image.load("LOADING.png")
	loading = pygame.transform.scale(loading, (250,25))
	


	surface.fill((0,0,0))
	surface.blit(loading,(840,700))	
	surface.blit(load_screen,(750,300))	
	pygame.display.update()
	



	def load_bars(load_bar,load_bar_color=(255,255,255)):

		load_bar_color=(255,255,255)

		#if renderLoad:
		pygame.draw.rect(surface,load_bar_color,(600,750,load_bar*7,15))
		pygame.display.update()

	
	back=pygame.image.load("background3.jpeg")
	back = pygame.transform.scale(back, (4000, 1080))

	player_icon=pygame.image.load("MAIN.png")
	enemy_icon=pygame.image.load("MAIN_2.png")

	jotaro_font=pygame.image.load("jotaroFONT.png")
	jotaro_font = pygame.transform.scale(jotaro_font, (300, 60))

	dio_font=pygame.image.load("dioFONT2.png")
	dio_font = pygame.transform.scale(dio_font, (300, 60))

	pause=pygame.image.load("pause.png")
	pause= pygame.transform.scale(pause, (100, 100))

	win_screen=pygame.image.load("win.png")
	win_screen= pygame.transform.scale(win_screen, (1920, 950))
	
	lose_screen=pygame.image.load("lose.png")
	lose_screen= pygame.transform.scale(lose_screen, (1920, 950))



	fat=300
	tall=500
	#Standing Animations
		#load back ground music


	pygame.mixer.music.load("back.mp3")
		#This is plays the music for an unlimted time
	pygame.mixer.music.play(-1)



	Za_Worldo=pygame.mixer.Sound("Za_Worldo.ogg")
	
	
	dio_muda=pygame.mixer.Sound("Dio_Sound/dio_muda.ogg")
	dio_roadrollar=pygame.mixer.Sound("Dio_Sound/dio_roadrollar.ogg")
	dio_knifethrow=pygame.mixer.Sound("Dio_Sound/dio_knifethrow.ogg")
	dio_attack=pygame.mixer.Sound("Dio_Sound/dio_attack.ogg")
	dio_hurt=pygame.mixer.Sound("Dio_Sound/dio_hurt.ogg")
	

	jotaro_attack=pygame.mixer.Sound("Jotaro_Sound/jotaro_attack.ogg")
	jotaro_attack2=pygame.mixer.Sound("Jotaro_Sound/jotaro_attack2.wav")
	jotaro_ora=pygame.mixer.Sound("Jotaro_Sound/jotaro_ora.wav")
	jotaro_oraoraend=pygame.mixer.Sound("Jotaro_Sound/jotaro_oraoraend.wav")
	jotaro_power1=pygame.mixer.Sound("Jotaro_Sound/jotaro_power1.wav")



	clock = pygame.time.Clock()
	#ANIMATION STUFF

	playerleft=[]
	for i in range(7):
		a="Jotaro/Left/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat,tall))
		playerleft.append(b)

	
	playerright=[]
	for i in range(7):
		a="Jotaro/Right/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat,tall))
		playerright.append(b)

	
	playerjump=[]
	for i in range(21):
		a="Jotaro/Jump/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat, tall))
		playerjump.append(b)

	
	playerJumpRight=[]
	for i in range(21):
		a="Jotaro/Jump/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat, tall))
		b=pygame.transform.flip(b,True,False)
		playerJumpRight.append(b)

	load_bar+=15
	load_bars(load_bar)


	
	playerstandinglist=[]
	for i in range(23):
		a="Jotaro/Standing/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat, tall))
		playerstandinglist.append(b)

	

	playerstandinglistRight=[]
	for i in range(23):
		a="Jotaro/Standing/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat, tall))
		b=pygame.transform.flip(b,True,False)
		playerstandinglistRight.append(b)



	#ATTACKS
	
	playerpunch=[]
	for i in range(9):
		a="Jotaro/Punch/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat, tall))
		playerpunch.append(b)

	
	
	playerpunchRight=[]
	for i in range(9):
		a="Jotaro/Punch/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat, tall))
		b=pygame.transform.flip(b,True,False)
		playerpunchRight.append(b)

	
	
	playerkick=[]
	for i in range(8):
		a="Jotaro/Kick/"+str(i)+".png"
		b=pygame.image.load(a)	 
		b=pygame.transform.scale(b, (fat, tall))
		playerkick.append(b)

	load_bar+=15
	load_bars(load_bar)

	
	
	playerkickRight=[]
	for i in range(8):
		a="Jotaro/Kick/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat, tall))
		b=pygame.transform.flip(b,True,False)
		playerkickRight.append(b)

	
	
	player_power1=[]
	for i in range(1,26):
		a="Jotaro/power_move1/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat, tall))
			 																																																							
		player_power1.append(b)

	
	
	player_power1Right=[]
	for i in range(1,26):
		a="Jotaro/power_move1/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat, tall))
		b=pygame.transform.flip(b,True,False)
		player_power1Right.append(b)

	
	
	player_power2=[]
	for i in range(0,40):
		a="Jotaro/power_move2/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat+80, tall))
		player_power2.append(b)

	
	
	player_power2Right=[]
	for i in range(0,40):
		a="Jotaro/power_move2/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat+80, tall))
		b=pygame.transform.flip(b,True,False)
		player_power2Right.append(b)

	load_bar+=15
	load_bars(load_bar)

	
	
	player_power3=[]
	for i in range(0,27):
		a="Jotaro/power_move3/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat, tall))
		player_power3.append(b)

	
	
	player_power3Right=[]
	for i in range(0,27):
		a="Jotaro/power_move3/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat, tall))
		b=pygame.transform.flip(b,True,False)
		player_power3Right.append(b)

	
	
	player_power4=[]
	for i in range(0,23):
		a="Jotaro/power_move4/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat+100, tall+10))
		player_power4.append(b)

	
	
	player_power4Right=[]
	for i in range(0,23):
		a="Jotaro/power_move4/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat+100, tall+10))
		b=pygame.transform.flip(b,True,False)
		player_power4Right.append(b)



	
	dio=[]
	for i in range(9):
		a="Dio/Standing/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat,tall))
		dio.append(b)

	
	load_bar+=15
	load_bars(load_bar)

	
	
	dioRightlist=[]
	for i in range(9):
		a="Dio/Standing/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat,tall))
		b=pygame.transform.flip(b,True,False)
		dioRightlist.append(b)


	
	
	dioWalkAnimation=[]
	for i in range(15):
		a="Dio/Right/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat, tall))
		dioWalkAnimation.append(b)

	
	
	dioLeftAnimation=[]
	for i in range(15):
		a="Dio/Left/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat,tall))
		dioLeftAnimation.append(b)

	
	
	dioPunchAnimation=[]
	for i in range(5):
		a="Dio/Punch/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat,tall))
		dioPunchAnimation.append(b)

	
	
	dioPunchAnimationRight=[]
	for i in range(5):
		a="Dio/Punch/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat,tall))
		b=pygame.transform.flip(b,True,False)
		dioPunchAnimationRight.append(b)

	
	load_bar+=15
	load_bars(load_bar)


	

	dioHurtAnimation=[]
	for i in range(7):
		a="Dio/Hurt/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat+10,tall))
		dioHurtAnimation.append(b)

	

	dioHurtAnimationRight=[]
	for i in range(7):
		a="Dio/Hurt/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat+10,tall))
		b=pygame.transform.flip(b,True,False)
		dioHurtAnimationRight.append(b)

	
	
	diopowermove1=[]
	for i in range(22):
		a="Dio/powermove_1/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat+10,tall))
		diopowermove1.append(b)

	
	
	diopowermove1Right=[]
	for i in range(22):
		a="Dio/powermove_1/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat+10,tall))
		b=pygame.transform.flip(b,True,False)
		diopowermove1Right.append(b)




	
	diopowermove2=[]
	for i in range(42):
		a="Dio/powermove_2/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat+10,tall))
		diopowermove2.append(b)

	load_bar+=15
	load_bars(load_bar)

	
	diopowermove2Right=[]
	for i in range(42):
		a="Dio/powermove_2/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat+10,tall))
		b=pygame.transform.flip(b,True,False)
		diopowermove2Right.append(b)



	
	diopowermove3=[]
	for i in range(55):
		a="Dio/powermove_3/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat+900,tall+300))
		diopowermove3.append(b)

	
	diopowermove3Right=[]
	for i in range(55):
		a="Dio/powermove_3/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat+900,tall+300))
		b=pygame.transform.flip(b,True,False)
		diopowermove3Right.append(b)


	
	diopowermove4=[]
	for i in range(10):
		a="Dio/powermove_4/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat+10,tall))
		diopowermove4.append(b)


	diopowermove4Right=[]
	for i in range(10):
		a="Dio/powermove_4/"+str(i)+".png"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (fat+10,tall))
		b=pygame.transform.flip(b,True,False)
		diopowermove4Right.append(b)

	load_bar+=15
	load_bars(load_bar)

	
	backgroundanimation=[]
	for i in range(7):
		a="background/"+str(i)+".jpeg"
		b=pygame.image.load(a)
		b=pygame.transform.scale(b, (4000,1080))
		backgroundanimation.append(b)


	
	dioProjectileAttack=pygame.image.load("Dio/powermove_1/22.png")
	dioProjectileAttack=pygame.transform.scale(dioProjectileAttack,(650,450))



	dioProjectileAttackRight=pygame.image.load("Dio/powermove_1/22.png")
	dioProjectileAttackRight=pygame.transform.scale(dioProjectileAttackRight,(650,450))
	dioProjectileAttackRight=pygame.transform.flip(dioProjectileAttackRight,True,False)



#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 
#                                                                  #======================#
#                                                                  # STATUS BAR FUNCTIONS #
# 																   #======================#
 
#Functions: These def functions are used to draw (acording to the specified conditions) the status bars (both health and power) on the screen.   

#                                                                    #======================#
#--------------------------------------------------------------------# HEALTH BARS FUNCTION #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#																     #======================#
	
# Function: This def functions are used to draw the enemy and player health bars on the screen.

	def health_bars(player_health,enemy_health):
		if player_health>75:
			player_health_color=green
		
		elif player_health>50:
			player_health_color=yellow
		
		else:
			player_health_color=red
		
		if enemy_health>75:
			enemy_health_color=green
		
		elif enemy_health>50:
			enemy_health_color=yellow
		
		else:
			enemy_health_color=red
		
		if render:
			pygame.draw.rect(surface,player_health_color,(1170,80,player_health*6,15))
			pygame.draw.rect(surface,enemy_health_color,(200,80,enemy_health*6,30))


#                                                                  #====================#
#------------------------------------------------------------------# POWER BAR FUNCTION #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#																   #====================#

# Function: This def functions are used to draw the enemy and player power bars on the screen.

	def power_bars(player_power,enemy_power):

		if player_power>75:
			power_move3=True

		elif player_power>50:
			power_move2=True

		elif player_power>25:
			power_move1=True

		player_power_color=blue
		enemy_power_color=blue

		if render:
			pygame.draw.rect(surface,player_power_color,(1170,100,player_power*6,15))
			#pygame.draw.rect(surface,enemy_power_color,(200,100,enemy_power*6,15))

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	
	def surfacerefresh():

		global walkCount
		global x
		global y
		global jumpCount
		global isJump
		global left
		global right
		global punch
		global kick
		global stand
		
		global xD
		global yD
		global dioHurt
		global walkCountDio
		global standDio
		global dioRight
		global dioLeft
		global dioPunchCount
		global dioPunch
		
		global green
		global yellow
		global red
		
		global enemy_health
		global player_health
		global enemy_power
		global player_power
		global PunchCount
		
		global gameRun
		global render
		global blue
		
		global power_move1
		global power_move2
		global power_move3
		global power_move4
		global power_move1_frame,power_move2_frame,power_move3_frame,power_move4_frame
		
		global xB,yB
		global playerkick_frame
		global playerpunch_frame
		global dioHurt_frame
		global walk_frame

		global dio_power_move1
		global dio_power_move2
		global dio_power_move4
		global dio_power_move3

		global dio_power_move1_frame
		global dio_power_move2_frame
		global dio_power_move3_frame
		global dio_power_move4_frame

		global dio_move

		global frame_count
		global power_move

		global dio_punch_frame
		global dio_frame_count
		global minDis

		#TIME PAUSE CHECK
		global dio_pause
		global dio_pause_frame_count
		global dio_pause_real

		global player_pause
		global player_pause_frame_count
		global player_pause_real

		global dio_power_move1_damage
		global dio_power_move2_damage
		global dio_power_move3_damage
		global dio_power_move4_damage

		global player_power_move1_damage
		global player_power_move2_damage
		global player_power_move3_damage
		global player_power_move4_damage

		global dio_projectile_attack

		global xK,yK,vK

		global Left,Right
		global dio_RIGHT,dio_LEFT
		global Za_Worldo_Sound
		global dio_muda_Sound
		global dio_roadrollar_Sound
		global dio_knifethrow_Sound
		global dio_attack_Sound
		global dio_hurt_Sound
		global jotaro_attack_Sound
		global jotaro_attack2_Sound
		global jotaro_ora_Sound
		global jotaro_oraoraend_Sound
		global jotaro_power1_Sound
		global background_count
		global background_check







		power_bars(player_power,enemy_power)
		distanceDioJotaro= abs(((xD-x)**2+(yD-y)**2)**0.5)
		distanceDioJotaro2= (xD-x)
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#                                                                       #===============#
#-----------------------------------------------------------------------# DIO ANIMATION #-----------------------------------------------------------------------------------------------------------------------------
#                                                                       #===============#
#player_health
    
#----#==========#
#----# DIO HURT #
#----#==========#
#- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -
		if dioHurt and not dio_pause_real and render and not power_move:	
			if dioHurt_frame<14:
				
				if dio_hurt_Sound<1 and render:
					dio_hurt.play()
					dio_hurt_Sound+=1
				
				if dio_RIGHT:
					surface.blit(dioHurtAnimation[dioHurt_frame//2],(xD,yD))
					#surface.blit(dioHurtAnimation[dioHurt_frame//3],(xD,yD))
					dioHurt_frame+=1
				
				elif dio_LEFT:
					surface.blit(dioHurtAnimationRight[dioHurt_frame//2],(xD,yD))
					#surface.blit(dioHurtAnimation[dioHurt_frame//3],(xD,yD))
					dioHurt_frame+=1
				
				else:
					surface.blit(dioHurtAnimation[dioHurt_frame//2],(xD,yD))
					#surface.blit(dioHurtAnimation[dioHurt_frame//3],(xD,yD))
					dioHurt_frame+=1

			else:
				dio_hurt_Sound=0
				dioHurt_frame=0
				standDio=True


		if walkCountDio+1>=28:
			walkCountDio=0

		if walkCount+1>=28:
			walkCount=0

#- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -
#-----#========================#	
#-----# DIO MOVEMENT ANIMATION #
#-----#========================#

#-  -  -  -  -  -  -  -  -   -  -  -  -  -  -  -  -  -   -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -   -  -  -  -  -   -   -   -  -  -   -   -   -   -     -   -   -   -    -  - - - - - - - - - - - - - - -- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -

#------------#==============================#
#------------# DIO RIGHT MOVEMENT ANIMATION #
#------------#==============================#

#-  -  -  -  -  -  -  -  -   -  -  -  -  -  -  -  -  -   -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -   -  -  -  -  -   -   -   -  -  -   -   -   -   -     -   -   -   -    -  - - - - - - - - - - - - - - -- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -
	
		if dioRight==True and render and not dioPunch and not dio_pause_real:
			xD+=8
			standDio=False

			surface.blit(dioWalkAnimation[walkCountDio//4],(xD,yD))
			walkCountDio+=1

#-  -  -  -  -  -  -  -  -   -  -  -  -  -  -  -  -  -   -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -   -  -  -  -  -   -   -   -  -  -   -   -   -   -     -   -   -   -    -  - - - - - - - - - - - - - - -- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -

#------------#=============================#
#------------# DIO LEFT MOVEMENT ANIMATION #
#------------#=============================#

		if dioLeft==True and render and not dio_pause_real:
			xD-=8
			standDio=False
			surface.blit(dioLeftAnimation[walkCountDio//4],(xD,yD))
			walkCountDio+=1

#-  -  -  -  -  -  -  -  -   -  -  -  -  -  -  -  -  -   -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -   -  -  -  -  -   -   -   -  -  -   -   -   -   -     -   -   -   -    -  - - - - - - - - - - - - - - -- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -

#------------#=============================#
#------------# DIO LEFT MOVEMENT ANIMATION #
#------------#=============================#

		if standDio and not dioRight and not dioLeft and render and not dio_pause_real:
			if dio_RIGHT:
				surface.blit(dio[walkCount//4],(xD,yD))
				walkCountDio+=1
			
			elif dio_LEFT:
				surface.blit(dioRightlist[walkCount//4],(xD,yD))
				walkCountDio+=1
			
			else:
				surface.blit(dio[walkCount//4],(xD,yD))
				walkCountDio+=1


#-  -  -  -  -  -  -  -  -   -  -  -  -  -  -  -  -  -   -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -   -  -  -  -  -   -   -   -  -  -   -   -   -   -     -   -   -   -    -  - - - - - - - - - - - - - - -- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -

#------------#====================#
#------------# DIO MOVEMENT LOGIC #
#------------#====================#
		
		if dioHurt==False and (dioRight==False or dioLeft==False) and dioPunch==False and not power_move :
			standDio=True

		elif dioHurt==True:
			dioRight=False
			dioLeft=False
			standDio=False
			dioPunch=False

		if dio_pause_real:
			surface.blit(dio[5],(xD,yD))

#-  -  -  -  -  -  -  -  -   -  -  -  -  -  -  -  -  -   -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -   -  -  -  -  -   -   -   -  -  -   -   -   -   -     -   -   -   -    -  - - - - - - - - - - - - - - -- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -- - - - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - - -

			
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////	

#                                                                       #==================#
#-----------------------------------------------------------------------# DIO ATTACK LOGIC #-----------------------------------------------------------------------------------------------------------------------------
#                                                                       #==================#		

		if abs(xD-x)<minDis and dioHurt==False and not power_move and not dio_pause_real:
		#	print("BRUUUUUUUUUUUUUUUUUUUUHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh",abs(xD-x))
				dioRight=False
				standDio=False
				dioLeft=False
				dioPunch=True
			#if dioPunch:

				#if x<=1600:

			#else: standDio=True	#	x+=50

		if dioPunch and render and dio_punch_frame<15 and dio_frame_count<30 and not dio_pause_real :

				#xD-=1
			#	if dio_frame_count<30:
			player_health-=0.05
					#if enemy_power<=100:
					#	enemy_power+=attack_reward

			#if dio_attack_Sound<1 and render:
			#	dio_attack.play()
			#	dio_attack_Sound+=1



			if dio_RIGHT:
				surface.blit(dioPunchAnimation[dio_punch_frame//3],(xD,yD))
				dio_punch_frame+=1
			
			elif dio_LEFT:
				surface.blit(dioPunchAnimationRight[dio_punch_frame//3],(xD,yD))
				dio_punch_frame+=1
			
			else:
				surface.blit(dioPunchAnimation[dio_punch_frame//3],(xD,yD))
				dio_punch_frame+=1

			dioRight=False
			dioLeft=False
				#else:
				#	dio_frame_count=0

		else:
			dio_attack_Sound=0
			dio_frame_count=0
			dio_punch_frame=0
			dioPunch=False
			standDio=True

		if dioHurt:
			standDio=False

		
		if dio_projectile_attack and render:


			
			if dio_RIGHT:
				surface.blit(dioProjectileAttack,(xK,yK))
				xK+=vK
			
			elif dio_LEFT:
				surface.blit(dioProjectileAttackRight,(xK,yK))
				xK-=vK
			
			else:
				surface.blit(dioProjectileAttack,(xK,yK))
				xK+=vK

			
			if abs(xK-x)<minDis:
				player_health-=player_power_move1_damage*7
			
			if xK>1850 or xK<-20:
				dio_projectile_attack=False
				xk=xD

		else:
			#dio_projectile_attack=False
			xK=xD
			yK=yD




		#if dio_projectile_attack and abs(xD-x)<minDis:
		#	player

		


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




		if not isJump:
			if left and render:
			
				if walk_frame<28:
					stand=False
					punch=False
					dioHurt=False
					surface.blit(playerleft[walk_frame//4],(x,y))
					walk_frame+=1
					if x>=10:
						x-=13
					#walkCount+=1
				else:
					walk_frame=0
					#left=False
					stand=True
		else:

			if left and render:
				dioHurt=False

				if x>=10:
					x-=30

		if not isJump:

			if stand and render:

				if Left:
					surface.blit(playerstandinglist[walkCount//4],(x,y))
					walkCount+=1
			
				elif Right:
					surface.blit(playerstandinglistRight[walkCount//4],(x,y))
					walkCount+=1
			
				else:
					surface.blit(playerstandinglist[walkCount//4],(x,y))
					walkCount+=1


		if not isJump:

			if right and render:

				stand=False
				punch=False
				dioHurt=False
				surface.blit(playerright[walkCount//4],(x,y))
				
				if x<=w-250:
					
					x+=13
					walkCount+=1
		else:

			if right and render:
				
				punch=False
				dioHurt=False
				
				if x<=w-300:
					
					x+=30
		
		if isJump and punch==False and render:
			#kick
			stand=False
			dioHurt=False
			
			if jotaro_attack2_Sound<1 and render:
				jotaro_attack2.play()
				jotaro_attack2_Sound+=1
			
			if Left:
				surface.blit(playerjump[walkCount//4],(x,y))
				walkCount+=1
			
			elif Right:
				surface.blit(playerJumpRight[walkCount//4],(x,y))
				walkCount+=1
			
			else:
				surface.blit(playerjump[walkCount//4],(x,y))
				walkCount+=1
			#pygame.display.update()
		
		if isJump:
		
			if jumpCount>=-10:
				neg=1
				
				if jumpCount<0:
				
					neg=-1
				y-=(jumpCount**2)*neg*1.5
				jumpCount-=1
				#pygame.display.update()
			else:
				jotaro_attack2_Sound=0

				isJump=False
				stand=True
				jumpCount=10
				#pygame.display.update()
		#if not isJump:

		if punch and render:
			if playerpunch_frame<18:

				#if jotaro_attack_Sound<1 and render:
				#	jotaro_attack.play()
				#	jotaro_attack_Sound+=1

				left=False
				right=False
				stand=False
				#isJump=False
				kick=False
				if Left:
					surface.blit(playerpunch[playerpunch_frame//2],(x,y))
				#surface.blit(playerpunch[playerpunch_frame//3],(x,y))
					playerpunch_frame+=1

				elif Right:
						surface.blit(playerpunchRight[playerpunch_frame//2],(x,y))
						#surface.blit(playerpunch[playerpunch_frame//3],(x,y))
						playerpunch_frame+=1
				else:
					surface.blit(playerpunch[playerpunch_frame//2],(x,y))
				#surface.blit(playerpunch[playerpunch_frame//3],(x,y))
					playerpunch_frame+=1

                                 
				if distanceDioJotaro<=minDis and xD>50 and xD<1600:
					standDio=False
					dioHurt=True
					enemy_health-=0.2
					if player_power<=100:
						player_power+=attack_reward*10
					if Left:
						xD-=50
					if Right:
						xD+=50

			else:
				jotaro_attack_Sound=0
				stand=True
				playerpunch_frame=0
				punch=False
				dioHurt=False
				


		if kick and render:

			#isJump=False
			if playerkick_frame<16:
				
				#if jotaro_attack_Sound<1 and render:
				#	jotaro_attack.play()
				#	jotaro_attack_Sound+=1
				if Left:
					surface.blit(playerkick[playerkick_frame//2],(x,y))
					playerkick_frame+=1
				elif Right:
					surface.blit(playerkickRight[playerkick_frame//2],(x,y))
					playerkick_frame+=1
				else:
					surface.blit(playerkick[playerkick_frame//2],(x,y))
					playerkick_frame+=1
				left=False
				right=False
				stand=False
				punch=False
				if kick and distanceDioJotaro<=minDis:
					standDio=False
					dioHurt=True
					enemy_health-=0.3
					if player_power<=100:
						player_power+=attack_reward*2
					xD-=100
			else:
				jotaro_attack_Sound=0
				playerkick_frame=0
				kick=False
				dioHurt=False
				stand=True

		if not isJump:

			distanceDioJotaro= abs(((xD-x)**2+(yD-y)**2)**0.5)
			distanceDioJotaro2=abs(xD-x)
			#speed=10

			if (xD-x)<0 and distanceDioJotaro2>minDis and dioHurt==False :
				
				dioRight=True
				dio_RIGHT
				dio_LEFT=False
				standDio=False
				dioLeft=False

			if (xD-x)>0 and distanceDioJotaro2>minDis and dioHurt==False:
			
				standDio=False
				dioRight=False
				dio_RIGHT=False
				dio_LEFT=True
				dioLeft=True

			if (xD-x)<0 and distanceDioJotaro2==minDis and dioHurt==False:
				
				standDio=True
				dioRight=False
				dioLeft=False

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 	                                                                    #=========================#
#-----------------------------------------------------------------------# PLAYER POWER MOVE LOGIC #-----------------------------------------------------------------------------------------------------------------------------
#                                                                       #=========================#		

# Funcion: These lines of code first check if a "power move" is "unlocked" and "activated" by the player or not and then accordingly activates "power moves". 

# NOTE: 1) power_move1 is enabled when the "player_power" variable is more than or equal to 25.
#		2) power_move2 is enabled when the "player_power" varibale is more than or equal to 50.
#		3) power_move3 is enabled when the "player_power" varibale is more than or equal to 75

# FUTURE ADDITIONs : Might add more power moves.....at least one more (when power level reaches 100)() DONE LOL

			if power_move1 and render:
				

				player_power=0
				if jotaro_power1_Sound<1 and render:
					jotaro_power1.play()
					jotaro_power1_Sound+=1

				if power_move1_frame<50:
					kick=False
					punch=False
					isJump=False
					right=False
					left=False
					stand=False
					if Left:
						surface.blit(player_power1[power_move1_frame//2],(x,y))
				 		power_move1_frame+=1
				 	elif Right:
				 		surface.blit(player_power1Right[power_move1_frame//2],(x,y))
				 		power_move1_frame+=1
				 	
				 	else:
				 		surface.blit(player_power1[power_move1_frame//2],(x,y))
				 		power_move1_frame+=1

					if abs(xD-x)<minDis:
				 		enemy_health-=player_power_move1_damage

				else:
					jotaro_power1_Sound=0
				 	power_move1_frame=2
				 	power_move1=False
				 	stand=True


			elif power_move2 and render:
				#player_power-=50
				#power_move2=False

				player_power=0
				if jotaro_ora_Sound<1 and render:
					jotaro_ora.play()
					jotaro_ora_Sound+=1

				if power_move2_frame<80:
					kick=False
					punch=False
					isJump=False
					right=False
					left=False
					stand=False
					if Left:
						surface.blit(player_power2[power_move2_frame//2],(x,y))
				 		power_move2_frame+=1
				 	elif Right:
				 		surface.blit(player_power2Right[power_move2_frame//2],(x,y))
				 		power_move2_frame+=1
				 	else:
				 		surface.blit(player_power2[power_move2_frame//2],(x,y))
				 		power_move2_frame+=1

					if abs(xD-x)<minDis:
				 		enemy_health-=player_power_move2_damage

				else:
					jotaro_ora_Sound=0
				 	power_move2_frame=0
				 	power_move2=False
				 	stand=True


			elif power_move3 and render:

				
				player_power=0

				if jotaro_oraoraend_Sound<1 and render:
					jotaro_oraoraend.play()
					jotaro_oraoraend_Sound+=1

				if power_move3_frame<54:
					kick=False
					punch=False
					isJump=False
					right=False
					left=False
					stand=False

					if Left:
						surface.blit(player_power3[power_move3_frame//2],(x,y))
				 		power_move3_frame+=1
				 	elif Right:
				 		surface.blit(player_power3Right[power_move3_frame//2],(x,y))
				 		power_move3_frame+=1
				 	else:
				 		surface.blit(player_power3[power_move3_frame//2],(x,y))
				 		power_move3_frame+=1

					if abs(xD-x)<minDis:				 	
				 		enemy_health-=player_power_move3_damage

				else:
					jotaro_oraoraend_Sound=0
				 	power_move3_frame=0
				 	power_move3=False
				 	stand=True

			elif power_move4 and render:
				if Za_Worldo_Sound<1:
					Za_Worldo.play()
					Za_Worldo_Sound+=1

				if power_move4_frame<46:

					kick=False
					punch=False
					isJump=False
					right=False
					left=False
					stand=False
					if Left:
						surface.blit(player_power4[power_move4_frame//2],(x,y))
				 		power_move4_frame+=1
				 	elif Right:
				 		surface.blit(player_power4Right[power_move4_frame//2],(x,y))
				 		power_move4_frame+=1
				 	else:
				 		surface.blit(player_power4[power_move4_frame//2],(x,y))
				 		power_move4_frame+=1

				 	if abs(xD-x)<minDis:
				 		enemy_health-=player_power_move4_damage




				else:
					Za_Worldo_Sound=0
				 	power_move4_frame=0
				 	power_move4=False
				 	stand=True

			if dio_pause and dio_pause_frame_count<300:
				dio_pause_real=True

			else:
				dio_pause_frame_count=0
				dio_pause_real=False
				dio_pause=False



#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#                                                                       #========================#
#-----------------------------------------------------------------------# ENEMY POWER MOVE LOGIC #-----------------------------------------------------------------------------------------------------------------------------
#                                                                       #========================#		
		if frame_count>175: # THIS BASICALLY ACTIVATES THE POWER MOVE EVERY 7000 FRAMES..... THIS POWER MOVE IS CHOSEN RANDOMLY SO AS TO MAKE THE GAME LESS PREDICTABLE 
			power_move=True
		else:
			power_move=False

		if power_move and not dioHurt and not dio_pause_real and render:

				powermovelist=["1","1","1","1","1","1","1","1","2","2","2","2","3","4","4","4",'4','4',"3","3","3","3"]
				
				if dio_move=="1":
					dio_power_move1=True
				else:
					dio_power_move1=False

				if dio_move=="2":
					dio_power_move2=True
				else:
					dio_power_move2=False

				if dio_move=="3":
					dio_power_move3=True
				else:
					dio_power_move3=False

				if dio_move=="4":
					
					dio_power_move4=True
				else:
					dio_power_move4=False	

	#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
			

				if dio_power_move1 and not dio_pause_real:

						
					
					if dio_power_move1_frame<44:
						

						if dio_knifethrow_Sound<1 and render:
							dio_knifethrow.play()
							dio_knifethrow_Sound+=1
						
						dioPunch=False
						#Jump=False
						dioRight=False
						dioLeft=False
						standDio=False
						if dio_RIGHT:
							surface.blit(diopowermove1[dio_power_move1_frame//2],(xD,yD))
						#print("READ THIS",power_move1_frame//2)
					 		dio_power_move1_frame+=1
					 	
					 	elif dio_LEFT:
					 		surface.blit(diopowermove1Right[dio_power_move1_frame//2],(xD,yD))
					 		dio_power_move1_frame+=1
					 	
					 	else:
					 		surface.blit(diopowermove1[dio_power_move1_frame//2],(xD,yD))
						#print("READ THIS",power_move1_frame//2)
					 		dio_power_move1_frame+=1

						#print("READ THIS",power_move1_frame//2)
					 		dio_power_move1_frame+=1



					else:
						dio_projectile_attack=True
					 	dio_power_move1_frame=0
					 	dio_power_move1=False
					 	standDio=True
					 	dio_knifethrow_Sound=0

					 	#if frame_count%1000==0:
						dio_move=powermovelist[random.randint(0,len(powermovelist)-1)]
						power_move=False
						frame_count=0
						
					



				elif dio_power_move2 and not dio_pause_real:

					if dio_muda_Sound<1 and render:
						dio_muda.play()
						dio_muda_Sound+=1

					if dio_power_move2_frame<82:
						#dioKick=False
						Punch=False
						#Jump=False
						dioRight=False
						dioLeft=False
						standDio=False

						if dio_RIGHT:
							surface.blit(diopowermove2[dio_power_move2_frame//2],(xD,yD))
						#print("READ THIS",power_move1_frame//2)
					 		dio_power_move2_frame+=1
					 	if dio_LEFT:
					 		surface.blit(diopowermove2Right[dio_power_move2_frame//2],(xD,yD))
						#print("READ THIS",power_move1_frame//2)
					 		dio_power_move2_frame+=1
					 	else:
					 		surface.blit(diopowermove2[dio_power_move2_frame//2],(xD,yD))
						#print("READ THIS",power_move1_frame//2)
					 		dio_power_move2_frame+=1


					 	if abs(xD-x)<minDis:
					 		player_health-=dio_power_move2_damage

					else:
					 	dio_power_move2_frame=0
					 	dio_power_move2=False
					 	standDio=True
					 	dio_muda_Sound=0
					 	#if frame_count%1000==0:
						dio_move=powermovelist[random.randint(0,len(powermovelist)-1)]
						power_move=False
						frame_count=0
						


				elif dio_power_move3 and not dio_pause_real:

					if dio_roadrollar_Sound<1 and render:
						dio_roadrollar.play()
						dio_roadrollar_Sound+=1

					if dio_power_move3_frame<108:
						#dioKick=False
						dioPunch=False
						#Jump=False																																																																							
						dioRight=False
						dioLeft=False
						standDio=False
						if dio_RIGHT:
							surface.blit(diopowermove3[dio_power_move3_frame//2],(xD,yD-200))
						#print("READ THIS",power_move1_frame//2)
					 		dio_power_move3_frame+=1
					 	if dio_LEFT:
					 		surface.blit(diopowermove3Right[dio_power_move3_frame//2],(xD,yD-200))
						#print("READ THIS",power_move1_frame//2)
					 		dio_power_move3_frame+=1
					 	else:
					 		surface.blit(diopowermove3[dio_power_move3_frame//2],(xD,yD-200))
						#print("READ THIS",power_move1_frame//2)
					 		dio_power_move3_frame+=1


					 	if abs(xD-x)<400:
					 		player_health-=dio_power_move3_damage
					 		

					else:
					 	dio_power_move3_frame=0
					 	dio_power_move3=False
					 	standDio=True
					 	dio_roadrollar_Sound=0

						#if frame_count%1000==0:
						dio_move=powermovelist[random.randint(0,len(powermovelist)-1)]
						power_move=False
						frame_count=0
						
				elif dio_power_move4 and not dio_pause_real:

					if dio_power_move4_frame<18:

						if Za_Worldo_Sound<1:
							Za_Worldo.play()
							Za_Worldo_Sound+=1

						#dioKick=False
						dioPunch=False
						#Jump=False
						dioRight=False
						dioLeft=False
						standDio=False
						player_pause=True
						background_check=True
						#Za_Worldo=pygame.mixer.music.load("Za_Worldo.wav")
						
						if dio_RIGHT:
							surface.blit(diopowermove4[dio_power_move4_frame//2],(xD,yD))
						#print("READ THIS",power_move4_frame)
					 		dio_power_move4_frame+=1
					 	
					 	elif dio_LEFT:
					 		surface.blit(diopowermove4Right[dio_power_move4_frame//2],(xD,yD))
						#print("READ THIS",power_move4_frame)
					 		dio_power_move4_frame+=1
					 	
					 	else:
					 		surface.blit(diopowermove4[dio_power_move4_frame//2],(xD,yD))
						#print("READ THIS",power_move4_frame)
					 		dio_power_move4_frame+=1

					 	if abs(xD-x)<minDis:
					 		player_health-=dio_power_move4_damage

					
					else:
					 	dio_power_move4_frame=0
					 	dio_power_move4=False
					 	standDio=True
					 	Za_Worldo_Sound=0
						#if frame_count%1000==0:
						dio_move=powermovelist[random.randint(0,len(powermovelist)-1)]
						power_move=False
						frame_count=0
						

				if player_pause and player_pause_frame_count<300:
					player_pause_real=True


				else:
					player_pause_frame_count=0
					player_pause_real=False
					player_pause=False


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		
		frame_count+=1
		dio_frame_count+=1
		dio_pause_frame_count+=1
		player_pause_frame_count+=1
		pygame.display.update()

	while gameRun==True:

		clock.tick(70)
		health_bars(player_health,enemy_health)
		distanceDioJotaro2oJotaro= abs(((xD-x)**2+(yD-y)**2)**0.5)
		distanceDioJotaro2= (xD-x)
		#power_bars(player_power,enemy_power)

		if left and dioLeft:
			xB+=3
			print(xB)
			#pygame.display.update()
		if right and dioRight:
			xB-=3 
			#pygame.display.update()
		if (dio_power_move4 or power_move4) and background_count<21 and background_check:
			surface.blit(backgroundanimation[background_count//3],(xB,0))

			background_count+=1


		else:
			if dio_pause_real or player_pause_real:
				surface.blit(backgroundanimation[6],(xB,0))
				pygame.mixer.music.pause()
			else:
				surface.blit(back,(xB,0))
				pygame.mixer.music.unpause()
			#surface.blit(back,(xB,0))
			background_count=0
			background_check=False











		surface.blit(player_icon,(1750,10))
		surface.blit(enemy_icon,(-30,10))
		surface.blit(jotaro_font,(1450,10))
		surface.blit(dio_font,(200,10))
		surface.blit(pause,(930,10))
		health_bars(player_health,enemy_health)

	

		if player_health<=0:
			render=False
			gameloop=False
			surface.fill((0,0,0))
			surface.blit(lose_screen,(0,60))



		if enemy_health<=0:
			render=False
			gameloop=False
			surface.fill((0,0,0))
			surface.blit(win_screen,(0,60))


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#                                                                       #=======================#
#-----------------------------------------------------------------------# DIO POWER MOVE LOGIC  #-----------------------------------------------------------------------------------------------------------------------------
#                                                                       #=======================#



#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


		for event in pygame.event.get():
			keys=pygame.key.get_pressed()

			if keys[pygame.K_LEFT] and not player_pause :

				left=True
				right=False
				stand=False
				punch=False
				kick=False
				Right=False
				Left=True
			elif keys[pygame.K_RIGHT] and not player_pause:
				left=False
				stand=False
				right=True
				punch=False
				kick=False
				Right=True
				Left=False
			else:
				left=False
				right=False
			#	punch=False
			#	dioHurt=False
			#	kick=False
				walkCount=0
			if not isJump:
				if keys[pygame.K_SPACE] and not player_pause : 
					isJump=True
					left=False
					right=False
					punch=False
					kick=False

			if  dio_power_move3 and abs(xD-x)<400:
				stand=False
				left=False
				right=False
				punch=False
				kick=False
				Right=False
				Left=False
				isJump=False
				power_move1=False
				power_move2=False
				power_move3=False
				power_move4=False




#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#                                                                       #=========================#
#-----------------------------------------------------------------------# PLAYER POWER MOVE CHECK #-----------------------------------------------------------------------------------------------------------------------------
#                                                                       #=========================#		
# Function: These lines of code check for the player "power" levels and accordingly enable "power moves" boolean, this will later enable the activation and animation of the player power move.

			if player_power>=25 and keys[pygame.K_1] and not player_pause:
				power_move1=True
			elif player_power>=50 and keys[pygame.K_2] and not player_pause:
				power_move2=True
			elif player_power>=75 and keys[pygame.K_3] and not player_pause:
				power_move3=True
			elif player_power>=90 and keys[pygame.K_4] and not player_pause:
				power_move4=True
				dio_pause=True
				background_check=True
			elif keys[pygame.K_w] and not player_pause :
				punch=True
			elif keys[pygame.K_q] and not player_pause :
				kick=True


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



			if left==False and right==False and isJump==False and punch==False and kick==False:
				stand=True
			if dioHurt==False:
				standDio=True
			if (xD-x)<0 and distanceDioJotaro2>=103 and dioHurt==False:
				standDio=False
				dioRight=True
			if(event.type==pygame.KEYDOWN):
			 	if (event.type==pygame.QUIT or event.key==pygame.K_ESCAPE ):
					surface.fill((0,0,0))
					pygame.display.update()
					render=False
					gameRun=False

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		
		surfacerefresh()



title_screen=pygame.image.load("TitleScreen1.png")
controls=pygame.image.load("help.png")
controls= pygame.transform.scale(controls, (1920,950))
#1610,885

credits=pygame.image.load("credits.png")
credits= pygame.transform.scale(credits, (1920,950))

title_screen= pygame.transform.scale(title_screen, (1920,950))
surface.blit(title_screen,(0,60))

pygame.display.update()
control=False
main=False
credits_check=False

z=True


while z==True:

	for event in pygame.event.get():
		if(event.type==pygame.KEYDOWN):
			if event.key==pygame.K_SPACE:
				gameloop()
				z=False
	keys=pygame.key.get_pressed()

	
	if keys[pygame.K_h]:
		main=False
		control=True
		credits_check=False

	
	if keys[pygame.K_c]:
		main=False
		control=False
		credits_check =True

	
	if control:
		surface.fill((0,0,0))
		surface.blit(controls,(0,60))
		if keys[pygame.K_BACKSPACE]:
			control=False
			main=True
		pygame.display.update()

	
	if credits_check:
		surface.fill((0,0,0))
		surface.blit(credits,(0,60))
		if keys[pygame.K_BACKSPACE]:
			control=False
			credits_check=False
			main=True
		pygame.display.update()

	
	if main:
		surface.blit(title_screen,(0,60))
		pygame.display.update()
	
	
	if(event.type==pygame.KEYDOWN):
		if (event.type==pygame.QUIT or event.key==pygame.K_ESCAPE ):
			surface.fill((0,0,0))
			pygame.display.update()
			pygame.quit()
			quit()
pygame.quit()
quit()
	 																																																							