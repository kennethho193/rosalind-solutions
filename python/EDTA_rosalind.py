from rosalind_utils import parseFASTA_from_file

def edta(s, t):
    #taking logic from edit function
    #initialize matrix
    n, m = len(s), len(t)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j

    #fill table
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:                
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],  #deletion
                                  dp[i][j-1],   #insertion
                                  dp[i-1][j-1]) #substitution
    edit_dist = dp[n][m]

    #edta: return edit distance, and both augmented strings representing optimal alignment of s and t
    s_aug, t_aug = "", ""
    i, j = n, m
    while i > 0 and j > 0:
        if s[i-1] == t[j-1] or dp[i][j] == dp[i-1][j-1] + 1:
            #match or substitution — move diagonally
            s_aug = s[i-1] + s_aug
            t_aug = t[j-1] + t_aug
            i -= 1
            j -= 1
        elif dp[i-1][j] < dp[i][j-1]:
            #deletion from s, s gets char, t gets gap -
            s_aug = s[i-1] + s_aug
            t_aug = "-" + t_aug
            i -= 1
        else:
            #insertion into s, t gets char and s gets gap -
            t_aug = t[j-1] + t_aug
            s_aug = "-" + s_aug
            j -= 1   

    #adds any potential remaing char from either string
    while i > 0:
        s_aug = s[i-1] + s_aug
        i -= 1
    while j > 0:
        t_aug = t[j-1] + t_aug
        j -= 1

    return f"{edit_dist}\n{s_aug}\n{t_aug}"

if __name__ == "__main__":
    data = parseFASTA_from_file("data/rosalind_edta.txt")
    seqs = list(data.values())
    print(edta(seqs[0], seqs[1]))
    