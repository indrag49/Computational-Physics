## Book: Computational Physics by Nicholas J. Giordano, Dean and Professor of Physics, Auburn University
## Reference Book: Matlab Version by Kevin Berwick, School of Electrical and Electronic Engineering, Dublin Institute of Technology
## Translated to R by Indranil Ghosh, Physics Department, Jadavpur University

## Laplace's equation using Jacobi relaxation method

V <- array(c(-1, -1, -1, -1, -1, -1, -1, -0.67, 0, 0, 0, 0, 0, -0.67, -0.33, 0, 0, 0, 0, 0, -0.33, 0, 0, 0, 0, 0, 0, 0, 0.33, 0, 0, 0, 0, 0, 0.33, 0.67, 0, 0, 0, 0, 0, 0.67, 1, 1, 1, 1, 1, 1, 1), dim=c(7, 7))
V
loops <- 1

Update_V <- function(V) {
  row_size <- nrow(V)
  column_size <- ncol(V)
  V_new <- V
  delta_V_new <- 0
  for (j in 3:column_size) {
    for (i in 3:row_size){
      V_new[i - 1, j - 1] <- (V[i - 2, j - 1]+ V[i, j - 1] + V[i - 1, j - 2] + V[i-1, j])/4
      delta_V_new <- delta_V_new + abs(V_new[i - 1, j - 1] - V[i - 1, j - 1])
    }
  }
  return(list(V_new, delta_V_new))
}

L <- Update_V(V)
V_new <- L[[1]]
delta_V_new <- L[[2]]
V_new
delta_V_new
require(plot3D)
while (delta_V_new > (49*10^-5) && loops<10) {
  loops <- loops+1
  l <- Update_V(V_new)
  V_new <- l[[1]]
  delta_V_new <- l[[2]]
  print(V_new)
  persp(z=V_new, theta=60, main="Potential surface")
  Sys.sleep(0.09)
}