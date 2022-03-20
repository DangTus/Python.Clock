import pygame
import time
import math

pygame.init()

screen = pygame.display.set_mode((500, 650))

GREY = (120, 120, 120)
BLACK = (0, 0, 0)
WHILE = (255, 255, 255)
RED = (255, 0, 0)

font = pygame.font.SysFont('sans', 25)

running = True
start_status = False
total = 0
time_start = 0

while running:
	screen.fill(GREY)

	if not start_status:
		pygame.draw.rect(screen, WHILE, (50, 550, 400, 50))
		pygame.draw.rect(screen, RED, (50, 550, 400, 50))
	else:
		if i>=0:
			if i % 100 == 0:
				print(i/100)
			redLen = (i/float(total))*400
			pygame.draw.rect(screen, RED, (50, 550, redLen, 50))
			pygame.draw.rect(screen, WHILE, (50+redLen, 550, 400-redLen, 50))			
			time.sleep(0.01)
			i = i-1
		else:
			start_status = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			i = 100
			total = 100
			start_status = True

	pygame.display.flip()

pygame.quit()