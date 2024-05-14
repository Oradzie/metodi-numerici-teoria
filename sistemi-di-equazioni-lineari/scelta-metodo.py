from scipy.io import loadmat

import numpy as np

import matplotlib.pyplot as plt

import SolveTriangular

dati = loadmat('test_06_05_2024.mat')

A=dati["A"] 

A=A.astype(float)

b=dati["b"]

b=b.astype(float)
n,m = A.shape
print(A.shape,A)
nz = np.count_nonzero(A)/(n*m)
perc_nz = nz * 100
print("percentuale elementi diversi da zero", perc_nz)
plt.spy(A) #bianco dove gli elementi sono nulli, un puntino nero dove ci sono elementi 
#matrice di grande dimensioni --> da 400 x 4000 in su
#matrice di piccole dimensioni --> massimo 50 x 50
#matrice sparsa --> numero di elementi diversi da zero non supera il 33%
#cholesky è piu veloce di Gauss


flag = A == A.T
if np.all(flag) == 0:
    print("Matrice non simmettrica")
else:
    print("Matrice è simmetrica")
    autovalori = np.linalg.eigvals(A)
    flag_dp = np.all(autovalori > 0)
    print("Matrice definita positiva", flag_dp)
#sto confrontando ogni elemento di A con a trasporto
    

#NB: in aggiunta utilizzare la mappa concettuale fornita dalla prof per capire quale metoedo è meglio utilizzare