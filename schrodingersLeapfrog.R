## Book: Computational Physics by Nicholas J. Giordano, Dean and Professor of Physics, Auburn University
## Reference Book: Matlab Version by Kevin Berwick, School of Electrical and Electronic Engineering, Dublin Institute of Technology
## Translated to R by Indranil Ghosh, Physics Department, Jadavpur University

## Time dependent schrodinger's equation in 1-D: Leapfrog method

N <- 1000
x <- seq(0, 1, length.out=1000)
x_0 <- 0.4
C <- 10
sigma_squared <- 10^(-3)
k_0 <- 500

delta_x <- 10^(-3)
delta_t <- 5*10^(-8)

psi <- C*exp(-(x - x_0)^2/sigma_squared)*exp(1i*k_0*x)

R_initial <- Re(psi)
I_initial <- Im(psi)


V <- numeric(N)
V[600:N] <- -10^6
V

I_current <- I_initial
R_current <- R_initial

imag_psi <- function(N, I_current, R_current, delta_t, delta_x, V) {
  I_next <- numeric(N)
  s <- delta_t/(2*delta_x^2)
  for (x in 3:N) {
    I_next[x-1] <- I_current[x-1]+s*(R_current[x]-2*R_current[x-1]+R_current[x-2])-delta_t*V[x-1]*R_current[x-1]
    I_next[1] <- I_next[2]
    I_next[N] <- I_next[N-1]
  }
  return(I_next)
}  

real_psi <- function(N, R_current, I_current, delta_t, delta_x, V) {
  R_next <- numeric(N)
  s <- delta_t/(2*delta_x^2)
  for (x in 3:N) {
    R_next[x-1] <- R_current[x-1]-s*(I_current[x]-2*I_current[x-1]+I_current[x-2])+delta_t*V[x-1]*I_current[x-1]
    R_next[1] <- R_next[2]
    R_next[N] <- R_next[N-1]
  }
  return(R_next)
} 


I_next <- imag_psi(N, I_current, R_current, delta_t, delta_x, V)
for (time_step in 1:15000){
  R_next <- real_psi(N, R_current, I_current, delta_t, delta_x, V)
  R_current <- R_next
  I_next <- imag_psi(N, I_current, R_current, delta_t, delta_x, V)
  prob_density <- R_current^2+I_next*I_current
  I_current <- I_next
  if (time_step%%10==0){
    plot(x, prob_density, type="l", col="red", main="Reflection from cliff", xlim=c(0, 1), ylim=c(0, 200), ylab="Probability density")
    Sys.sleep(0.09)
  }
}