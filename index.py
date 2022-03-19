import pygame
import time

def draw_function():
	pygame.draw.rect(screen, WHILE, (100, 50, 50, 50))
	pygame.draw.rect(screen, WHILE, (200, 50, 50, 50))
	pygame.draw.rect(screen, WHILE, (300, 50, 150, 50))

	pygame.draw.rect(screen, WHILE, (100, 200, 50, 50))
	pygame.draw.rect(screen, WHILE, (200, 200, 50, 50))
	pygame.draw.rect(screen, WHILE, (300, 200, 150, 50))

def setText_function():
	screen.blit(text_plus, (100, 50))
	screen.blit(text_minus, (100, 200))
	screen.blit(text_plus, (200, 50))
	screen.blit(text_minus, (200, 200))
	screen.blit(text_start, (300, 50))
	screen.blit(text_reset, (300, 200))

def setTime_function(total):
	text_min = font.render(str(int(total/60)), True, BLACK)
	text_colon = font.render(":", True, BLACK)
	text_sec = font.render(str(total-int(total/60)*60), True, BLACK)

	screen.blit(text_min, (100, 125))
	screen.blit(text_colon, (160, 125))
	screen.blit(text_sec, (200, 125))

pygame.init()

screen = pygame.display.set_mode((500, 600))

GREY = (120, 120, 120)
BLACK = (0, 0, 0)
WHILE = (255, 255, 255)

font = pygame.font.SysFont('sans', 25)

text_plus = font.render("+", True, BLACK)
text_minus = font.render("-", True, BLACK)
text_start = font.render("Start", True, BLACK)
text_reset = font.render("Reset", True, BLACK)

running = True
total = 0

while running:
	screen.fill(GREY)

	mouseX, mouseY = pygame.mouse.get_pos()

	draw_function()

	setText_function()

	setTime_function(total)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				#reset button
				if mouseX >= 300 and mouseX <= 450 and mouseY >= 200 and mouseY <= 250:
					total = 0
				#plus min button
				if mouseX >= 100 and mouseX <= 150 and mouseY >= 50 and mouseY <= 100:
					total = total + 60
				#minus min button
				if mouseX >= 100 and mouseX <= 150 and mouseY >= 200 and mouseY <= 250:
					total = total - 60 if total >= 60 else 0
				#plus sec button
				if mouseX >= 200 and mouseX <= 250 and mouseY >= 50 and mouseY <= 100:
					total = total + 1
				#minus sec button
				if mouseX >= 200 and mouseX <= 250 and mouseY >= 200 and mouseY <= 250:
					total = total - 1 if total >= 1 else 0

	pygame.display.flip()

pygame.quit()