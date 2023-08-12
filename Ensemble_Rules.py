from Rules import *

def Summation(num_alts, data, weights):
    
    scores = np.zeros(num_alts)
    
    w_r = RCV(num_alts, data)
    w_p = Plurality(num_alts, data)
    w_b = Borda(num_alts, data)
    w_h = Harmonic_Borda(num_alts, data)
    w_c = Copeland(num_alts, data)
    
    scores[w_r - 1] += 1 * float(weights.loc['R'].iloc[0])
    scores[w_p - 1] += 1 * float(weights.loc['P'].iloc[0])
    scores[w_b - 1] += 1 * float(weights.loc['B'].iloc[0])
    scores[w_h - 1] += 1 * float(weights.loc['H'].iloc[0])
    scores[w_c - 1] += 1 * float(weights.loc['C'].iloc[0])
    
    winner = np.where(scores == scores.max())[0][0]
    winner += 1
    
    return winner

def Likelihood(num_alts, data, weights):
    
    candidates = set()
    candidates_freq = {}
    
    w_r = RCV(num_alts, data)
    w_p = Plurality(num_alts, data)
    w_b = Borda(num_alts, data)
    w_h = Harmonic_Borda(num_alts, data)
    w_c = Copeland(num_alts, data)

    candidates.add(w_r)
    if (not (w_r in candidates_freq)):
        candidates_freq[w_r] = 0
    candidates_freq[w_r] += 1
    
    candidates.add(w_p)
    if (not (w_p in candidates_freq)):
        candidates_freq[w_p] = 0
    candidates_freq[w_p] += 1
    
    candidates.add(w_b)
    if (not (w_b in candidates_freq)):
        candidates_freq[w_b] = 0
    candidates_freq[w_b] += 1
    
    candidates.add(w_h)
    if (not (w_h in candidates_freq)):
        candidates_freq[w_h] = 0
    candidates_freq[w_h] += 1
    
    candidates.add(w_c)
    if (not (w_c in candidates_freq)):
        candidates_freq[w_c] = 0
    candidates_freq[w_c] += 1
        
    scores = np.ones(num_alts)
    
    for candidate in candidates:
        if (w_r == candidate):
            scores[candidate - 1] *= weights['RCV']
        else:
            scores[candidate - 1] *= (1 - weights['RCV'])
            
        if (w_p == candidate):
            scores[candidate - 1] *= weights['Plurality']
        else:
            scores[candidate - 1] *= (1 - weights['Plurality'])
            
        if (w_b == candidate):
            scores[candidate - 1] *= weights['Borda']
        else:
            scores[candidate - 1] *= (1 - weights['Borda'])
            
        if (w_h == candidate):
            scores[candidate - 1] *= weights['Harmonic_Borda']
        else:
            scores[candidate - 1] *= (1 - weights['Harmonic_Borda'])
            
        if (w_c == candidate):
            scores[candidate - 1] *= weights['Copeland']
        else:
            scores[candidate - 1] *= (1 - weights['Copeland'])
            
    for alternative in {x for x in range(1, num_alts + 1)} - candidates:
        scores[alternative - 1] = 0
                
    winner = np.where(scores == scores.max())[0][0] + 1
    
    # in case of a tie
    if (scores.max() == 0):
        winner = max(candidates_freq, key=candidates_freq.get)
    
    return winner

def Triple_Weight(num_alts, data, e1, e2, e3):
    
    scores = np.zeros(num_alts)
        
    w_r = RCV(num_alts, data)
    w_p = Plurality(num_alts, data)
    w_b = Borda(num_alts, data)
    w_h = Harmonic_Borda(num_alts, data)
    w_c = Copeland(num_alts, data)
    
    alts = []
    alts.append(w_r)
    alts.append(w_p)
    alts.append(w_b)
    alts.append(w_h)
    alts.append(w_c)
    alts = np.array(alts)
    
    p_r = np.where(alts == w_r)[0]
    p_p = np.where(alts == w_p)[0]
    p_b = np.where(alts == w_b)[0]
    p_h = np.where(alts == w_h)[0]
    p_c = np.where(alts == w_c)[0]
    
    for p in p_r:
        scores[w_r - 1] += float(e1.loc['R'].iloc[0]) / e1.loc['distance'].iloc[1]
        scores[w_r - 1] += float(e2.loc['R'].iloc[0]) / e2.loc['distance'].iloc[1]
        scores[w_r - 1] += float(e3.loc['R'].iloc[0]) / e3.loc['distance'].iloc[1]
        
    for p in p_p:
        scores[w_p - 1] += float(e1.loc['P'].iloc[0]) / e1.loc['distance'].iloc[1]
        scores[w_p - 1] += float(e2.loc['P'].iloc[0]) / e2.loc['distance'].iloc[1]
        scores[w_p - 1] += float(e3.loc['P'].iloc[0]) / e3.loc['distance'].iloc[1]
        
    for p in p_b:
        scores[w_b - 1] += float(e1.loc['B'].iloc[0]) / e1.loc['distance'].iloc[1]
        scores[w_b - 1] += float(e2.loc['B'].iloc[0]) / e2.loc['distance'].iloc[1]
        scores[w_b - 1] += float(e3.loc['B'].iloc[0]) / e3.loc['distance'].iloc[1]
        
    for p in p_h:
        scores[w_h - 1] += float(e1.loc['H'].iloc[0]) / e1.loc['distance'].iloc[1]
        scores[w_h - 1] += float(e2.loc['H'].iloc[0]) / e2.loc['distance'].iloc[1]
        scores[w_h - 1] += float(e3.loc['H'].iloc[0]) / e3.loc['distance'].iloc[1]
        
    for p in p_c:
        scores[w_c - 1] += float(e1.loc['C'].iloc[0]) / e1.loc['distance'].iloc[1]
        scores[w_c - 1] += float(e2.loc['C'].iloc[0]) / e2.loc['distance'].iloc[1]
        scores[w_c - 1] += float(e3.loc['C'].iloc[0]) / e3.loc['distance'].iloc[1]
        
    winner = np.where(scores == scores.max())[0][0]
    winner += 1
    
    return winner