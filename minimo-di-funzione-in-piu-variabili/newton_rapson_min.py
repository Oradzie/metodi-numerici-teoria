import numpy as np
import matplotlib.pyplot as plt

def min_newton_rapson(fun, grad, hes, x0, tolx, tolf, itmax):
    
    # Calcolo l'hessiana in x0
    mathes = hes(x0)

    # Controllo che l'hessiana non sia nulla
    if np.linalg.det(mathes) == 0:
        print("L'hessiana in x0 é nulla")
        return None, None, None
    
    it = 1
    
    # Risolvo l'hessiana in x0
    s = -np.linalg.solve(mathes, grad(x0))
    
    # Calcolo il nuovo iterato
    x1 = x0 + s

    # Calcolo il valore della funzione in x1
    fx1 = fun(x1)

    # Aggiungo l'errore relativo alla lista
    Xm = [np.linalg.norm(s, 1)/np.linalg.norm(x1, 1)]

    while it <= itmax and np.abs(fx1) >= tolf and np.linalg.norm(s, 1) >= tolx*np.linalg.norm(x1, 1) and grad(x1).all() != 0:
        
        # Imposto il valore del veccio iterato a quello nuovo
        x0 = x1
        
        # Calcolo l'hessiana in x0
        mathes = hes(x0)
        
        # Controllo che l'hessiana non sia nulla
        if np.linalg.det(mathes) == 0:
            print("L'hessiana in x0 é nulla")
            return None, None, None
        
        # Incremento il contatore delle iterazioni
        it += 1
        
        # Risolvo l'hessiana in x0
        s = -np.linalg.solve(mathes, np.gradient(fun(x0)))
        
        # Calcolo il nuovo iterato
        x1 = x0 + s
        
        # Calcolo il valore della funzione in x1
        fx1 = fun(x1)
        
        # Aggiungo l'errore relatovo alla lista
        Xm.append(np.linalg.norm(s, 1)/np.linalg.norm(x1, 1))

    return x1, it, Xm

# Funzione da minimizzare
F = lambda x: x[0]**2 + x[1]**2 -4*x[0] -2*x[1]

# Hessiana della funzione
H = lambda x: np.array([[2, 0], [0, 2]])

# Gradiente della funzione
G = lambda x: np.array([2*x[0]-4, 2*x[1]-2])

# Intervallo di inizio della ricerca
x0 = np.array([-2, 1])

# Tolleranza per il valore da trovare
tolx = 1e-10

# Tolleranza per il valore della funzione
tolf = 1e-10

# Numero massimo di iterazioni in caso di non convergenza
itmax = 100

zero, it, Xm = min_newton_rapson(F, G, H, x0, tolx, tolf, itmax)
print(f"Il punto di minimo della funizione é: {zero}, trovato dopo {it} iterazioni")

plt.semilogy(range(it), Xm, 'o')
plt.title("Andamento errore relativo durante il metodo iterativo")
plt.show()