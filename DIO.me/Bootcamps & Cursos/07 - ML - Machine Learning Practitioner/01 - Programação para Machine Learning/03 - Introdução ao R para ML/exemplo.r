# library(caTools)        # external package providing write.gif function 

# jet.colors = colorRampPalette(c("#00007F", "blue", "#007FFF", "cyan", "#7FFF7F", "yellow", "#FF7F00", "red", "#7F0000"))
# m = 1200                # define size
# C = complex( real=rep(seq(-1.8,0.6, length.out=m), each=m ),
#               imag=rep(seq(-1.2,1.2, length.out=m), m ) )
# C = matrix(C,m,m)       # reshape as square matrix of complex numbers
# Z = 0                   # initialize Z to zero
# X = array(0, c(m,m,50)) # initialize output 3D array 
# for (k in 1:50) {       # loop with 50 iterations
#   Z = Z^2+C             # the central difference equation
#   X[,,k] = exp(-abs(Z)) # capture results
# }

# write.gif(X, "Mandelbrot.gif", col=jet.colors, delay=100)

# month.abb
# month.name
# LETTERS


# X < Y
# X > Y
# X == Y
# X != Y
# X >= Y
# X <= Y

x = 10
y = 20
print(x)
print(y)
print(x < y)
print(x > y)
print(x == y)
print(x != y)
print(x <= y)
print(x >= y)


primeiro_vetor = c(1, 3, 5, 9, 10)
segundo_vetor = c(1, 5, 10, 2, 8)

print(primeiro_vetor)
print(segundo_vetor)

print(primeiro_vetor == segundo_vetor)
print(primeiro_vetor != segundo_vetor)

print(length(primeiro_vetor))
print(length(segundo_vetor))

terceiro_vetor = c(primeiro_vetor, segundo_vetor)
print(terceiro_vetor)

MATRIZ_A <- matrix(c(2, 4, 3, 1, 5, 7), nrow = 3 , ncol = 2, byrow = TRUE)

MATRIZ_B <- matrix(c(1, 4, 34, 1, 6, 3), nrow = 3 , ncol = 2, byrow = TRUE)

print(MATRIZ_A)
print(MATRIZ_A * MATRIZ_B)
