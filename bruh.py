import pygame
import random
import time
surface=pygame.display.set_mode((1200,800))



a=True
move=""
move_list=["Right","Left","Up","Down"]
move_learnt=[]
move_dict={}
m=1
time=0
dead=False
learn_list=[]
clock = pygame.time.Clock()
og_x=500
og_y=500
x=og_x
y=og_y
while a:
	clock.tick(5)	
	surface.fill((200,255,255)) 
	

	if not dead:
		i=random.randint(0,len(move_list)-1)
		move=move_list[i]
	#for event in pygame.event.get():
	#keys=pygame.key.get_pressed()
	#print(move_learnt)
	#print(move_dict)
	#print(m)
		print(time)
		#print(len(move_learnt))
		time+=1
		
		if move=="Left":
			if x>0:
				x-=10
				move_learnt.append(move)
				move_dict[m]=move_learnt

			else:
				dead=True
				print("\noops")
				x=og_x
				y=og_y
				m+=1
				time=0
								#x-=10
		elif move=="Right":
			if x<1100:
				x+=10
				move_learnt.append(move)
				move_dict[m]=move_learnt
			else:
				print("\noops")
				dead=True
				x=og_x
				y=og_y
				m+=1
				time=0
				move_learnt=[]

		elif move=="Down":
			if y<700:
				y+=10
				move_learnt.append(move)
				move_dict[m]=move_learnt
			else:
				dead=True
				print("\noops")
				x=og_x
				y=og_y	
				m+=1
				time=0
				move_learnt=[]		#y+=10
		elif move=="Up":
			if y>0:
				y-=10
				move_learnt.append(move)
				move_dict[m]=move_learnt	
			else:
				dead=True
				print("\noops")
				x=og_x
				y=og_y
				m+=1
				time=0
				move_learnt=[]
		
		#print(m,m-1)
		learn_list=[]
		move_dict_values=move_dict.values()
		learn_list=move_dict_values[-1]
		#if len(learn_list)>1:
		#	learn_list.pop()
		#	learn_list.pop()
		#for f in range (0,len(move_dict_values)-2):
		#	learn_list.append(move_dict_values[f])

		#print(learn_list)
	
	else:


		for move_play in learn_list:
			
			if move_play=="Left":
				if x>0:
					x-=10
					#move_learnt.append(move_play)
					#move_dict[m]=move_learnt
			
				else:
					learn_list.pop()
					i=random.randint(0,len(move_list)-1)
					learn_list.append(move_list[i])
					x=og_x
					y=og_y
					#break
									#x-=10
			elif move_play=="Right":
				if x<1100:
					x+=10
					#move_learnt.append(move_play)
					#move_dict[m]=move_learnt
				else:
					learn_list.pop()
					i=random.randint(0,len(move_list)-1)
					learn_list.append(move_list[i])
					x=og_x
					y=og_y
					#move_learnt=[]
					#break

			elif move_play=="Down":
				if y<700:
					y+=10
					#move_learnt.append(move_play)
					#move_dict[m]=move_learnt
				else:
					learn_list.pop()
					i=random.randint(0,len(move_list)-1)
					learn_list.append(move_list[i])
					x=og_x
					y=og_y	
					#move_learnt=[]	
					#break	#y+=10
			elif move_play=="Up":
				if y>0:
					y-=10
					#move_learnt.append(move_play)
					#move_dict[m]=move_learnt	
				else:
					learn_list.pop()
					i=random.randint(0,len(move_list)-1)
					learn_list.append(move_list[i])
					x=og_x
					y=og_y
					#move_learnt=[]
			
			#pygame.display.update()

					#break
		
		i=random.randint(0,len(move_list)-1)
		learn_list.append(move_list[i])
		
		print(len(learn_list))
		#print("learn ",learn_list)



		#print(learn_list)
		#print(move_dict)
				#y-=10
	for event in pygame.event.get():

		if event.type==pygame.QUIT:
			a=False

			


	#up,down,left,right=False,False,False,False
	pygame.draw.rect(surface,(0,100,100),(x,y,98,98))
	pygame.display.update()

#	print(len(move_learnt))
print(move_dict)
pygame.quit()
quit()