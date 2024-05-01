TEOREMA DEGLI ZERI DI FUNZIONI CONTINUE:
- sia f(x) continua nell'intervallo [a,b] e sia tale che f(a)*f(b) < 0, allora:
f ammette almeno uno zero in (a,b), cioè esiste almeno un punto alfa in (a,b) t.c f(alfa) = 0

METODO DI BISEZIONE:
- tale metodo si basa sul teorema citato sopra
- questo metodo consiste nel generare nel generare una successione di sottointervalli I(1) = [a1,b1] .... I(k) = [a(k),b(k)]
In particolare:
1) si determina al passo k --> c(k) = 1/2(a(k-1) + b(k-1))
2) si calcola f(c(k)), se viene =0 allora c(k) è la radice alfa cercata,altrimenti:
    - se f(a(k-1))*f(c(k)) < 0 --> si pone b(k) = c(k) e a(k) = a(k-1)
    - in questo modo l'intervallo iniziale viene via via dimezzato, in particolare dopo k iterazioni si arriva all'intervallo [a(k),b(k)] 
      di ampiezza (b(k) - a(k)) = 1/2^k * (b(0) - a (0))
- l'errore al passo k è |e(k)| = |x(k) - alfa| <= 1/2 * |b(0) - a(0)|
- si ricorda che il metodo di bisezione è un metodo molto lento, servono fino a 4 iterazioni per ottenere una cifra significativa esatta nella
  soluzione approssimata
- il criterio di arresto del metodo di bisezione si ottiene nel seguente modo:
  - |b-a/2^(k+1)| <= epsilon (questo permette di verificare qunate iterazioni sono necessarie per raggiungere la precisazione epsilon prefissata)
    2^(k+1) >= b-a/epsilon --> k >= log2(b-a/epsilon) - 1
- il metodo di bisezione ha ordine di convergenza lineare 

METODO DELLA REGULA FALSI:
- ricordiamo che il metodo di bisezione è lento perchè non trae nessun vantaggio dalle caratteristiche della funzione, come la sua derivabilità.
- il metodo della regula falsi considera come nuova approssimazione della soluzione l'intersezione dell'asse delle ascisse (x) con la retta passante per 
  [(a,f(a)),(b,f(b))]
- tale retta si ottiene tramite il sistema formato dalle due seguenti equazioni:
   1. y - f(a) = [(f(b) - f(a))/(b - a)] * (x - a)
   2. y = 0
- quindi x = a - f(a) * [(b-a)/(f(b) - f(a))]
- f(a) e f(b) devono avere comunque segno opposto 
- PSEUDO-CODICE REGULA FALSI:
  1. se f(a) * f(b) < 0 si pone a(0) = a e b(0) = b
  2. finchè non risulta verificato il criterio di arresto:
      - poni x(k+1) = a(k) - f(a(k)) * [(b(k) - a(k))/ f(b(k) - f(a(k)))]
        - se f(x(k+1)) * f(a(k)) < 0 --> a(k+1) = a(k) ; b(k+1) = x(k+1)
        - altrimenti se f(x(k+1)) * f(b(k)) < 0 --> a(k+1) = x(k+1) ; b(k+1) = b(k)
        - altrimenti se f(x(k+1)) = 0 --> x(k+1) = alfa (significa che ho trovato la radice)
      - k = k + 1

METODI DI LINEARIZZAZIONE:
I metodi di linearizzazione sono metodi che in generale utilizzano la suguente formula:
  -  x(k+1) = x(k) - f(x)/m(k)
- m(k) gioca un ruolo importante, infatti, a seconda della scelta di m(k) posso distinguere 3 metodi diversi:
  1. metodo delle corde 
  2. metodo delle secanti
  3. metodo di newton 
- in generale: se al posto di m(k) sostituisco m' (derivata prima), avrò la migliore approssimazione locale nell'intorno di quel punto.

  1. METODO DELLE CORDE:
  - utilizza un valore di m costante e =!0 
  - quindi x(k+1) = [x(k) - f(x(k))]/m
  - una scelta classica è quella di usare m = [f(b) - f(a)] / b -a 
  - sostituendo m nella formula al punto due si otterrà infine che l'iterato successivo si calcolerà nel seguente modo:
    - x(k+1) = x(k) - f(x(k)) * (b - a)/[f(b) - f(a)]
  - si può notare poi dai grafici delle rette che vengono calcolate ad ogni passo per cercare lo zero che sono tutte parallele fra di loro
   (m = costante), quindi esse avranno tutte lo stesso coefficiente angolare

  2. METODO DELLE SECANTI:
  - assegno inizialmente due valori iniziale x(0) e x(1)
  - come coefficiente angolare viene scelto m(k) = [f(x(k)) - f(x(k-1))] / [x(k) - x(k-1)]
  - la retta che intersecca l'asse x ad ogni iterazioni passerà nel punto di ascissa:
    x(k+1) = x(k) - f(x(k)) * [x(k) - x(k-1)]/[f(x(k)) - f(x(k-1))]
  - la convergenza di tale metodo è garantita se le approssimazioni x(0) ed x(1) si scelgono abbastanza vicine alla soluzione: quindi ha CONVERGENZA LOCALE.
  - in tal caso la convergenza è superlineare (il metodo raggiunge convergenza in massimo 1,618 iterazioni)
  - si può dire infine che tale metodo dipende molto dagli iterati iniziali scelti.

  3. METODO DI NEWTON:
  - tale metodo sceglie m(k) = f'(x(k)) (derivata prima)
  - sostituendo tale m sempre nella formula generale dei metodi di linearizzazione si ottiene la seguente formula ricorsiva:
    x(k+1) = x(k) - f(x(k))/f'(x(k))
  - quindi ad ogni passo k, si considera la retta passenta pe ril punto [x(k),f(x(k))] e tangente alla curva f(x) e si determina il nuovo iterato come il punto di incontro tra questa retta e l'asse delle x (come dice la formula fornita al punto 2)
 
 CONFRONTO FRA REGULA FALSI E SECANTI
 - regula falsi ha una convergenza più sicura, mentre secanti dipende molto dagli iterati iniziali (anche se converge più velocemente)

 PROBLEMI CON IL MEODO DI NEWTON
 1. se la derivata della funzione valutata in x(k) è uguale a zero il metodo di blocca (dato che dovrebbe dividere per 0)
 2. se alfa è uno zero di molteplicità m, si dimostra che il metodo di newton avrà convergenza lineare 

 RIASSUNTO SULL'ORDINE DI CONVERGENZA p DEI METODI:
 - Metodo di Newton: p=2 --> convergenza quadratica
 - Metodo delle secanti: p=1.618 --> convergenza superlineare
 - Metodo regula falsi: convergenza superlineare
 - Metodo di bisezione: p=1 --> convergenza lineare
 