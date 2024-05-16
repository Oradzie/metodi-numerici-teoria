import numpy as np
import scipy.linalg as la
import SolveTriangular
import matplotlib.pyplot as plt

def eqnorm(A, b):
    
    # Matrice simmetrica utlizzata per il calcolo del vettore che annulla il gradiente
    G = A.T@A
    
    # Calcolo del condizionamento della matrice G
    condG = np.linalg.cond(G)
    print(f"Condizionamento della matrice G: {condG}")
    
    # Termine noto del sistema per il calcolo del vettore che annulla il gradiente
    f = A.T @ b
    
    # Fattorizzazione di Cholesky della matrice G, prendo solo la matrice triangolare inferiore
    L = la.cholesky(G, lower=True)
    
    # Risoluzione del sistema lineare Lz = f
    z, flag = SolveTriangular.Lsolve(L, f)
    if flag == 0:
        # Risoluzione del sistema lineare L.Ta = z
        a, flag = SolveTriangular.Usolve(L.T, z)
        
    return a

# La metrice che rappresenta il sistema lineare sovradeterminato
A = np.array([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]])

# Il vettore dei termini noti calcolato in modo tale che il vettore delle soluzioni siano tutti elementi uguali a 1
b = np.sum(A, axis=1)

# Calcolo della soluzione del sistema lineare sovradeterminato tramite equazioni normali
a = eqnorm(A, b)
print(f"Solutzione: {a}")
