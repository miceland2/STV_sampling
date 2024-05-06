# -*- coding: utf-8 -*-
"""
Created on Tue May 16 10:38:54 2023

@author: matti
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
import os


path = 'NYC_Democratic_Council/'
data_path = path + 'data/'
plots_path = path + 'plots/'
distances_path = path + 'distances/'
average_plot_name = 'NYC Democratic Council Average'

if (not os.path.exists(plots_path)):
    os.mkdir(plots_path)

profiles = os.listdir(path + 'complete/')
if ('.DS_Store' in profiles):
    profiles.remove('.DS_Store')

num_elections = len(profiles)

percents = [0.5, 1, 3, 5, 7, 10]

index = ['R', 'P', 'Bo', 'H', 'C', 'M', 'Bu', 'PV', 'V', 'SUM', 'MPW']

avg_accs = pd.DataFrame(np.zeros([len(percents), len(index)]), columns=index)

for election_no in range(num_elections):
        
    profile_name = pd.read_csv(data_path + '{}0/RCV.txt'.format(percents[0]), names=[0, 1]).iloc[election_no][0][0:-4]
    
    distances_name = profile_name + '_distances.txt'
    distances_df = pd.read_csv(distances_path + distances_name, names=[1, 2])
    closest_idx = np.where(distances_df.iloc[:, 1] == min(distances_df.iloc[:, 1]))[0][0]
    closest_culture = distances_df.iloc[closest_idx][1]
    closest_distance = distances_df.iloc[closest_idx][2]
    closest_distance = '{:.3e}'.format(closest_distance)
    
    mov_df = pd.read_csv(path + 'mov.txt', names=[1, 2, 3])
    mov_idx = np.where(mov_df.iloc[:, 0] == profile_name + '.csv')[0][0]
    LB1 = mov_df.iloc[mov_idx][2]
    LB1 = '{:.3e}'.format(LB1)
    UB1 = mov_df.iloc[mov_idx][3]
    UB1 = '{:.3e}'.format(UB1)
    
    accs_rcv = []
    for i in range (len(percents)):
        r = pd.read_csv(data_path + '{}0/RCV.txt'.format(percents[i]), names=[0, 1]).iloc[election_no][1] * 100
        accs_rcv.append(r)
        avg_accs['R'][i] += r
    
    accs_plurality = []
    for i in range (len(percents)):
        p = pd.read_csv(data_path + '{}0/Plurality.txt'.format(percents[i]), names=[0, 1]).iloc[election_no][1] * 100
        accs_plurality.append(p)
        avg_accs['P'][i] += p
        
    accs_borda = []
    for i in range (len(percents)):
        bo = pd.read_csv(data_path + '{}0/Borda.txt'.format(percents[i]), names=[0, 1]).iloc[election_no][1] * 100
        accs_borda.append(bo)
        avg_accs['Bo'][i] += bo
        
    accs_harmonic = []
    for i in range (len(percents)):
        h = pd.read_csv(data_path + '{}0/Harmonic_Borda.txt'.format(percents[i]), names=[0, 1]).iloc[election_no][1] * 100
        accs_harmonic.append(h)
        avg_accs['H'][i] += h
        
    accs_copeland = []
    for i in range (len(percents)):
        c = pd.read_csv(data_path + '{}0/Copeland.txt'.format(percents[i]), names=[0, 1]).iloc[election_no][1] * 100
        accs_copeland.append(c)
        avg_accs['C'][i] += c
        
    accs_minimax = []
    for i in range (len(percents)):
        m = pd.read_csv(data_path + '{}0/Minimax.txt'.format(percents[i]), names=[0, 1]).iloc[election_no][1] * 100
        accs_minimax.append(m)
        avg_accs['M'][i] += m
        
    accs_bucklin = []
    for i in range (len(percents)):
        bu = pd.read_csv(data_path + '{}0/Bucklin.txt'.format(percents[i]), names=[0, 1]).iloc[election_no][1] * 100
        accs_bucklin.append(bu)
        avg_accs['Bu'][i] += bu
        
    accs_plurality_veto = []
    for i in range (len(percents)):
        pv = pd.read_csv(data_path + '{}0/Plurality_Veto.txt'.format(percents[i]), names=[0, 1]).iloc[election_no][1] * 100
        accs_plurality_veto.append(pv)
        avg_accs['PV'][i] += pv
        
    accs_veto = []
    for i in range (len(percents)):
        v = pd.read_csv(data_path + '{}0/Veto.txt'.format(percents[i]), names=[0, 1]).iloc[election_no][1] * 100
        accs_veto.append(v)
        avg_accs['V'][i] += v
        
    accs_sum = []
    for i in range (len(percents)):
        s = pd.read_csv(data_path + '{}0/SUM.txt'.format(percents[i]), names=[0, 1]).iloc[election_no][1] * 100
        accs_sum.append(s)
        avg_accs['SUM'][i] += s
        
    accs_mpw = []
    for i in range (len(percents)):
        mpw = pd.read_csv(data_path + '{}0/MPW.txt'.format(percents[i]), names=[0, 1]).iloc[election_no][1] * 100
        accs_mpw.append(mpw)
        avg_accs['MPW'][i] += mpw
        
    caption = r'{}, EMD={}    {}$\leq$MoV$\leq${}'.format(closest_culture.upper(), closest_distance, LB1, UB1)
        
    plt.title(profile_name)
    plt.xlabel(caption)
    plt.ylim(-5, 105)
    
    plt.style.use('seaborn-v0_8-whitegrid')
    
    percents_array = np.array(percents)
    percents_array *= 10
    
    plt.scatter(percents_array, accs_plurality, marker='o', label='Plurality', color='sienna')
    plt.scatter(percents_array, accs_borda, marker='v', label='Borda', color='darkred')
    plt.scatter(percents_array, accs_harmonic, marker='*', label='Harmonic', color='darkgoldenrod')
    plt.scatter(percents_array, accs_copeland, marker='d', label='Copeland', color='darkolivegreen')
    plt.scatter(percents_array, accs_minimax, marker='p', label='Minimax', color='forestgreen')
    plt.scatter(percents_array, accs_bucklin, marker='P', label='Bucklin', color='darkslategrey')
    plt.scatter(percents_array, accs_plurality_veto, marker='D', label='Pl. Veto', color='darkcyan')
    plt.scatter(percents_array, accs_veto, marker='^', label='Veto', color='navy')
    plt.scatter(percents_array, accs_sum, marker='X', label='SUM', color='indigo')
    plt.scatter(percents_array, accs_mpw, marker='+', label='MPW', color='darkmagenta')
    plt.scatter(percents_array, accs_rcv, marker='s', label='RCV', color='black')
    
    plt.plot(percents_array, accs_plurality, linestyle='dotted', color='sienna')
    plt.plot(percents_array, accs_borda, linestyle='dashed', color='darkred')
    plt.plot(percents_array, accs_harmonic, linestyle='dashdot', color='darkgoldenrod')
    plt.plot(percents_array, accs_copeland, linestyle=(0, (1, 10)), color='darkolivegreen')
    plt.plot(percents_array, accs_minimax, linestyle=(5, (10, 3)), color='forestgreen')
    plt.plot(percents_array, accs_bucklin, linestyle=(0, (5, 10)), color='darkslategrey')
    plt.plot(percents_array, accs_plurality_veto, linestyle=(0, (5, 1)), color='darkcyan')
    plt.plot(percents_array, accs_veto, linestyle=(0, (3, 10, 1, 10)), color='navy')
    plt.plot(percents_array, accs_sum, linestyle=(0, (3, 5, 1, 5)), color='indigo')
    plt.plot(percents_array, accs_mpw, linestyle=(0, (3, 1, 1, 1)), color='darkmagenta')
    plt.plot(percents_array, accs_rcv, linestyle='solid', color='black')
    plt.legend()
    
    plt.savefig(plots_path + profile_name + '.pdf')
    plt.show()
    
# plot average
plt.title(average_plot_name)

for idx in index:
    avg_accs[idx] /= num_elections
    
percents_array = np.array(percents)
percents_array *= 10

plt.ylim(-5, 105)

plt.scatter(percents_array, avg_accs['P'], marker='o', label='Plurality', color='sienna')
plt.scatter(percents_array, avg_accs['Bo'], marker='v', label='Borda', color='darkred')
plt.scatter(percents_array, avg_accs['H'], marker='*', label='Harmonic', color='darkgoldenrod')
plt.scatter(percents_array, avg_accs['C'], marker='d', label='Copeland', color='darkolivegreen')
plt.scatter(percents_array, avg_accs['M'], marker='p', label='Minimax', color='forestgreen')
plt.scatter(percents_array, avg_accs['Bu'], marker='P', label='Bucklin', color='darkslategrey')
plt.scatter(percents_array, avg_accs['PV'], marker='D', label='Pl. Veto', color='darkcyan')
plt.scatter(percents_array, avg_accs['V'], marker='^', label='Veto', color='navy')
plt.scatter(percents_array, avg_accs['SUM'], marker='X', label='SUM', color='indigo')
plt.scatter(percents_array, avg_accs['MPW'], marker='+', label='MPW', color='darkmagenta')
plt.scatter(percents_array, avg_accs['R'], marker='s', label='RCV', color='black')

plt.plot(percents_array, avg_accs['P'], linestyle='dotted', color='sienna')
plt.plot(percents_array, avg_accs['Bo'], linestyle='dashed', color='darkred')
plt.plot(percents_array, avg_accs['H'], linestyle='dashdot', color='darkgoldenrod')
plt.plot(percents_array, avg_accs['C'], linestyle=(0, (1, 10)), color='darkolivegreen')
plt.plot(percents_array, avg_accs['M'], linestyle=(5, (10, 3)), color='forestgreen')
plt.plot(percents_array, avg_accs['Bu'], linestyle=(0, (5, 10)), color='darkslategrey')
plt.plot(percents_array, avg_accs['PV'], linestyle=(0, (5, 1)), color='darkcyan')
plt.plot(percents_array, avg_accs['V'], linestyle=(0, (3, 10, 1, 10)), color='navy')
plt.plot(percents_array, avg_accs['SUM'], linestyle=(0, (3, 5, 1, 5)), color='indigo')
plt.plot(percents_array, avg_accs['MPW'], linestyle=(0, (3, 1, 1, 1)), color='darkmagenta')
plt.plot(percents_array, avg_accs['R'], linestyle='solid', color='black')
plt.legend()

plt.savefig(plots_path + average_plot_name + '.pdf')
plt.show()
        
        