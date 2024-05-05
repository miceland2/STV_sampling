#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 14:54:56 2023

@author: miceland
"""

import pandas as pd
import numpy as np
import random
import os
import argparse
from Rules import RCV, Plurality, Borda, Harmonic_Borda, Copeland_Minimax, Plurality_Veto, Bucklin, Veto


parser = argparse.ArgumentParser(description='Real Election Sampling')

parser.add_argument('-a', '--num_alts', default=5, type=int,
                    help='number of elections (default: 10)')
parser.add_argument('-v', '--num_voters', default=100, type=int,
                    help='number of voters (default: 100)')
parser.add_argument('-s', '--num_samples', default=100, type=int,
                    help='number of samples (default: 50)')

parser.add_argument('-p', '--file_path', default='profiles', type=str,
                    help='file path with csv profiles (default: profiles)')

args = parser.parse_args()

path = args.file_path + '/'
models = os.listdir(args.file_path)

num_alts = args.num_alts
num_voters = args.num_voters
samples = args.num_samples
eps = 0.001

rule_names = ['R', 'P', 'B', 'H', 'C', 'M', 'V', 'b', 'v']

def weighted_select(weights):
    
    weight_total = sum(weights)
    rand_number = random.random() * weight_total
    
    offset = 0
    for idx in weights.index:
        if (rand_number >= offset and rand_number <= (offset + weights[idx])):
            return idx
        offset += weights[idx]
        
    # error
    return None

for model in models:
    #total_mat =[[x for x in range(6)]]
    
    print(model)
    
    for p in [0.5]:
        
        mat = []
        mat.append(['', 'R', 'P', 'B', 'H', 'C', 'M', 'V', 'b', 'v'])
        
        profiles = os.listdir(path + model)
        
        weights = pd.Series(np.ones(9), index=rule_names)
        
        for i, target_rule in enumerate([RCV]):
            row = list(rule_names[i])
            
            for profile in profiles:
                votes = pd.read_csv(path + model + '/' + profile)
                    
                alt_winner = target_rule(num_alts, votes)
                
                for k in range(samples):
                    s = np.random.choice(num_voters, size=int((num_voters * p) / 10), replace=False)
                    svotes = votes.iloc[s]
                    
                    winner_rcv = RCV(num_alts, svotes)
                    winner_plurality = Plurality(num_alts, svotes)
                    winner_borda = Borda(num_alts, svotes)
                    winner_harmonic = Harmonic_Borda(num_alts, svotes)
                    winner_copeland, winner_minimax = Copeland_Minimax(num_alts, svotes)
                    winner_plurality_veto = Plurality_Veto(num_alts, svotes)
                    winner_bucklin = Bucklin(num_alts, svotes)
                    winner_veto = Veto(num_alts, svotes)
                    
                    strToWinner = {
                        'R' : winner_rcv,
                        'P' : winner_plurality,
                        'B' : winner_borda,
                        'H' : winner_harmonic,
                        'C' : winner_copeland,
                        'M' : winner_minimax,
                        'V' : winner_plurality_veto,
                        'b' : winner_bucklin,
                        'v' : winner_veto
                    }
                    
                    chosen_winner = strToWinner[weighted_select(weights)]
                    
                    if (chosen_winner == alt_winner):
                        if (chosen_winner == winner_rcv):
                            weights['R'] *= ((1 + eps) ** 1)
                        else:
                            weights['R'] *= ((1 - eps) ** 1)
                            
                        if (chosen_winner == winner_plurality):
                            weights['P'] *= ((1 + eps) ** 1)
                        else:
                            weights['P'] *= ((1 - eps) ** 1)
                            
                        if (chosen_winner == winner_borda):
                            weights['B'] *= ((1 + eps) ** 1)
                        else:
                            weights['B'] *= ((1 - eps) ** 1)
                            
                        if (chosen_winner == winner_harmonic):
                            weights['H'] *= ((1 + eps) ** 1)
                        else:
                            weights['H'] *= ((1 - eps) ** 1)
                            
                        if (chosen_winner == winner_copeland):
                            weights['C'] *= ((1 + eps) ** 1)
                        else:
                            weights['C'] *= ((1 - eps) ** 1)
                            
                        if (chosen_winner == winner_minimax):
                            weights['M'] *= ((1 + eps) ** 1)
                        else:
                            weights['M'] *= ((1 - eps) ** 1)
                            
                        if (chosen_winner == winner_plurality_veto):
                            weights['V'] *= ((1 + eps) ** 1)
                        else:
                            weights['V'] *= ((1 - eps) ** 1)
                            
                        if (chosen_winner == winner_bucklin):
                            weights['b'] *= ((1 + eps) ** 1)
                        else:
                            weights['b'] *= ((1 - eps) ** 1)
                            
                        if (chosen_winner == winner_veto):
                            weights['v'] *= ((1 + eps) ** 1)
                        else:
                            weights['v'] *= ((1 - eps) ** 1)
                    
                    if (chosen_winner != alt_winner):
                        if (chosen_winner == winner_rcv):
                            weights['R'] *= ((1 - eps) ** 1)
                            
                        if (chosen_winner == winner_plurality):
                            weights['P'] *= ((1 - eps) ** 1)
                            
                        if (chosen_winner == winner_borda):
                            weights['B'] *= ((1 - eps) ** 1)
                            
                        if (chosen_winner == winner_harmonic):
                            weights['H'] *= ((1 - eps) ** 1)
                            
                        if (chosen_winner == winner_copeland):
                            weights['C'] *= ((1 - eps) ** 1)
                            
                        if (chosen_winner == winner_minimax):
                            weights['M'] *= ((1 - eps) ** 1)
                            
                        if (chosen_winner == winner_plurality_veto):
                            weights['V'] *= ((1 - eps) ** 1)
                            
                        if (chosen_winner == winner_bucklin):
                            weights['b'] *= ((1 - eps) ** 1)
                            
                        if (chosen_winner == winner_veto):
                            weights['v'] *= ((1 - eps) ** 1)
                            
                        # normalize
                        #weight_total = sum(weights)
                        #weights /= weight_total
                            
            row.append(weights['R'])
            row.append(weights['P'])
            row.append(weights['B'])
            row.append(weights['H'])
            row.append(weights['C'])
            row.append(weights['M'])
            row.append(weights['V'])
            row.append(weights['b'])
            row.append(weights['v'])
            
            mat.append(row)
            mat = np.array(mat, dtype=object).transpose()
            
        if (not os.path.exists('MPW_{}0%'.format(p))):
            os.mkdir('MPW_{}0%'.format(p))
        pd.DataFrame(mat).to_csv('MPW_{}0%/{}.csv'.format(p, model), index=False)
                    