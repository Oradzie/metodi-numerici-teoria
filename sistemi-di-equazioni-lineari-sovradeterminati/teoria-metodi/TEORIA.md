DEFINIZIONE DI SISTEMI LINEARI SOVRADETERMINATI:
-Tali sistemi hanno un numero di equazioni superiore al numero di incognite, ossia sono della forma:

![sistema sovradeterminato](image.png)

-In particolare se:
 1. rank(A) != rank(A|b) --> sistema incompatibile, nessuna soluzione
 2. rank(A) = rank(A|b) --> sistema compatibile
    - rank(A) = n soluzione unica

La risoluzione di un sistema lineare sovradeterminato risulta quindi essere un problema mal posto,in quanto potrebbe accadere
che la soluzione non esista o, se esiste, non sia unica.

RISOLUZIONE DI SISTEMI LINEARI SOVRADETERMINATI NEL SENSO DEI MINIMI QUADRATI
-Cerchiamo la soluzione del sistema lineare sovradeterminato Ax=b con m>n nel senso dei minimi quadrati, cioè r definito come:

![Alt text](image-1.png)

-Ricordando quindi che G è simmetrica e G=A.T*A, otteniamo:

![Alt text](image-2.png)

-Per calcolare il valore x* che rende minimo F(x), calcoliamo il gradiente della funzione F(x) ed imponiamo che si annulli:

![Alt text](image-3.png)

-Il vettore x* che annulla il gradiente della funzione F(x) è la soluzione del sistema lineare:

![Alt text](image-4.png)

• l'equazione sopra citata è definita EQUAZIONE NORMALE... abbiamo quindi trasferito il problema della risoluzione di un sistema 
  sovradeterminato in quello della risoluzione di un sistema quadrato con matrice G=A.T*A di dimensione nxn.
  