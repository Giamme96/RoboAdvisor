# Progetto-Fintech

Librerie--------------------------------------------------------------------------------------------------------------------------------
Installando il package Scipy vengono installate molte di quelle necessarie qui sotto.

Librerie necessarie(dovrebbero essere tutte): tkinter, datetime, matplotlib, pandas, statistics, plotly.graph_objects, numpy, statsmodels.api, investpy, tksheet.

Generale--------------------------------------------------------------------------------------------------------------------------------
-File principale per lo start dell'applicazione è Inizio.py.
-I file in JSON sono file su cui vengono scritti i dati in caso di chiusura dell'applicazione.
-Il manager non viene aggiornato quando vi sono cambiamenti nel programma che abilitano le tabs. Dopo l'invio del questionario sarà necessario il riavvio del programma, sarà necessario anche dopo l'inserimento del primo titolo in portafoglio per la tab CONSULENTE (ho preferito far si che queste tab vengano disattivate malgrado il riavvio necessario).

Assunzioni------------------------------------------------------------------------------------------------------------------------------
-E' possibile avere una sola istanza per ogni strumento nel portafoglio, quindi una sola data di acquuisto.
-Gli strumenti acquistabili/cercabili sono Stock-Etf-Funds (è possibile inserire altri strumenti con 3-4 righe di codice e piccole            modifiche in generale, dipende anche dalle API).
-E' possibile cercare/acquistare gli strumenti solo in determinati paesi (US-IT-GB, modificabili nel dictionary countries)
-E' probabile che vi siano exploit nell'inserimento di valori/stringhe nei form, ci sono molti controlli in ogni caso.
-Ovviamente non è stata presa in considerazione la sicurezza dei dati o il login dell'utente.

Primi passi-----------------------------------------------------------------------------------------------------------------------------
-Compilazione questionario. Dato che le tabs sono disabilitate, è necessario fare il riavvio dell'applicazione come annunciato sopra
-Dato che non vi sono strumenti nel portafoglio la tab CONSULENTE è disabilitata, ancora dopo il primo inserimento nel portafoglio sarà possibile ricevere i consigli del roboadvisor, sarà necessario il riavvio dell'applicazione.

Spunti per trasformarla in un applicazione utile----------------------------------------------------------------------------------------

