## Book: Computational Physics by Nicholas J. Giordano, Dean and Professor of Physics, Auburn University
## Reference Book: Matlab Version by Kevin Berwick, School of Electrical and Electronic Engineering, Dublin Institute of Technology
## Translated to Python by Indranil Ghosh, Physics Department, Jadavpur University

## Solution of Laplace's equation for a finite sized capacitor
## We need to download and activate the plot3D package

## Chaotic tumbling of Hyperion
from mpmath  import *
import random, pygame, sys
from pygame.locals import *
mp.dps=1000
Pi=mpf(pi)

##set up the window
DISPLAYSURF=pygame.display.set_mode((800, 800), RESIZABLE)
pygame.display.set_caption("Chaotic tumbling of Hyperion")

##set up the colors
WHITE=(255, 255, 255)
RED=(255, 0, 0)

DISPLAYSURF.fill(WHITE)

##set up the initial points 
X=[1]
Y=[0]
Vx=[0]
Vy=[2*Pi]
theta=[0]
omega=[0]
T=[0]
rc=[]
dt=0.0001
i=1

## run the loop
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
##            pygame.image.save(DISPLAYSURF, 'Hyperion.png')
            pygame.quit()
            sys.exit()
    
    rc+=[sqrt(X[i- 1]**2 + Y[i - 1]**2), ]
    Vx+=[Vx[i - 1] - (4*Pi**2*X[i - 1]*dt)/(rc[i - 1]**3), ]
    Vy+=[Vy[i - 1] - (4*Pi**2*Y[i - 1]*dt)/(rc[i - 1]**3), ]
    X+=[X[i - 1] + Vx[i]*dt, ]
    Y+=[Y[i - 1] + Vy[i]*dt, ]
    t1=12*Pi**2/rc[i - 1]**5
    t2=X[i - 1]*sin(theta[i - 1]) - Y[i - 1]*cos(theta[i - 1])
    t3=X[i - 1]*cos(theta[i - 1]) + Y[i - 1]*sin(theta[i - 1])
    omega+=[omega[i - 1] - t1*t2*t3*dt, ]
    temp=theta[i - 1] + omega[i]*dt
    if temp<-Pi:
        temp+=2*Pi
    elif temp>pi:
        temp-=2*Pi
    theta+=[temp, ]
    T+=[T[i - 1] + dt, ]

    pygame.draw.line(DISPLAYSURF, RED,  (int(T[i - 1]*90), 400 - int(theta[i - 1]*80)), (int(T[i]*90), 400 - int(theta[i]*80)), 1) # Plotting the points after required transformations
##    pygame.draw.line(DISPLAYSURF, RED,  (int(T[i - 1]*90), 600 - int(omega[i - 1]*40)), (int(T[i]*90), 600 - int(omega[i]*40)), 1) # Plotting the points after required transformations
##    pygame.draw.line(DISPLAYSURF, RED,  (int(T[i - 1]*45), 400 - int(theta[i - 1]*80)), (int(T[i]*45), 400 - int(theta[i]*80)), 1) # Plotting the points after required transformations
##    pygame.draw.line(DISPLAYSURF, RED,  (int(T[i - 1]*90), 600 - int(omega[i - 1]*10)), (int(T[i]*90), 600 - int(omega[i]*10)), 1) # Plotting the points after required transformations
    i+=1    
    pygame.display.update()