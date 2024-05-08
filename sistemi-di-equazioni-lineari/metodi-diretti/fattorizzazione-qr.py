import numpy as np
import scipy.linalg as spl
import SolveTriangular

def QRsolve(Q, R, b):
    # Essendo Q una matrice ortogonale la soluzione di Qy = b -> y = Q.Tb poiché l'inversa coincide con la trasposta
    y = Q.T@b
    x, flag = SolveTriangular.Usolve(R, y)
    return x, flag
    

# Matrice che rappresenta il sitema da risolvere
A=np.array([[2,1,3],[1,5,7],[3,7,12]])
print(f"Matrice A: {A}")

# Faccio si che la soluzione del sistma siano tutti uno
b = np.sum(A, axis=1).reshape(3, 1)

Q, R = spl.qr(A)
print(f"Matrice Q: {Q}")
print(f"Matrice R: {R}")

# Se A é una matrice m x n con rango massimo allora può essere fattorizzata in una matrice Q ortogonale m x m e R una matrice m x n composta da una matrice R_1 triangolare superiore n x n e il resto zero
A1 = Q@R
print(f"Matrice A1: {A1}")

# La soluzione del sistema lineare si riduce a Qy = b -> Rx = y
x, flag = QRsolve(Q, R, b)
print(f"Solution: {x}")