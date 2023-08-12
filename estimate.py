# -*- coding: utf-8 -*-
"""
Created on Mon May  1 20:05:12 2023

@author: matti
"""

import pandas as pd
import numpy as np
import argparse

from Rules import RCV, Borda, Harmonic_Borda, Plurality, Copeland
from Ensemble_Rules import Summation, Likelihood, Triple_Weight

from uklabor_distances import top3_uklabor
from debian_distances import top3_debian
from berkley_distances import top3_berkley
from apa_distances import top3_apa
from Glasgow_distances import top3_glasgow
from minneapolis_distances import top3_minneapolis


parser = argparse.ArgumentParser(description='Real Election Sampling')

parser.add_argument('-n', '--num_elections', default=21, type=int,
                    help='number of elections (default: 21)')
parser.add_argument('-s', '--num_samples', default=1000, type=int,
                    help='number of samples (default: 1000)')
parser.add_argument('-d', '--dataset', default='Glasgow', type=str,
                    help='dataset name (default: Glasgow)')
parser.add_argument('-r', '--rule', default='Triple_Weight', type=str,
                    help='prediction rule (default: Triple_Weight)')

args = parser.parse_args()

rule_function_dict = {'RCV' : RCV,
                      'Plurality' : Plurality,
                      'Borda' : Borda,
                      'Harmonic_Borda' : Harmonic_Borda,
                      'Copeland' : Copeland,
                      'Summation' : Summation,
                      'Triple_Weight' : Triple_Weight}
print(rule_function_dict.keys())

Rule = rule_function_dict[args.rule]

top_weight_dict = {'Glasgow' : top3_glasgow,
                      'apa' : top3_apa,
                      'debian' : top3_debian,
                      'berkley' : top3_berkley,
                      'uklabor' : top3_uklabor,
                      'minneapolis' : top3_minneapolis}
print(top_weight_dict.keys())
print()

weight_list = top_weight_dict[args.dataset]

for p in range(1, 11):
    save = '{}/data/{}0/'.format(args.dataset, p)
    avg_acc = 0
    
    for election_no in range(args.num_elections):
    
        print("Election " + str(election_no + 1))
        
        votes = pd.read_csv('{}/{}_complete_{}.csv'.format(args.dataset, args.dataset, election_no + 1))
        votes = votes.iloc[:, 1:].astype('int')
        votes -= 1
        
        num_alts = len(votes.iloc[0])
        num_voters = len(votes)
        
        alt_winner = RCV(num_alts, votes)
        
        correct = 0
        
        for k in range(args.num_samples):
            s = np.random.choice(num_voters, size=int((num_voters/10)*p), replace=False)
            svotes = votes.iloc[s]
            s_winner = None
            
            weight_path = '../predTable/Matrix_{}0%'.format(p)
            
            if args.rule == 'Triple_Weight':

                distance_name_1 = list(weight_list[election_no].keys())[0]
    
                weight_dict_1 = pd.read_csv(weight_path + '/' + distance_name_1 + '.csv')
                weight_dict_1 = weight_dict_1.iloc[:, :2]
                weight_dict_1 = weight_dict_1.transpose()
                weight_dict_1.columns = weight_dict_1.iloc[0]
                weight_dict_1 = weight_dict_1.iloc[1]
                weight_dict_1 = pd.concat([weight_dict_1, pd.DataFrame({distance_name_1 : weight_list[election_no][distance_name_1]}, index=['distance'])])
    
    
                distance_name_2 = list(weight_list[election_no].keys())[1]
    
                weight_dict_2 = pd.read_csv(weight_path + '/' + distance_name_2 + '.csv')
                weight_dict_2 = weight_dict_2.iloc[:, :2]
                weight_dict_2 = weight_dict_2.transpose()
                weight_dict_2.columns = weight_dict_2.iloc[0]
                weight_dict_2 = weight_dict_2.iloc[1]
                weight_dict_2 = pd.concat([weight_dict_2, pd.DataFrame({distance_name_2 : weight_list[election_no][distance_name_2]}, index=['distance'])])
    
                distance_name_3 = list(weight_list[election_no].keys())[2]
    
                weight_dict_3 = pd.read_csv(weight_path + '/' + distance_name_3 + '.csv')
                weight_dict_3 = weight_dict_3.iloc[:, :2]
                weight_dict_3 = weight_dict_3.transpose()
                weight_dict_3.columns = weight_dict_3.iloc[0]
                weight_dict_3 = weight_dict_3.iloc[1]
                weight_dict_3 = pd.concat([weight_dict_3, pd.DataFrame({distance_name_3 : weight_list[election_no][distance_name_3]}, index=['distance'])])
                            
                s_winner = Triple_Weight(num_alts, svotes, weight_dict_1, weight_dict_2, weight_dict_3)
                
            elif args.rule == 'Summation':
                
                distance_name_1 = list(weight_list[election_no].keys())[0]
    
                weight_dict_1 = pd.read_csv(weight_path + '/' + distance_name_1 + '.csv')
                weight_dict_1 = weight_dict_1.iloc[:, :2]
                weight_dict_1 = weight_dict_1.transpose()
                weight_dict_1.columns = weight_dict_1.iloc[0]
                weight_dict_1 = weight_dict_1.iloc[1]
                weight_dict_1 = pd.concat([weight_dict_1, pd.DataFrame({distance_name_1 : weight_list[election_no][distance_name_1]}, index=['distance'])])
            
                s_winner = Rule(num_alts, svotes, weight_dict_1)
                
            else:
                s_winner = Rule(num_alts, svotes)
            
            if (s_winner == alt_winner):
                correct += 1
                
        with open(save + '{}_{}.txt'.format(args.rule, args.num_samples), 'a') as f:
            f.write('{}'.format((correct / args.num_samples)))
            f.write('\n')
            
        print(correct / args.num_samples)
        avg_acc += correct / args.num_samples
        
    avg_acc /= args.num_elections
    print('Average accuracy: {:.4f}'.format(avg_acc))
    
    with open(save + '{}_{}.txt'.format(args.rule, args.num_samples), 'a') as f:
        f.write('{}'.format(avg_acc))