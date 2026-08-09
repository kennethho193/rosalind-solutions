from rosalind_utils import parseFASTA_from_file, BLOSUM62

def glob(s, t):
    #taking structure from edit function
    #initialize matrix
    n, m = len(s), len(t)
    dp = [[0] * (m+1) for _ in range(n+1)]
    #base case, linear gap penalty of -5
    for i in range(n+1):
        dp[i][0] = i * -5
    for j in range(m+1):
        dp[0][j] = j * -5

    #fill table - dp[i][j] gives max alignment score
    #Blosum62 handles matches and subst. scores
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = max(dp[i-1][j-1] + BLOSUM62[s[i-1]][t[j-1]],  #match or subst.
                        dp[i][j-1] - 5,   #insertion, gap in s
                        dp[i-1][j] - 5)   #deletion, gap in t

    global_score = dp[n][m]
    return global_score

if __name__ == "__main__":
    data = parseFASTA_from_file("data/rosalind_glob.txt")
    seqs = list(data.values())
    print(glob(seqs[0], seqs[1]))