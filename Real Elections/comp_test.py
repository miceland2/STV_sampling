# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 13:56:53 2023

@author: matti
"""

import mapel.elections as mapel
import pandas as pd
from statistics import mean
import argparse


parser = argparse.ArgumentParser(description='Real Election Sampling')

parser.add_argument('-n', '--election_number', default=1, type=int,
                    help='number of elections (default: 1)')
parser.add_argument('-s', '--num_profiles', default=100, type=int,
                    help='number of elections (default: 100)')
parser.add_argument('-d', '--dataset', default='Glasgow', type=str,
                    help='dataset name (default: Glasgow)')

args = parser.parse_args()

distance_id = 'emd-positionwise'
election_no = args.election_number

votes = pd.read_csv('{}/{}_complete_{}.csv'.format(args.dataset, args.dataset, election_no))
votes = votes.iloc[:, 1:].astype('int')
votes -= 1
votes = votes.values.tolist()

num_alts = len(votes[0])
num_voters = len(votes)

print('uklabor election {}'.format(election_no))
print('Number of Alternatives: {}'.format(num_alts))
print('Number of Voters: {}\n'.format(num_voters))

size = args.num_profiles

with open('distances_uklabor_{}.txt'.format(election_no), 'a') as f:
    f.write('uklabor election {}\n'.format(election_no))
    f.write('Number of Alternatives: {}\n'.format(num_alts))
    f.write('Number of Voters: {}\n\n'.format(num_voters))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    
    experiment.add_family(culture_id='impartial_culture', size=size,
                            color='green',
                            marker='o',
                            family_id='ic')
    
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('ic: {}'.format(m))
    f.write('ic: {}\n'.format(m))
    
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='mallows', size=size,
                                   params={'phi': 0.1},
                                   color='blue', marker='o',
                                   family_id='mallows_1')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('m1: {}'.format(m))
    f.write('m1: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='mallows', size=size,
                                   params={'phi': 0.2},
                                   color='blue', marker='o',
                                   family_id='mallows_2')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('m2: {}'.format(m))
    f.write('m2: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='mallows', size=size,
                                   params={'phi': 0.3},
                                   color='blue', marker='o',
                                   family_id='mallows_3')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('m3: {}'.format(m))
    f.write('m3: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='mallows', size=size,
                                   params={'phi': 0.4},
                                   color='blue', marker='o',
                                   family_id='mallows_4')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('m4: {}'.format(m))
    f.write('m4: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='mallows', size=size,
                                   params={'phi': 0.5},
                                   color='blue', marker='o',
                                   family_id='mallows_5')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('m5: {}'.format(m))
    f.write('m5: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='mallows', size=size,
                                   params={'phi': 0.6},
                                   color='blue', marker='o',
                                   family_id='mallows_6')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('m6: {}'.format(m))
    f.write('m6: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='mallows', size=size,
                                   params={'phi': 0.7},
                                   color='blue', marker='o',
                                   family_id='mallows_7')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('m7: {}'.format(m))
    f.write('m7: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='mallows', size=size,
                                   params={'phi': 0.8},
                                   color='blue', marker='o',
                                   family_id='mallows_8')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('m8: {}'.format(m))
    f.write('m8: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='mallows', size=size,
                                   params={'phi': 0.9},
                                   color='blue', marker='o',
                                   family_id='mallows_9')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('m9: {}'.format(m))
    f.write('m9: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='mallows', size=size,
                                   params={'phi': 1.0},
                                   color='blue', marker='o',
                                   family_id='mallows_10')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('m10: {}'.format(m))
    f.write('m10: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='walsh', size=size,
                          color='brown', marker='o',
                          family_id='walsh')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('walsh: {}'.format(m))
    f.write('walsh: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='single-crossing', size=size,
                          color='navy', marker='o',
                          family_id='sc')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('sc: {}'.format(m))
    f.write('sc: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='urn', size=size,
                          params={'alpha': 0.01},
                          color='tan', marker='o',
                          family_id='urn_1')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('u1: {}'.format(m))
    f.write('u1: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='urn', size=size,
                          params={'alpha': 0.02},
                          color='tan', marker='o',
                          family_id='urn_2')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('u2: {}'.format(m))
    f.write('u2: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='urn', size=size,
                          params={'alpha': 0.05},
                          color='tan', marker='o',
                          family_id='urn_3')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('u3: {}'.format(m))
    f.write('u3: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='urn', size=size,
                          params={'alpha': 0.1},
                          color='tan', marker='o',
                          family_id='urn_4')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('u4: {}'.format(m))
    f.write('u4: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='urn', size=size,
                          params={'alpha': 0.2},
                          color='tan', marker='o',
                          family_id='urn_5')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('u5: {}'.format(m))
    f.write('u5: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='urn', size=size,
                          params={'alpha': 0.5},
                          color='tan', marker='o',
                          family_id='urn_6')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('u6: {}'.format(m))
    f.write('u6: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='5d_sphere', size=size,
                          params={'dim': 5},
                          color='yellow', marker='o',
                          family_id='5d_sphere')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('5d_sphere: {}'.format(m))
    f.write('5d_sphere: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='conitzer', size=size,
                          color='pink', marker='o',
                          family_id='csp')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('csp: {}'.format(m))
    f.write('csp: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='3d_cube', size=size,
                          params={'dim': 3},
                          color='black', marker='o',
                          family_id='3d_cube')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('3d_cube: {}'.format(m))
    f.write('3d_cube: {}\n'.format(m))
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    experiment.add_family(culture_id='10d_cube', size=size,
                          params={'dim': 10},
                          color='grey', marker='o',
                          family_id='10d_cube')
    experiment.add_family(culture_id='norm-mallows', color='blue', family_id='glasgow',
                                       params={'norm-phi': 0.5}, size=1)
    
    experiment.elections['glasgow_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['glasgow_0'].values())
    print('10d_cube: {}'.format(m))
    f.write('10d_cube: {}\n'.format(m))