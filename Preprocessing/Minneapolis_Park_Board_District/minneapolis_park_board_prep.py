#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:59:02 2023

@author: miceland
"""

import pandas as pd
import os


path = 'raw/'

for file in os.listdir(path):
    print(file)

    df = pd.read_csv(path + file)
    
    nRank = 0
    for column in df.columns:
        if 'rank' in column:
            nRank += 1
    
    df = df.iloc[:, len(df.columns) - nRank:]
    
    names = dict()
    
    for i in range(len(df)):
        row = df.iloc[i]
        
        for name in row:
            if name not in names:
                names[name] = 0
            names[name] += 1
            
    print(names)
    print()
    
    nWriteIn = 0
    nOvervote = 0
        
    if ('writein' in names):
        nWriteIn += names['writein']
        del names['writein']
    if ('Write-in' in names):
        nWriteIn += names['Write-in']
        del names['Write-in']
    if ('Write-In' in names):
        nWriteIn += names['Write-In']
        del names['Write-In']
    if ('skipped' in names):
        del names['skipped']
    if ('overvote' in names):
        nOvervote += names['overvote']
        del names['overvote']
            
    nameToInt = dict()
    m = 0
    
    for name in names:
        nameToInt[name] = m
        m += 1
        
    profileInt = []
    profileInt.append([None for x in range(m)])
    profileInt.append(['Write-In cells: {}'.format(nWriteIn)])
    profileInt.append(['Overvote cells: {}'.format(nOvervote)])
    for name in nameToInt:
        profileInt.append(['{}: {}'.format(name, nameToInt[name])])
    
    nTruncated = 0
    for i in range(len(df)):
        row = df.iloc[i]
        rowInt = []
        ints = set()
        
        truncated = 0
        
        for name in row:
            if (name in nameToInt):
                if (nameToInt[name] not in ints):
                    rowInt.append(nameToInt[name])
                    ints.add(nameToInt[name])
                else:
                    truncated = 1
        nTruncated += truncated
        
        profileInt.append(rowInt)
        
    with open('truncated.txt', 'a') as f:
        f.write('{}, {}\n'.format(file, nTruncated))
            
    df = pd.DataFrame(profileInt, columns=[x for x in range(m)])
    df = df.dropna(how='all')
    
    df.to_csv('preprocessed/' + file)