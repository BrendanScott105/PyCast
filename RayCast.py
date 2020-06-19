import pygame
import keyboard
import time
from math import * #For Canvas, Keypresses, Speed, and various math functions

########################
#### Start settings ####
########################
Map = [
[1,1,1,1,1,1,1,1,1,1,1,1,1],             #██████████████████████████
[1,0,0,0,1,0,1,0,0,0,0,0,1],             #██      ██  ██          ██
[1,0,1,0,1,0,1,0,0,0,0,0,1],             #██  ██  ██  ██          ██
[1,1,1,0,1,0,0,0,0,S,0,0,1],             #██████  ██        []    ██
[1,0,1,0,1,0,1,0,0,0,0,0,1],             #██  ██  ██  ██          ██
[1,0,0,0,0,0,1,0,0,0,0,0,1],             #██          ██          ██
[1,0,1,1,1,1,1,1,1,0,1,1,1],             #██  ██████████████  ██████
[1,0,1,0,1,0,1,0,0,0,0,0,1],             #██  ██  ██  ██          ██
[1,0,0,0,0,0,0,0,1,1,1,0,1],             #██              ██████  ██
[1,0,1,0,1,0,1,0,1,0,0,0,1],             #██  ██  ██  ██  ██      ██
[1,0,0,0,0,0,0,0,1,1,1,0,1],             #██              ██████  ██
[1,0,1,0,1,0,1,0,0,0,0,1,1],             #██  ██  ██  ██          ██
[1,1,1,1,1,1,1,1,1,1,1,1,1]]             #██████████████████████████
#When changing the map, always enclose it, otherwise the program is likely to close/hang
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
X,Y = 0,0 #Initialize positional and rotational variables
pygame.init()
pygame.display.set_caption("Python raycasting demo © Brendan Scott")
Canvas = pygame.display.set_mode((WindowLength, WindowHeight)) #Create canvas
while (keyboard.is_pressed("escape") == False): #Halt program on pressing "Esc"
	try:
		if keyboard.is_pressed("up"): #Realistically this should give proper values
			DeltaY = sin(Rotation)*PlayerSpeed
			print(DeltaY)
			DeltaX = sqrt(abs(pow(PlayerSpeed,2)-pow(DeltaY,2)))
			print(DeltaX)
		if keyboard.is_pressed("left"): #Decrements rotation and loops back to 360
			if Rotation <= 0 :
				Rotation = 360 - TurnSpeed
			else : Rotation = Rotation - TurnSpeed
			print(Rotation)
		if keyboard.is_pressed("right"): #Increments rotation up to 360
			Rotation = (Rotation + TurnSpeed) % 360
			print(Rotation)
		time.sleep(.01)
	except:
		break
