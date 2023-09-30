import pygame 
pygame.init()
	#vẽ kích thước khung
screen = pygame.display.set_mode((700,700))
PIN = (255,255,255)
VIOLET = (179,25,255)
BLU = (0,0,0)
GREY = (150,150,150)#màu sắc trong bảng igp color
running = True
font = pygame.font.SysFont('sans', 50)
text_1 = font.render('+', True, VIOLET)
text_2 = font.render('-', True, VIOLET)
text_3 = font.render('START', True, VIOLET)
text_4 = font.render('Reset', True, VIOLET)

while running: # vòng lặp cho game ko biến mất
	screen.fill(GREY)

			# mouse_x, mouse_y = pygame.mouse.get_pos()
			# print((mouse_x,mouse_y))
	pygame.draw.rect(screen, PIN, (150,75,65,65))
	pygame.draw.rect(screen, PIN, (250,75,65,65))
	pygame.draw.rect(screen, PIN, (360,75,250,65))

	pygame.draw.rect(screen, PIN, (150,250,65,65))
	pygame.draw.rect(screen, PIN, (250,250,65,65))
	pygame.draw.rect(screen, PIN, (360,250,250,65))

	pygame.draw.circle(screen, BLU, (375,460),125)
	pygame.draw.circle(screen, PIN, (375,460),120)
	pygame.draw.circle(screen, BLU, (375,460),3)

	pygame.draw.line(screen, BLU, (375,460), (375,350))
	pygame.draw.line(screen, BLU, (375,460), (375,400))
	pygame.draw.rect(screen, BLU, (100,605,555,60))
	pygame.draw.rect(screen, PIN, (105,607,540,55))
	screen.blit(text_1, (175,80))
	screen.blit(text_1, (275,80))
	screen.blit(text_2, (175,245))
	screen.blit(text_2, (265,245))
	screen.blit(text_3, (400,80))
	screen.blit(text_4, (400,245))

			
			
		    #chạy các sự kiện trong pygame
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				pass
			else:
				print("kiệt đẹp zai")
				

	pygame.display.flip() 


