from scipy.io import loadmat

import numpy as np

import matplotlib.pyplot as plt

import SolveTriangular

def gauss_seidel_sor(A,b,x0,toll,it_max,omega):
    errore=1000
    d=np.diag(A)
    D=np.diag(d)
    Dinv=np.diag(1/d)
    E=np.tril(A,-1)
    F=np.triu(A,1)
    Momega=D+omega*E
    Nomega=(1-omega)*D-omega*F
    T=np.dot(np.linalg.inv(Momega),Nomega)
    autovalori=np.linalg.eigvals(T)
    raggiospettrale=np.max(np.abs(autovalori))
    print("raggio spettrale Gauss-Seidel SOR ", raggiospettrale)
    
    M=D+E
    N=-F
    it=0
    xold=x0.copy()
    xnew=x0.copy()
    er_vet=[]
    while it<=it_max and errore>=toll:
        temp=b-np.dot(F,xold)
        xtilde,flag=SolveTriangular.Lsolve(M,temp)
        xnew=(1-omega)*xold+omega*xtilde
        errore=np.linalg.norm(xnew-xold)/np.linalg.norm(xnew)
        er_vet.append(errore)
        xold=xnew.copy()
        it=it+1
    return xnew,it,er_vet

#la matrice era stata fornita dalla prof all'esame (guarda in scelta metodo come caricarla)
dati = loadmat('test_06_05_2024.mat')

A=dati["A"] 

A=A.astype(float)

b=dati["b"]

b=b.astype(float)
n,m = A.shape
print(A.shape,A)
nz = np.count_nonzero(A)/(n*m)
perc_nz = nz * 100

#costruisco l'iterato iniziale
x0 = np.zeros_like(b)

#numero massimo di iterazioni
it_max = 500

#tolleranza
toll = 1e-8


#nota bene: la prof ha detto che omega va scelto fra 1.1 e 1.5, puoi accorgerti facilmente che gauss_seidel_sor è più veloce di gauss seidel
omega = 1.2
x_sor,it_sor,er_vet_sor = gauss_seidel_sor(A,b,x0,toll,it_max,omega)
print("il numero di iterazioni è:",it_sor)
