from Rules import RCV, Plurality, Borda, Harmonic_Borda, Copeland
import numpy as np
import pandas as pd
import os
import argparse


parser = argparse.ArgumentParser(description='Map Visual Sampling')

parser.add_argument('-n', '--total_num_elections', default=550, type=int,
                    help='number of elections (default: 25)')
parser.add_argument('-a', '--num_alts', default=10, type=int,
                    help='number of alternatives (default: 10)')
parser.add_argument('-ns', '--num_samples', default=1000, type=int,
                    help='percent sample size (default: 1000)')
parser.add_argument('-v', '--num_voters', default=100, type=int,
                    help='number of elections (default: 100)')
parser.add_argument('-s', '--sample_size', default=50, type=int,
                    help='size of random sample (default: 50)')

parser.add_argument('-nf', '--election_name_file', default='elections.txt', type=str,
                    help='txt file with culture names (default: elections.txt)')
parser.add_argument('-fp', '--file_path', default='csv_files/', type=str,
                    help='path with profile csv files (default: csv_files/)')

args = parser.parse_args()

num_alts = args.num_alts
num_voters = args.num_voters
samples = args.num_samples
s = args.sample_size / 10

elections = pd.read_csv(args.election_name_file, names=[i for i in range(args.total_num_elections)])
electionsL = list(elections.iloc[0])
electionsL.insert(0, 'ic_0')

for election in electionsL:
    
    print(election)
    
    path = args.file_path + election + '.csv'
    votes = pd.read_csv(path)
    col = votes.iloc[:, 1]
    
    #alt_winner = Copeland(num_alts, votes)                                                                                                                                   
    #alt_winner = Plurality(num_alts, votes)
    #alt_winner = Borda(num_alts, votes)
    #alt_winner = Harmonic_Borda(num_alts, votes)
    alt_winner = RCV(num_alts, votes)
    
    count = np.zeros(num_alts)
    
    for p in range(s, s + 1):
        cnt = 0
        for k in range(samples):
            votes.iloc[:, 1] = col
            #print(votes)
            s = np.random.choice(num_voters, size=int((num_voters/10)*p), replace=False)
            svotes = votes.iloc[s]
            s_winner = None
            
            #s_winner = Copeland(num_alts, svotes)
            #s_winner = Plurality(num_alts, svotes)
            #s_winner = Borda(num_alts, svotes)
            #s_winner = Harmonic_Borda(num_alts, svotes)
            s_winner = RCV(num_alts, svotes)
    
            if (s_winner == alt_winner):
                count[p - 1] += 1
            cnt += 1
    
    
    for i in range(s, s + 1):
        print("%d0 percent sample: %.2f" %(i, count[i - 1]/samples))
    

    with open('r_{}.txt'.format(args.sample_size), 'a') as f:
        for c in count:
            f.write(str(c / samples) + ",")
        f.write("\n")


