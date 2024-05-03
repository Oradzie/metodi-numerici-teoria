import numpy as np
import matplotlib.pyplot as plt

def newton_rapson_shamanskii(fun, jac, x0, tolx, tolf, itmax):
    
    # Calcolo lo jacobiano in x0
    matjac = jac(x0)
    
    # Controllo che il jacobiano non sia nullo
    if np.linalg.det(matjac) == 0:
        print("Lo jacobiano in x0 é nullo")
        return None, None, None
    
    it = 1
    
    # Risolvo lo jacobiano in x0
    s = -np.linalg.solve(matjac, fun(x0))
    
    # Calcolo il nuovo iterato
    x1 = x0 + s

    # Calcolo il valore della funzione in x1
    fx1 = fun(x1)

    # Aggiungo l'errore relativo alla lista
    Xm = [np.linalg.norm(s, 1)/np.linalg.norm(x1, 1)]
    
    while it <= itmax and np.linalg.norm(fx1, 1) >= tolf and np.linalg.norm(s, 1) >= tolx*np.linalg.norm(x1, 1):
        # Imposto il valore del veccio iterato a quello nuovo
        x0 = x1
        
        # Calcolo lo jacobiano solo ogni 4 iterazioni
        if it % 4 == 0:
            
            # Calcolo lo jacobiano in x0
            matjac = jac(x0)
            
            # Controllo che lo jacobiano non sia nullo
            if np.linalg.det(matjac) == 0:
                print("Lo jacobiano in x0 é nullo")
                return None, None, None

        # Incremento il contatore delle iterazioni
        it += 1
        
        # Risolvo lo jacobiano in x0
        s = -np.linalg.solve(matjac, fun(x0))
        
        # Calcolo il nuovo iterato
        x1 = x0 + s
        
        # Calcolo il valore della funzione in x1
        fx1 = fun(x1)
        
        # Aggiungo l'errore relatovo alla lista
        Xm.append(np.linalg.norm(s, 1)/np.linalg.norm(x1, 1))
        

    return x1, it, Xm

# Sistema di equazioni non lineari
F = lambda x: np.array([2 * x[0] - np.cos(x[1]), np.sin(x[0]) + 2 * x[1]])

# Jacobiano del sistema
J = lambda x: np.array([[2, np.sin(x[1])], [np.cos(x[0]), 2]])

# Intervallo di inizio della ricerca
x0 = np.array([-1, 1])

# Tolleranza per il valore da trovare
tolx = 1e-10

# Tolleranza per il valore della funzione
tolf = 1e-10

# Numero massimo di iterazioni in caso di non convergenza
itmax = 100

zero, it, Xm = newton_rapson_shamanskii(F, J, x0, tolx, tolf, itmax)
print(f"La soluzione del sistema di equzaioni é: {zero}, trovato in {it} iterazioni")


plt.semilogy(range(it), Xm, 'o')
plt.title("Andamento errore relativo durante il metodo iterativo")
plt.show()