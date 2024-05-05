#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:19:47 2022

@author: miceland
"""
import pandas as pd
import mapel.elections as mapel
import os


num_alts = 5
num_voters = 100
size = 100

experiment = mapel.prepare_online_ordinal_experiment()
experiment.set_default_num_candidates(num_alts)


experiment.add_family(culture_id='impartial_culture', size=size,
                        color='green',
                        marker='o',
                        family_id='ic')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.001},
                               color='blue', marker='o',
                               family_id='mallows_001')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.01},
                               color='blue', marker='o',
                               family_id='mallows_01')


experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.05},
                               color='blue', marker='o',
                               family_id='mallows_05')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.1},
                               color='blue', marker='o',
                               family_id='mallows_1')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.25},
                               color='blue', marker='o',
                               family_id='mallows_25')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.5},
                               color='blue', marker='o',
                               family_id='mallows_5')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.75},
                               color='blue', marker='o',
                               family_id='mallows_75')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.95},
                               color='blue', marker='o',
                               family_id='mallows_95')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.99},
                               color='blue', marker='o',
                               family_id='mallows_99')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.999},
                               color='blue', marker='o',
                               family_id='mallows_999')

#experiment.add_family(culture_id='norm-mallows', size=size,
#                               params={'phi': 1.0},
#                               color='blue', marker='o',
#                               label='Mallows',
#                               family_id='mallows_10')

experiment.add_family(culture_id='spoc_conitzer', size=size,
                      color='black', marker='o',
                      family_id='spoc_conitzer')

experiment.add_family(culture_id='walsh', size=size,
                      color='brown', marker='o',
                      family_id='walsh')

experiment.add_family(culture_id='single-crossing', size=size,
                      color='navy', marker='o',
                      family_id='sc')

experiment.add_family(culture_id='urn', size=size,
                      params={'alpha': 0.01},
                      color='tan', marker='o',
                      family_id='urn_01')

experiment.add_family(culture_id='urn', size=size,
                      params={'alpha': 0.02},
                      color='tan', marker='o',
                      family_id='urn_02')

experiment.add_family(culture_id='urn', size=size,
                      params={'alpha': 0.05},
                      color='tan', marker='o',
                      family_id='urn_05')

experiment.add_family(culture_id='urn', size=size,
                      params={'alpha': 0.1},
                      color='tan', marker='o',
                      family_id='urn_1')

experiment.add_family(culture_id='urn', size=size,
                      params={'alpha': 0.2},
                      color='tan', marker='o',
                      family_id='urn_2')

experiment.add_family(culture_id='urn', size=size,
                      params={'alpha': 0.5},
                      color='tan', marker='o',
                      family_id='urn_5')

experiment.add_family(culture_id='euclidean', size=size,
                      params={'dim': 5, 'space': 'sphere'},
                      color='yellow', marker='o',
                      family_id='5d_sphere')

experiment.add_family(culture_id='euclidean', size=size,
                      params={'dim': 2, 'space': 'sphere'},
                      color='yellow', marker='o',
                      family_id='2d_sphere')

experiment.add_family(culture_id='euclidean', size=size,
                      params={'dim': 3, 'space': 'sphere'},
                      color='yellow', marker='o',
                      family_id='3d_sphere')

experiment.add_family(culture_id='conitzer', size=size,
                      color='pink', marker='o',
                      family_id='csp')


experiment.add_family(culture_id='euclidean', size=size,
                      params={'dim': 3, 'space': 'uniform'},
                      color='black', marker='o',
                      family_id='3d_cube')

experiment.add_family(culture_id='euclidean', size=size,
                      params={'dim': 2, 'space': 'uniform'},
                      color='black', marker='o',
                      family_id='2d_square')

experiment.add_family(culture_id='euclidean', size=size,
                      params={'dim': 5, 'space': 'uniform'},
                      color='grey', marker='o',
                      family_id='5d_cube')

experiment.add_family(culture_id='euclidean', size=size,
                      params={'dim': 10, 'space': 'uniform'},
                      color='grey', marker='o',
                      family_id='10d_cube')

experiment.add_family(culture_id='euclidean', size=size,
                      params={'dim': 20, 'space': 'uniform'},
                      color='grey', marker='o',
                      family_id='20d_cube')

experiment.add_family(culture_id='euclidean', size=size,
                      params={'dim': 1, 'space': 'uniform'},
                      color='black', marker='o',
                      family_id='1d_interval')

if (not os.path.exists('profiles')):
    os.mkdir('profiles')

for key in experiment.elections.keys():
    data = experiment.elections[key].votes
    df = pd.DataFrame(data)
    df.to_csv('profiles/'  + key + ".csv", index=False)


#df = pd.DataFrame(experiment.coordinates)
#df.to_csv('coordinates.csv')
#experiment.compute_distances(distance_id='emd-positionwise')
#experiment.embed(algorithm='mds')


### export coordinates and elction names

#with open('elections_10D.txt', 'a') as f:
#    for e in experiment.elections.keys():
#        f.write(str(e) + ",")