# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 22:41:26 2023

@author: matti
"""

import math
import pandas as pd
import random
import os

path = './'
if (not os.path.exists(path + 'complete')):
    os.mkdir(path + 'complete')

for file in os.listdir(path + 'preprocessed'):
    print(file)
    
    df = pd.read_csv(path + 'preprocessed/' + file)
    num_voters = len(df)
    num_alts = len(df.columns) - 1
    
    data = pd.read_csv(path + 'preprocessed/' + file, skiprows=num_alts + 2)
    data = data.iloc[:, 1:]
    data.columns = [x for x in range(1, num_alts + 1)]
    
    #data = pd.DataFrame()
    
    #cnt = 0
    #for i in range(len(df)):
    #    for j in range(df.iloc[i, 0]):
    #        data = data.append(df.iloc[i, 1:])
    #        
    #data = data.iloc[:, 0: num_alts]
    #
    data_new = data.copy()
    
    def next(row, pos):        
        search = list(data_new.iloc[row, :pos])
        
        floats = (data.iloc[:, pos] == data.iloc[:, pos])
        no_nan = data[floats]
        
        for i in range(len(search)):
            b = no_nan.iloc[:, i] == search[i]
            no_nan = no_nan[b]
        
        """
        for i in range(len(data)):
            if (search == list(data.iloc[i, :pos])):
                if (not (math.isnan(data.iloc[i, pos]))):
                    select.append(list(data.iloc[i]))
        """
                    
                    
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
        alts = {i for i in range(0, num_alts)}
        for col in range(num_alts):
            if (math.isnan(data_new.iloc[row, col])):
                alt = random.choice(list(alts))
                alts = alts - {alt}
                data_new.iloc[row, col] = alt
            else:
                alts = alts - {data_new.iloc[row, col]}
                
    data_new.to_csv(path + 'complete/' + file[0:-4] + '_complete.csv', index=False)
