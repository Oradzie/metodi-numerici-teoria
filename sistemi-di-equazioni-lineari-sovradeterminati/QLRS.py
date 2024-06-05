import numpy as np
import scipy.linalg as la
import SolveTriangular
import matplotlib.pyplot as plt

def QLRS(A, b):
    
    # Numero di colonne della matrice A
    n=A.shape[1]
    
    # Fattorizzazione QR della matrice
    Q, R = la.qr(A)
    
    h=Q.T@b
    
    # Calcolo della soluzione del sistema con la matrice triengolare superiore R e il nuovo vettore dei temrini noti h escludendo le righe oltre la dimensione della matrice originale
    x, flag = SolveTriangular.Usolve(R[0:n,:],h[0:n])
    
    # Calcolo del residuo
    residuo=np.linalg.norm(h[n:])**2
    
    return x,residuo

# La metrice che rappresenta il sistema lineare sovradeterminato
# A = np.array([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]])
A = np.array([
[1, 1, 1],
[1, 2, 2],
[1, 2, 3],
[1, 2, 3]
])

# Controllo del condizionamento e del rango della matrice A
print(f"Condizionamento della matrice A: {np.linalg.cond(A)}")
print(f"Rango della matrice A: {np.linalg.matrix_rank(A)}")

# Il vettore dei termini noti calcolato in modo tale che il vettore delle soluzioni siano tutti elementi uguali a 1
b = np.sum(A, axis=1)

# Calcolo della soluzione del sistema lineare sovradeterminato tramite equazioni normali
a, residuo = QLRS(A, b)
print(f"Soluzione: {a}, con un residuo pari a {residuo}")
