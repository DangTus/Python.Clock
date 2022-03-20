import pygame
import time
import math

def draw_function():
	# vẽ 2 dấu cộng, start
	pygame.draw.rect(screen, WHILE, (100, 50, 50, 50))
	pygame.draw.rect(screen, WHILE, (200, 50, 50, 50))
	pygame.draw.rect(screen, WHILE, (300, 50, 150, 50))

	# vẽ 2 dấu trừ, reset
	pygame.draw.rect(screen, WHILE, (100, 200, 50, 50))
	pygame.draw.rect(screen, WHILE, (200, 200, 50, 50))
	pygame.draw.rect(screen, WHILE, (300, 200, 150, 50))

# vẽ đồng hồ
def draw_clock(time, tamX, tamY, r, lenKimPhut, lenKimGiay, speed):
	pygame.draw.circle(screen, WHILE, (tamX, tamY), r) # vẽ mặt đồng hồ
	pygame.draw.circle(screen, BLACK, (tamX, tamY), 5) # vẽ tâm đồng hồ

	#vẽ kim đồng hồ
	minute = int((time/speed)/60)
	second = time - minute*(60*speed)
	minute_alpa = float(minute) + second/(60*speed)

	# vẽ kim phút
	x = tamX + lenKimPhut*math.sin((minute_alpa*math.pi)/30)
	y = tamY - lenKimPhut*math.cos((minute_alpa*math.pi)/30)
	pygame.draw.line(screen, BLACK, (tamX, tamY), (x, y))

	# vẽ kim giây
	x = tamX + lenKimGiay*math.sin((second*math.pi)/(30*speed))
	y = tamY - lenKimGiay*math.cos((second*math.pi)/(30*speed))
	pygame.draw.line(screen, RED, (tamX, tamY), (x, y))

def setText_function():
	screen.blit(text_plus, (100, 50))
	screen.blit(text_minus, (100, 200))
	screen.blit(text_plus, (200, 50))
	screen.blit(text_minus, (200, 200))
	screen.blit(text_start, (300, 50))
	screen.blit(text_reset, (300, 200))

def setTime_function(time, speed):
	minute = int(time/60/speed)
	second = (time - minute*60*speed)/speed

	if second % 1 != 0:
		if second + 1 >= 60:
			second = 0
			minute += 1
		else:
			second += 1

	text_min = font.render(str(minute), True, BLACK)
	text_colon = font.render(":", True, BLACK)
	text_sec = font.render(str(int(second)), True, BLACK)

	screen.blit(text_min, (100, 125))
	screen.blit(text_colon, (160, 125))
	screen.blit(text_sec, (200, 125))

def draw_thanh_thoi_gian(time, total):
	if total == 0:
		redLen = 0	
	else:
		redLen = (time/total)*394
	pygame.draw.rect(screen, BLACK, (50, 550, 400, 50))
	pygame.draw.rect(screen, WHILE, (53, 553, 394, 44))
	pygame.draw.rect(screen, RED, (53, 553, redLen, 44))

pygame.init()

screen = pygame.display.set_mode((500, 650))
pygame.display.set_caption('Đồng hồ đếm ngược')

GREY = (120, 120, 120)
BLACK = (0, 0, 0)
WHILE = (255, 255, 255)
RED = (255, 0, 0)

font = pygame.font.SysFont('sans', 25)

text_plus = font.render("+", True, BLACK)
text_minus = font.render("-", True, BLACK)
text_start = font.render("Start", True, BLACK)
text_reset = font.render("Reset", True, BLACK)

running = True
status = False
total = 0
remaining = 0
speed = 100

while running:
	screen.fill(GREY)

	mouseX, mouseY = pygame.mouse.get_pos()

	draw_function()

	setText_function()

	# draw_clock(thời gian(sec), tâm X, tâm Y, bán kính, len kim dài, len kim ngắn, tốc độ)
	draw_clock(remaining, 250, 400, 100, 90, 90, speed)

	draw_thanh_thoi_gian(remaining, total * speed)
	
	setTime_function(remaining, speed)		

	if status:
		if remaining < 0:
			total = 0
			status = False
		else:
			remaining = remaining - 1
			time.sleep(1/speed)
	else:
		remaining = total * speed

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				#reset button
				if mouseX >= 300 and mouseX <= 450 and mouseY >= 200 and mouseY <= 250:
					status = False
					total = 0

				#start button
				elif mouseX >= 300 and mouseX <= 450 and mouseY >= 50 and mouseY <= 100:
					status = True

				#plus min button
				elif mouseX >= 100 and mouseX <= 150 and mouseY >= 50 and mouseY <= 100:
					if not status:
						total = total + 60

				#minus min button
				elif mouseX >= 100 and mouseX <= 150 and mouseY >= 200 and mouseY <= 250:
					if not status:
						total = total - 60 if total >= 60 else 0

				#plus sec button
				elif mouseX >= 200 and mouseX <= 250 and mouseY >= 50 and mouseY <= 100:
					if not status:
						total = total + 1

				#minus sec button
				elif mouseX >= 200 and mouseX <= 250 and mouseY >= 200 and mouseY <= 250:
					if not status:
						total = total - 1 if total >= 1 else 0

	pygame.display.flip()

pygame.quit()