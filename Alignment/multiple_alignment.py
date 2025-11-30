#Faraz Doagooye Tehrani 402105998
def score(first, second, third):
    if first == second == third:
        return 1
    else:
        return 0
    
def multiple_alignment(v, w, u):
    rows = len(v) + 1
    cols = len(w) + 1
    height = len(u) + 1

    S = [[[0 for _ in range(height)] for _ in range(cols)] for _ in range(rows)]  
    b = [[[(0, 0, 0) for _ in range(height)] for _ in range(cols)] for _ in range(rows)]  

    for i in range(1, len(S)):
        for j in range(1, len(S[0])):
            for k in range(1, len(S[0][0])):
                match_score = S[i-1][j-1][k-1] + score(v[i-1], w[j-1], u[k-1])

                move_2 = S[i-1][j-1][k]
                move_3 = S[i-1][j][k-1]
                move_4 = S[i][j-1][k-1]
                move_5 = S[i-1][j][k]
                move_6 = S[i][j-1][k]
                move_7 = S[i][j][k-1]
                
                max_score = match_score
                move = (1, 1, 1)

                if move_2 > max_score: max_score, move = move_2, (1, 1, 0)
                if move_3 > max_score: max_score, move = move_3, (1, 0, 1)
                if move_4 > max_score: max_score, move = move_4, (0, 1, 1)
                if move_5 > max_score: max_score, move = move_5, (1, 0, 0)
                if move_6 > max_score: max_score, move = move_6, (0, 1, 0)
                if move_7 > max_score: max_score, move = move_7, (0, 0, 1)

                S[i][j][k] = max_score
                b[i][j][k] = move
                
    return (S[len(S) - 1][len(S[0]) - 1][len(S[0][0]) - 1], b)

def printMulti(v, w, u, b):
    i = len(v)
    j = len(w)
    k = len(u)
    a1 = []
    a2 = []
    a3 = []

    while i > 0 or j > 0 or k > 0:
        if i == 0:
            a1.append('_')
            if j == 0:  
                a2.append('_')
            else:
                a2.append(w[j - 1])
                j -= 1
            if k == 0:
                a3.append("_")
            else:
                a3.append(u[k - 1])
                k -= 1
            continue
        if j == 0:
            a2.append('_')
            a1.append(v[i - 1])
            i -= 1
            if k == 0:
                a3.append("_")
            else:
                a3.append(u[k - 1])
                k -= 1
            continue
        if k == 0:
            a3.append("_")
            a1.append(v[i - 1])
            i -= 1            
            a2.append(w[j - 1])
            j -= 1
            continue

        move = b[i][j][k]
        if move[0] == 1:
            a1.append(v[i - 1])
            i -= 1
        else:
            a1.append('_')
        if move[1] == 1:
            a2.append(w[j - 1])
            j -= 1
        else:
            a2.append('_')
        if move[2] == 1:
            a3.append(u[k - 1])
            k -= 1
        else:
            a3.append('_')
            
    print(''.join(reversed(a1)))
    print(''.join(reversed(a2)))
    print(''.join(reversed(a3)))
    return

            
dna1 = input().strip()
dna2 = input().strip()
dna3 = input().strip()

result = multiple_alignment(dna1, dna2, dna3)

print(result[0])
printMulti(dna1, dna2, dna3, result[1])


