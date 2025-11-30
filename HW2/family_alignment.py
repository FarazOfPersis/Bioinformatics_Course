#Faraz Doagooye Tehrani 402105998

def score(first, second):
    if first == second:
        return 1
    return -1

def ga(v, w):
    rows = len(v) + 1
    cols = len(w) + 1

    S = [[0 for _ in range(cols)] for _ in range(rows)]  
    for i in range(len(S)):
        S[i][0] = -1 * i
    for i in range(len(S[0])):
        S[0][i] = -1 * i

    for i in range(1, len(S)):
        for j in range(1, len(S[0])):
            S[i][j] = max(S[i - 1][j] - 1, S[i][j - 1] - 1, 
                           S[i - 1][j - 1] + score(v[i - 1], w[j - 1]))

    return S

            
first = input().strip()
maxNum = [float('-inf')] * (len(first) + 1)
maxNum_Reversed = [float('-inf')] * (len(first) + 1)
maxFinal = float('-inf')
num = int(input())

strings = []
result = []
result_rev = []
for i in range(num):
    strings.append(input().strip())

for string in strings:
    result = ga(first, string)
    result_rev = ga(''.join(reversed(first)), ''.join(reversed(string)))



for i in range(1, len(first) + 1):
    if maxNum[i] + maxNum_Reversed[len(first) - i] > maxFinal:
        maxFinal = maxNum[i] + maxNum_Reversed[len(first) - i]

print(maxFinal)


