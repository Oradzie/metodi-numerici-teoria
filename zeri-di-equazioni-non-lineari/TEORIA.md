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

