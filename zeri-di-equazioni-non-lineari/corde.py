import math
import numpy as np
import matplotlib.pyplot as plt

def corde(fname, m, x0, tolx, tolf, maxit):
    """
    Implementa il metodo delle corde per il calcolo degli zeri di un'equazione non lineare.

    Parametri:
    fname: La funzione da cui si vuole calcolare lo zero.
    m: La pendenza della retta che passa per i punti (a, f(a)) e (b, f(b)).
    x0: Il punto di partenza.
    tolx: La tolleranza di errore.
    tolf: La tolleranza di errore sulla funzione.
    maxit: Il numero massimo di iterazioni.

    Restituisce:
    Lo zero approssimato della funzione, il numero di iterazioni e la lista di valori intermedi.
    """
    xk = []
    
    # Calcolo il valore della funzione nell'iterato di partenza
    fx0 = fname(x0)
    
    # Calcolo l'operando della formula per il calcolo del nuovo iterato ((1/m)*f(x0))
    d = fx0/m
    
    # Calcolo del nuobo iterato (x0-(1/m)*f(x0))
    x1 = x0-d
    
    # Calcolo il valore della funzione nel nuovo iterato
    fx1 = fname(x1)
    
    # Aggiundo il nuovo iterato alla lista degli iterati
    xk.append(x1)
    
    it = 1
    
    while it < maxit and  abs(fx1) >= tolf and abs(d) >= tolx*abs(x1):
        # Imposo l'ultimo iterato a quello vecchio e calcolo il nuovo iterato
        x0 = x1
        fx0 = fname(x0)
        d = fx0/m
        '''
        #x1= ascissa del punto di intersezione tra la retta che passa per il punto
        (xi,f(xi)) e ha pendenza uguale a m
        '''
        x1 = x0-d
        
        # Calcolo il valore della funzione nel nuovo iterato
        fx1 = fname(x1)
        
        # Incremento il contatore delle iterazioni
        it += 1
        
        # Aggiungo il nuovo iterato alla lista degli iterati
        xk.append(x1)
    
    if it == maxit:
        print('raggiunto massimo numero di iterazioni \n')
        
    return x1, it, xk

# Funzione di cui si vuole trovare lo zero
f = lambda x: np.exp(-x)-(x+1)              # e^(-x) = x+1

# Zero reale della funzione
alpha = 0

# Intervallo di partenza
a = -1
b = 2

# Punto di partenza del metodo
x0 = -0.5

# Tolleranza per il risultato finale
tolx = 1e-12

# Tolleranza per il valore della funzione
tolf = 1e-12

# Numero massimo di iterazioni
maxit = 1000

# Intervallo della funzione che staimo calcolando
xx = np.linspace(a, b, 200)

# Coefficiente angolare della retta che passa per i punti (a, f(a)) e (b, f(b))
m = (f(b)-f(a))/(b-a)

# Applico il metodo di bisezione per trovare il 
zero, it, xk = corde(f, m, x0, tolx, tolf, maxit)
print(f"Zero: {zero}, trovato in {it} iterazioni")

# Disegno il grafico della funzione
plt.plot(xx, f(xx), '-r')
plt.title(f"Function: exp(-x)-(x+1)")
plt.grid(True)
plt.show()

# Trasformo la lista degli iterati in un array numpy
xk = np.array(xk)

# Calcolo dell'errore assoluto
err = np.abs(xk-alpha)
plt.title("Errore assoluto del metodo nel calcolo dello zero della funzione")
plt.semilogy(range(it), err, '-o')
plt.show()