
import numpy as np
import statsmodels.api as sm
import investpy as inv

import globalita as GLOBE
import API_call as CALLAPI




def DeltaChange(array, column_type):    #calcola i change moltiplicati * 100

    colonna = array[column_type]

    delta = colonna.pct_change() * 100

    # print(delta, "\n\n\n")

    return delta.dropna()

def DeltaChangeAvg(array, column_type): #calcola media change

    colonna = array[column_type]

    delta = colonna.pct_change().dropna()

    avg_delta = delta.mean() * 100

    # print(avg_delta, "\n\n\n")
    
    return avg_delta

def DeltaStd(array, column_type):  #calcola std di una colonna

    colonna = array[column_type]

    std_delta = colonna.std()    

    # print(std_delta, "\n\n\n")

    return std_delta

def DeltaChangeStd(array, column_type): #calcola std su change colonna

    colonna = array[column_type]

    delta = colonna.pct_change().dropna()

    std_delta = delta.std()
    
    return std_delta

def CalcoloChange(array, colonna, prezzo_riferimento_t0):  #restituisce un change moltipicato  per 100

    if isinstance(array, int):    
        
        return 0
    
    else:
        
        tempo1 = array[colonna].iloc[-1]
        # tempo0 = array[colonna].iloc[-2]

        change = (tempo1 - prezzo_riferimento_t0) / prezzo_riferimento_t0 * 100  

        return change

def TotaleInvestimento():

    key_societa = list(GLOBE.societa.keys())
    totale = 0

    for i in range(len(key_societa)):

        totale_parziale = GLOBE.societa.get(key_societa[i]).get("totale_ordine")

        totale = totale + totale_parziale

    return totale

def CreaMatriceCov():      #array di tipo lista, portafoglio[aapl, aal, msft, ecc]

    lista_portafoglio_dropped = []
    for i in GLOBE.societa.values():
        
        lista_portafoglio_return = DeltaChange(i.get("daily_adj"), "Close")
        lista_portafoglio_dropped.append(lista_portafoglio_return)


    matrice_cov = np.cov(lista_portafoglio_dropped)
    # print("La matrice covarianza del portafoglio: ", matrice_cov)
    # print("shape matrice: ", np.shape(matrice_cov))

    return matrice_cov

def TrasponiMatrice(matrice):

    matrice_trasposta = np.transpose(matrice)
    # print("Trasposta: ", matrice_trasposta)
    # print("shape matrice trasposta: ", np.shape(matrice_trasposta))

    return matrice_trasposta

def VettorePesi():
 
    key_societa = list(GLOBE.societa.keys())
    totale_investimento = TotaleInvestimento()
    vettore_pesi = []
    for i in range(len(key_societa)):

        peso_societa = GLOBE.societa.get(key_societa[i]).get("totale_ordine") / totale_investimento
        vettore_pesi.append(peso_societa)


    # print("Il vettore pesi è: ", vettore_pesi)

    return vettore_pesi

def MatriceProdotto(matriceA, matriceB):


    matrice_prodotto = np.dot(matriceA, matriceB)
    # print("Matrice prodotto: ", matrice_prodotto)

    return matrice_prodotto

def CalcolaDevStdPortafoglio():

    # array_portafoglio = []      #lista da inserire per creare la matrice var-cov
    # for i in range(len(list(GLOBE.societa.keys()))):

    #     array_portafoglio.append(list(GLOBE.societa.keys())[i])
    
    matrice_cov = CreaMatriceCov()

    vettore_pesi = np.array([VettorePesi()])

    var_portafoglio = MatriceProdotto(vettore_pesi, MatriceProdotto(matrice_cov, TrasponiMatrice(vettore_pesi)))

    dev_std_portafoglio = np.sqrt(var_portafoglio)

    # print("La dev-std di portafoglio è: ", dev_std_portafoglio)

    return dev_std_portafoglio

def RendimentoAttesoPortafoglio():

    pesi = np.array([VettorePesi()])

    lista_portafoglio_return_avg = []
    for i in GLOBE.societa.values():
        
        lista_portafoglio_return = DeltaChangeAvg(i.get("daily_adj"), "Close")
        lista_portafoglio_return_avg.append(lista_portafoglio_return)

    rendimento_atteso = MatriceProdotto(pesi, TrasponiMatrice(np.array([lista_portafoglio_return_avg])))
    # print("Il rendimento atteso è:", rendimento_atteso)

    return rendimento_atteso

def RegressioneBetaPortafoglio(y_titolo_datafetch, x_index_datafetch):  #inserire i datafetch raw

    if isinstance(y_titolo_datafetch, int):    
        
        return 0
    # dfindex = CALLAPI.BEESCALLER().ApiIndexCallPortafoglio(x_indice_symbol)  #call all'indice

    df_return = DeltaChange(y_titolo_datafetch, "Close")
    dfindex_return = DeltaChange(x_index_datafetch, "Close")

    X = dfindex_return
    X = sm.add_constant(X)

    Y = df_return
    model = sm.OLS(Y, X).fit()
    # prediction = model.predict(X)
    # print_model = model.summary()
    # print(print_model)
    coeff = model.params

    return coeff[1] #ritorna il beta


def GetCurrency(array):   #restituisce la curency dell'datafetch inserito

    if isinstance(array, int):    
    
        return 0

    currency = array["Currency"].iloc[0]

    return currency

def MovingAvgCerca(symbol, periodo_dati):   #country e tipo bloccati
    

    mav = inv.moving_averages(name = symbol,  country = 'united states', product_type='stock', interval = periodo_dati)

    return mav