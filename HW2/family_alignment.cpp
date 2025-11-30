//Faraz Doagooye Tehrani

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

int score(char first, char second) {
    return (first == second) ? 1 : -1;
}

vector< vector<int> > ga(const string &v, const string &w) {
    int rows = v.size() + 1;
    int cols = w.size() + 1;
    vector< vector<int> > S(rows, vector<int>(cols, INT_MIN/2));
    
    S[0][0] = 0;
    for (int i = 1; i < rows; i++) S[i][0] = -i;
    for (int j = 1; j < cols; j++) S[0][j] = -j;
    
    for (int i = 1; i < rows; i++) {
        for (int j = 1; j < cols; j++) {
            S[i][j] = max(max(
                S[i-1][j-1] + score(v[i-1], w[j-1]),
                S[i-1][j] - 1),
                S[i][j-1] - 1
            );
        }
    }
    return S;
}

int main() {
    string first;
    getline(cin, first);
    
    int n;
    cin >> n;
    cin.ignore();
    
    vector<string> strings(n);
    for (int i = 0; i < n; i++)
        getline(cin, strings[i]);
    
    int maxNum = INT_MIN;
    
    vector< vector< vector<int> > > prefixScores(n);
    vector< vector < vector<int> > > suffixScores(n);
    
    for (int i = 0; i < n; i++) {
        prefixScores[i] = ga(first, strings[i]);
    }
    
    string revFirst(first.rbegin(), first.rend());
    for (int i = 0; i < n; i++) {
        string revStr(strings[i].rbegin(), strings[i].rend());
        suffixScores[i] = ga(revFirst, revStr);
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int len1 = strings[i].size();
            int len2 = strings[j].size();
            int m = first.size();
            
            for (int k = 0; k <= m; k++) {
                int score1 = prefixScores[i][k][len1];
                int score2 = suffixScores[j][m-k][len2];
                maxNum = max(maxNum, score1 + score2);
            }
        }
    }
    
    cout << maxNum << "\n";
    return 0;
}
