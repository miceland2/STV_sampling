# -*- coding: utf-8 -*-
"""
Created on Mon May  1 20:05:49 2023

@author: matti
"""

import numpy as np
import pandas as pd
from random import randrange
import math


def max_tie(alts):
    """
    Randomly choose and return the index of one of the alternatives with the 
    most points
    
    """
    indexes = np.where(alts == alts.max())[0]
    ind = randrange(0, len(indexes))
    return alts.index[indexes[ind]]

def min_tie(alts):
    """
    Randomly choose and return the index of one of the alternatives with the 
    least points
    
    """
    
    indexes = np.where(alts == alts.min())[0]
    ind = randrange(0, len(indexes))
    return alts.index[indexes[ind]]

def RCV(num_alts, data):
    
    data = data + 1
        
    inds = [i for i in range(1, num_alts + 1)]
    alt_winner = None
    r = 0
    alts_len = num_alts
    
    while(r < (num_alts)):
        alts = pd.Series(np.zeros(num_alts - r), dtype=int, index=[i for i in range(1, num_alts - r + 1)])
        alts.index = inds
        
        for i in inds:
            alts[i] = len(data[data.iloc[:, 0] == i])
        
                
        for i in list(alts.index):
            if (alts[i] > alts.sum() - alts[i]):
                # If an alternative achieved a majority
                alt_winner = i
                return alt_winner
                
        alt_min = min_tie(alts)
        
        alts = alts.drop(alt_min)
        alts_len -= 1
        inds = alts.index
        alts.index = inds
        
        data.iloc[:, :] = data.iloc[:, :].replace(float(alt_min), np.nan)
        
        ind = pd.isna(data.iloc[:, 0])
        ind = data[ind].index
        sdata = data.loc[ind].shift(-1, axis=1)
        data.loc[ind] = sdata
        data = data[data.iloc[:, :].notnull().any(axis=1)]
        
        
        r += 1
        
    
    return alt_winner

def Borda(num_alts, votes):
    
    votes = votes + 1
    
    inds = [i for i in range(1, num_alts + 1)]
    
    
    alts = pd.Series(np.zeros(num_alts), dtype=int, index=[i for i in range(1, num_alts + 1)])
    alts.index = inds
    
    scores = pd.Series(dtype='float64')
    
    for i in range(num_alts):
        for j in range(1, num_alts + 1):
            scores = votes.shape[1] - (i + 1)
            alts[j] += scores * votes[votes.iloc[:, i] == float(j)].shape[0]
        
    winner = max_tie(alts)
    return (winner)

def Harmonic_Borda(num_alts, data):
    
    inds = [i for i in range(1, num_alts + 1)]
    
    data = data + 1
    
    alts = pd.Series(np.zeros(num_alts), dtype=int, index=[i for i in range(1, num_alts + 1)])
    alts.index = inds
    
    scores = pd.Series(dtype='float64')
    
    for i in range(num_alts):
        for j in range(1, num_alts + 1):
            scores = 1 / (i + 1)
            alts[j] += scores * data[data.iloc[:, i] == float(j)].shape[0]
        
    winner = max_tie(alts)
    return (winner)

def Plurality(num_alts, data):
    
    data = data + 1
    
    inds = [i for i in range(1, num_alts + 1)]
    
    alt_winner = None
    
    alts = pd.Series(np.zeros(num_alts), dtype=int, index=[i for i in range(1, num_alts + 1)])
    alts.index = inds
        
        
    for i in inds:
        alts[i] = len(data[data.iloc[:, 0] == i])
    
    return (max_tie(alts))

def Copeland(num_alts, data):
    
    inds = [i for i in range(1, num_alts + 1)]
    
    data = data + 1
    
    alts = pd.Series(np.zeros(num_alts), dtype=int, index=[i for i in range(1, num_alts + 1)])
    alts.index = inds
    
    alt_mat = np.zeros((num_alts, num_alts))
    
    for k in range(data.index.size):
    
        d_test = data.iloc[k]
                
        ranked = []
        cnt = 1
        for i in d_test:
            if (not(math.isnan(i))):
                ranked.append(i)
            if (math.isnan(i)):
                break
            else:
                for j in d_test[cnt:]:
                    if (math.isnan(j)):
                        break
                    alt_mat[int(i) - 1][int(j) - 1] += 1
            cnt+= 1
                
    for i in range(num_alts):
        for j in range(num_alts):
            if (alt_mat[i][j] > alt_mat[j][i]):
                alts[i + 1] += 1
            elif ((alt_mat[i][j] == alt_mat[j][i]) and (i != j)):
                alts[i + 1] += 0.5
                
    
                                
    winner = max_tie(alts)
    return(winner)