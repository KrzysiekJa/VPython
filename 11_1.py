import numpy as np
from vpython import *
import time


scene = canvas (width = 800, height = 650)


fi     = np.pi
theta  = np.pi - 0.1
L      = 2
x1     = L  * np.sin (fi)
y1     = -L * np.cos (fi)
x2     = L  * (np.sin (fi) + np.sin (theta))
y2     = -L * (np.cos (fi) + np.cos (theta))


ball1  = sphere   (pos = vector (x1,y1,0), radius = 0.1, color = color.blue,  vel = vector (0, 0, 0), make_trail = True)
ball2  = sphere   (pos = vector (x2,y2,0), radius = 0.1, color = color.green, vel = vector (0, 0, 0), make_trail = True)
cy1    = cylinder (pos = vector (0,0,0), axis = ball1.pos,        length = L, radius = 0.02, color = color.red)
cy2    = cylinder (pos = ball1.pos, axis = ball2.pos - ball1.pos, length = L, radius = 0.02, color = color.red)


t      = 0
dt     = 0.001
fiV    = 0
thetaV = 0
g      = 9.8
g1     = 9.80000001
d      = 0.000000009
de     = 1

m        = (1 + np.power (np.sin(fi -theta), 2))
fi_a     = (-(g/L)  * (2 * np.sin(fi) - np.sin (theta) * np.cos (fi - theta))     - 0.5 * np.power (fiV, 2) * np.sin (2 * fi - 2 * theta)    - np.power (thetaV, 2) * np.sin (fi - theta)) /m
theta_a  = (-(g1/L) * (2 * np.sin(theta) - 2 * np.sin (fi) * np.cos (fi - theta)) + 0.5 * np.power (thetaV, 2) * np.sin (2 * fi - 2 * theta) + 2 * np.power (fiV, 2) * np.sin (fi - theta))/m
PERIOD   = 60

for i in range (0, 5):
    start = time.time()
    while True:
        rate (600)
        fiV    = fiV    + fi_a * dt
        thetaV = thetaV + theta_a * dt
        fi     = fi     + fiV * dt
        theta  = theta  + thetaV * dt
        
        ball1.pos.x = L  * np.sin (fi)
        ball1.pos.y = -L * np.cos (fi)
        ball2.pos.x = L  * (np.sin (fi) + np.sin (theta))
        ball2.pos.y = -L * (np.cos (fi) + np.cos (theta))
        cy1.axis    = ball1.pos
        cy2.pos     = ball1.pos
        cy2.axis    = ball2.pos - ball1.pos
        
        m        = (1 + np.power (np.sin(fi -theta), 2))
        fi_a     = (-(g/L)  * (2 * np.sin(fi) - np.sin (theta) * np.cos (fi - theta))     - 0.5 * np.power (fiV, 2) * np.sin (2 * fi - 2 * theta)    - np.power (thetaV, 2) * np.sin (fi - theta)) /m
        theta_a  = (-(g1/L) * (2 * np.sin(theta) - 2 * np.sin (fi) * np.cos (fi - theta)) + 0.5 * np.power (thetaV, 2) * np.sin (2 * fi - 2 * theta) + 2 * np.power (fiV, 2) * np.sin (fi - theta))/m
        
        if (time.time() > start + PERIOD and i < 4):
            break
        t = t + dt
        
    g1      = g1 - (d * de)
    de      = de / 10
    t       = 0
    fi      = np.pi
    theta   = np.pi - 0.1
    ball1.pos.x = L  * np.sin (fi)
    ball1.pos.y = -L * np.cos (fi)
    ball2.pos.x = L  * (np.sin (fi) + np.sin (theta))
    ball2.pos.y = -L * (np.cos (fi) + np.cos (theta))
    ball1.color = ball1.color + vector (0.1,-0.2,0.2)
    ball2.color = ball2.color + vector (0.1,0.2,-0.2)
    cy1.axis    = ball1.pos
    cy2.pos     = ball1.pos
    cy2.axis    = ball2.pos - ball1.pos
    fiV     = 0
    thetaV  = 0
    fi_a    = (-(g/L)  * (2 * np.sin(fi) - np.sin (theta) * np.cos (fi - theta))     - 0.5 * np.power (fiV, 2) * np.sin (2 * fi - 2 * theta)    - np.power (thetaV, 2) * np.sin (fi - theta)) /m
    theta_a = (-(g1/L) * (2 * np.sin(theta) - 2 * np.sin (fi) * np.cos (fi - theta)) + 0.5 * np.power (thetaV, 2) * np.sin (2 * fi - 2 * theta) + 2 * np.power (fiV, 2) * np.sin (fi - theta))/m 