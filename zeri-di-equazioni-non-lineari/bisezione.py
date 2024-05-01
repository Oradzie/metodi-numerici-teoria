import math
import numpy as np
import matplotlib.pyplot as plt

def sign(x):
    """
    Funzione segno che restituisce 1 se x è positivo, 0 se x è zero e -1 se x è negativo.
    """
    return math.copysign(1, x)

def bisezione(fname, a, b, tolx):
    """
    Implementa il metodo di bisezione per il calcolo degli zeri di un'equazione non lineare.

    Parametri:
    fname: La funzione di cui si vuole calcolare lo zero.
    a: L'estremo sinistro dell'intervallo di ricerca.
    b: L'estremo destro dell'intervallo di ricerca.
    tolx: La tolleranza di errore.

    Restituisce:
    Lo zero approssimato della funzione, il numero di iterazioni e la lista di valori intermedi.
    """
    fa = fname(a)
    fb = fname(b)

    # Siamo nell'intervallo sbagliato
    if sign(fa)*sign(fb) >= 0:
        print("Non é possibile applicare il metodo di bisezione\n")
        return None,None,None

    
    maxit = math.ceil(math.log2((b-a)/tolx))-1

    it = 0
    v_xk = []

    while abs(b-a) > tolx and it <= maxit:
        # Dimezzo l'intervallo
        xk = a+(b-a)/2
        
        # Aggiungo il valore di xk alla lista delle iterazioni
        v_xk.append(xk)
        
        # Incremento il contatore delle iterazioni
        it += 1

        # Calcolo la funzione nel punto xk
        fxk = fname(xk)

        # Ho trovato il valore esatto
        if fxk == 0:
            return xk, it, v_xk

        # Viene scelto l'intervallo in cui continuare la ricerca
        if sign(fa)*sign(fxk)>0:     # Si continua a lavorare su [xk, b]
            a = xk
            fa = fxk
        elif sign(fxk)*sign(fb)>0:   # Si contiuna a lvaorare su [a, xk]
            b = xk
            fb = fxk
    
    return xk, it, v_xk

# Funzione di cui si vuole trovare lo zero
f = lambda x: np.exp(-x)-(x+1)              # e^(-x) = x+1

# Zero reale della funzione
alpha = 0

# Intervallo di partenza
a = -1
b = 2

# Tolleranza per il risultato finale
tol = 1e-12

# Intervallo della funzione che staimo calcolando
xx = np.linspace(a, b, 200)

# Applico il metodo di bisezione per trovare il 
zero, it, xk = bisezione(f, a, b, tol)
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