## Book: Computational Physics by Nicholas J. Giordano, Dean and Professor of Physics, Auburn University
## Reference Book: Matlab Version by Kevin Berwick, School of Electrical and Electronic Engineering, Dublin Institute of Technology
## Translated to R by Indranil Ghosh, Physics Department, Jadavpur University

## Waves on a string
 
propagate <- function(y_current, y_previous) {
  r <- 1
  M <- length(y_current)
  y_next <- numeric()
  for(i in 2:M-1) y_next <- c(y_next, 2*(1-r^2)*y_current[i]-y_previous[i]+r^2*(y_current[i+1]+y_current[i-1]))
  y_next <- c(0, y_next)
  y_next <- c(y_next, 0)
  return(y_next)
}

string_dimension <- 100
x <- seq(1/string_dimension, 1, 1/string_dimension)
x_scale <- 1:string_dimension
y_next <- numeric(string_dimension)
k <- 1000
x_0 <- 0.3
ini_pos <- exp(-k*(x-x_0)^2)
y_current <- ini_pos
y_prev <- ini_pos
for (time_step in 1:500) {
  y_next <- propagate(y_current, y_prev)
  y_prev <- y_current
  y_current <- y_next
  plot(x_scale/string_dimension, y_current, type="l", col="green", main="Waves on a string: fixed ends", xlab="distance", ylab="displacement", xlim=c(0, 1), ylim=c(-1, 1))
  Sys.sleep(0.09)
}