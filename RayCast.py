import tkinter

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
R08 = [1,0,1,0,1,0,1,1,0,0,0,1,1]             #██  ██  ██  ████      ████
R09 = [1,0,0,0,0,0,1,0,0,1,0,0,1]             #██          ██    ██    ██
R10 = [1,1,0,1,0,0,0,0,1,1,1,0,1]             #████  ██        ██████  ██
R11 = [1,0,0,0,0,0,1,0,0,1,0,0,1]             #██          ██    ██    ██
R12 = [1,0,1,0,1,0,1,1,0,0,0,1,1]             #██  ██  ██  ████      ████
R13 = [1,1,1,1,1,1,1,1,1,1,1,1,1]             #██████████████████████████
#Individual map rows for easy modification     ^ Above is a better view ^
CeilingColor = "#0000FF"
FloorColor = "#FF0000"
#The above two are in Hexadecimal [ie #7F289A] or a supported color name
#Supported color list : http://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm
PlayerSpeed = .25 #In terms of map units
TurnSpeed = 1 #In terms of degrees
WindowLength = 500 #In pixels
WindowHeight = 500 #In pixels

#################################
#### Start main Raycast code ####
#################################

Map = [R01,R02,R03,R04,R05,R06,R07,R08,R09,R10,R11,R12,R13]
