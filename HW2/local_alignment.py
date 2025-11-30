#Faraz Doagooye Tehrani 402105998

alpha = -11
beta = -1

score = {
    'A': {'A': 4,  'C': 0,  'D': -2, 'E': -1, 'F': -2, 'G': 0,  'H': -2, 'I': -1, 'K': -1, 'L': -1,
          'M': -1, 'N': -2, 'P': -1, 'Q': -1, 'R': -1, 'S': 1,  'T': 0,  'V': 0,  'W': -3, 'Y': -2},
    'C': {'A': 0,  'C': 9,  'D': -3, 'E': -4, 'F': -2, 'G': -3, 'H': -3, 'I': -1, 'K': -3, 'L': -1,
          'M': -1, 'N': -3, 'P': -3, 'Q': -3, 'R': -3, 'S': -1, 'T': -1, 'V': -1, 'W': -2, 'Y': -2},
    'D': {'A': -2, 'C': -3, 'D': 6,  'E': 2,  'F': -3, 'G': -1, 'H': -1, 'I': -3, 'K': -1, 'L': -4,
          'M': -3, 'N': 1,  'P': -1, 'Q': 0,  'R': -2, 'S': 0,  'T': -1, 'V': -3, 'W': -4, 'Y': -3},
    'E': {'A': -1, 'C': -4, 'D': 2,  'E': 5,  'F': -3, 'G': -2, 'H': 0,  'I': -3, 'K': 1,  'L': -3,
          'M': -2, 'N': 0,  'P': -1, 'Q': 2,  'R': 0,  'S': 0,  'T': -1, 'V': -2, 'W': -3, 'Y': -2},
    'F': {'A': -2, 'C': -2, 'D': -3, 'E': -3, 'F': 6,  'G': -3, 'H': -1, 'I': 0,  'K': -3, 'L': 0,
          'M': 0,  'N': -3, 'P': -4, 'Q': -3, 'R': -3, 'S': -2, 'T': -2, 'V': -1, 'W': 1,  'Y': 3},
    'G': {'A': 0,  'C': -3, 'D': -1, 'E': -2, 'F': -3, 'G': 6,  'H': -2, 'I': -4, 'K': -2, 'L': -4,
          'M': -3, 'N': 0,  'P': -2, 'Q': -2, 'R': -2, 'S': 0,  'T': -2, 'V': -3, 'W': -2, 'Y': -3},
    'H': {'A': -2, 'C': -3, 'D': -1, 'E': 0,  'F': -1, 'G': -2, 'H': 8,  'I': -3, 'K': -1, 'L': -3,
          'M': -2, 'N': 1,  'P': -2, 'Q': 0,  'R': 0,  'S': -1, 'T': -2, 'V': -3, 'W': -2, 'Y': 2},
    'I': {'A': -1, 'C': -1, 'D': -3, 'E': -3, 'F': 0,  'G': -4, 'H': -3, 'I': 4,  'K': -3, 'L': 2,
          'M': 1,  'N': -3, 'P': -3, 'Q': -3, 'R': -3, 'S': -2, 'T': -1, 'V': 3,  'W': -3, 'Y': -1},
    'K': {'A': -1, 'C': -3, 'D': -1, 'E': 1,  'F': -3, 'G': -2, 'H': -1, 'I': -3, 'K': 5,  'L': -2,
          'M': -1, 'N': 0,  'P': -1, 'Q': 1,  'R': 2,  'S': 0,  'T': -1, 'V': -2, 'W': -3, 'Y': -2},
    'L': {'A': -1, 'C': -1, 'D': -4, 'E': -3, 'F': 0,  'G': -4, 'H': -3, 'I': 2,  'K': -2, 'L': 4,
          'M': 2,  'N': -3, 'P': -3, 'Q': -2, 'R': -2, 'S': -2, 'T': -1, 'V': 1,  'W': -2, 'Y': -1},
    'M': {'A': -1, 'C': -1, 'D': -3, 'E': -2, 'F': 0,  'G': -3, 'H': -2, 'I': 1,  'K': -1, 'L': 2,
          'M': 5,  'N': -2, 'P': -2, 'Q': 0,  'R': -1, 'S': -1, 'T': -1, 'V': 1,  'W': -1, 'Y': -1},
    'N': {'A': -2, 'C': -3, 'D': 1,  'E': 0,  'F': -3, 'G': 0,  'H': 1,  'I': -3, 'K': 0,  'L': -3,
          'M': -2, 'N': 6,  'P': -2, 'Q': 0,  'R': 0,  'S': 1,  'T': 0,  'V': -3, 'W': -4, 'Y': -2},
    'P': {'A': -1, 'C': -3, 'D': -1, 'E': -1, 'F': -4, 'G': -2, 'H': -2, 'I': -3, 'K': -1, 'L': -3,
          'M': -2, 'N': -2, 'P': 7,  'Q': -1, 'R': -2, 'S': -1, 'T': -1, 'V': -2, 'W': -4, 'Y': -3},
    'Q': {'A': -1, 'C': -3, 'D': 0,  'E': 2,  'F': -3, 'G': -2, 'H': 0,  'I': -3, 'K': 1,  'L': -2,
          'M': 0,  'N': 0,  'P': -1, 'Q': 5,  'R': 1,  'S': 0,  'T': -1, 'V': -2, 'W': -2, 'Y': -1},
    'R': {'A': -1, 'C': -3, 'D': -2, 'E': 0,  'F': -3, 'G': -2, 'H': 0,  'I': -3, 'K': 2,  'L': -2,
          'M': -1, 'N': 0,  'P': -2, 'Q': 1,  'R': 5,  'S': -1, 'T': -1, 'V': -3, 'W': -3, 'Y': -2},
    'S': {'A': 1,  'C': -1, 'D': 0,  'E': 0,  'F': -2, 'G': 0,  'H': -1, 'I': -2, 'K': 0,  'L': -2,
          'M': -1, 'N': 1,  'P': -1, 'Q': 0,  'R': -1, 'S': 4,  'T': 1,  'V': -2, 'W': -3, 'Y': -2},
    'T': {'A': 0,  'C': -1, 'D': -1, 'E': -1, 'F': -2, 'G': -2, 'H': -2, 'I': -1, 'K': -1, 'L': -1,
          'M': -1, 'N': 0,  'P': -1, 'Q': -1, 'R': -1, 'S': 1,  'T': 5,  'V': 0,  'W': -2, 'Y': -2},
    'V': {'A': 0,  'C': -1, 'D': -3, 'E': -2, 'F': -1, 'G': -3, 'H': -3, 'I': 3,  'K': -2, 'L': 1,
          'M': 1,  'N': -3, 'P': -2, 'Q': -2, 'R': -3, 'S': -2, 'T': 0,  'V': 4,  'W': -3, 'Y': -1},
    'W': {'A': -3, 'C': -2, 'D': -4, 'E': -3, 'F': 1,  'G': -2, 'H': -2, 'I': -3, 'K': -3, 'L': -2,
          'M': -1, 'N': -4, 'P': -4, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V': -3, 'W': 11, 'Y': 2},
    'Y': {'A': -2, 'C': -2, 'D': -3, 'E': -2, 'F': 3,  'G': -3, 'H': 2,  'I': -1, 'K': -2, 'L': -1,
          'M': -1, 'N': -2, 'P': -3, 'Q': -1, 'R': -2, 'S': -2, 'T': -2, 'V': -1, 'W': 2,  'Y': 7}
}

def lcs(v, w):
    rows = len(v) + 1
    cols = len(w) + 1

    middle = [[0 for j in range(cols)] for i in range(rows)]  
    lower = [[0 for j in range(cols)] for i in range(rows)]  
    upper = [[0 for j in range(cols)] for i in range(rows)]  

    bMid = [['' for j in range(cols)] for i in range(rows)] 
    bLow = [['' for j in range(cols)] for i in range(rows)] 
    bUp = [['' for j in range(cols)] for i in range(rows)]    


    for i in range(1, len(middle)):
        for j in range(1, len(middle[0])):
            max_move = max(lower[i - 1][j] + beta, middle[i - 1][j] + alpha, 0)
            lower[i][j] = max_move
            if max_move == middle[i - 1][j] + alpha:
                bLow[i][j] = 'm'
            elif max_move == lower[i - 1][j] + beta:
                bLow[i][j] = 'l'
            else:
                bLow[i][j] = 'f'
            max_move = max(upper[i][j - 1] + beta, middle[i][j - 1] + alpha, 0)
            upper[i][j] = max_move
            if max_move == middle[i][j - 1] + alpha:
                bUp[i][j] = 'm'
            elif max_move == upper[i][j - 1] + beta:
                bUp[i][j] = 'u'
            else:
                bUp[i][j] = 'f'
            max_move = max(lower[i][j], upper[i][j], middle[i - 1][j - 1] + score[v[i - 1]][w[j - 1]], 0)
            middle[i][j] = max_move
            if max_move == middle[i - 1][j - 1] + score[v[i - 1]][w[j - 1]]:
                bMid[i][j] = 'm'
            elif max_move == upper[i][j]:
                bMid[i][j] = 'u'
            elif max_move == lower[i][j]:
                bMid[i][j] = 'l'
            else:
                bMid[i][j] = 'f'
            
    return (upper, middle, lower, bUp, bMid, bLow)

def traceBack(v, w, bUp, bMid, bLow, max_pos):
    i = max_pos[0]
    j = max_pos[1]
    main = bMid
    current = 'm'
    last_i, last_j = 0, 0
    while i > 0 and j > 0:   
        move = main[i][j]
        if move == 'm': 
            if current != 'u':  
                i -= 1
            if current != 'l':
                j -= 1
            main = bMid
            current = 'm'
        elif move == 'l': 
            if current != 'm':
                i -= 1
            main = bLow
            current = 'l'
        elif move == 'u':  
            if current != 'm':           
                j -= 1
            main = bUp
            current = 'u'
        else:
            last_i = i
            last_j = j
            break

    return (last_i, last_j)

            
amino1 = input().strip()
amino2 = input().strip()

result = lcs(amino1, amino2)

middle = result[1]

max_val = float('-inf')
max_pos = (0, 0)

for i in range(len(middle)):
    for j in range(len(middle[0])):
        if middle[i][j] > max_val:
            max_val = middle[i][j]
            max_pos = (i, j)

print(max_val)

(amino1_start, amino2_start) = traceBack(amino1, amino2, result[3], result[4], result[5], max_pos)

print(amino1[amino1_start:max_pos[0]])
print(amino2[amino2_start:max_pos[1]])



