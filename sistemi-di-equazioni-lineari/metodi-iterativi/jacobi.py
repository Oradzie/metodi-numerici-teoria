import numpy as np
import scipy.linalg as spl

# T = M^-1 * N ,dove T è la matrice di iterazione
# si ricorda che in Jacobi M=D (matrice che sulla diagonale ha gli elementi della matrice A e nelle altre posizioni tutti 0)
# e che la matrice N = - (E + F)
# q= M^-1 * b
def jacobi(A,b,x0,toll,it_max):

    d = np.diag(A) #restituisce un array 1D
    invM = np.diag(1/d) #matrice che sulla diagonale ha reciproci di D

    E = np.tril(A,-1) #E sarà la matrice triangolare inferiore di A, esclusi i suoi elementi diagonali

    F = np.triu(A,1) #F sarà la matrice triangolare superiore di A

    N = -(E+F)

    T = invM@N

    autovalori = np.linalg.eigvals(T)
    raggio_spettrale = np.max(np.abs(autovalori)) #il raggio spettrale è l'autovalore di valore assoluto massimo
    print("raggio spettrale jacobi", raggio_spettrale) #se il raggio spettrale della matrice di iterazione è >1, il metodo potrebbe non convergere e fornire una soluzione errata
    
    it = 0
    er_vet = []
    errore = 1000
    while it <= it_max and errore >= toll:

        q = invM@b
        x = T@x0 + q
        errore = np.linalg.norm(x-x0)/np.linalg.norm(x)
        er_vet.append(errore)

        x0 = x.copy()
        it = it+1
    
    return x,it,er_vet

#matrice che rappresenta il sistema da risolvere
A = np.array([[2,1,3],[1,5,7],[3,7,12]])
print(f"Matrice A: {A}")

n=3
#costruisco il vettore dei termini noti
b = np.sum(A,axis = 1).reshape(n,1)

#costruisco l'iterato iniziale
x0 = np.zeros_like(b)

#numero massimo di iterazioni
it_max = 500

#tolleranza
toll = 1e-8

#testo la funzione
x,it,er_vet = jacobi(A,b,x0,it_max,toll)
print(x,it,er_vet)

print(np.linalg.solve(A,b))
