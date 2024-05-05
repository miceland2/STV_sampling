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
                return alt_winner - 1
                
        alt_min = min_tie(alts)
        
        alts = alts.drop(alt_min)
        alts_len -= 1
        inds = alts.index
        alts.index = inds
        
        data = data.replace(float(alt_min), np.nan)
        
        for i in range(num_alts - 1):
            ind = pd.isna(data.iloc[:, 0])
            ind = data[ind].index
            sdata = data.loc[ind].shift(-1, axis=1)
            data.loc[ind] = sdata
        #data = data[data.notnull().any(axis=1)]
                
        r += 1
    
    # error, alt_winner = None
    return None

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
    return winner - 1

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
    return winner - 1

def Plurality(num_alts, data):
    
    data = data + 1
    
    inds = [i for i in range(1, num_alts + 1)]
        
    alts = pd.Series(np.zeros(num_alts), dtype=int, index=[i for i in range(1, num_alts + 1)])
    alts.index = inds
        
        
    for i in inds:
        alts[i] = len(data[data.iloc[:, 0] == i])
    
    winner = max_tie(alts)
    return winner - 1

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
            cnt += 1
                
    for i in range(num_alts):
        for j in range(num_alts):
            if (alt_mat[i][j] > alt_mat[j][i]):
                alts[i + 1] += 1
            elif ((alt_mat[i][j] == alt_mat[j][i]) and (i != j)):
                alts[i + 1] += 0.5
                
    
                                
    winner = max_tie(alts)
    return winner - 1

def Minimax(num_alts, data):
    
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
            cnt += 1
    
    # now calculate minimax instead of copeland
    for alt in range(1, num_alts + 1):
        alts[alt] = np.max(alt_mat[:, alt - 1])
        
    winner = min_tie(alts)
    return winner - 1

def Copeland_Minimax(num_alts, data):
    
    inds = [i for i in range(1, num_alts + 1)]
    
    data = data + 1
    
    alts_copeland = pd.Series(np.zeros(num_alts), dtype=int, index=[i for i in range(1, num_alts + 1)])
    alts_minimax = pd.Series(np.zeros(num_alts), dtype=int, index=[i for i in range(1, num_alts + 1)])
    alts_copeland.index = inds
    alts_minimax.index = inds
    
    # calculate all pairwise victories
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
            cnt += 1
    
    # calculate copeland winner
    for i in range(num_alts):
        for j in range(num_alts):
            if (alt_mat[i][j] > alt_mat[j][i]):
                alts_copeland[i + 1] += 1
            elif ((alt_mat[i][j] == alt_mat[j][i]) and (i != j)):
                alts_copeland[i + 1] += 0.5
    winner_copeland = max_tie(alts_copeland)
    
    # calculate minimax winner
    for alt in range(1, num_alts + 1):
        alts_minimax[alt] = np.max(alt_mat[:, alt - 1])
    winner_minimax = min_tie(alts_minimax)
    
    return winner_copeland - 1, winner_minimax - 1

def Plurality_Veto(num_alts, data):
    
    inds = [i for i in range(1, num_alts + 1)]
    
    data = data + 1
    
    alts = pd.Series(np.zeros(num_alts), dtype=int, index=[i for i in range(1, num_alts + 1)])
    alts.index = inds
    
    alts_len = num_alts
    
    # count first-place votes
    for i in inds:
        alts[i] = len(data[data.iloc[:, 0] == i])
        
    # automatically eliminate alts with 0 1st place votes
    for i in inds:
        if (alts[i] == 0):
            alts = alts.drop(i)
            alts_len -= 1
            data = data.replace(float(i), np.nan)
        
    # begin n elimination rounds, random order
    rng = np.random.default_rng()
    perm = rng.permutation(data.index.size)
    for k in perm:
        
        if (alts_len == 1):
            winner = alts.index[0]
            return winner - 1
        
        vote = data.iloc[k]
        
        alt_last = np.nan
        for i in range(len(vote)):
            alt_last = vote[len(vote) - 1 - i]
            if (alt_last > 1):
                break
        
        alts[alt_last] -= 1
        
        if (alts[alt_last] == 0):
            
            alts = alts.drop(alt_last)
            alts_len -= 1
            #inds = alts.index
            
            data = data.replace(float(alt_last), np.nan)
            #data = data[data.iloc[:, :].notnull().any(axis=1)]
        
    # error
    return None

def Veto(num_alts, data):
    
    inds = [i for i in range(1, num_alts + 1)]
    
    data = data + 1
    
    alts = pd.Series(np.zeros(num_alts), dtype=int, index=[i for i in range(1, num_alts + 1)])
    alts.index = inds
    
    for i in inds:
        alts[i] =  - 1 * len(data[data.iloc[:, num_alts - 1] == i])
    
    winner = max_tie(alts)
    return winner - 1

def Bucklin(num_alts, data):
    
    inds = [i for i in range(1, num_alts + 1)]
    
    data = data + 1
    
    alts = pd.Series(np.zeros(num_alts), dtype=int, index=[i for i in range(1, num_alts + 1)])
    alts.index = inds
    
    for k in range(num_alts):
        
        # add k-place votes
        for i in inds:
            alts[i] += len(data[data.iloc[:, k] == i])
                        
        # check for majority
        majority_winners = []
        for i in inds:
            if (alts[i] > (len(data) / 2)):
                # If an alternative achived a majority
                majority_winners.append(i)
        if (len(majority_winners) > 0):
            winner_idx = randrange(0, len(majority_winners))
            winner = majority_winners[winner_idx]
            return winner - 1
    
    # error
    return None
