#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 17:38:48 2023

@author: miceland
"""

import numpy as np
import pandas as pd
from random import randrange, random


def max_tie(scores):
    """
    Randomly choose and return the index of one of the alternatives with the 
    most points
    
    """
    indexes = np.where(scores == scores.max())[0]
    ind = randrange(0, len(indexes))
    return indexes[ind]

def weighted_select(weights):
    
    weight_total = sum(weights)
    rand_number = random() * weight_total
    
    offset = 0
    for idx in weights.index:
        if (rand_number >= offset and rand_number <= (offset + weights[idx])):
            return idx
        offset += weights[idx]
        
    # error
    return None

def SUM(w_rcv, w_plurality, w_borda, w_harmonic, w_copeland, w_minimax, w_plurality_veto,
        w_bucklin, w_veto, path, percent, num_alts):
    
    path = path[0:-4]
    path += '_distances.txt'
    
    distances_df = pd.read_csv(path, names=[1, 2])
    
    closest_idx = np.where(distances_df.iloc[:, 1] == min(distances_df.iloc[:, 1]))[0][0]
    closest_culture = distances_df.iloc[closest_idx][1]
    
    weights_df = pd.read_csv('Weights/RCV_Accuracies/RCV_{}0%/{}.csv'.format(percent, closest_culture))
    weights_df = weights_df.iloc[1:, 1:]
    weights_df.index = ['R', 'P', 'B', 'H', 'C', 'M', 'V', 'b', 'v']
    
    weights = weights_df.to_dict()['1']
    
    scores = np.zeros(num_alts)
    
    scores[w_rcv] += float(weights['R'])
    scores[w_plurality] += float(weights['P'])
    scores[w_borda] += float(weights['B'])
    scores[w_harmonic] += float(weights['H'])
    scores[w_copeland] += float(weights['C'])
    scores[w_minimax] += float(weights['M'])
    scores[w_plurality_veto] += float(weights['V'])
    scores[w_bucklin] += float(weights['b'])
    scores[w_veto] += float(weights['v'])
        
    winner = max_tie(scores)
    return winner

def MPW(w_rcv, w_plurality, w_borda, w_harmonic, w_copeland, w_minimax, w_plurality_veto,
        w_bucklin, w_veto, path, percent):
    
    path = path[0:-4]
    path += '_distances.txt'
    
    distances_df = pd.read_csv(path, names=[1, 2])
    
    
    closest_idx = np.where(distances_df.iloc[:, 1] == min(distances_df.iloc[:, 1]))[0][0]
    closest_culture = distances_df.iloc[closest_idx][1]
    
    weights_df = pd.read_csv('Weights/Multiplicative_Weights/MPW_{}0%/{}.csv'.format(percent, closest_culture))
    weights_df = weights_df.iloc[1:, 1:]
    weights_df.index = ['R', 'P', 'B', 'H', 'C', 'M', 'V', 'b', 'v']
    
    weights = weights_df.to_dict()['1']
    weights_series = pd.Series(weights, index=['R', 'P', 'B', 'H', 'C', 'M', 'V', 'b', 'v'], dtype='float64')
    
    strToWinner = {
        'R' : w_rcv,
        'P' : w_plurality,
        'B' : w_borda,
        'H' : w_harmonic,
        'C' : w_copeland,
        'M' : w_minimax,
        'V' : w_plurality_veto,
        'b' : w_bucklin,
        'v' : w_veto
    }
    
    chosen_winner = strToWinner[weighted_select(weights_series)]
    return chosen_winner
