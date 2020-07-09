import numpy as np
from vpython import *

# VPython symulation of box with moving N balls that making collisions

def changeFunction (v1, v2, r1, r2, R1, R2, m1, m2) :
    a  = np.power (mag (v1 - v2), 2)
    if a != 0 :
        b  = -2 * dot (r1 - r2, v1 - v2)
        c  = np.power (mag (r1 - r2), 2) - np.power (R1 + R2, 2)
        delta = np.power (b, 2) - 4 * a * c
        if delta >= 0:
            ddt = (-b + sqrt (delta)) / (2 * a)
            r1  = r1 - v1 * ddt
            r2  = r2 - v2 * ddt
    
    rd = (r1 - r2) / mag (r1 - r2)
    v1 = v1 - 2 * (m2 / (m1 + m2)) * dot (v1 - v2, rd) * rd
    v2 = v2 + 2 * (m1 / (m1 + m2)) * dot (v1 - v2, rd) * rd
    
    r1 = r1 + v1 * ddt
    r2 = r2 + v2 * ddt
    return v1, v2, r1, r2
  
def checkFunction (r1, r2, R1, R2, wallR, wallL, ceil, floor) :
    if (r1.x >= wallR.pos.x - (R1 + 0.5)):
        r1.x = r1.x - (r1.x - wallR.pos.x)
        r2.x = r2.x - (r1.x - wallR.pos.x)
    if (r1.x <= wallL.pos.x + (R1 + 0.5)): 
        r1.x = r1.x + (wallL.pos.x - r1.x)
        r2.x = r2.x + (wallL.pos.x - r1.x)
    if (r1.y >= ceil.pos.y  - (R1 + 0.5)):
        r1.y = r1.y - (r1.y - wallR.pos.y)
        r2.y = r2.y - (r1.y - wallR.pos.y)
    if (r1.y <= floor.pos.y + (R1 + 0.5)):
        r1.y = r1.y + (wallL.pos.y - r1.y)
        r2.y = r2.y + (wallL.pos.y - r1.y)
    if (r2.x >= wallR.pos.x - (R2 + 0.5)):
        r1.x = r1.x - (r2.x - wallR.pos.x)
        r2.x = r2.x - (r2.x - wallR.pos.x)
    if (r2.x <= wallL.pos.x + (R2 + 0.5)): 
        r1.x = r1.x + (wallL.pos.x - r2.x)
        r2.x = r2.x + (wallL.pos.x - r2.x)
    if (r2.y >= ceil.pos.y  - (R2 + 0.5)):
        r1.y = r1.y - (r2.y - wallR.pos.y)
        r2.y = r2.y - (r2.y - wallR.pos.y)
    if (r2.y <= floor.pos.y + (R2 + 0.5)):
        r1.y = r1.y + (wallL.pos.y - r2.y)
        r2.y = r2.y + (wallL.pos.y - r2.y)
    
    return r1, r2


scene = canvas (width = 800, height = 650)

# box :
wallR = box (pos = vector (50,0,0),  size = vector (1,101,1), color = color.red)
wallL = box (pos = vector (-50,0,0), size = vector (1,101,1), color = color.red)
ceil  = box (pos = vector (0,50,0),  size = vector (101,1,1), color = color.red)
floor = box (pos = vector (0,-50,0), size = vector (101,1,1), color = color.red)


N = np.random.randint (7, 20)
x = -50
y = 42
listOfBalls = []

for i in range (0, N):
    x  = x + 8
    if (x >= 50):
        x = -42
        y  = y - 8
        if (y <= -50):
            y = 42
    vx = np.random.randint (10)
    vy = np.random.randint (10)
    r  = np.random.uniform (1,3)
    listOfBalls.append (sphere (pos = vector (x,y,0), radius = r, mass = np.power (r, 3), color = color.green, vel = vector (vx, vy, 0)))

r  = np.random.uniform (8,12)
listOfBalls.append (sphere (pos = vector (0,-33,0), radius = r, mass = np.power (r, 3), color = color.blue, vel = vector (0, 0, 0), make_trail = True))

t  = 0
dt = 0.01
sleep (0.3)

while True:
    rate (50)
    for ball in listOfBalls:
        ball.pos.x = ball.pos.x + ball.vel.x * dt
        ball.pos.y = ball.pos.y + ball.vel.y * dt
        
    for ball in listOfBalls:
        for i in range (listOfBalls.index (ball) + 1, N + 1):
            if (mag (ball.pos - listOfBalls[i].pos) < ball.radius + listOfBalls[i].radius):
                ball2 = listOfBalls[i]
                [ball.vel, ball2.vel, ball.pos, ball2.pos] = changeFunction (ball.vel, ball2.vel, ball.pos, ball2.pos, ball.radius, ball2.radius, ball.mass, ball2.mass)
                [ball.pos, ball2.pos]                      = checkFunction  (ball.pos, ball2.pos, ball.radius, ball2.radius, wallR, wallL, ceil, floor)
    
    for ball in listOfBalls:
        if ball.pos.x >= wallR.pos.x - (ball.radius + 0.6):
            ball.vel.x = -ball.vel.x
        if ball.pos.x <= wallL.pos.x + (ball.radius + 0.6): 
            ball.vel.x = -ball.vel.x
        if ball.pos.y >= ceil.pos.y  - (ball.radius + 0.6):
            ball.vel.y = -ball.vel.y
        if ball.pos.y <= floor.pos.y + (ball.radius + 0.6):
            ball.vel.y = -ball.vel.y
    
    t = t + dt