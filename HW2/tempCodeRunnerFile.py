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