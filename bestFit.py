## Book: Computational Physics by Nicholas J. Giordano, Dean and Professor of Physics, Auburn University
## Reference Book: Matlab Version by Kevin Berwick, School of Electrical and Electronic Engineering, Dublin Institute of Technology
## Translated to Python by Indranil Ghosh, Physics Department, Jadavpur University

# Best fitting - linear model


def best_fit(X, Y):
        #X and Y are lists
        sum_x=0
        sum_y=0
        sum_xy=0
        sum_x2=0
        n=len(X)
        pylab.xlim(X[0] - 2, X[-1] + 2)
        pylab.ylim(Y[0] - 2, Y[-1] + 2)
        pylab.xlabel("X Axis ->")
        pylab.ylabel("Y Axis ->")
        for i in range(n):
                sum_x+=X[i]
                sum_y+=Y[i]
                sum_xy+=X[i]*Y[i]
                sum_x2+=X[i]**2
        slope=(n*sum_xy - sum_x*sum_y)/(n*sum_x2 - sum_x*sum_x)
        intercept=(sum_y*sum_x2 - sum_x*sum_xy)/(n*sum_x2 - sum_x*sum_x)
        pylab.plot(X, Y, 'ko')
        x=[X[0], X[-1]]
        y=[x[0]*slope + intercept, x[1]*slope + intercept]
        pylab.plot(x, y, 'k')
        pylab.show()

