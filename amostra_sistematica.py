"""
Created on Tue Feb 19 00:38:02 2019

@author: paulo

CRIAR UMA AMOSTRA SISTEMÁTICA USANDO A TÉCNICA DO K, USANDO O CEIL PARA ARREDONDAMENTO

"""

import numpy as np
import pandas as pd
from math import ceil

populacao = 150
amostra = 15
k = ceil(populacao/amostra)

r = np.random.randint(low = 1, high = k + 1, size = 1)

acumulador = r[0]
sorteados = []
for i in range(amostra):
    sorteados.append(acumulador)
    acumulador += k

base = pd.read_csv("iris.csv")

base_final = base.loc[sorteados]
