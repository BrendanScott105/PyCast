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
R08 = [1,0,1,0,1,0,1,0,0,0,0,1,1]             #██  ██  ██  ██        ████
R09 = [1,0,0,0,0,0,0,0,0,1,0,0,1]             #██                ██    ██
R10 = [1,1,0,1,0,1,0,0,1,0,0,0,1]             #████  ██  ██    ██      ██
R11 = [1,0,0,0,0,0,0,0,0,1,0,0,1]             #██                ██    ██
R12 = [1,0,1,0,1,0,1,0,0,0,0,1,1]             #██  ██  ██  ██        ████
R13 = [1,1,1,1,1,1,1,1,1,1,1,1,1]             #██████████████████████████
#Individual map rows for easy modification     ^ Above is a better view ^
CeilingColor = "#0000FF"
FloorColor = "#FF0000"
#The above two are in Hexadecimal [ie #7F289A] or a supported color name
#Supported color list : http://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm
PlayerSpeed = .25 #In terms of map units
TurnSpeed = 1/360 #In terms of fractions of a full circle [1/360 = 1 deg.]
WindowLength = 500 #In pixels [Also equal to number of rays cast]
WindowHeight = 500 #In pixels [Multiplicative value for the heights]
FOV = 1/2000 #Distance between rays in fractions of a circle, 1/[WindowLength*4] = 90 deg. 

###############################
#### Start window creation ####
###############################
