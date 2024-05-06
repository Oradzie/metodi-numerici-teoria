SISTEMI DI EQUAZIONI LINEARI:
- sono sistemi che possono essere visti nella seguente forma matriciale:
    - Ax = b
- A rappresenta la matrice dei coefficienti
- x rappresentra il vettore delle incognite
- b rappresenta il vettore dei termini noti
- un sistema lineare si dice COMPATIBILE se ammette almeno una soluzione, INCOMPATIBILE nel caso non ammetta alcuna soluzione

DEFINIZIONE DI MATRICE NON SINGOLARE:
- A(nxn) è detta NON SINGOLARE se soddisfa una delle seguenti condizioni equivalenti:
    1. det(A) != 0
    2. esiste la matrice A^-1 di A
    3. rank(A) = n
.. altrimenti A è detta SINGOLARE.

DEFINIZIONE DI MATRICE DEFINITA POSITIVA:
• sia A una matirce, per essere def. pos. deve valere che per ogni x!=0:
    - o x(trasposto)Ax > 0
    - o i suoi autovalori sono tutti reali e definiti positivi
    - oppure det(A(k)) > 0 per ogni k (A(k) = matrice di testa)

TEOREMA:
Condizione necessaria e sufficiente affinchè il sistema lineare Ax=b ammetta una e una sola soluzione, è che la matrice A sia a rango massimo (cioè che A sia invertibile); si ha perciò:
- x = A^-1 * b
- da notare che la matrice inversa ha un costo di calcolo elevato, ma anche poco accurato... infatti risolvere il sistema tramite l'inversa porta spesso ad un risultato che si discosta da quello reale

CONDIZIONAMENTO DI UN SISTEMA LINEARE:
In questa sezione si vuole esaminare come perturbazioni sugli elementi della matrice a e sugli elementi del termine noto b influenzano la soluzione x del sistema lineare.
Queste perturbazioni sono tipicamente dovute dal fatto che stiamo lavorando con l'aritmetica finita nell'algoritmo, e che ci sono evidenti errori di approssimazione dovuti alla rappresentazione con numeri finiti degli elementi di A e b.

PERTURBAZIONE DEL TERMINE NOTO: (guardare anche dimostrazione sulle slide della formula seguente)
- si ricorda che per calcolare l'errore relativo su un vettore bisogna utilizzare le norme
-l'errore relativo sarà dato dalla seguente formula:
  ||x(perturbato)||/||x|| <= ||A||*||A^-1|| * ||b(perturbato)||/||b||

.. il termine ||A||*||A^-1|| indica l'indice di condizionamento, cioè la sensibilità del problema a piccole perturbazioni sui dati --> in linalg la funzione cond calcola tale indice (numpy.linalg.cond(A,1))

PERTURBAZIONE SIA SULLA MATRICE CHE SUL TERMINE NOTO:
||x(perturbato)||/||x|| <= ||A^-1||*||A|| * [||A(perturbata)||/||A|| + ||b(perturbato)||/b]/ 1 - ||A^-1||*||A|| * ||A(perturbata)||/||A||

MATRICI MEGLIO CONDIZIONATE:
- si dimostra che la matrice identità e le matrici ortogonali sono le matrici meglio condizionate:
    - l'indice di condizionamento della matrice identità è 1 (è la matrice meglio condizionata)
    - se A è ortogonale invece si dimostra che la sua norma due è 1.

INDICE DI CONDIZIONAMENTO:
- si indica con K(A) la quantità  ||A||*||A^-1||:
    - se K(A) è piccolo (ordine 10^p dove p=0,1,2,3) --> il problema/matrice è ben condizionato
    - se K(A) è grande (ordine > 10^3) --> il problema/matrice è mal condizionato
- osservazione: l'indice di condizionamento di una matrice dipende intrinsecamente dal problema (dalla matrice stessa), cioè non ha nulla a che vedere
                con l'algoritmo risolutivo

METODI NUMERICI PER LA SOLUZIONE DI UN SISTEMA LINEARE:
Suddividiamo tali metodi in due tipologie:
1. Metodi diretti --> sono adatti per la soluzione di sistemi con matrice dei coefficienti densa (la % di elementi !=0 è > del 33%) e di moderate dimensioni
2. Metodi iterativi --> la matrice dei coefficienti non viene modificata durante il calcolo e quindi è più agevole sfruttarne la sparsità.
                        Sono adatti,quindi, per la soluzione di sistemi con matrice dei coefficienti di grandi dimensioni e sparsa.
                        L'idea sarebbe quella di partire da un iterato iniziale x(0) e generare una successione di iterati x(k) fino a convergere a soluzione.

METODI DIRETTI:
Tali metodi trasformano attraverso un numero finito di passi un sistema lineare generico in un sistema equivalente dotato di una struttura particolare che ne semplifichi la risoluzione.
Sono quindi basati nella fattorizzazione di A nel prodotto di due matrici B e C:
- Ax = b dove A = B*C
    - tale fattorizzazione mi permette di spezzare il problema in due sottoproblemi sotto forma di sistema di due equazioni:
        - equazione 1: By = b
        - equazione 2: Cx = y

- i metodi diretti si dividono principalmente in 3 algoritmi risolutivi diversi:
1. FATTORIZZAZIONE LU (di Gauss):
    • A viene fattorizzata in A = LU dove L è matrice triangolare inferiore e U matrice triangolare superiore
    • Ax=b diventa LUx=b
    • alla fine il sistema sarà composto dalle due seguenti equazioni:
        • equazione 1: Ly = b
        • equazione 2: Ux = y
    • TEOREMA 1: "sia A(k) la sottomatrice principale di testa di A, se A(k) ha det(A(k))!=0 --> esiste ed è unica la fattorizzazione LU di A"
    • tale fattorizzazione si basa sull'algoritmo di Gauss --> complessità computazionale =1/3 * n^3:
        - la matrice L servirà per memorizzare i moltiplicatori utilizzati per trasformare la matrice del sistema A in triangolare superioreù
    • se in posizione diagonale è presente uno zero, scambio le righe tra di loro --> quindi esiste una MATRICE DI PERMUTAZIONE tc:
        - PA = LU  .. il sistema diventerà quindi LUx = Pb (gli scambi effettuati per la matrice A andranno applicati anche al termine noto)
    • TEOREMA 2: "data una qualunque matrice A non singolare, esiste una matrice di permutazione P non singolare t.c PA = LU"

2. FATTORIZZAZIONE DI CHOLESKY:
    • A deve essere simmetrica e definita positiva 
    • A viene fattorizzata in A = L * L(trasposta) dove L è triangolare inferiore e L(trasposta) è triangolare superiore
    • alla fine il sistema sarà composto dalle due seguenti equazioni:
        • equazione 1: Ly = b
        • equazione 2: L(trasposta)x = y
    • TEOREMA: sia A una matrice di ordine n simmetrica e def. pos. --> allora esiste una matrice triangolare inferiore L con elementi diagonali positivi tc:
        - A = L*L(trasposta)
    • complessità computazionale = 1/6 * n^3

3. FATTORIZZAZIONE QR:
    • A viene fattorizzata in A = QR dove Q è ortogonale (Q*Q(trasposto) = I) e R triangolare superiore
    • • alla fine il sistema sarà composto dalle due seguenti equazioni:
        • equazione 1: Qy = b
        • equazione 2: Rx = y

STABILITA' DI UN ALGORITMO DI FATTORIZZAZIONE:
• Considero A = B*C e studiamo il fatto che questa fattorizzazione venga eseguita operando con i numeri finiti:
    • A + A(perturbato) = (B + B(perturbato))*(C + C(perturbato))
• Questa relazione mette in evidenza che la perturbazoine su A, non solo dipende dalle piccole perturbazioni su B e C, ma è tanto più grande quanro più grandi sono gli elementi dei fatti B e C.
• Quindi la stabilità si definisce in termini degli elementi di B e di C.
• Data una matrice A i cui elementi sono tutti minori od uguali ad 1, si dice che un algoritmo di fattorizzazione che produce una fattorizzazione BC della
  matrice A è numericamente stabile in senso forte, se esistono delle costanti positive a e b, indipendenti dall'ordine e dagli elementi di A t.c:
    • |b(ij)| <= a e |c(ij)| <= b
    • se le costanti a e b dipendono dall'ordine di A si dice che la fattorizzazione è stabile in senso debole.

STABILITA' DELL'ALGORITMO DI FATTORIZZAZIONE DI GAUSS, A = LU:
• nel caso in cui si utilizzi la tecnica di pivotaggio a perno massimo per colonne, che nasce da un'opportuna scelta della matrice P , si ha:
    • |l(ij)| <= 1
    • |u(ij)| <= 2^(n-1)*max|a(ij)|
• l'algoritmo di fattorizzazione di Gauss è stabile in senso debole perchè la costante che maggiora gli elementi di L non dipende dall'ordine della matrice,
  mentre ciò non accade per la costante che maggiora gli elementi di U, che dipende in maniera esponenziale dall'ordine della matrice.

METODI ITERATIVI PER LA SOLUZIONE DI SISTEMI LINEARI:
• i metodi iterativi raggiungono la soluzione esatta come limite di un procedimenti iterativo
• si basano sulla decomposizione della matrice A e presentano una complessità di O(kn^2) dove k = numero di iterazioni
• questi metodi risultano PARTICOLARMENTE CONVENIENTI quando la matrice A del sistema è di grandi dimensioni e SPARSA (il numero di elementi non nulli è di molto infeririore al numero degli elementi nulli)
• con le matrici sparse, applicando i metodi diretti, si potrebbe verificare il fenomeno del fill-in --> impedisce di avere dei metodi di memorizzazione che tengono conto degli elementi non nulli... questo non avviene applicando i metodi iterativi, in quanto essi si limitano ad utilizzare elementi non nulli della matrice senza toccare gli elementi nulli

IDEA DEI METODI ITERATIVI:
1. partire da un vettore x(0) iniziale arbitrario (stima iniziale della soluzione del sistema)
2. costruire una successione di iterati x(k) medinate il seguente procedimento iterativo:
    x(k) = Tx(k-1) + q  dove T = M^-1 * N è detta MATRICE DI ITERAZIONE DEL METODO ITERATIVO e q = M^-1 * b
3. A viene fattorizzata in M - N (splitting), dove M è facilmente invertibile e ha det!=0

– i metodi iterativi si suddividono in due principali algoritmi di risoluzione:
    • in entrambi si considera la matrice A del sistema come somma di 3 matrici A = D + E + F:
        • D ha sulla diagonale gli elementi sulla diagonale di A 
        • E è una matrice triangolare inferiore dove dalla diagonale in su sono tutti 0 e sotto la diagonale ci sono gli el. corrispondenti della matrice A
        • F è una matrice triangolare superiore dove dalla diagonale in giù sono tutti 0 e dalla diagonale in sù ci sono tutti gli el. corrispondenti di A
    1. METODO DI JACOBI:
    • M = D e N = -(E + F)
    • x(k) si ottiene seguendo la formula:
        • x(k) = -D^-1(E + F)*x(k-1) + D^-1 * b
        • si può notare facilmente che E+F rappresenta la matrice A senza elementi sulla diagonale, e da li posso trovare la formula per calcolare l'elemento j-esimo del vettore degli iterati (guardare formula nelle slide)
    • NB: l'algoritmo di Jacobi, per calcolare le nuove componenti del vettore degli iterati, utilizza solo gli elementi calcolati al passo k-1, senza
      sfruttare quelli che sta calcolando al passo k
    
    2. METODO DI GAUSS-SEIDEL:
    • M = (D + E) e N = -F
    • (guardare formula sulle slide per trovare la componente j-esima del vettore degli iterati)
    • a differenza del metodo di Jacobi, tale algoritmo  sfrutta le i-1 soluzioni già calcolate in precedenza

    OSSERVAZIONE: 
    • l'algoritmo di Jacobi è definito se gli elementi diagonali  di A sono diversi da 0, in caso contrario, si possono riordinare le equazioni e le incognite del sistema, in modo da rendere il metodo definito.

TEOREMA: CONDIZIONE NECESSARIA E SUFFICIENTE ALLA CONVERGENZA:
• sia A = M - N  una matrice di ordine n, con det(A) != 0, e T = M^-1 * N la matrice di iterazione del procedimento iterativo.
• condizione necessaria e sufficiente per la convergenza del metodo iterativo, comunque si scelga il valore iniziale x(0), al vettore soluzione x
  del sistema Ax=b, è che:
    – ∂(T) < 1  dove ∂ è il raggio spettrale (autovalore di modulo massimo) della matrice di iterazione T

CONDIZIONI SUFFICIENTI PER LA CONVERGENZA:
-TEOREMA 1:
• se per una qualunque norma, risulta che ||T|| < 1, allora il procedimento iterativo:
    •  x(k) = Tx(k-1) + q   è convergente per ogni x(0)
-TEOREMA 2:
• se la matrice A è strettamente dominante, cioè: per ogni riga della matrice, il valore dell'elemento diagonale è maggiore della somma dei valori assoluti 
  degli altri elementi nella stessa riga --> allora sia il metodo di Jacobi che quello di Gauss-Seidel convergono
NB: più è piccolo ∂, + srà veloce il metodo a convergereù
-TEOREMA 3:
• se la matrice A è simmetrica e definita positiva --> allora il metodo di Gauss-Seidel è convergente

ACCELERAZIONI DI UN METODO ITERATIVO:
- è possibile accelerare la convergenza di un metodo iterativo? sì, tramite una famiglia di metodi nota come motodi di rilassamento.
• L'idea di base di questi metodi è la seguente:
    • poichè la velocità di convergenza di un metodo iterativo dipende dal raggio spettrale della matrice di iterazione associata al metodo, un modo per cercare di accelerare la convergenza è quello di far dipendere la matrice di iterazione da un parametro, detto parametro di rilassamento (omega), e di scegliere tale parametro in modo tale che la matrice abbia minimo raggio spettrale.
    
