#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:19:47 2022

@author: miceland
"""
import pandas as pd
import mapel.elections as mapel
import os
import math
import argparse


parser = argparse.ArgumentParser(description='Map Visual Data')

parser.add_argument('-n', '--num_elections', default=25, type=int,
                    help='number of elections (default: 25)')
parser.add_argument('-v', '--num_voters', default=100, type=int,
                    help='number of elections (default: 100)')
parser.add_argument('-a', '--num_alts', default=10, type=int,
                    help='number of elections (default: 10)')

args = parser.parse_args()

num_alts = args.num_alts
num_voters = args.num_voters
size = args.num_elections

experiment = mapel.prepare_online_ordinal_experiment()
experiment.set_default_num_candidates(num_alts)

experiment.add_family(culture_id='impartial_culture', size=size,
                        color='green',
                        marker='o',
                        family_id='ic')


experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.1},
                               color='blue', marker='o',
                               family_id='mallows_1')


experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.2},
                               color='blue', marker='o',
                               family_id='mallows_2')


experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.3},
                               color='blue', marker='o',
                               family_id='mallows_3')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.4},
                               color='blue', marker='o',
                               family_id='mallows_4')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.5},
                               color='blue', marker='o',
                               family_id='mallows_5')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.6},
                               color='blue', marker='o',
                               family_id='mallows_6')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.7},
                               color='blue', marker='o',
                               family_id='mallows_7')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.8},
                               color='blue', marker='o',
                               family_id='mallows_8')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.9},
                               color='blue', marker='o',
                               family_id='mallows_9')

"""
experiment.add_family(culture_id='norm-mallows', size=size,
                               params={'phi': 1.0},
                               color='blue', marker='o',
                               label='Mallows',
                               family_id='mallows_10')
"""


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

experiment.add_family(culture_id='5d_sphere', size=size,
                      params={'dim': 5},
                      color='yellow', marker='o',
                      family_id='5d_sphere')

experiment.add_family(culture_id='conitzer', size=size,
                      color='pink', marker='o',
                      family_id='csp')

experiment.add_family(culture_id='3d_cube', size=size,
                      params={'dim': 3},
                      color='black', marker='o',
                      family_id='3d_cube')

experiment.add_family(culture_id='10d_cube', size=size,
                      params={'dim': 10},
                      color='grey', marker='o',
                      family_id='10d_cube')

# Generate 100 csv files
"""
di = 'tie_profiles/'
os.mkdir(di)
model = ""
families = list(experiment.families.keys())
cnt = 0

for family in families:
    os.mkdir(di + family)

for key in experiment.elections.keys():
    
    model = families[math.floor(cnt / size)] + "/"
        
    data = experiment.elections[key].votes
    df = pd.DataFrame(data)
    df.to_csv(di + model + key + ".csv", index=False)
    
    cnt += 1
"""

# generate election coordinates
df = pd.DataFrame(experiment.coordinates)
df.to_csv('coordinates.csv')
experiment.compute_distances(distance_id='emd-positionwise')
experiment.embed()

# generate election csv files
for key in experiment.elections.keys():
    data = experiment.elections[key].votes
    df = pd.DataFrame(data)
    df.to_csv('csv_files/' + key + ".csv", index=False)


### export coordinates and elction names
with open('elections.txt', 'a') as f:
    for e in experiment.elections.keys():
        f.write(str(e) + ",")


experiment.print_map()
