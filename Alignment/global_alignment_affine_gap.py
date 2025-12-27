#Faraz Doagooye Tehrani 402105998

import numpy as np
alpha = -4
beta = -1

def score(a, b):
    if a == b:
        return 5
    else:
        return -3


def lcs(v, w):
    rows = len(v) + 1
    cols = len(w) + 1

    middle = [[0 for j in range(cols)] for i in range(rows)]  
    lower = [[0 for j in range(cols)] for i in range(rows)]  
    upper = [[0 for j in range(cols)] for i in range(rows)]  
    for i in range(rows):
        middle[i][0] = alpha + (i - 1) * beta
        upper[i][0] = float('-inf')
        lower[i][0] = alpha + (i - 1) * beta
    for i in range(cols):
        middle[0][i] = alpha + (i - 1) * beta
        lower[0][i] = float('-inf')
        upper[0][i] = alpha + (i - 1) * beta
    
    upper[0][0] = float('-inf')
    middle[0][0] = 0


    bMid = [['' for j in range(cols)] for i in range(rows)] 
    bLow = [['' for j in range(cols)] for i in range(rows)] 
    bUp = [['' for j in range(cols)] for i in range(rows)]    


    for i in range(1, len(middle)):
        for j in range(1, len(middle[0])):
            max_move = max(lower[i - 1][j] + beta, middle[i - 1][j] + alpha)
            lower[i][j] = max_move
            if max_move == middle[i - 1][j] + alpha:
                bLow[i][j] = 'm'
            elif max_move == lower[i - 1][j] + beta:
                bLow[i][j] = 'l'
           
            max_move = max(upper[i][j - 1] + beta, middle[i][j - 1] + alpha)
            upper[i][j] = max_move
            if max_move == middle[i][j - 1] + alpha:
                bUp[i][j] = 'm'
            elif max_move == upper[i][j - 1] + beta:
                bUp[i][j] = 'u'

            max_move = max(lower[i][j], upper[i][j], middle[i - 1][j - 1] + score(v[i - 1],w[j - 1]))
            middle[i][j] = max_move
            if max_move == middle[i - 1][j - 1] + score(v[i - 1], w[j - 1]):
                bMid[i][j] = 'm'
            elif max_move == upper[i][j]:
                bMid[i][j] = 'u'
            elif max_move == lower[i][j]:
                bMid[i][j] = 'l'
    
    return (upper, middle, lower, bUp, bMid, bLow)

            
amino1 = input().strip()
amino2 = input().strip()

result = lcs(amino1, amino2)

middle = result[1]

max_val = float('-inf')
max_pos = (len(middle), len(middle[0]))


# (amino1_start, amino2_start) = traceBack(amino1, amino2, result[3], result[4], result[5], max_pos)

for i in range(6):
    print("---------")
    print(np.array(result[i]))



