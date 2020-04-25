
import numpy as np
import statsmodels.api as sm
import investpy as inv

import globalita as GLOBE
import API_call as CALLAPI


def DeltaChange(dataframe, column_type):    #calcola i change moltiplicati * 100

    colonna = dataframe.get("datafetch")[column_type]

    delta = colonna.pct_change() * 100

    # print(delta, "\n\n\n")

    return delta.dropna()

def DeltaChangeAvg(dataframe, column_type): #calcola media change

    colonna = dataframe.get("datafetch")[column_type]

    delta = colonna.pct_change().dropna()

    avg_delta = delta.mean() * 100

    # print(avg_delta, "\n\n\n")
    
    return avg_delta

# def DeltaStd(array, column_type):  #calcola std di una colonna

#     colonna = array[column_type]

#     std_delta = colonna.std()    

#     # print(std_delta, "\n\n\n")

#     return std_delta

def DeltaChangeStd(dataframe, column_type): #calcola std su change colonna

    colonna = dataframe.get("datafetch")[column_type]

    delta = colonna.pct_change().dropna()

    std_delta = delta.std()
    
    return std_delta

def CalcoloChange(dataframe, prezzo_riferimento_t0):  #restituisce il change dall'acquisto * 100

    if isinstance(dataframe, int):    
        
        return 0
    
    else:
        
        tempo1 = dataframe.get("datafetch")["Close"].iloc[-1]
        # tempo0 = array[colonna].iloc[-2]

        change = (tempo1 - prezzo_riferimento_t0) / prezzo_riferimento_t0 * 100  

        return round(change, 2)

def TotaleInvestimento():

    totale = 0

    for i in GLOBE.titolo.values():

        totale_parziale =i.get("totale_ordine")

        totale = totale + totale_parziale

    return totale

def TotaleInvestimentoNoFund():

    totale_no_fund = 0

    for i in GLOBE.titolo.values():

        if i.get("tipo_strumento") != "fund":

            totale_parziale = i.get("totale_ordine")
            
            totale_no_fund = totale_no_fund + totale_parziale
            # print("Totale è: ", totale_no_fund)

    return totale_no_fund

def CreaMatriceCov():      #array di tipo lista, portafoglio[aapl, aal, msft, ecc]

    lista_portafoglio_dropped = []
    for i in GLOBE.titolo.values():
        
        lista_portafoglio_dropped.append(DeltaChange(i.get("dataframe"), "Close"))

    matrice_cov = np.cov(lista_portafoglio_dropped)
    # print("La matrice covarianza del portafoglio: ", matrice_cov)
    # print("shape matrice: ", np.shape(matrice_cov))

    return matrice_cov

def CreaMatriceCovNoFund():      #array di tipo lista, portafoglio[aapl, aal, msft, ecc]

    lista_portafoglio_dropped = []
    for i in GLOBE.titolo.values():
        
        if i.get("tipo_strumento") != "fund":

            lista_portafoglio_dropped.append(DeltaChange(i.get("dataframe"), "Close"))

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
 
    key_titolo = list(GLOBE.titolo.keys())
    totale_investimento = TotaleInvestimento()
    vettore_pesi = []
    for i in range(len(key_titolo)):

        peso_titolo = GLOBE.titolo.get(key_titolo[i]).get("totale_ordine") / totale_investimento
        vettore_pesi.append(peso_titolo)

    # print("Il vettore pesi è: ", vettore_pesi)

    return vettore_pesi

def VettorePesiNoFund():
    
    totale_investimento_no_fund = TotaleInvestimentoNoFund()
    vettore_pesi_no_fund = []
    for i in GLOBE.titolo.values():

        if i.get("tipo_strumento") != "fund":

            peso_titolo = i.get("totale_ordine") / totale_investimento_no_fund
            vettore_pesi_no_fund.append(peso_titolo)

    # print("Il vettore pesi è: ", vettore_pesi_no_fund)

    return vettore_pesi_no_fund

def MatriceProdotto(matriceA, matriceB):

    matrice_prodotto = np.dot(matriceA, matriceB)
    # print("Matrice prodotto: ", matrice_prodotto)

    return matrice_prodotto

def CalcolaDevStdPortafoglio():

    matrice_cov = CreaMatriceCov()

    vettore_pesi = np.array(VettorePesi())

    var_portafoglio = MatriceProdotto(vettore_pesi, MatriceProdotto(matrice_cov, TrasponiMatrice(vettore_pesi)))

    dev_std_portafoglio = np.sqrt(var_portafoglio)

    # print("La dev-std di portafoglio è: ", dev_std_portafoglio)

    return dev_std_portafoglio

def RendimentoAttesoPortafoglio():

    pesi = np.array(VettorePesi())

    lista_portafoglio_return_avg = []
    for i in GLOBE.titolo.values():
        
        lista_portafoglio_return = DeltaChangeAvg(i.get("dataframe"), "Close")
        lista_portafoglio_return_avg.append(lista_portafoglio_return)

    rendimento_atteso = MatriceProdotto(pesi, TrasponiMatrice(np.array(lista_portafoglio_return_avg)))
    # print("Il rendimento atteso è:", rendimento_atteso)

    return rendimento_atteso

def BetaPortafoglio():

    if not GLOBE.titolo:
        
        return 0

    pesi = np.array(VettorePesiNoFund())

    lista_portafoglio_beta = []
    for i in GLOBE.titolo.values():

        if i.get("tipo_strumento") != "fund":
            
            lista_portafoglio_beta.append(i.get("beta"))
            

    beta_portafoglio = MatriceProdotto(pesi, TrasponiMatrice(np.array(lista_portafoglio_beta)))

    return beta_portafoglio

# def RegressioneBetaPortafoglio(y_titolo_datafetch, x_index_datafetch):  #inserire i datafetch raw

#     if isinstance(y_titolo_datafetch, int):    
        
#         return 0

#     df_return = DeltaChange(y_titolo_datafetch, "Close")
#     dfindex_return = DeltaChange(x_index_datafetch, "Close")

#     X = dfindex_return
#     X = sm.add_constant(X)

#     Y = df_return
#     model = sm.OLS(Y, X).fit()
#     # prediction = model.predict(X)
#     # print_model = model.summary()
#     # print(print_model)
#     coeff = model.params

#     return coeff[1] #ritorna il beta

def GetCurrencyFromInfoGen(dataframe):   #restituisce la curency dell'datafetch inserito

    if isinstance(dataframe, int):    
    
        return 0

    currency = dataframe.get("info_gen")["currency"].values[0]

    return currency

def GetItemFromInfoTech(dataframe, tipo_strumento, column):   #restituisce la colonna derivante dal datfetch

    if isinstance(dataframe, int):    
    
        return 0

    if tipo_strumento == GLOBE.mappa_strumenti.get("fund") and column == "Beta":
        
        column_item = dataframe.get("info_tech")["Risk Rating"].values[0]

    else:    
        column_item = dataframe.get("info_tech")[column].values[0]

    return column_item

def MovingAvgCerca(dataframe, tipo_strumento, periodizzazione):   #country e tipo bloccati

    if tipo_strumento == GLOBE.mappa_strumenti.get("stock"):    #primo parametro simbolo
        
        mav = inv.moving_averages(name = dataframe.get("info_gen")["symbol"].values[0], country = dataframe.get("info_gen")["country"].values[0], product_type = tipo_strumento, interval = periodizzazione.lower())
        return mav

    else:

        mav = inv.moving_averages(name = dataframe.get("info_gen")["name"].values[0], country = dataframe.get("info_gen")["country"].values[0], product_type = tipo_strumento, interval = periodizzazione.lower())
        return mav

def RoundCalcolo(variabile, stato):

    if stato == True:

        rounded = round(variabile, 2)

        return rounded

    else:

        return variabile