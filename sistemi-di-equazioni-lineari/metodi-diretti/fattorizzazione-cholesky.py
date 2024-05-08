import numpy as np
import scipy.linalg as spl
import SolveTriangular

def cholesky_solve(L, b):
    y, flag = SolveTriangular.Lsolve(L, b)
    if flag == 0:
        x, flag = SolveTriangular.Usolve(L.T, y)
    else:
        print(f"I criteri di applicabilitá non sono soddisfatti")
        return None, None
    
    return x, flag

# Matrice che rappresenta il sitema da risolvere
A=np.array([[2,1,3],[1,5,7],[3,7,12]])
print(f"Matrice A: {A}")

# Faccio si che la soluzione del sistma siano tutti uno
b = np.sum(A, axis=1).reshape(3, 1)

L = spl.cholesky(A, lower=True)
print(f"Matrice L: {L}")

# Se A é una matrice di ordine n simmetrica e definita positiva, allora esiste una matrice L con elementi diagonali positvi tale che A = L*L.T
A1 = L@L.T
print(f"Matrice A1: {A1}")

# La soluzione del sistema lineare si riduce a Ly = b -> L.Tx = y
x, flag = cholesky_solve(L, b)
print(f"Solution: {x}")