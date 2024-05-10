import numpy as np
import scipy.linalg as spl
import SolveTriangular

# A = M - N
# M = (D + E)
# N = -F
def gauss_seidel(A,b,x0,toll,it_max):
    errore = 1000

    d = np.diag(A) #d contiene gli elementi sulla diagonale di A
    
    #costruisco la matrice D
    D = np.diag(d)

    #costruisco la matrice E triangolare inferiore di A, eslusi i suoi elementi diagonali
    E = np.tril(A,-1) 

    #costruisco la matrice F  triangolare superiore di a
    F = np.triu(A,1)

    M = (D+E)
    N = -F
    T = np.linalg.inv(M)@N

    autovalori=np.linalg.eigvals(T)
    raggiospettrale=np.max(np.abs(autovalori))
    print("raggio spettrale gauss seidel", raggiospettrale)

    it=0
    er_vet=[]
    while it<=it_max and errore>=toll:
        temp=b-F@x0
        x,flag = SolveTriangular.Lsolve(M,temp)  #Calcolare la soluzione al passo k equivale a calcolare la soluzione del sistema triangolare con matrice M=D+E
                               # e termine noto b-F@x0
        errore=np.linalg.norm(x-x0)/np.linalg.norm(x)
        er_vet.append(errore)
        x0=x.copy()
        it=it+1
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
x,it,er_vet = gauss_seidel(A,b,x0,it_max,toll)
print(x,it,er_vet)

print(np.linalg.solve(A,b))

#NOTA BENE!!:
#Il raggio spettrale del metodo di Gauss-Seidel è più piccolo del raggio spettrale del metodo di Jacobi, questo giustifica il fatto che 
# il metodo di Gauss-Seidel + più veloce !!
