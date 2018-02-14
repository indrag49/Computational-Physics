## Book: Computational Physics by Nicholas J. Giordano, Dean and Professor of Physics, Auburn University
## Reference Book: Matlab Version by Kevin Berwick, School of Electrical and Electronic Engineering, Dublin Institute of Technology
## Translated to Python by Indranil Ghosh, Physics Department, Jadavpur University

from mpmath  import *
import random, pygame, sys
from pygame.locals import *
mp.dps=1000
Pi=mpf(pi)
##set up the window
DISPLAYSURF=pygame.display.set_mode((800, 800), RESIZABLE)
pygame.display.set_caption("Three body problem")

##set up the colors
WHITE=(255, 255, 255)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
DISPLAYSURF.fill(WHITE)

#set up the initial points 
dt=0.0001
i=1
x_earth=[1]
y_earth=[0]
vx_earth=[0]
vy_earth=[2*Pi]
x_jupiter=[5.2]
y_jupiter=[0]
vx_jupiter=[0]
vy_jupiter=[2.7549]
me=6*10**24
##mj=1.9*10**10 # use 10**30 to get a chaotic effect
mj=1.9*10**30
ms=2*10**30
dt=0.0001
re=[]
r_j=[]
r_ej=[]


##run the loop
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.image.save(DISPLAYSURF, 'ThreeBody.png')
            pygame.quit()
            sys.exit()

    re+=[sqrt(x_earth[i - 1]**2 + y_earth[i - 1]**2), ]
    r_j+=[sqrt(x_jupiter[i - 1]**2 + y_jupiter[i - 1]**2), ]
    r_ej+=[sqrt((x_earth[i - 1] - x_jupiter[i - 1])**2 + (y_earth[i - 1] - y_jupiter[i - 1])**2), ]
    vx_earth+=[vx_earth[i - 1] - 4*Pi**2*x_earth[i - 1]*dt/(re[i - 1]**3) - 4*Pi**2*(mj/ms)*(x_earth[i - 1] - x_jupiter[i - 1])*dt/r_ej[i - 1]**3, ]
    vy_earth+=[vy_earth[i - 1] - 4*Pi**2*y_earth[i - 1]*dt/(re[i - 1]**3) - 4*Pi**2*(mj/ms)*(y_earth[i - 1] - y_jupiter[i - 1])*dt/r_ej[i - 1]**3, ]
    vx_jupiter+=[vx_jupiter[i - 1] - 4*Pi**2*x_jupiter[i - 1]*dt/r_j[i - 1]**3 - 4*Pi**2*(mj/ms)*(x_jupiter[i - 1] - x_earth[i - 1])*dt/r_ej[i - 1]**3, ]
    vy_jupiter+=[vy_jupiter[i - 1] - 4*Pi**2*y_jupiter[i - 1]*dt/r_j[i - 1]**3 - 4*Pi**2*(mj/ms)*(y_jupiter[i - 1] - y_earth[i - 1])*dt/r_ej[i - 1]**3, ]
    x_earth+=[x_earth[i - 1] + vx_earth[i]*dt, ]
    y_earth+=[y_earth[i - 1] + vy_earth[i]*dt, ]
    x_jupiter+=[x_jupiter[i - 1] + vx_jupiter[i]*dt, ]
    y_jupiter+=[y_jupiter[i - 1] + vy_jupiter[i]*dt, ]

    pygame.draw.line(DISPLAYSURF, GREEN,  (int(400 + x_earth[i - 1]*40), 400 - int(y_earth[i - 1]*40)), (int(400 + x_earth[i]*40), 400 - int(y_earth[i]*40)), 1) # Plotting the points after required transformations
    pygame.draw.line(DISPLAYSURF, RED,  (int(400 + x_jupiter[i - 1]*40), 400 - int(y_jupiter[i - 1]*40)), (int(400 + x_jupiter[i]*40), 400 - int(y_jupiter[i]*40)), 1) # Plotting the points after required transformations

    i+=1    
    pygame.display.update()