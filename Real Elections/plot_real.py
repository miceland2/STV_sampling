# -*- coding: utf-8 -*-
"""
Created on Tue May 16 10:38:54 2023

@author: matti
"""

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style


path = 'uklabor/data/'
election_no = 1
samples = 1000

p = []
for i in range(1, 11):
    p.append(pd.read_csv(path + '{}0/Plurality_{}.txt'.format(i, samples), names=['0']).iloc[election_no] * 100)

b = []
for i in range(1, 11):
    b.append(pd.read_csv(path + '{}0/Borda_{}.txt'.format(i, samples), names=['0']).iloc[election_no] * 100)

h = []
for i in range(1, 11):
    h.append(pd.read_csv(path + '{}0/Harmonic Borda_{}.txt'.format(i, samples), names=['0']).iloc[election_no] * 100)

r = []
for i in range(1, 11):
    r.append(pd.read_csv(path + '{}0/RCV_{}.txt'.format(i, samples), names=['0']).iloc[election_no] * 100)

c = []
for i in range(1, 11):
    c.append(pd.read_csv(path + '{}0/Copeland_{}.txt'.format(i, samples), names=['0']).iloc[election_no] * 100)

s = []
for i in range(1, 11):
    s.append(pd.read_csv(path + '{}0/Summation_{}.txt'.format(i, samples), names=['0']).iloc[election_no] * 100)
    
s3 = []
for i in range(1, 11):
    s3.append(pd.read_csv(path + '{}0/Triple_Weight_1000.txt'.format(i, samples), names=['0']).iloc[election_no] * 100)

#l = []
#for i in range(1, 11):
#    l.append(pd.read_csv(path + '{}0/Likelihood_{}.txt'.format(i, samples), names=['0']).iloc[election_no] * 100)


x = [x * 10 for x in range(1, 11)]

plt.style.use('ggplot')
plt.plot(x, p, label='Plurality', c='navy', linestyle='dotted')
plt.scatter(x, p, edgecolor='gray', marker='s', s=25, c='navy')
plt.plot(x, b, label='Borda', c='darkgreen', linestyle='dotted')
plt.scatter(x, b, edgecolor='gray', marker='s', s=25, c='darkgreen')
plt.plot(x, h, label='Harmonic', c='maroon', linestyle='dotted')
plt.scatter(x, h, edgecolor='gray', marker='s', s=25, c='maroon')
plt.plot(x, r, label='RCV', c='black')
plt.scatter(x, r, edgecolor='gray', marker='s', s=25, c='black')
plt.plot(x, c, label='Copeland', c='darkgoldenrod', linestyle='dotted')
plt.scatter(x, c, edgecolor='gray', marker='s', s=25, c='darkgoldenrod')

plt.plot(x, s, label='Summation', c='darkslategray', linestyle='dashed')
plt.scatter(x, s, edgecolor='gray', marker='s', s=25, c='darkslategray')
plt.plot(x, s3, label='Summation3', c='mediumorchid', linestyle='dashed')
plt.scatter(x, s3, edgecolor='gray', marker='s', s=25, c='mediumorchid')

plt.ylim(-5, 105)
#plt.xlabel('Sample Size')
#plt.ylabel('Accuracy')
plt.title('UK Labor Election Average'.format(election_no + 1))
#plt.legend()
plt.savefig('election_avg_1000_uklabor.png'.format(election_no + 1))
plt.show()