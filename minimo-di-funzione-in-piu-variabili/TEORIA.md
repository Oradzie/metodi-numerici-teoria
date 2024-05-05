METODO DI NEWTON-RAPHSON PER IL CALCOLO DEL MINIMO DI UNA FUNZIONE A 2 VARIABILI:
- il problema sta nell'identificare la x* che renda minima la funzione 
- i punti di stazionarietà locale x* sono soluzione del seguente sistema non lineare:
    gradiente di f(x*) = 0 --> si traduce in un sistema dove:
        - equazione 1: derivata rispetto a x1 della funzione = a 0
        - equazione 2: derivata rispetto a x2 della funxione = a 0
- successivamente faccio lo sviluppo di taylor del primo ordine in un intorno x(k) delle due equazioni del sistema:
- il sistema può essere visto nella seguente forma matriciale:
    - [gradiente di f(x(k))] + H(x(k)) * (x-x(k)) = 0
    - se la matrice Hessiana presenta det!=0 allora:
        - x(k+1) = x(k) + s(k) --> dove s(k) = -H^-1(x(k)) * (gradientef(x(k)))

SCHEMA FINALE PER L'ALGORITMO DI NEWTON RAPHSON PER LA MINIMIZZAZIONE:
Dato x(0) ed F, per ogni iterazione k:
1. Valutare H(x(k-1)) (hessiana)
2. risolvere il sistema lineare H(x(k-1))*s(k-1) = - (gradientef(x(k-1)))
3. porre x(k) = x(k-1) + s(k-1)

.. s(k-1) definisce una direzione di discesa da x(k-1) ad x(k).
Il criterio di arresto dell'algoritmo è definito dal gradiente, poichè quando il gradiente si annulla non posso più proseguire.
