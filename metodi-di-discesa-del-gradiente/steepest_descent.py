import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.io import loadmat

def steepestdescent(A,b,x0,itmax,tol):
 
    n,m=A.shape
    if n!=m:
        print("Matrice non quadrata")
        return [],[]
    
    
   # inizializzare le variabili necessarie
    x = x0

     
    r = A@x-b #residuo (gradiente)
    p = -r #direzione antigradiente
    it = 0
    nb=np.linalg.norm(b) 
    errore=np.linalg.norm(r)/nb
    vec_sol=[]
    vec_sol.append(x)
    vet_r=[] 
    vet_r.append(errore)
     
# utilizzare il metodo del gradiente per trovare la soluzione
    while errore>= tol and it< itmax:
        it=it+1
        Ap=A@p
       
        alpha = -(r.T@p)/(p.T@Ap)
                
        x = x + alpha*p  #aggiornamento della soluzione nella direzione opposta a quella del gradiente: alpha mi dice dove fermarmi 
         
        vec_sol.append(x)
        r=r+alpha*Ap
        errore=np.linalg.norm(r)/nb
        vet_r.append(errore)
        p = -r #Direzione opposta alla direzione del gradiente
        
     
    return x,vet_r,vec_sol,it

dati = loadmat('test_06_05_2024.mat')

A=dati["A"] 

A=A.astype(float)

b=dati["b"]

b=b.astype(float)

# Vettore delle soluzioni di partenza
x0 = np.zeros_like(b)

# Numero massimo di iterazini prima che il metodo venga interrotto
it_max = 1000

# Tolleranza sull'errore
toll = 1e-10

# Applico il metodo del gradiente coniugato
xG, vec_rG, vec_solG, itG = steepestdescent(A, b, x0, it_max, toll)
print(f"Soluzione: {xG}, trovata in {itG} iterazioni")

# Grafico contenente l'andamento dell'errore
plt.semilogy(np.arange(itG+1), vec_rG, '-r')
plt.title("Andamento dell'errore")
plt.show()

#se nel metodo voglio disegnare le curve di livello:
"""
 from mpl_toolkits.mplot3d import Axes3D
 plt.contour(X, Y, Z, levels=f(x,A,b).flatten())
 plt.plot(x[0],x[1],'ro')
"""