import numpy as np
from vpython import *

# program is simulating the restoring force putted in the system of balls and springs

scene = canvas (width = 800, height = 650)

# walls :
wallR = box (pos = vector (5,0,0),  size = vector (0.1,5,5), color = color.blue)
wallL = box (pos = vector (-5,0,0), size = vector (0.1,5,5), color = color.blue)

# program is finding random number
N = np.random.randint (3, 50)
a = (wallR.pos.x - wallL.pos.x) / (N + 1)
L = []
S = []

# creation of list of N balls
for i in range (0, N):
    L.append (sphere (pos = vector (wallL.pos.x + (i + 1) * a,0,0), vel = vector (0, 0, 0), radius = 2/N, color = color.red))

# initial velocity putted in the system
L[0].pos.y     = 0.5
L[0].vel       = vector (0, 0.2, 0)
L[N - 1].pos.y = -0.5
L[N - 1].vel   = vector (0, 0.2, 0)

# creation of list of N springs
S.append (helix (pos = wallL.pos, axis = L[0].pos - wallL.pos, radius = 1/N, coils = 10, thickness = 0.5/N, color = color.green))

for i in range (1, N):
    S.append (helix (pos = L[i - 1].pos, axis = L[i].pos - L[i - 1].pos, radius = 1/N, coils = 10, thickness = 0.5/N, color = color.green))
    
S.append (helix (pos = L[N - 1].pos, axis = wallR.pos - L[N - 1].pos, radius = 1/N, coils = 10, thickness = 0.5/N, color = color.green))
# Fi = k * (ri-1 + ri+1 - 2 * ri)
# vi = vi + (Fi * dt)/ m
# ri = ri + vi * dt

sleep (0.5)

# necessery values
k  = 2
m  = 1.5
dt = 0
F = [vector (0, 0, 0) for i in enumerate (L)]
F[0]     = k * (wallL.pos + L[1].pos - 2 * L[0].pos)
F[N - 1] = k * (L[N - 2].pos + wallR.pos - 2 * L[N - 1].pos)


# iterations needed in making simulation- necessery to make move steps
while True:
    rate (200)
    
    for i in range (0, N):
        if i == 0:
            F[i] = k * (wallL.pos + L[i + 1].pos - 2 * L[i].pos)
            continue
        if i == N - 1:
            F[i] = k * (L[i - 1].pos + wallR.pos - 2 * L[i].pos)
            continue
        
        F[i] = k * (L[i - 1].pos + L[i + 1].pos - 2 * L[i].pos)
    
    for i in range (0, N):
        if i == 0:
            L[i].vel  += (F[i] / m) * 0.01
            L[i].pos  += L[i].vel * 0.01
            continue
        if i == N - 1:
            L[i].vel   += (F[i] / m) * 0.01
            L[i].pos   += L[i].vel * 0.01
            continue
        
        L[i].vel  += (F[i] / m) * 0.01
        L[i].pos  += L[i].vel * 0.01
    
    for i in range (0, N + 1):
        if i == 0:
            S[i].axis = L[i].pos - wallL.pos
            continue
        if i == N:
            S[i].pos  = L[i - 1].pos
            S[i].axis = wallR.pos - L[i - 1].pos
            continue
            
        S[i].pos  = L[i - 1].pos
        S[i].axis = L[i].pos - L[i - 1].pos
    
    dt += 0.01 