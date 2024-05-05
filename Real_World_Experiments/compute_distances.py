#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:52:24 2023

@author: miceland
"""

import mapel.elections as mapel
import pandas as pd
import numpy as np
from statistics import mean
import argparse
import os

def compare(file, culture_id, size, params={}):
    
    votes = pd.read_csv(file)
    
    votes = votes.values.tolist()    
    votes = np.array(votes, dtype=int)
    
    num_alts = len(votes[0])
    num_voters = len(votes)
    
    experiment = mapel.prepare_online_ordinal_experiment()
    experiment.set_default_num_candidates(num_alts)
    experiment.set_default_num_voters(num_voters)
    
    experiment.add_family(culture_id=culture_id, size=size, params=params)
    experiment.add_family(culture_id='norm-mallows', family_id='dum', size=1)
    
    experiment.elections['dum_0'].votes = votes
    experiment.compute_distances(distance_id=distance_id)
    m = mean(experiment.distances['dum_0'].values())
    
    return m


parser = argparse.ArgumentParser(description='Real Election Sampling')

parser.add_argument('-n', '--election_number', default=1, type=int,
                    help='election_number (default: 1)')
parser.add_argument('-s', '--num_profiles', default=100, type=int,
                    help='number of profiles (default: 100)')

args = parser.parse_args()

size = args.num_profiles

distance_id = 'emd-positionwise'

cultures = [

{'id' : 'impartial_culture',
 'abr' : 'ic',
 'prams' : {}
},

{'id' : 'mallows',
 'abr' : 'mallows_001',
 'prams' : {'phi' : 0.001}
},

{'id' : 'mallows',
 'abr' : 'mallows_01',
 'prams' : {'phi' : 0.01}
},

{'id' : 'mallows',
 'abr' : 'mallows_05',
 'prams' : {'phi' : 0.05}
},

{
'id' : 'mallows',
 'abr' : 'mallows_1',
 'prams' : {'phi' : 0.1}
},

{
'id' : 'mallows',
 'abr' : 'mallows_25',
 'prams' : {'phi' : 0.25}
},

{
'id' : 'mallows',
 'abr' : 'mallows_5',
 'prams' : {'phi' : 0.5}
},

{
'id' : 'mallows',
 'abr' : 'mallows_75',
 'prams' : {'phi' : 0.75}
},

{
'id' : 'mallows',
 'abr' : 'mallows_95',
 'prams' : {'phi' : 0.95}
},

{
'id' : 'mallows',
 'abr' : 'mallows_99',
 'prams' : {'phi' : 0.99}
},

{
'id' : 'mallows',
 'abr' : 'mallows_999',
 'prams' : {'phi' : 0.999}
},

{
'id' : 'spoc_conitzer',
 'abr' : 'spoc_conitzer',
 'prams' : {}
},

{
'id' : 'walsh',
 'abr' : 'walsh',
 'prams' : {}
},

{
'id' : 'single-crossing',
 'abr' : 'sc',
 'prams' : {}
},

{
'id' : 'urn',
'abr' : 'urn_01',
'prams' : {'alpha' : 0.01}
},

{
'id' : 'urn',
'abr' : 'urn_02',
'prams' : {'alpha' : 0.02}
},

{
'id' : 'urn',
'abr' : 'urn_05',
'prams' : {'alpha' : 0.05}
},

{
'id' : 'urn',
'abr' : 'urn_1',
'prams' : {'alpha' : 0.1}
},

{
'id' : 'urn',
'abr' : 'urn_2',
'prams' : {'alpha' : 0.2}
},

{
'id' : 'urn',
'abr' : 'urn_5',
'prams' : {'alpha' : 0.5}
},

{
'id' : 'euclidean',
'abr' : '5d_sphere',
'prams' : {'dim' : 5, 'space' : 'sphere'}
},

{
'id' : 'euclidean',
'abr' : '2d_sphere',
'prams' : {'dim' : 2, 'space' : 'sphere'}
},

{
'id' : 'euclidean',
'abr' : '3d_sphere',
'prams' : {'dim' : 3, 'space' : 'sphere'}
},

{
'id' : 'conitzer',
 'abr' : 'csp',
 'prams' : {}
},

{
 'id' : 'euclidean',
 'abr' : '1d_interval',
 'prams' : {'dim' : 1, 'space' : 'uniform'}
},

{
 'id' : 'euclidean',
 'abr' : '2d_square',
 'prams' : {'dim' : 2, 'space' : 'uniform'}
},

{
 'id' : 'euclidean',
 'abr' : '3d_cube',
 'prams' : {'dim' : 3, 'space' : 'uniform'}
},

{
 'id' : 'euclidean',
 'abr' : '5d_cube',
 'prams' : {'dim' : 5, 'space' : 'uniform'}
},

{
 'id' : 'euclidean',
 'abr' : '10d_cube',
 'prams' : {'dim' : 10, 'space' : 'uniform'}
},

{
 'id' : 'euclidean',
 'abr' : '20d_cube',
 'prams' : {'dim' : 20, 'space' : 'uniform'}
},
]

path = 'apa/complete/'

outer_path = path[0:-9]

if (not os.path.exists(outer_path + 'distances')):
    os.mkdir(outer_path + 'distances')

for profile in os.listdir(path):

    with open(outer_path + 'distances/{}_distances.txt'.format(profile[0:-4]), 'w') as f:
        
        file = path + profile
        
        for culture in cultures:
            dist = compare(file, culture['id'], size, culture['prams'])
            
            print('{}: {}'.format(culture['abr'], dist))
            f.write('{}, {}\n'.format(culture['abr'], dist))