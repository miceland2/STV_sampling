#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 20:33:41 2024

@author: miceland
"""

import pandas as pd
import numpy as np
import os
import heapq
from random import randrange
import math


def min_tie(alts):
    """
    Randomly choose and return the index of one of the alternatives with the 
    least points
    
    """
    
    indexes = np.where(alts == alts.min())[0]
    ind = randrange(0, len(indexes))
    return alts.index[indexes[ind]]

def RCV_mov(num_alts, data):
    
    data = data + 1
        
    inds = [i for i in range(1, num_alts + 1)]
    alt_winner = None
    r = 0
    alts_len = num_alts
    
    LB_candidates = []
    UB_candidates = []
    
    majority_threshold = math.ceil(len(data) / 2)
    
    while(r < (num_alts - 1)):
        alts = pd.Series(np.zeros(num_alts - r), dtype=int, index=[i for i in range(1, num_alts - r + 1)])
        alts.index = inds
        
        for i in inds:
            alts[i] = len(data[data.iloc[:, 0] == i])
            
        bottom2 = heapq.nsmallest(2, alts.values)
        LB_candidates.append(math.ceil(abs(bottom2[0] - bottom2[1]) / 2))
        
        top2 = heapq.nlargest(2, alts.values)
        second = min(top2)
        UB_candidates.append(majority_threshold - second)
        
        #for i in list(alts.index):
        #    if (alts[i] > alts.sum() - alts[i]):
        #        
        #        top2 = heapq.nlargest(2, alts.values)
        #        UB_candidates.append(abs(top2[0] - top2[1]))
        #        
        #         If an alternative achieved a majority
        #         alt_winner = i
        #         return alt_winner - 1, LB, UB
        
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
    LB = min(LB_candidates) / len(data)
    UB = min(UB_candidates) / len(data)
    
    return None, LB, UB

path = 'NYC_Democratic_Council/complete/'
print(path)
profiles = os.listdir(path)
if ('.DS_Store' in profiles):
    profiles.remove('.DS_Store')
    
with open(path[0:-9] + 'mov.txt', 'w') as f:
    for profile in profiles:
        
        votes = pd.read_csv(path + profile)
        num_alts = len(votes.iloc[0])
        
        _, LB, UB = RCV_mov(num_alts, votes)
        
        f.write('{}, {}, {}\n'.format(profile, LB, UB))