from vpython import *

# simulation of solar system with Earth in the center of scren

S_m = 2 * 10**30
G   = 6.7 * 10**-11

scene = canvas (width = 900, height = 700, range = 3 * 10**11)

Sun     = sphere (pos = vector (0, 0, 0), radius = 10**10, color = color.yellow, emissive = True)
Mercure = sphere (pos = vector (70 * 10**9, 0, 0),  vel = vector (0, 47 * 10**3, 0), radius = 30 * 10**8, color = color.cyan)
Venus   = sphere (pos = vector (110 * 10**9, 0, 0), vel = vector (0, 35 * 10**3, 0), radius = 30 * 10**8, color = color.white)
Earth   = sphere (pos = vector (150 * 10**9, 0, 0), vel = vector (0, 30 * 10**3, 0), radius = 30 * 10**8, color = color.blue)
Mars    = sphere (pos = vector (250 * 10**9, 0, 0), vel = vector (0, 24 * 10**3, 0), radius = 30 * 10**8, color = color.red)
L = [ Mercure, Venus, Earth, Mars]

scene.center    = Earth.pos
scene. userzoom = False
dt = 1440

while True:
    rate (600)
    for i in L:
        a     = (-G * S_m * i.pos) / mag(i.pos) ** 3
        i.vel = i.vel + a * dt
        i.pos = i.pos + i.vel * dt
        if (i == Earth) :
            scene.center = Earth.pos