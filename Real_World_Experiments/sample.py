# -*- coding: utf-8 -*-
"""
Created on Mon May  1 20:05:12 2023

@author: matti
"""

from Rules import RCV, Plurality, Borda, Harmonic_Borda, Copeland_Minimax, Plurality_Veto, Bucklin, Veto
from Ensembles import SUM, MPW
import pandas as pd
import numpy as np
import time
import os

#Rules = [RCV, Plurality, Borda, Harmonic_Borda, Copeland, Minimax, Veto, Bucklin]
rules = ['RCV', 'Plurality', 'Borda', 'Harmonic_Borda', 'Copeland', 'Minimax', 'Plurality_Veto', 'Bucklin', 'Veto']

path = 'debian/'
profile_path = path + 'complete/'
distances_path = path + 'distances/'
data_path = path + 'data/'
if (not os.path.exists(data_path)):
    os.mkdir(data_path)

pValues = [0.5, 1, 3, 5, 7, 10]

samples = 1000

if (not os.path.exists(data_path)):
    os.mkdir(data_path)

#start_time = time.time()
    
for p in pValues:
    save = data_path + '{}0/'.format(p)
    if (not os.path.exists(save)):
        os.mkdir(save)
        
    avg_acc_rcv = 0
    avg_acc_plurality = 0
    avg_acc_borda = 0
    avg_acc_harmonic = 0
    avg_acc_copeland = 0
    avg_acc_minimax = 0
    avg_acc_plurality_veto = 0
    avg_acc_bucklin = 0
    avg_acc_veto = 0
    avg_acc_sum = 0
    avg_acc_mpw = 0
    
    print('{}0 percent:'.format(p))
        
    num_elections = len(os.listdir(profile_path))
        
    for profile_name in os.listdir(profile_path):
            
        print("Profile: " + profile_name)
        votes = pd.read_csv(profile_path + profile_name)
        #votes = votes.iloc[:, 1:].astype('int')
        #votes -= 1
            
        num_alts = len(votes.iloc[0])
        num_voters = len(votes)
            
        alt_winner = RCV(num_alts, votes)
            
        correct_rcv = 0
        correct_plurality = 0
        correct_borda = 0
        correct_harmonic = 0
        correct_copeland = 0
        correct_minimax = 0
        correct_plurality_veto = 0
        correct_bucklin =0
        correct_veto = 0
        correct_sum = 0
        correct_mpw = 0
        
        for k in range(samples):
            s = np.random.choice(num_voters, size=int((num_voters * p) / 10), replace=False)
            svotes = votes.iloc[s]
                            
            w_rcv = RCV(num_alts, svotes)
            w_plurality = Plurality(num_alts, svotes)
            w_borda = Borda(num_alts, svotes)
            w_harmonic = Harmonic_Borda(num_alts, svotes)
            w_copeland, w_minimax = Copeland_Minimax(num_alts, svotes)
            w_plurality_veto = Plurality_Veto(num_alts, svotes)
            w_bucklin = Bucklin(num_alts, svotes)
            w_veto = Veto(num_alts, svotes)
            w_sum = SUM(w_rcv, w_plurality, w_borda, w_harmonic, w_copeland, w_minimax, w_plurality_veto, w_bucklin, w_veto,
                        distances_path + profile_name, p, num_alts)
            w_mpw = MPW(w_rcv, w_plurality, w_borda, w_harmonic, w_copeland, w_minimax, w_plurality_veto, w_bucklin, w_veto,
                        distances_path + profile_name, p)
                
            if (w_rcv == alt_winner):
                correct_rcv += 1
            if (w_plurality == alt_winner):
                correct_plurality += 1
            if (w_borda == alt_winner):
                correct_borda += 1
            if (w_harmonic == alt_winner):
                correct_harmonic += 1
            if (w_copeland == alt_winner):
                correct_copeland += 1
            if (w_minimax == alt_winner):
                correct_minimax += 1
            if (w_plurality_veto == alt_winner):
                correct_plurality_veto += 1
            if (w_bucklin == alt_winner):
                correct_bucklin += 1
            if (w_veto == alt_winner):
                correct_veto += 1
            if (w_sum == alt_winner):
                correct_sum += 1
            if (w_mpw == alt_winner):
                correct_mpw += 1
                    
        with open(save + 'RCV.txt', 'a') as f:
            f.write('{}, {}\n'.format(profile_name, (correct_rcv / samples)))
        with open(save + 'Plurality.txt', 'a') as f:
            f.write('{}, {}\n'.format(profile_name, (correct_plurality / samples)))
        with open(save + 'Borda.txt', 'a') as f:
            f.write('{}, {}\n'.format(profile_name, (correct_borda / samples)))
        with open(save + 'Harmonic_Borda.txt', 'a') as f:
            f.write('{}, {}\n'.format(profile_name, (correct_harmonic / samples)))
        with open(save + 'Copeland.txt', 'a') as f:
            f.write('{}, {}\n'.format(profile_name, (correct_copeland / samples)))
        with open(save + 'Minimax.txt', 'a') as f:
            f.write('{}, {}\n'.format(profile_name, (correct_minimax / samples)))
        with open(save + 'Plurality_Veto.txt', 'a') as f:
            f.write('{}, {}\n'.format(profile_name, (correct_plurality_veto / samples)))
        with open(save + 'Bucklin.txt', 'a') as f:
            f.write('{}, {}\n'.format(profile_name, (correct_bucklin / samples)))
        with open(save + 'Veto.txt', 'a') as f:
            f.write('{}, {}\n'.format(profile_name, (correct_veto / samples)))
        with open(save + 'SUM.txt', 'a') as f:
            f.write('{}, {}\n'.format(profile_name, (correct_sum / samples)))
        with open(save + 'MPW.txt', 'a') as f:
            f.write('{}, {}\n'.format(profile_name, (correct_mpw / samples)))
                
        avg_acc_rcv += correct_rcv / samples
        avg_acc_plurality += correct_plurality / samples
        avg_acc_borda += correct_borda / samples
        avg_acc_harmonic += correct_harmonic / samples
        avg_acc_copeland += correct_copeland / samples
        avg_acc_minimax += correct_minimax / samples
        avg_acc_plurality_veto += correct_plurality_veto / samples
        avg_acc_bucklin += correct_bucklin / samples
        avg_acc_veto += correct_veto / samples
        avg_acc_sum += correct_sum / samples
        avg_acc_mpw += correct_mpw / samples
            
    avg_acc_rcv /= num_elections
    print('Average accuracy RCV: {:.4f}'.format(avg_acc_rcv))
    avg_acc_plurality /= num_elections
    print('Average accuracy Plurality: {:.4f}'.format(avg_acc_plurality))
    avg_acc_borda /= num_elections
    print('Average accuracy Borda: {:.4f}'.format(avg_acc_borda))
    avg_acc_harmonic /= num_elections
    print('Average accuracy Harmonic Borda: {:.4f}'.format(avg_acc_harmonic))
    avg_acc_copeland /= num_elections
    print('Average accuracy Copeland: {:.4f}'.format(avg_acc_copeland))
    avg_acc_minimax /= num_elections
    print('Average accuracy Minimax: {:.4f}'.format(avg_acc_minimax))
    avg_acc_plurality_veto /= num_elections
    print('Average accuracy Plurality Veto: {:.4f}'.format(avg_acc_plurality_veto))
    avg_acc_bucklin /= num_elections
    print('Average accuracy Bucklin: {:.4f}'.format(avg_acc_bucklin))
    avg_acc_veto /= num_elections
    print('Average accuracy Veto: {:.4f}'.format(avg_acc_veto))
    avg_acc_sum /= num_elections
    print('Average accuracy SUM: {:.4f}'.format(avg_acc_sum))
    avg_acc_mpw /= num_elections
    print('Average accuracy MPW: {:.4f}'.format(avg_acc_mpw))
        
    with open(save + 'RCV.txt', 'a') as f:
        f.write('{}'.format(avg_acc_rcv))
    with open(save + 'Plurality.txt', 'a') as f:
        f.write('{}\n'.format(avg_acc_plurality))
    with open(save + 'Borda.txt', 'a') as f:
        f.write('{}\n'.format(avg_acc_borda))
    with open(save + 'Harmonic_Borda.txt', 'a') as f:
        f.write('{}\n'.format(avg_acc_harmonic))
    with open(save + 'Copeland.txt', 'a') as f:
        f.write('{}\n'.format(avg_acc_copeland))
    with open(save + 'Minimax.txt', 'a') as f:
        f.write('{}\n'.format(avg_acc_minimax))
    with open(save + 'Plurality_Veto.txt', 'a') as f:
        f.write('{}\n'.format(avg_acc_plurality_veto))
    with open(save + 'Bucklin.txt', 'a') as f:
        f.write('{}\n'.format(avg_acc_bucklin))
    with open(save + 'Veto.txt', 'a') as f:
        f.write('{}\n'.format(avg_acc_veto))
    with open(save + 'SUM.txt', 'a') as f:
        f.write('{}\n'.format(avg_acc_sum))
    with open(save + 'MPW.txt', 'a') as f:
        f.write('{}\n'.format(avg_acc_mpw))
    
    print()
        
#print()    
#print('Runtime: ' + str(time.time() - start_time))
# 50 samples: 14845.760975122452 s