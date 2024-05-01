import math
import numpy as np
import matplotlib.pyplot as plt

def sign(x):
    """
    Funzione segno che restituisce 1 se x è positivo, 0 se x è zero e -1 se x è negativo.
    """
    return math.copysign(1, x)

def regula_falsi(fname, a, b, maxit, tolx, tolf):
    """
    Implementa il metodo di falsa posizione per il calcolo degli zeri di un'equazione non lineare.

    Parametri:
    fname: La funzione da cui si vuole calcolare lo zero.
    a: L'estremo sinistro dell'intervallo di ricerca.
    b: L'estremo destro dell'intervallo di ricerca.
    tolx: La tolleranza di errore.

    Restituisce:
    Lo zero approssimato della funzione, il numero di iterazioni e la lista di valori intermedi.
    """
    fa=fname(a)
    fb=fname(b)
    
    if sign(fa)*sign(fb)>=0:
        print("Non è possibile applicare il metodo di falsa posizione \n")
        return None, None,None

    it = 0
    v_xk = []
    
    fxk=10

    
    while it < maxit and abs(b - a) > tolx and abs(fxk) > tolf:
        # Calcolo il punto xk
        xk = a-fa*(b-a)/(fb-fa)
        
        # Aggiungo il valore di xk alla lista delle iterazioni
        v_xk.append(xk)
        
        # Incremento il contatore delle iterazioni
        it += 1
        
        # Calcolo la funzione nel punto xk
        fxk=fname(xk)
        
        # Ho trovato il valore esatto
        if fxk==0:
            return xk, it, v_xk

        # Viene scelto l'intervallo in cui continuare la ricerca
        if sign(fa)*sign(fxk)>0:  #continua su [xk,b]
            a = xk
            fa=fxk
        elif sign(fxk)*sign(fb)>0:   #continua su [a,xk]
            b = xk
            fb=fxk

    
    return xk, it, v_xk

# Funzione di cui si vuole trovare lo zero
f = lambda x: np.exp(-x)-(x+1)              # e^(-x) = x+1

# Zero reale della funzione
alpha = 0

# Intervallo di partenza
a = -1
b = 2

# Tolleranza per il risultato finale
tolx = 1e-12

# Tolleranza per il valore della funzione
tolf = 1e-12

# Numero massimo di iterazioni
maxit = 1000

# Intervallo della funzione che staimo calcolando
xx = np.linspace(a, b, 200)

# Applico il metodo di bisezione per trovare il 
zero, it, xk = regula_falsi(f, a, b, maxit, tolx, tolf)
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