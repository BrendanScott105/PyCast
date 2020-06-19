import pygame
import keyboard
import time
from math import *

########################
#### Start settings ####
########################

R01 = [1,1,1,1,1,1,1,1,1,1,1,1,1]             #██████████████████████████
R02 = [1,0,0,0,1,0,1,0,0,0,0,0,1]             #██      ██  ██          ██
R03 = [1,0,1,0,1,0,1,0,0,0,0,0,1]             #██  ██  ██  ██          ██
R04 = [1,1,1,0,1,0,0,0,0,0,0,0,1]             #██████  ██        []    ██
R05 = [1,0,1,0,1,0,1,0,0,0,0,0,1]             #██  ██  ██  ██          ██
R06 = [1,0,0,0,0,0,1,0,0,0,0,0,1]             #██          ██          ██
R07 = [1,0,1,1,1,1,1,1,1,0,1,1,1]             #██  ██████████████  ██████
R08 = [1,0,1,0,1,0,1,0,0,0,0,0,1]             #██  ██  ██  ██          ██
R09 = [1,0,0,0,0,0,0,0,1,1,1,0,1]             #██              ██████  ██
R10 = [1,0,1,0,1,0,1,0,1,0,0,0,1]             #██  ██  ██  ██  ██      ██
R11 = [1,0,0,0,0,0,0,0,1,1,1,0,1]             #██              ██████  ██
R12 = [1,0,1,0,1,0,1,0,0,0,0,1,1]             #██  ██  ██  ██          ██
R13 = [1,1,1,1,1,1,1,1,1,1,1,1,1]             #██████████████████████████
#Individual map rows for easy modification     ^ Above is a better view ^
CeilingColor = "#0000FF"
FloorColor = "#FF0000"
#The above two are in Hexadecimal [ie #7F289A] or a supported color name
#Supported color list : http://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm
PlayerSpeed = .25 #In terms of map units
TurnSpeed = 1 #In terms of degrees
WindowLength = 500 #In pixels [Also equal to number of rays cast]
WindowHeight = 500 #In pixels [Multiplicative value for the heights]
FOV = 75 #In terms of degrees

#############################################################
#### Start window creation, rotation and positional code ####
#############################################################

Rotation = 0
X,Y = 0,0
pygame.init()
pygame.display.set_caption("Python raycasting demo © Brendan Scott")
Canvas = pygame.display.set_mode((WindowLength, WindowHeight))
while (keyboard.is_pressed("escape") == False):
	try:
		if keyboard.is_pressed("up"):
			print("To be added")
		if keyboard.is_pressed("down"):
			print("To be added")
		if keyboard.is_pressed("left"):
			if Rotation <= 0 :
				Rotation = 360 - TurnSpeed
			else : Rotation = Rotation - TurnSpeed
			print(Rotation)
		if keyboard.is_pressed("right"):
			Rotation = (Rotation + TurnSpeed) % 360
			print(Rotation)
		time.sleep(.01)
	except:
		break
