# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:14:48 2019

@author: Eliana-DEV
"""

import pandas as pd
# Lê o csv:
idh_base = pd.read_csv('Human Development Index (HDI).csv', encoding = 'latin1',
                       sep =',', engine = 'python', delimiter=',', skiprows=1)
# Oderna os dados pelo index (opcional para o tratamento do enconding, mas obrigatório para gerar o novo csv):
idh_base = idh_base.sort_index()
# Retira as colunas vazias:
idh_base = idh_base.drop(["Unnamed: 3","Unnamed: 5", "Unnamed: 7",
                          "Unnamed: 9", "Unnamed: 11", "Unnamed: 13",
                          "Unnamed: 15", "Unnamed: 17", "Unnamed: 19",
                          "Unnamed: 21", "Unnamed: 23", "Unnamed: 25",
                          "Unnamed: 27","Unnamed: 29", "Unnamed: 31",
                          "Unnamed: 33", "Unnamed: 35", "Unnamed: 37",
                          "Unnamed: 39", "Unnamed: 41", "Unnamed: 43",
                          "Unnamed: 45", "Unnamed: 47", "Unnamed: 49",
                          "Unnamed: 51", "Unnamed: 53", "Unnamed: 55",
                          "Unnamed: 57"], axis=1)
# Trás o dataframe de anos e series de paises
idh_base_2000_a_2015, y = (idh_base.iloc[:,12:28], idh_base.iloc[:,1])
#recupera range dos anos
anos = idh_base_2000_a_2015.columns
anos =anos.tolist()#[0:28]
#recupera range de países
paises = y.tolist()
# Monta lista paises x ano:
lista_anos = []
lista_paises = []
for pais in paises:
    for ano in anos:
        lista_paises.append(pais)
        lista_anos.append(ano)
# Monta lista de IDH:
lista_idh = []
for linha in range(0, len(idh_base_2000_a_2015)):
    for coluna in range(0, len(anos)):
        lista_idh.append(idh_base_2000_a_2015.iloc[linha][coluna])
# Cria novo DataFrame:        
dataHDI = pd.DataFrame()
dataHDI["Country"] = lista_paises
dataHDI["year"] =lista_anos
dataHDI['hdi'] = lista_idh
# Exporta novo CSV:
dataHDI.to_csv('hdi_new.csv', sep=':', encoding='utf-8')
