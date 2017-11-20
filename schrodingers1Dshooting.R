## Book: Computational Physics by Nicholas J. Giordano, Dean and Professor of Physics, Auburn University
## Reference Book: Matlab Version by Kevin Berwick, School of Electrical and Electronic Engineering, Dublin Institute of Technology
## Translated to R by Indranil Ghosh, Physics Department, Jadavpur University

##Schrodinger's 1-D wave equation solution with shooting method

N <- 200
delta_x <- 0.01
E_initial <- 1.879
delta_E <- 0.1
x <- seq(delta_x, N*delta_x, delta_x)
length(x)

V <- numeric(N)
V[100:N] <- 1000
length(V)

b <- 1.5
last_diverge <- 0
minimum_delta_E <- 0.005
E <- E_initial

calc <- function(psi, N, delta_x, E, b, V){
  for (i in 3:N){
    psi[i] <- 2*psi[i-1]-psi[i-2]-2*(E - V[i-1])*delta_x^2*psi[i-1]
    if (abs(psi[i])>b) return(list(psi, i-1))
  }
}

while (abs(delta_E)>minimum_delta_E) {
  psi <- numeric(N)
  psi[1] <- 1
  psi[2] <- 1
  
  l <- calc(psi, N, delta_x, E, b, V)
  psi <- l[[1]]
  i <- l[[2]]
  plot(x, psi, type="l", col="blue", main="Square well")
  Sys.sleep(0.09)
  
  if (sign(psi[i]) != sign(last_diverge)) delta_E <- -delta_E/2
  E <- E+delta_E
  last_diverge <- sign(psi[i])
}