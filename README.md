# PyCast - A Pseudo 3D Ray-casting "Engine"

Map :    
![Map](https://i.imgur.com/wzdNiEX.png)    
Where [ ] is the initial location

Basic render method learned from here : https://www.youtube.com/watch?v=gYRrGTC7GtA

# What it does

1. Creates a 2D grid of the world layout
2. Defines player location and rotation and sets it accordingly
3. Uses location and rotation to cast out rays until a surface is hit
4. Draws lines of unspecified height based on the distance to each surface
5. When moving, nullifies movement values if entering a filled map unit
