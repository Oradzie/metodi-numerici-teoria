SISTEMI DI EQUAZIONI NON LINEARI:
- Sono sistemi che possono essere scritti nella seguente forma:
  f1(x1....xn)=0 ..... fn(x1...xn)=0    (a sistema)
- le funzioni del sistema sono non lineari, continue e differenziabili
- consideriamo la funzione vettoriale, cioè quel vettore colonna le cui componenti sono le funzioni presentate nel punto 1:
    - risolvere il sistema di equazioni non lineari equivale a calcolare alpha trasposto t.c la funzione vettoriale in quel punto si annulla..
- .. a questo scopo introduciamo il gradiente di una funzione, che rappresenta il vettore colonna delle derivate parziali delle sue componenti
- si ricorda che il gradiente è uguale alla trasposta dello Jacobiano

METODO DI NEWTON-RAPHSON:
- il metodo di newton-raphson segue la teoria spiegata al punto precedente
- l'iterato successivo si calcola secondo la seguente formula:
    - x(k+1) = x(k) + s(k) dove s(k) rappresenta la soluzione di: J(x(k))^-1 * F(x(k))  .. dove J sta per Jacobiano
- l'algoritmo di Newton-Raphson si può quindi schematizzare così:
    - dato x(0) appartenente ad Rn ed F, per ogni iterazione k:
      1. valutare J(x(k-1))
      2. risolvere il sistema lineare J(x(k-1))*s(k-1) = - F(x(k-1))
      3. porre x(k) = x(k-1) * s(k-1)
- si ricorda che la Jacobiana deve avere determinante diverso da zero, altrimenti non è possibile determinare s
- tale metodo è a convergenza locale e ordine di convergenza quadratico
- si può dire che s(k) mi dice la direzione successiva verso cui muovermi per giungere a convergenza

VARIANTI METODO DI NEWTON-RAPHSON:
    1. NEWTON-RAPHSON-CORDE:
    - valuto lo jacobianno di partenza poi utilizzo sempre quello anche nelle  iterazioni successive

    2. NEWTON-RAPHSON-SHAMANSKII:
    - si valuta lo jacobiano ogni m iterazioni e quindi lo si utilizza per le m iterazioni