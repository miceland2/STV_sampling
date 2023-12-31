# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 22:54:41 2023

@author: matti
"""

import os
from Rules import RCV, Plurality, Borda, Harmonic_Borda, Copeland
import pandas as pd
import numpy as np
import argparse


parser = argparse.ArgumentParser(description='Real Election Sampling')

parser.add_argument('-a', '--num_alts', default=10, type=int,
                    help='number of elections (default: 10)')
parser.add_argument('-v', '--num_voters', default=100, type=int,
                    help='number of voters (default: 100)')
parser.add_argument('-s', '--num_samples', default=50, type=int,
                    help='number of samples (default: 50)')

parser.add_argument('-p', '--file_path', default='profiles', type=str,
                    help='file path with csv profiles (default: profiles)')

args = parser.parse_args()

path = args.file_path + '/'
models = os.listdir(args.file_path)

num_alts = args.num_alts
num_voters = args.num_voters
samples = args.num_samples

Rules = [RCV, Plurality, Borda, Harmonic_Borda, Copeland]
rule_names = ['R', 'P', 'B', 'H', 'C']

for model in models:
    total_mat =[[x for x in range(6)]]
    
    print(model)
    
    for p in range(1, 11):
        
        
        mat = []
        mat.append(['', 'R', 'P', 'B', 'H', 'C'])
        
        profiles = os.listdir(path + model)
        
        for i, target_rule in enumerate(Rules):
            row = list(rule_names[i])
                
            for j, sample_rule in enumerate(Rules):
                correct = 0
                    
                for profile in profiles:
                    votes = pd.read_csv(path + model + '/' + profile)
                        
                    alt_winner = target_rule(num_alts, votes)
                                            
                    for k in range(samples):
                        s = np.random.choice(num_voters, size=int((num_voters/10)*p), replace=False)
                        svotes = votes.iloc[s]
                        s_winner = None
                                
                        s_winner = sample_rule(num_alts, svotes)
                
                        if (s_winner == alt_winner):
                            correct += 1
                                
                row.append(str(correct / (len(profiles) * samples)))
            
            mat.append(row)
            
        mat = np.array(mat, dtype=object).transpose()
        #total_mat = np.append(total_mat, mat, axis=0)
        #total_mat = np.append(total_mat,[['', '', '', '', '' , '']], axis=0)
                                  
            
        pd.DataFrame(mat).to_csv('Matrix_{}0%/{}.csv'.format(p, model), index=False)
        
