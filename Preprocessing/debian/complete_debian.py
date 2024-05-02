# -*- coding: utf-8 -*-
"""
Created on Tue May  2 10:12:11 2023

@author: matti
"""

import math
import pandas as pd
import random


path = 'preprocessed/'

no = 8
file = '00002-0000000{}-comma.soi'.format(no)
 
num_alts = 8   
df = pd.read_csv(file, skiprows=(num_alts + 12), names = [i for i in range(15)])

data = pd.DataFrame()

cnt = 0
for i in range(len(df)):
    for j in range(int(df.iloc[i, 0])):
        data = data.append(df.iloc[i, 1:])
        
data = data.iloc[:, 0: num_alts]

data_new = data.copy()

def next(row, pos):        
    search = list(data_new.iloc[row, :pos])
    
    floats = (data.iloc[:, pos] == data.iloc[:, pos])
    no_nan = data[floats]
    
    for i in range(len(search)):
        b = no_nan.iloc[:, i] == search[i]
        no_nan = no_nan[b]
    
    #
    #for i in range(len(data)):
    #    if (search == list(data.iloc[i, :pos])):
    #        if (not (math.isnan(data.iloc[i, pos]))):
    #            select.append(list(data.iloc[i]))
    #
                
                
    candidates = no_nan.iloc[:, pos]
    candidates = list(candidates)
    
    if (len(candidates) == 0):
        return None
    
    alt = random.choice(candidates)
            
    return alt

# main loop

for row in range(len(data_new)):
    for col in range(1, num_alts):
        if (math.isnan(data.iloc[row, col])):
            new = next(row, col)
            data_new.iloc[row, col] = new


for row in range(len(data_new)):
    alts = {i for i in range(1, num_alts + 1)}
    for col in range(num_alts):
        if (math.isnan(data_new.iloc[row, col])):
            alt = random.choice(list(alts))
            alts = alts - {alt}
            data_new.iloc[row, col] = alt
        else:
            alts = alts - {data_new.iloc[row, col]}
            
data_new.to_csv('{}_complete.csv'.format(file[0:-10]))