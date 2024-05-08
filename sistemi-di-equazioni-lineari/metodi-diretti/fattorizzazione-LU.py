import numpy as np
import scipy.linalg as spl
import SolveTriangular

def LUsolve(P, L, U, b):
    y, flag = SolveTriangular.Lsolve(L, P@b)
    if flag == 0:
        x, flag = SolveTriangular.Usolve(U, y)
    else:
        print(f"I criteri di applicabilitá non sono soddisfatti")
        return None, None
    
    return x, flag

# Matrice che rappresenta il sitema da risolvere
A = np.array([[2, 5, 8, 7], [5, 2, 2, 8], [7, 5, 6, 6], [5, 4, 4, 8]])

# Faccio si che la soluzione del sistma siano tutti uno
b = np.sum(A, axis=1).reshape(4, 1)

# Usiamo la funzione per la fattorizzazione LU di scipy (con pivotaggio a perno massimo per colonne) che restituisce la matrice P trasposta (P é la matrice di permutazione, teorema 2, ossia vengono memorizzati in essa gli scambi delle righe), la matrice U é una matrice triangolare superiore che contiene il sistema permutato e termine noto trasformato y, la matrice L é una matrice triangolare inferiore che contiene i moltiplicatori utilizzati per trasformare la matrice del sistema A in triangolare superiore -> PAx = Pb -> LUx = Pb
PT, L, U = spl.lu(A)

# Ci salviamo la matrice non trasposta
P = PT.T.copy()

print(f"Matrice A: {A}")
print(f"Matrice L: {L}")
print(f"Matrice U: {U}")
print(f"Matrice P: {P}")

# LU á la fattorizzazione di P*A (teorema 2)
A1 = P@A
A1_fatt = L@U

print(f"Matrice P*A: {A1}")
print(f"Matrice ottenuta moltiplicando L ed U {A1_fatt}")

# La risoluzione del sistema lineare la si ottine: Ly = Pb -> Ux = y
x, flag = LUsolve(P, L, U, b)
print(f"Solution: {x}")
