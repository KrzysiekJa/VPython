from vpython import *

# simulation of solar system
# with better optimalization : make_trail

S_m = 2 * 10**30    # mass of San
G   = 6.7 * 10**-11 # gravitational constant

scene = canvas ( width = 900, height = 700)

Sun     = sphere (pos = vector (0, 0, 0), radius = 10**10, color = color.yellow, emissive = True)
Mercure = sphere (pos = vector (70 * 10**9, 0, 0),  vel = vector (0, 47 * 10**3, 0), radius = 20 * 10**8, color = color.cyan, texture = textures.stucco, make_trail = True)
Venus   = sphere (pos = vector (110 * 10**9, 0, 0), vel = vector (0, 35 * 10**3, 0), radius = 20 * 10**8, color = color.white,texture = textures.stucco, make_trail = True)
Earth   = sphere (pos = vector (150 * 10**9, 0, 0), vel = vector (0, 30 * 10**3, 0), radius = 20 * 10**8, color = color.blue, make_trail = True)
Mars    = sphere (pos = vector (250 * 10**9, 0, 0), vel = vector (0, 24 * 10**3, 0), radius = 20 * 10**8, color = color.red,  texture = textures.stucco, make_trail = True)
L = [ Mercure, Venus, Earth, Mars]


dt = 1440 # one hour
sleep(0.2)

# looping for making move in animation
while True:
    rate (600)
    for i in L:
        a     = (-G * S_m * i.pos) / mag(i.pos) ** 3 # acceleration
        i.vel = i.vel + a * dt
        i.pos = i.pos + i.vel * dt