import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.io import loadmat

# Metodo per per trovare la soluzione del sistema tramite il gradiente coniugato
def conjugate_gradient(A, b, x0, itmax, toll):
    
    # Dimensioni della matrice
    n, m = A.shape
    
    # Controllo che la matrice sia quadrata, se non lo é ritorno dei valori nulli
    if n != m:
        print("Matrice non quadrata")
        return None, None, None, None

    x = x0
    
    # Calcolo la direzione del gradiente
    r = A@x-b
    
    # Direzione coniugata ad r
    p = -r
    
    # Inizializzo il numero di iterazioni
    it = 0
    
    # Calcolo la norma di b
    nb = np.linalg.norm(b)
    
    # Criterio d'arresto (errore)
    cda = np.linalg.norm(r)/nb

    # Vettore delle soluzioni a cui aggiungo la prima soluzione (vettore con tutti zeri)
    vec_sol = []
    vec_sol.append(x)
    
    # Vettore degli errori a cui aggiungo il primo valore di errori trovato
    vec_r = []
    vec_r.append(cda)

    
    while cda >= toll and it < itmax:
        
        # Incremento il numero di iterazioni
        it = it+1

        # Prodotto matrice A per vettore direzione
        Ap = A@p
        
        # Calcolo il numeratore per trovare il nuovo alpha (<r^(k), r^(k)>), dove p = -R^(k)
        num = -(r.T@p)
        
        # Calcolo il nuovo alpha 
        alpha = num/(p.T@Ap)

        # Calcolo del nuovo iterato
        x = x+alpha*p
        
        # Mi salvo il vecchio valore di r
        r_old = r
        
        # Calcolo il nuovo E
        r = r+alpha*Ap
        
        # Calcolo il valore di gamme (un parametro che applica una correzione alla direzione di discesa)
        gamma = (r.T@r)/(r_old.T@r_old)
        
        # Aggiungo la nuova soluzine al vettore
        vec_sol.append(x)
        
        # Calcolo il nuovo errore e lo aggiungo al vettore
        cda = np.linalg.norm(r)/nb
        vec_r.append(cda)
        
        # Calcolo la nuova direzione coniugata
        p = -r+(gamma*p)
    return x, vec_r, vec_sol, it

dati = loadmat('test_06_05_2024.mat')

A=dati["A"] 

A=A.astype(float)

b=dati["b"]

b=b.astype(float)

# Matrice che rappresenta il sistema di equazioni
# A = np.array([[8,4],[4,3]])

# Vettore dei termini noti
# b = np.array([[8],[10]])

# Vettore delle soluzioni di partenza
x0 = np.zeros_like(b)

# Numero massimo di iterazini prima che il metodo venga interrotto
it_max = 1000

# Tolleranza sull'errore
toll = 1e-10

# Applico il metodo del gradiente coniugato
xG, vec_rG, vec_solG, itG = conjugate_gradient(A, b, x0, it_max, toll)
print(f"Soluzione: {xG}, trovata in {itG} iterazioni")

# Grafico contenente l'andamento dell'errore
plt.semilogy(np.arange(itG+1), vec_rG, '-r')
plt.title("Andamento dell'errore")
plt.show()