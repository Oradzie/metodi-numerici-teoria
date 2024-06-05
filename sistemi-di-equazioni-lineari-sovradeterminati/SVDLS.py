import numpy as np
import scipy.linalg as la
import SolveTriangular
import matplotlib.pyplot as plt

def SVDLS(A, b):
    
    # Numero di righe e numero di colonne di A
    m, n = A.shape
    
    # Fattorizzazione SVD della matrice
    U, s, VT = la.svd(A)  #Attenzione : Restituisce U, il numpy-array 1d che contiene la diagonale della matrice Sigma e VT=VTrasposta)
    
    # Calcolo di V dato che il metodo SVD restituisce la trasposta di V
    V=VT.T
    
    # Calcolo del rango della matrice, numero dei valori singolari maggiori di una soglia
    thresh = np.spacing(1)*m*s[0]
    k = np.count_nonzero(s>thresh)
    print("Rango =",k)
    
    # Decomposizione ai valori singolari
    d=U.T@b
    d1 = d[:k].reshape(k,1)
    s1 = s[:k].reshape(k,1)
    
    # Risolve il sistema diagonale di dimensione kxk avente come matrice dei coefficienti la matrice Sigma
    c = d1/s1
    
    x = V[:,:k]@c
    
    # Calcolo del residuo
    residuo = np.linalg.norm(d[k:])**2
    return x, residuo

# La metrice che rappresenta il sistema lineare sovradeterminato
A = np.array([
    [1., 1.001, 1.002],
    [1., 1.001, 1.003],
    [1., 1.001, 1.004],
    [1., 1.001, 1.005],
    [1., 1.001, 1.0013],
    [1., 1.001, 1.0014],
    [1., 1.001, 1.0015],
    [1., 1.001, 1.0016]
])

# Controllo del condizionamento e del rango della matrice A
print(f"Condizionamento della matrice A: {np.linalg.cond(A)}")
print(f"Rango della matrice A: {np.linalg.matrix_rank(A)}")

# Il vettore dei termini noti calcolato in modo tale che il vettore delle soluzioni siano tutti elementi uguali a 1
b = np.sum(A, axis=1)

# Calcolo della soluzione del sistema lineare sovradeterminato tramite equazioni normali
a, residuo = SVDLS(A, b)
print(f"Soluzione: {a}, con un residuo pari a {residuo}")
