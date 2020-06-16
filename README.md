# PyCast - A Pseudo 3D Ray-casting "Engine"
This is a demo program which :    
• Demonstrates a basic understanding of 2D Geometry and Triginometric functions    
• Demonstrates usage of detecting inputs and real time screen rendering    
• Showcases the ability to translate a 2D space into a 3D space    
• As well as advanced 2D array utilization    

While not yet completed, plans for the "Engine" are :    
• Custom map support and colorization    
• Customizable image size and detail level    

How it works :    
• An array is created specifying the map layout    
• A player has a position on the grid, with values from 0 to 1 in the X and Y directions specifying their detailed position    
• Rays are cast out from the players position and are changed based on rotation    
• The nearest point in the array with a "block" is found and the distance is calculated    
• The distance is used to calculate the height of a line and it's color, creating a 3D environment    
• These are then put in front of an image with a different colored top and bottom half, creating a ceiling and floor    
• Buttons are then used, most likely arrow keys, to move the players position/angle which then requires a recasting of the rays    
    
Basic render method taken from here : https://www.youtube.com/watch?v=gYRrGTC7GtA - No actual code taken or copied from the video, nor has any segments with code visible been watched, just the first part of the video where the rendering method is explained.
