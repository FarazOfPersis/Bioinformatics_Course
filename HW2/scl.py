#Faraz Doagooye Tehrani 402105998

def score(first, second):
    if first == second:
        return 3
    else:
        return -10**15


def lcs(v, w):
    rows = len(v) + 1
    cols = len(w) + 1

    S = [[0 for j in range(cols)] for i in range(rows)]  
    b = [[0 for j in range(cols)] for i in range(rows)]    
    #it gets 0 for up, 1 for left and 2 for diagonal
    for i in range(len(S)):
        S[i][0] = -1 * i
    for i in range(len(S[0])):
        S[0][i] = -1 * i

    for i in range(1, len(S)):
        for j in range(1, len(S[0])):
            max_move = max(S[i - 1][j] - 1, S[i][j - 1] - 1, S[i - 1][j - 1] + score(v[i - 1], w[j - 1]))
            S[i][j] = max_move
            if max_move == S[i - 1][j - 1] + score(v[i - 1], w[j - 1]):
                b[i][j] = 2
            elif max_move == S[i - 1][j] - 1:
                b[i][j] = 0
            else:
                b[i][j] = 1
    return (S[len(S) - 1][len(S[0]) - 1], b, S)

def printnum(v, w, b):
    i = len(v)
    j = len(w)
    num = 0

    while i > 0 or j > 0:
        if i == 0:
            num += 1
            j -= 1
        elif j == 0:
            num += 1
            i -= 1
        else :
            move = b[i][j]
            if move == 2:     
                i -= 1
                j -= 1
            elif move == 0:   
                num += 1
                i -= 1
            else:              
                num += 1
                j -= 1
    return num
 
first = input().strip()
second = input().strip()

result = lcs(first, second)

print(printnum(first, second, result[1]))


