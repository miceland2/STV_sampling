#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 10:35:29 2022

@author: miceland
"""

import mapel.elections as mapel
import pandas as pd
import argparse


parser = argparse.ArgumentParser(description='Map Visual Plot')

parser.add_argument('-n', '--num_elections', default=25, type=int,
                    help='number of elections (default: 25)')
parser.add_argument('-a', '--num_alts', default=10, type=int,
                    help='number of elections (default: 10)')
parser.add_argument('-s', '--sample_size', default=50, type=int,
                    help='percent sample size (default: 50)')

args = parser.parse_args()

mat = pd.read_csv('r_{}.txt'.format(args.sample_size), names=[i for i in range(1, 11)])
mat = mat.iloc[:, 0:10]

col = (args.sample_size / 10) - 2;
if (args.sample_size == 10):
    a = mat.index.values
else:
    a = list(mat.iloc[:, col])

num_alts = args.num_alts
size = args.num_elections

experiment = mapel.prepare_online_ordinal_experiment()
experiment.set_default_num_candidates(num_alts)

experiment.add_family(culture_id='impartial_culture', size=size,
                        color='green',
                        marker='o',
                        family_id='ic',
                        label='Impartial Culture',
                        alpha=a[0:25])


experiment.add_family(culture_id='mallows', size=size,
                      label='Mallows',
                               params={'phi': 0.1},
                               color='mediumblue', marker='o',
                               family_id='mallows_1',
                               alpha=a[25:50])


experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.2},
                               label='',
                               color='blue', marker='o',
                               family_id='mallows_2',
                               alpha=a[50:75])


experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.3},
                               label='',
                               color='blue', marker='o',
                               family_id='mallows_3',
                               alpha=a[75:100])

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.4},
                               label='',
                               color='blue', marker='o',
                               family_id='mallows_4',
                               alpha=a[100:125])

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.5},
                               label='',
                               color='blue', marker='o',
                               family_id='mallows_5',
                               alpha=a[125:150])

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.6},
                               label='',
                               color='blue', marker='o',
                               family_id='mallows_6',
                               alpha=a[150:175])

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.7},
                               label='',
                               color='blue', marker='o',
                               family_id='mallows_7',
                               alpha=a[175:200])

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.8},
                               label='',
                               color='blue', marker='o',
                               family_id='mallows_8',
                               alpha=a[200:225])

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.9},
                               label='',
                               color='blue', marker='o',
                               family_id='mallows_9',
                               alpha=a[225:250])


#experiment.add_family(culture_id='norm-mallows', size=size,
#                               params={'phi': 1.0},
#                               color='blue', marker='o',
#                               label='Mallows',
#                               family_id='mallows_10')



experiment.add_family(culture_id='walsh', size=size,
                      color='brown', marker='o',
                      label='Walsh',
                      family_id='walsh',
                      alpha=a[250:275])

experiment.add_family(culture_id='single-crossing', size=size,
                      color='indigo', marker='o',
                      family_id='sc',
                      label='Single-Crossing',
                      alpha=a[275:300])

experiment.add_family(culture_id='urn', size=size,
                      params={'alpha': 0.01},
                      color='tan', marker='o',
                      family_id='urn_01',
                      label='Urn',
                      alpha=a[300:325])

experiment.add_family(culture_id='urn', size=size,
                      params={'alpha': 0.02},
                      color='tan', marker='o',
                      family_id='urn_02',
                      label='',
                      alpha=a[325:350])

experiment.add_family(culture_id='urn', size=size,
                      params={'alpha': 0.05},
                      color='tan', marker='o',
                      family_id='urn_05',
                      label='',
                      alpha=a[350:375])

experiment.add_family(culture_id='urn', size=size,
                      params={'alpha': 0.1},
                      color='tan', marker='o',
                      family_id='urn_1',
                      label='',
                      alpha=a[375:400])

experiment.add_family(culture_id='urn', size=size,
                      params={'alpha': 0.2},
                      color='tan', marker='o',
                      family_id='urn_2',
                      label='',
                      alpha=a[400:425])

experiment.add_family(culture_id='urn', size=size,
                      params={'alpha': 0.5},
                      color='tan', marker='o',
                      family_id='urn_5',
                      label='',
                      alpha=a[425:450])

experiment.add_family(culture_id='5d_sphere', size=size,
                      params={'dim': 5},
                      color='gold', marker='o',
                      label='5D Sphere',
                      family_id='5d_sphere',
                      alpha=a[450:475])

experiment.add_family(culture_id='conitzer', size=size,
                      color='orchid', marker='o',
                      family_id='csp',
                      label='Conitzer',
                      alpha=a[475:500])

experiment.add_family(culture_id='3d_cube', size=size,
                      params={'dim': 3},
                      color='black', marker='o',
                      family_id='3d_cube',
                      label = '3D Cube',
                      alpha=a[500:525])

experiment.add_family(culture_id='10d_cube', size=size,
                      params={'dim': 10},
                      color='grey', marker='o',
                      family_id='10d_cube',
                      label='10D Cube',
                      alpha=a[525:550])



coordinates = pd.read_csv('coordinates.csv')
coordinates = coordinates.to_dict()

experiment.compute_distances(distance_id='emd-positionwise')
experiment.embed(algorithm='mds')

experiment.coordinates = coordinates
experiment.print_map()
