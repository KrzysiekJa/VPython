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


ball1  = sphere   (pos = vector (x1,y1,0), radius = 0.1, color = color.blue,  vel = vector (0, 0, 0))
ball2  = sphere   (pos = vector (x2,y2,0), radius = 0.1, color = color.green, vel = vector (0, 0, 0))
cy1    = cylinder (pos = vector (0,0,0), axis = ball1.pos,        length = L, radius = 0.02, color = color.red)
cy2    = cylinder (pos = ball1.pos, axis = ball2.pos - ball1.pos, length = L, radius = 0.02, color = color.red)
ball3  = sphere   (pos = vector (x1,y1,0), radius = 0.1, color = color.blue,  vel = vector (0, 0, 0))
ball4  = sphere   (pos = vector (x2,y2,0), radius = 0.1, color = color.green, vel = vector (0, 0, 0))
cy3    = cylinder (pos = vector (0,0,0), axis = ball3.pos,        length = L, radius = 0.02, color = color.white)
cy4    = cylinder (pos = ball3.pos, axis = ball4.pos - ball3.pos, length = L, radius = 0.02, color = color.white)


t      = 0
dt     = 0.001
fi1    = 0
thetaV = 0
fi2    = 0
theta2 = 0
g      = 9.8
g1     = 9.8
g2     = 9.800000000001

m        = (1 + np.power (np.sin(fi -theta), 2))
fi_a     = (-(g/L)  * (2 * np.sin(fi) - np.sin (theta) * np.cos (fi - theta))     - 0.5 * np.power (fi1, 2) * np.sin (2 * fi - 2 * theta)    - np.power (thetaV, 2) * np.sin (fi - theta)) /m
theta_a  = (-(g1/L) * (2 * np.sin(theta) - 2 * np.sin (fi) * np.cos (fi - theta)) + 0.5 * np.power (thetaV, 2) * np.sin (2 * fi - 2 * theta) + 2 * np.power (fi1, 2) * np.sin (fi - theta))/m
m        = (1 + np.power (np.sin(fi -theta), 2))
fi_a2     = fi_a
theta_a2  = theta_a

fii     = np.pi
thetaa  = np.pi - 0.1


while True:
    rate (2000)
    fi1    = fi1    + fi_a * dt
    thetaV = thetaV + theta_a * dt
    fi     = fi     + fi1 * dt
    theta  = theta  + thetaV * dt
    
    ball1.pos.x = L  * np.sin (fi)
    ball1.pos.y = -L * np.cos (fi)
    ball2.pos.x = L  * (np.sin (fi) + np.sin (theta))
    ball2.pos.y = -L * (np.cos (fi) + np.cos (theta))
    cy1.axis    = ball1.pos
    cy2.pos     = ball1.pos
    cy2.axis    = ball2.pos - ball1.pos
    
    m        = (1 + np.power (np.sin(fi -theta), 2))
    fi_a     = (-(g/L)  * (2 * np.sin(fi) - np.sin (theta) * np.cos (fi - theta))     - 0.5 * np.power (fi1, 2) * np.sin (2 * fi - 2 * theta)    - np.power (thetaV, 2) * np.sin (fi - theta)) /m
    theta_a  = (-(g1/L) * (2 * np.sin(theta) - 2 * np.sin (fi) * np.cos (fi - theta)) + 0.5 * np.power (thetaV, 2) * np.sin (2 * fi - 2 * theta) + 2 * np.power (fi1, 2) * np.sin (fi - theta))/m
    
    fi2    = fi2    + fi_a2 * dt
    theta2 = theta2 + theta_a2 * dt
    fii    = fii    + fi2 * dt
    thetaa = thetaa + theta2 * dt
    
    ball3.pos.x = L  * np.sin (fii)
    ball3.pos.y = -L * np.cos (fii)
    ball4.pos.x = L  * (np.sin (fii) + np.sin (thetaa))
    ball4.pos.y = -L * (np.cos (fii) + np.cos (thetaa))
    cy3.axis    = ball3.pos
    cy4.pos     = ball3.pos
    cy4.axis    = ball4.pos - ball3.pos
    
    m1       = (1 + np.power (np.sin(fii -thetaa), 2))
    fi_a2    = (-(g/L)  * (2 * np.sin(fii) - np.sin (thetaa) * np.cos (fii - thetaa))     - 0.5 * np.power (fi2, 2) * np.sin (2 * fii - 2 * thetaa)    - np.power (theta2, 2) * np.sin (fii - thetaa)) /m1
    theta_a2 = (-(g2/L) * (2 * np.sin(thetaa) - 2 * np.sin (fii) * np.cos (fii - thetaa)) + 0.5 * np.power (theta2, 2) * np.sin (2 * fii - 2 * thetaa) + 2 * np.power (fi2, 2) * np.sin (fii - thetaa))/m1
    
    t = t + dt