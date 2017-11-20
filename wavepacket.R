## Book: Computational Physics by Nicholas J. Giordano, Dean and Professor of Physics, Auburn University
## Reference Book: Matlab Version by Kevin Berwick, School of Electrical and Electronic Engineering, Dublin Institute of Technology
## Translated to R by Indranil Ghosh, Physics Department, Jadavpur University

##Schrodinger's 1-D wave equation solution with shooting method

x <- seq(0, 1, 0.0005)
x_0 <- 0.4
C <- 25
sigma_squared <- 10^(-3)
delta_x <- 0.0005
delta_t <- 0.2
k_0 <- 500
psi <- C*exp(-(x-x_0)^2/sigma_squared)*exp(1i*k_0*x)

par(mfrow=c(2, 2))
plot(x, Re(psi), type="l", main="Real part of wavefunction", xlab="distance")
plot(x, Im(psi), type="l", col="blue", main="Imaginary part of the wave function", xlab="distance")
plot(x, Conj(psi)*psi, type="l", col="green", main="Probability of finding particle", xlab="distance")