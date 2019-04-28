# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:14:48 2019

@author: Eliana-DEV
"""

import pandas as pd

def encoding(file_name_imp):
# Lê o csv:
    sep = ''
    base=pd.read_csv(file_name_imp, encoding = 'latin1',
                     sep =',', engine = 'python', delimiter=',', skiprows=1)
    file_name_exp = sep.join(file_name_imp.split('.')[:-1]).replace("'",'') + 'exit.csv'
    return base.to_csv(file_name_exp)
print('''
****************************************************************      
* Observação: Este script só faz conversão de arquivos .csv.   *
****************************************************************
''')
try:
    encoding(file_name_imp = input("Nome do arquivo: "))
except:
   print ("erro")