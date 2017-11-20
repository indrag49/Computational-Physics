## Book: Computational Physics by Nicholas J. Giordano, Dean and Professor of Physics, Auburn University
## Reference Book: Matlab Version by Kevin Berwick, School of Electrical and Electronic Engineering, Dublin Institute of Technology
## Translated to R by Indranil Ghosh, Physics Department, Jadavpur University

## Solution of Laplace's equation for a finite sized capacitor
## We need to download and activate the plot3D package

require(plot3D)
V <- array(c(numeric(120), c(0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0), numeric(100), c(0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0), numeric(140)), dim=c(20, 20))

capacitor_update <- function(V) {
  row_size <- nrow(V)
  column_size <- ncol(V)
  V_new <- array(numeric(400), dim=c(20, 20))
  delta_V_new <- 0
  for (j in 3:column_size) {
    for (i in 3: row_size) {
      if (V[i - 1, j - 1]!=1 && V[i - 1, j - 1]!=-1) {
        V_new[i- 1, j - 1] <- (V[i - 2, j - 1] + V[i, j - 1] + V[i - 1, j - 2] + V[i - 1, j])/4
        delta_V_new <- delta_V_new + abs(V_new[i - 1, j - 1] - V[i - 1, j - 1])
      }
      else V_new[i - 1, j - 1] <- V[i - 1, j - 1]
    }
  }
  return(list(V_new, delta_V_new))
}

 L<-capacitor_update(V)
 V_new <- L[[1]]
 delta_V_new <- L[[2]]
 par(mfrow=c(1, 3))
 loops <- 1
 while (delta_V_new>(400*10^-5) || loops<20) {
   loops <- loops+1
   L<-capacitor_update(V_new)
   V_new <- L[[1]]
   print(V_new)
   delta_V_new <- L[[2]]
   persp(z=V_new, theta=120, main="Pitential surface")
   persp3D(z=V_new, theta=120, main="potential Surface")
   image2D(V_new, main="contour plots", theta=180)
   Sys.sleep(0.09)
 }