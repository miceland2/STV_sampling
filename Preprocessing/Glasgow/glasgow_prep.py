#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:10:01 2023

@author: miceland
"""

import pandas as pd
import os


path = 'raw/'
preprocessed_path = 'preprocessed/'

if (not os.path.exists(preprocessed_path)):
    os.mkdir(preprocessed_path)


for file in os.listdir(path):
    print(file)
    
    # Replace colons with commas
    with open(path + file, 'r') as f:
        lines = f.readlines()
        
        with open(preprocessed_path + file[0:-4] + '-comma.soi', 'w') as g:
            for line in lines:
                line = line.replace(':', ',')
                g.write(line)