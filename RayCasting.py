import pygame
from pygame.locals import *
from sys import exit
from math import *
from random import *
pygame.init()

WIDTH = 960
HEIGHT = 640
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
pygame.display.set_caption("RAY CASTING!")

WALLS = []
for i in range(7):
	x1 = randint(100,860)
	x2 = randint(100,860)
	y1 = randint(100,540)
	y2 = randint(100,540)
	WALLS.append(((x1,y1),(x2,y2)))

DENSITY = 2
INTENSITY = 2000
SPAN = int(DENSITY*360)

def cross(R,S):
	return R[0]*S[1]-R[1]*S[0]

def sub(Q,P):
	return (Q[0]-P[0],Q[1]-P[1])

while True:

	SCREEN.fill((0,0,0))

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	x, y = pygame.mouse.get_pos()
	POINT = [-1 for _ in range(SPAN)]
	t = [INTENSITY for _ in range(SPAN)]

	for i in range(len(WALLS)):
		Q = WALLS[i][0]
		SUB = sub(Q,(x,y))
		S = sub(WALLS[i][1],WALLS[i][0])

		for angle in range(SPAN):
			R = (cos(angle*pi/(180*DENSITY)),sin(angle*pi/(180*DENSITY)))
			POINT[angle] = (x + t[angle]*R[0],y + t[angle]*R[1])
			CROSS = cross(R,S)

			if CROSS:
				temp = cross(SUB,S)/CROSS

				if temp >= 0:
					NUM2 = cross(SUB,R)
					u = NUM2/CROSS

					if u <= 1 and u >= 0:
						t[angle] = min(t[angle],temp)
						POINT[angle] = (x + t[angle]*R[0],y + t[angle]*R[1])

	for angle in range(SPAN):
		pygame.draw.aaline(SCREEN,(255,255,255),(x,y),POINT[angle])

	for wall in WALLS:
		pygame.draw.aaline(SCREEN,(255,255,255),wall[0],wall[1])

	pygame.display.update()