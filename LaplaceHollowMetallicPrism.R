## Book: Computational Physics by Nicholas J. Giordano, Dean and Professor of Physics, Auburn University
## Reference Book: Matlab Version by Kevin Berwick, School of Electrical and Electronic Engineering, Dublin Institute of Technology
## Translated to R by Indranil Ghosh, Physics Department, Jadavpur University

## Solution of Laplace's equation for a hollow metallic prism with a solid, metallic inner conductor
## We need to download and activate the plot3D package

require(plot3D)
V <- array(c(numeric(140),rep(c(0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0), times=7), numeric(140)), dim=c(20, 20))
Update_prism <- function(V) {
  row_size <- nrow(V)
  column_size <- ncol(V)
  V_new <- V
  delta_V_new <- 0
  for (j in 3:column_size) {
    for (i in 3:row_size) {
      if (V[i - 1, j - 1]!=1) {
        V_new[i - 1, j - 1] <- (V[i - 2, j - 1] + V[i, j - 1] + V[i - 1, j - 2] + V[i - 1, j])/4
        delta_V_new <- delta_V_new + abs(V_new[i - 1, j - 1] - V[i - 1, j - 1])
      }
      else V_new[i - 1, j - 1] <- V[i - 1, j - 1]
    }
  }
  return(list(V_new, delta_V_new))
}

L <- Update_prism(V)
V_new <- L[[1]]
delta_V_new <- L[[2]]
loops <- 0

while (delta_V_new > 4*10^-5 || loops<20) {
  loops <- loops+1
  L <- Update_prism(V_new)
  V_new <- L[[1]]
  delta_V_new <- L[[2]] 
  print(V_new)
  persp3D(z=V_new, theta=45, main="Potential surface")
  Sys.sleep(0.09)
}