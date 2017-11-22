## Book: Computational Physics by Nicholas J. Giordano, Dean and Professor of Physics, Auburn University
## Reference Book: Matlab Version by Kevin Berwick, School of Electrical and Electronic Engineering, Dublin Institute of Technology
## Translated to Python by Indranil Ghosh, Physics Department, Jadavpur University

##Lorenz Attractor

import random, pygame, sys
from pygame.locals import *

##set up the window
DISPLAYSURF=pygame.display.set_mode((800, 800), RESIZABLE)
pygame.display.set_caption("Lorenz Attractor")

##set up the colors
WHITE=(255, 255, 255)
RED=(255, 0, 0)

X=[1]
Y=[0]
Z=[0]
t=[0.0]
sigma=10.
b=8/3.
dt=0.0001
r=25
##r=163.8
i=1

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.image.save(DISPLAYSURF, 'LorenzAttractor.png')
            pygame.quit()
            sys.exit()

    X+=[X[i - 1] + sigma*(Y[i - 1] - X[i - 1])*dt, ]
    Y+=[Y[i - 1] + (-X[i - 1]*Z[i - 1] + r*X[i - 1] - Y[i - 1])*dt, ]
    Z+=[Z[i - 1] + (X[i - 1]*Y[i - 1] - b*Z[i - 1])*dt, ]
    t+=[t[i - 1] + dt]

##    pygame.draw.line(DISPLAYSURF, RED, (int(t[i-1]*18), 550 - int(Z[i-1])), (int(t[i]*18), 550 - int(Z[i])), 1)
    pygame.draw.line(DISPLAYSURF, RED, (400 + int(X[i-1]*12), 550 - int(Z[i-1]*12)), (400 + int(X[i]*12), 550 - int(Z[i]*12)), 1)
    i+=1    
    pygame.display.update()