## Book: Computational Physics by Nicholas J. Giordano, Dean and Professor of Physics, Auburn University
## Reference Book: Matlab Version by Kevin Berwick, School of Electrical and Electronic Engineering, Dublin Institute of Technology
## Translated to R by Indranil Ghosh, Physics Department, Jadavpur University

## Chaos in the driven Non-linear pendulum

from sympy import sqrt, sin
import pylab
def chaos_pendulum(theta_, omega_, t_, length, dt, q, drive_force, drive_freq):
    i=0
    g=9.8
    pi=3.141
    period = 2*3.14*sqrt(length/g)
    theta=[theta_]
    omega=[omega_]
    time=[t_]
    while True:
        i+=1
        time+=[time[i - 1]+ dt, ]
        omega+=[omega[i - 1] - (g/length)*sin(theta[i - 1])*dt - q*omega[i - 1]*dt + drive_force*sin(drive_freq*time[i - 1])*dt, ]
        theta+=[theta[i - 1] + omega[i]*dt, ]
        if theta[i]>pi: theta[i]=theta[i] - 2*pi
        if theta[i]<-pi: theta[i]=theta[i] + 2*pi
        if time[i]>=10*period: break        
    return (time, theta)

####
def chaos_pendulum_2(theta_, omega_, t_, length, dt, q, drive_force, drive_freq):
    i=0
    g=9.8
    pi=3.141
    period = 2*3.14*sqrt(length/g)
    theta=[theta_]
    omega=[omega_]
    time=[t_]
    while True:
        i+=1
        time+=[time[i - 1]+ dt, ]
        omega+=[omega[i - 1] - (g/length)*sin(theta[i - 1])*dt - q*omega[i - 1]*dt + drive_force*sin(drive_freq*time[i - 1])*dt, ]
        theta+=[theta[i - 1] + omega[i]*dt, ]
        if theta[i]>pi: theta[i]=theta[i] - 2*pi
        if theta[i]<-pi: theta[i]=theta[i] + 2*pi
        if time[i]>=10*period: break
    return (time, omega)
####
def chaos_pendulum_plot():
    f1=chaos_pendulum(0.2, 0, 0.0, 9.8, 0.04, 0.5, 0.0, 2/3.)
    pylab.plot(f1[0], f1[1])
    f2=chaos_pendulum(0.2, 0, 0.0, 9.8, 0.04, 0.5, 0.5, 2/3.)
    pylab.plot(f2[0], f2[1])
    f3=chaos_pendulum(0.2, 0, 0.0, 9.8, 0.04, 0.5, 1.2, 2/3.)
    pylab.plot(f3[0], f3[1])
    pylab.xlabel('time(s) --->')
    pylab.ylabel('radians(theta)--->')
    pylab.show()


####    
def chaos_pendulum_plot_2():
    f1=chaos_pendulum_2(0.2, 0, 0.0, 9.8, 0.04, 0.5, 0, 2/3.)
    pylab.plot(f1[0], f1[1])
    f2=chaos_pendulum_2(0.2, 0, 0.0, 9.8, 0.04, 0.5, 0.5, 2/3.)
    pylab.plot(f2[0], f2[1])
    f3=chaos_pendulum_2(0.2, 0, 0.0, 9.8, 0.04, 0.5, 1.2, 2/3.)
    pylab.plot(f3[0], f3[1])
    pylab.xlabel('time(s) --->')
    pylab.ylabel('omega--->')
    pylab.show()
    
##chaos_pendulum_plot()
##chaos_pendulum_plot_2()

def chaos_pendulum_3(theta_, omega_, t_, length, dt, q, drive_force, drive_freq):
    i=0
    g=9.8
    pi=3.141
    period = 2*3.14*sqrt(length/g)
    theta=[theta_]
    omega=[omega_]
    time=[t_]
    while True:
        i+=1
        time+=[time[i - 1]+ dt, ]
        omega+=[omega[i - 1] - (g/length)*sin(theta[i - 1])*dt - q*omega[i - 1]*dt + drive_force*sin(drive_freq*time[i - 1])*dt, ]
        theta+=[theta[i - 1] + omega[i]*dt, ]
        if theta[i]>pi: theta[i]=theta[i] - 2*pi
        if theta[i]<-pi: theta[i]=theta[i] + 2*pi
        if time[i]>=10*period: break
    pylab.plot(theta, omega, 'o', ms=1)
    pylab.xlabel("$\\theta$ -->")
    pylab.ylabel("$\omega$ -->")
    pylab.show()
##chaos_pendulum_3(0.2, 0, 0.0, 9.8, 0.04, 0.5, 1.2, 2/3.)

def chaos_pendulum_4():
    length=9.8
    g=9.8
    q=0.5
    f_drive=1.2
    pi=3.141
    omega_d=2/3.
    npoints=15*10**3
    dt=0.04
    omega=[0]*npoints
    theta=[0]*npoints
    time=[0]*npoints
    theta[0]=0.2
    omega[0]=0
    for i in range(1, npoints):
        omega[i]=omega[i-1]+(-(g/length)*sin(theta[i-1])-q*omega[i-1]+f_drive*sin(omega_d*time[i-1]))*dt
        temp=theta[i-1]+omega[i]*dt
        if temp<-pi:
            temp+=2*pi
        elif temp>pi:
            temp-=2*pi

        theta[i]=temp
        time[i]=time[i-1]+dt
    pylab.plot(theta, omega, '-')
    pylab.xlabel("$\\theta$ -->")
    pylab.ylabel("$\omega$ -->")
    pylab.show()
chaos_pendulum_4()


def chaos_pendulum_5(theta1_, theta2_, omega_, t_, length, dt, q, drive_force, drive_freq):
    i=0
    g=9.8
    pi=3.141
    period = 2*pi*sqrt(length/g)
    theta1=[theta1_]
    theta2=[theta2_]
    theta=[abs(theta1_ - theta2_)]
    omega1=[omega_]
    omega2=[omega_]
    time=[t_]
    while True:
        i+=1
        time+=[time[i - 1]+ dt, ]
        omega1+=[omega1[i - 1] - (g/length)*sin(theta1[i - 1])*dt - q*omega1[i - 1]*dt + drive_force*sin(drive_freq*time[i - 1])*dt, ]
        theta1+=[theta1[i - 1] + omega1[i]*dt, ]
        omega2+=[omega2[i - 1] - (g/length)*sin(theta2[i - 1])*dt - q*omega2[i - 1]*dt + drive_force*sin(drive_freq*time[i - 1])*dt, ]
        theta2+=[theta2[i - 1] + omega2[i]*dt, ]
        theta+=[abs(theta1[i - 1] - theta2[i - 1]), ]
        if theta[i]>pi: theta[i]=theta[i] - 2*pi
        if theta[i]<-pi: theta[i]=theta[i] + 2*pi
        if time[i]>=10*period: break        
    pylab.plot(time, theta)
    pylab.yscale('log')
    pylab.show()

