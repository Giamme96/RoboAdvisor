# RoboAdvisor
**ENG VERSION SCROLL DOWN FOR IMGS** -----------------

Libraries
 * Installing Scipy package worth a lot of necessary libraries below there.
 * Libraries (should be all of them): tkinter, datetime, matplotlib, pandas, statistics, plotly.graph_objects, numpy, statsmodels.api, investpy, tksheet.

General
 * Inizio.py is the file for begin to use application.
 * In JSON files there are all data stored by the application, no DB needed, it's my choice, i don't remember SQL and so on.
 * I have a problem with the update and mainloop function from tkinter, so just restart application after sending the survey as a first step (tabs Panoramica, Modifica and Consulente **disabled**), and after adding a title in the portfolio (**enabling** tab Consulente).
 * Obviously the advices are not for Warren Buffet, but a newbie in finance could keeps them in mind.
 * Problems with *ISINtoCountry* when legal head office differs from country retrieved by the function.
 
Assumptions
 * There is only one instance for every title in portfolio, so there is only one timestap for every title.
 * 3 available assets (Stock-Etf-Fund), it takes very few changes to add others from API (https://investpy.readthedocs.io/index.html).
 * Available countries are (US-IT-GB-NL-FR-IE), described in a dictionary in *globalita.py*, just add the country you are looking for.
 * Surely there are exploits in the platform, especially in tab Modifica.
 * Not the best looking platform, but in Italy we say "Brutto ma buono", by the way i'm not sure at all my code is "buono".
 * Funds have risk rating instead of Beta, but are displayed in the same column, just pay attention.

First steps
 * Start to fill out the survey, it's a form representig MIFID II, the main pourpouses is the user profiling. (**restart application**)
 * Now you could looking for financial assets, as you add one in portfolio i recommend to **restart application**.
  
**ITA VERSION IMMAGINI IN FONDO** -----------------

Librerie
 * Installando il package Scipy vengono installate molte di quelle necessarie qui sotto.
 * Librerie necessarie(dovrebbero essere tutte): tkinter, datetime, matplotlib, pandas, statistics, plotly.graph_objects, numpy, statsmodels.api, investpy, tksheet.

Generale
 * File principale per lo start dell'applicazione è Inizio.py.
 * I file in JSON sono file su cui vengono scritti i dati in caso di chiusura dell'applicazione.
 * Il manager non viene aggiornato quando vi sono cambiamenti nel programma che abilitano le tabs. Dopo l'invio del questionario sarà necessario il riavvio del programma, sarà necessario anche dopo l'inserimento del primo titolo in portafoglio per la tab CONSULENTE (ho preferito far si che queste tab vengano disattivate malgrado il riavvio necessario).

Assunzioni
* E' possibile avere una sola istanza per ogni strumento nel portafoglio, quindi una sola data di acquuisto.
* Gli strumenti acquistabili/cercabili sono Stock-Etf-Funds (è possibile inserire altri strumenti con 3-4 righe di codice e piccole        modifiche in generale, dipende anche dalle API).
* E' possibile cercare/acquistare gli strumenti solo in determinati paesi (US-IT-GB-NL-FR-IE, modificabili nel dictionary countries)
* E' probabile che vi siano exploit nell'inserimento di valori/stringhe nei form, ci sono molti controlli in ogni caso.
* Ovviamente non è stata presa in considerazione la sicurezza dei dati o il login dell'utente.

Primi passi
* Compilazione questionario. Dato che le tabs sono disabilitate, è necessario fare il riavvio dell'applicazione come annunciato sopra
* Dato che non vi sono strumenti nel portafoglio la tab CONSULENTE è disabilitata, ancora dopo il primo inserimento nel portafoglio sarà possibile ricevere i consigli del roboadvisor, sarà necessario il riavvio dell'applicazione.

Spunti per trasformarla in un applicazione utile
* La cosa migliore sarebbe avere la possibilità di inserire direttamente il momento di acquisto dello strumento, in questo modo si 
avrebbe un allineamento del prezzo utilizzando l'applicazione anche con effetto retroattivo.
* Malgrado ci siano calcoli semplici da fare, per un utente che non abbia studiato materie economiche potrebbe essere un avvicinamento alla gestione del proprio portafoglio, magari evitando di esporre tutto il patrimonio investito in una società consigliata dall'amico del cugino dello zio, quindi ascoltando il consulente per una diversificazione del portafoglio.
* Purtroppo essendo un newbie di python e della programmazione in generale, aggiungendo lacune in matematica e non troppa documentazione su internet non sono riuscito ad aggiungere una feature per la simulazione dell'aggiunta di uno strumento in portafoglio per calcolare i delta in termini di rendimento atteso, var ecc. (scopo ottenibile programmando in termini semplici con cicli e array, ma mi sono rifiutato).
* Per le motivazioni sopra descritte sarebbe stato opportuno anche la simulazione attraverso l'applicazione di vincoli. In prima battuta il progetto lo prevedeva, considerando anche la posizione LONG-SHORT, sarebbe stata necessaria in ogni caso un'interfaccia più complessa.
* Il programma è stato sviluppato in Python non per necessità derivanti dalla piattaforma stessa, ma solo per imparare un nuovo linguaggio (a quanto pare richiesto dal mondo della finanza), da qua derivano i possibili errori e ripetizioni nel codice. In corso d'opera ho deciso di adottare tkinter come GUI non per convenienza ma per scarsa informazione, quindi non escludo che vi potevano essere modi migliori per lo sviluppo.

Ringraziamenti
* Per la tabella, a quanto pare gli sviluppatori di tkinter non c'hanno ancora pensato. https://github.com/ragardner/tksheet
* Un rigraziamento particolare ad Alvaro Barolome (alvarob96@usal.es), ha creato le API senza limitazioni da INVESTING, a quanto pare nessuno c'aveva pensato, dall'email deduco abbia la mia stessa età, chapeau. Magari utilizzare l'ISIN direttamente come chiave sarebbe stata la mossa del secolo, invece che paese, lingua e nome, ma c'è sempre tempo per migliorare. https://pypi.org/project/investpy/
* A mio fratello, paziente nello spiegarmi i dictionary e le classi, un abbraccio.


![Questionario](/Questionario.png)
![Cerca](/Cerca.png)
![panoramica](/Panoramica.png)
