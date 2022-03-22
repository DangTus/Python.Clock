import pygame
import time
import math

def align_center(text, startX, startY, width, height):
	return text.get_rect(center=(startX+width/2, startY+height/2))

def draw_function(status, mouseX, mouseY, colorHover):
	# vẽ nền thời gian
	pygame.draw.rect(screen, WHILE, (50, 125, 250, 50))

	if status == "off":
		# vẽ 3 dấu cộng, start
		pygame.draw.rect(screen, colorHover if mouseX >= 50 and mouseX <= 100 and mouseY >= 50 and mouseY <= 100 else WHILE, (50, 50, 50, 50))
		pygame.draw.rect(screen, colorHover if mouseX >= 150 and mouseX <= 200 and mouseY >= 50 and mouseY <= 100 else WHILE, (150, 50, 50, 50))
		pygame.draw.rect(screen, colorHover if mouseX >= 250 and mouseX <= 300 and mouseY >= 50 and mouseY <= 100 else WHILE, (250, 50, 50, 50))
		pygame.draw.rect(screen, colorHover if mouseX >= 350 and mouseX <= 500 and mouseY >= 50 and mouseY <= 100 else WHILE, (350, 50, 150, 50))

		# vẽ 3 dấu trừ, reset
		pygame.draw.rect(screen, colorHover if mouseX >= 50 and mouseX <= 100 and mouseY >= 200 and mouseY <= 250 else WHILE, (50, 200, 50, 50))
		pygame.draw.rect(screen, colorHover if mouseX >= 150 and mouseX <= 200 and mouseY >= 200 and mouseY <= 250 else WHILE, (150, 200, 50, 50))
		pygame.draw.rect(screen, colorHover if mouseX >= 250 and mouseX <= 300 and mouseY >= 200 and mouseY <= 250 else WHILE, (250, 200, 50, 50))
		pygame.draw.rect(screen, colorHover if mouseX >= 350 and mouseX <= 500 and mouseY >= 200 and mouseY <= 250 else WHILE, (350, 200, 150, 50))

	else:
		# vẽ nút pause
		pygame.draw.rect(screen, colorHover if mouseX >= 350 and mouseX <= 500 and mouseY >= 125 and mouseY <= 175 and status != "alarm" else WHILE, (350, 125, 150, 50))
		if status == "pause":
			# vẽ nút reset
			pygame.draw.rect(screen, colorHover if mouseX >= 350 and mouseX <= 500 and mouseY >= 200 and mouseY <= 250 else WHILE, (350, 200, 150, 50))

def setText_function():
	if status == "off":
		screen.blit(text_plus, align_center(text_plus, 50, 50, 50, 50))
		screen.blit(text_minus, align_center(text_minus, 50, 200, 50, 50))

		screen.blit(text_plus, align_center(text_plus, 150, 50, 50, 50))
		screen.blit(text_minus, align_center(text_minus, 150, 200, 50, 50))

		screen.blit(text_plus, align_center(text_plus, 250, 50, 50, 50))
		screen.blit(text_minus, align_center(text_minus, 250, 200, 50, 50))

		screen.blit(text_start, align_center(text_start, 350, 50, 150, 50))
		screen.blit(text_reset, align_center(text_reset, 350, 200, 150, 50))

	else:
		screen.blit(text_pause, align_center(text_pause, 350, 125, 150, 50))
		if status == "pause":
			screen.blit(text_reset, align_center(text_reset, 350, 200, 150, 50))

# vẽ đồng hồ
def draw_clock(time, tamX, tamY, r, lenKimGio, lenKimPhut, lenKimGiay):
	# vẽ mặt đồng hồ
	pygame.draw.circle(screen, BLACK, (tamX, tamY), r+3)
	pygame.draw.circle(screen, WHILE, (tamX, tamY), r)

	# vẽ điểm đánh dấu số phút
	for i in range(0, 60, 5):
		x1 = tamX + (r-10)*math.sin(i*math.pi/6)
		y1 = tamY - (r-10)*math.cos(i*math.pi/6)
		x2 = tamX + r*math.sin(i*math.pi/6)
		y2 = tamY - r*math.cos(i*math.pi/6)		
		pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2))

	# vẽ logo
	text_logo = font.render("Tus", True, BLACK)
	screen.blit(text_logo, align_center(text_logo, tamX-r, tamY-r, r*2, r))

	# vẽ kim đồng hồ
	hour = math.floor(time/3600)
	minute = math.floor((time - hour*3600) / 60)
	second = time - hour*3600 - minute*60

	hour_alpa = hour + minute/60
	minute_alpa = minute + second/60

	# vẽ kim giờ
	x = tamX + lenKimGio*math.sin(hour_alpa*math.pi/6)
	y = tamY - lenKimGio*math.cos(hour_alpa*math.pi/6)
	pygame.draw.line(screen, BLACK, (tamX, tamY), (x, y))

	# vẽ kim phút
	x = tamX + lenKimPhut*math.sin(minute_alpa*math.pi/30)
	y = tamY - lenKimPhut*math.cos(minute_alpa*math.pi/30)
	pygame.draw.line(screen, BLACK, (tamX, tamY), (x, y))

	# vẽ kim giây
	x = tamX + lenKimGiay*math.sin(second*math.pi/30)
	y = tamY - lenKimGiay*math.cos(second*math.pi/30)
	pygame.draw.line(screen, RED, (tamX, tamY), (x, y))

	# vẽ tâm đồng hồ
	pygame.draw.circle(screen, BLACK, (tamX, tamY), 5)

def setTime_function(time):
	time = math.ceil(time)

	hour = math.floor(time/3600)
	minute = math.floor((time - hour*3600) / 60)
	second = time - hour*3600 - minute*60

	text_hour = font.render(str(hour), True, BLACK)
	text_min = font.render(str(minute), True, BLACK)
	text_colon = font.render(":", True, BLACK)
	text_sec = font.render(str(second), True, BLACK)

	screen.blit(text_hour, align_center(text_min, 50, 125, 50, 50))
	screen.blit(text_colon, align_center(text_colon, 100, 125, 50, 50))
	screen.blit(text_min, align_center(text_min, 150, 125, 50, 50))
	screen.blit(text_colon, align_center(text_colon, 200, 125, 50, 50))
	screen.blit(text_sec, align_center(text_sec, 250, 125, 50, 50))

def draw_thanh_thoi_gian(time, total):
	if total == 0:
		redLen = 0
	else:
		redLen = (time/total)*(WIDTH_SCREEN - 106)
	pygame.draw.rect(screen, BLACK, (50, 550, WIDTH_SCREEN - 100, 50))
	pygame.draw.rect(screen, WHILE, (53, 553, WIDTH_SCREEN - 106, 44))
	pygame.draw.rect(screen, RED, (53, 553, redLen, 44))

def alarm_function(x, y):
	text_alarm = font.render("Time out!", True, WHILE)

	pygame.draw.rect(screen, BLACK, (0, y/2 - 50, x, 100))
	screen.blit(text_alarm, align_center(text_alarm, 0, y/2 - 50, x, 100))

pygame.init()
pygame.mixer.init()

WIDTH_SCREEN = 550
HEIGHT_SCREEN = 650
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))

pygame.display.set_caption('Đồng hồ đếm ngược')
pygame_icon = pygame.image.load('imgs/clock_img.png')
pygame.display.set_icon(pygame_icon)

running = True
status = "off"
total = 0
remaining = 0
music = pygame.mixer.Sound("music/music.mp3")

GREY = (120, 120, 120)
BLACK = (0, 0, 0)
WHILE = (255, 255, 255)
RED = (255, 0, 0)

font = pygame.font.SysFont('sans', 25)

text_plus = font.render("+", True, BLACK)
text_minus = font.render("-", True, BLACK)
text_start = font.render("Start", True, BLACK)
text_reset = font.render("Reset", True, BLACK)

while running:
	screen.fill(GREY)

	text_pause = font.render("Countinue" if status == "pause" else "Pause", True, BLACK)

	mouseX, mouseY = pygame.mouse.get_pos()

	draw_function(status, mouseX, mouseY, RED)

	setText_function()

	# draw_clock(thời gian(sec), tâm X, tâm Y, bán kính, len kim dài, len kim ngắn, tốc độ)
	draw_clock(remaining, 275, 400, 100, 50, 80, 80)

	draw_thanh_thoi_gian(remaining, total)
	
	setTime_function(remaining)	

	if status == "run":
		if remaining < 0:
			music.play()
			status = "alarm"
			total = 0
		else:
			remaining = remaining - 0.01
			time.sleep(0.01)
	elif status == "off":
		remaining = total		
	elif status == "alarm":		
		alarm_function(WIDTH_SCREEN, HEIGHT_SCREEN)		

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			# sự kiện khi click chuột trái
			if event.button == 1:

				#stop alarm
				if status == "alarm":
					music.stop()
					status = "off"

				#reset button
				elif mouseX >= 350 and mouseX <= 500 and mouseY >= 200 and mouseY <= 250:
					if status != "run":
						status = "off"
						total = 0

				#start button
				elif mouseX >= 350 and mouseX <= 500 and mouseY >= 50 and mouseY <= 100 and total > 0 and status == "off":
					status = "run"

				#pause button
				elif mouseX >= 350 and mouseX <= 500 and mouseY >= 125 and mouseY <= 175:
					status = "pause" if status == "run" else "run"

				#plus hour button
				elif mouseX >= 50 and mouseX <= 100 and mouseY >= 50 and mouseY <= 100 and status == "off":
					total = total + 3600

				#minus hour button
				elif mouseX >= 50 and mouseX <= 100 and mouseY >= 200 and mouseY <= 250 and status == "off":
					total = total - 3600 if total >= 3600 else 0

				#plus min button
				elif mouseX >= 150 and mouseX <= 200 and mouseY >= 50 and mouseY <= 100 and status == "off":
					total = total + 60

				#minus min button
				elif mouseX >= 150 and mouseX <= 200 and mouseY >= 200 and mouseY <= 250 and status == "off":
					total = total - 60 if total >= 60 else 0

				#plus sec button
				elif mouseX >= 250 and mouseX <= 300 and mouseY >= 50 and mouseY <= 100 and status == "off":
					total = total + 1

				#minus sec button
				elif mouseX >= 250 and mouseX <= 300 and mouseY >= 200 and mouseY <= 250 and status == "off":
					total = total - 1 if total >= 1 else 0

				# set giá trị tối đa là 12 giờ
				total = total if total <= 43200 else 43200

	pygame.display.flip()

pygame.quit()