# RobotArm
A Robot Arm on SolidWork and Onshape programm, and A algorithm expline the Working Area, Dead Zone, and Area we dont need at work.

I drew a picture of the robot arm and manually marked the required areas. In the picture below on PNG.


I used precise Python code that describes the robot arm in detail.
The Robot Arm had four joints, all of which rotated. The base rotated 360 degrees, while the remaining three joints rotated 180 degrees. It had also 2 links of lengths 70 cm and 60 cm.

# CODE PYTHON EXPLINE 
Trigonometric equations are then used to calculate the location of the end effector in space for each set. The projection is first calculated in the X-Z plane, then rotated around the Z-axis at the angle of the first joint to simulate a full rotation of the arm. All these locations are collected and plotted as points in a 3D graph using the Matplotlib library, providing a clear visual representation of the arm's reach and indirectly indicating areas that are considered "dead" or unreachable.

*Experiment with all possible angles:*
- Try all possible angles for the first joint (0° to 360°)
- With each angle for the first joint, try each angle for the second joint (0° to 180°)
- With each combination of these, try each angle for the third joint (0° to 180°)

*Using the equations cos() and sin(), calculate:*
- Horizontal position
- Vertical position
- Then rotate the arm around the base (first joint)

Finally, each point the arm can reach is plotted as a three-dimensional point cloud, representing the arm's range of motion. 


