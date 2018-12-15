from vpython import *
import numpy as np

# VPython symulation of box with moving ball

scene = canvas (width = 900, height = 800)

ball = sphere (pos = vector(0,0,0), radius = 1, color = color.white)

wallR = box (pos = vector (5,0,0),  size = vector (1,10,10), color = color.red)
wallL = box (pos = vector (-5,0,0), size = vector (1,10,10), color = color.blue)
ceil  = box (pos = vector (0,5,0),  size = vector (10,1,10), color = color.orange)
floor = box (pos = vector (0,-5,0), size = vector (10,1,10), color = color.green)
back  = box (pos = vector (0,0,-5), size = vector (10,10,1), color = color.cyan)

x = np.random.randint (50)
y = np.random.randint (50)
z = np.random.randint (50)

ball.vel = vector (x/10, y/10, z/10) # velocity of ball

t  = 0
dt = 0.01                            # to change velocity
v  = vector (0.9, 0, 0.9)

while 1:
    rate (400)
    ball.pos.x = ball.pos.x + ball.vel.x * dt
    ball.pos.y = ball.pos.y + ball.vel.y * dt
    ball.pos.z = ball.pos.z + ball.vel.z * dt
    """if (ball.pos.x >= wallR.pos.x - 1.5 and ball.pos.y >= ceil.pos.y - 1.5):
        ball.vel.x = -ball.vel.x
        ball.vel.y = -ball.vel.y
        ball.color = v
    if (ball.pos.x >= wallR.pos.x - 1.5 and ball.pos.y <= floor.pos.y + 1.5):
        ball.vel.x = -ball.vel.x
        ball.vel.y = -ball.vel.y
        ball.color = v
    if (ball.pos.x <= wallL.pos.x + 1.5 and ball.pos.y >= ceil.pos.y - 1.5):
        ball.vel.x = -ball.vel.x
        ball.vel.y = -ball.vel.y
        ball.color = v
    if (ball.pos.x <= wallL.pos.x + 1.5 and ball.pos.y <= floor.pos.y + 1.5):
        ball.vel.x = -ball.vel.x
        ball.vel.y = -ball.vel.y
        ball.color = v
    if (ball.pos.z <= back.pos.z + 1.5 and ball.pos.x >= wallR.pos.x - 1.5): 
        ball.vel.x = -ball.vel.x
        ball.vel.z = -ball.vel.z
        ball.color = v
    if (ball.pos.z <= back.pos.z + 1.5 and ball.pos.x <= wallL.pos.x + 1.5):
        ball.vel.x = -ball.vel.x
        ball.vel.z = -ball.vel.z
        ball.color = v
    if (ball.pos.z <= back.pos.z + 1.5 and ball.pos.y >= ceil.pos.y - 1.5):
        ball.vel.z = -ball.vel.z
        ball.vel.y = -ball.vel.y
        ball.color = v
    if (ball.pos.z <= back.pos.z + 1.5 and ball.pos.y <= floor.pos.y + 1.5):
        ball.vel.z = -ball.vel.z
        ball.vel.y = -ball.vel.y
        ball.color = v"""
    if ball.pos.x >= wallR.pos.x - 1.5:
        ball.vel.x = -ball.vel.x
        ball.color = wallR.color
    if ball.pos.x <= wallL.pos.x + 1.5:
        ball.vel.x = -ball.vel.x
        ball.color = wallL.color
    if ball.pos.y >= ceil.pos.y - 1.5:
        ball.vel.y = -ball.vel.y
        ball.color = ceil.color
    if ball.pos.y <= floor.pos.y + 1.5:
        ball.vel.y = -ball.vel.y
        ball.color = floor.color
    if ball.pos.z <= back.pos.z + 1.5:
        ball.vel.z = -ball.vel.z
        ball.color = back.color
    if ball.pos.z >= 4.0:
        ball.vel.z = -ball.vel.z
        ball.color = color.white
    if ( (ball.pos.x >= wallR.pos.x - 1.5 and ball.pos.y >= ceil.pos.y - 1.5) or\
        (ball.pos.x >= wallR.pos.x - 1.5 and ball.pos.y <= floor.pos.y + 1.5) or\
        (ball.pos.x <= wallL.pos.x + 1.5 and ball.pos.y >= ceil.pos.y - 1.5)  or\
        (ball.pos.x <= wallL.pos.x + 1.5 and ball.pos.y <= floor.pos.y + 1.5) or\
        (ball.pos.z <= back.pos.z + 1.5 and ball.pos.x >= wallR.pos.x - 1.5)  or\
        (ball.pos.z <= back.pos.z + 1.5 and ball.pos.x <= wallL.pos.x + 1.5)  or\
        (ball.pos.z <= back.pos.z + 1.5 and ball.pos.y >= ceil.pos.y - 1.5)   or\
        (ball.pos.z <= back.pos.z + 1.5 and ball.pos.y <= floor.pos.y + 1.5) ) :
        ball.color = v  # for pink color
    
    t = t + dt
