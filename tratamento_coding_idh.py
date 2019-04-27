# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:14:48 2019

@author: Eliana-DEV
"""

import pandas as pd
# Lê o csv:
idh_base = pd.read_csv('Human Development Index (HDI).csv', encoding = 'latin1',
                       sep =',', engine = 'python', delimiter=',', skiprows=1)
# Oderna os dados pelo index (opcional para o tratamento do enconding):
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


