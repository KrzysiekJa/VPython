from vpython import *
import numpy as np

# VPython symulation of box with moving N balls

scene = canvas (width = 850, height = 750)

# box :
wallR = box (pos = vector (5,0,0),  size = vector (1,10,10), color = color.red)
wallL = box (pos = vector (-5,0,0), size = vector (1,10,10), color = color.blue)
ceil  = box (pos = vector (0,5,0),  size = vector (10,1,10), color = color.orange)
floor = box (pos = vector (0,-5,0), size = vector (10,1,10), color = color.green)
back  = box (pos = vector (0,0,-5), size = vector (10,10,1), color = color.cyan)

N = np.random.randint (2, 30)
L = []

for i in range (0, N):
    x = np.random.randint (50)
    y = np.random.randint (50)
    z = np.random.randint (50)
    L.append (sphere (pos = vector (2,3,-1.5), radius = 0.3, color = color.white, vel = vector (x/10, y/10, z/10)))

t  = 0
dt = 0.01

while t < 1000:
    rate (400)
    for ball in L:
        ball.pos.x = ball.pos.x + ball.vel.x * dt
        ball.pos.y = ball.pos.y + ball.vel.y * dt
        ball.pos.z = ball.pos.z + ball.vel.z * dt
    
        if ball.pos.x >= wallR.pos.x - 0.8:
            ball.vel.x = -ball.vel.x
            ball.color = wallR.color
        if ball.pos.x <= wallL.pos.x + 0.8:
            ball.vel.x = -ball.vel.x
            ball.color = wallL.color
        if ball.pos.y >= ceil.pos.y - 0.8:
            ball.vel.y = -ball.vel.y
            ball.color = ceil.color
        if ball.pos.y <= floor.pos.y + 0.8:
            ball.vel.y = -ball.vel.y
            ball.color = floor.color
        if ball.pos.z <= back.pos.z + 0.8:
            ball.vel.z = -ball.vel.z
            ball.color = back.color
        if ball.pos.z >= 4.7:
            ball.vel.z = -ball.vel.z
            ball.color = color.white
    
    t = t + dt
