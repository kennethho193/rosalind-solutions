from rosalind_utils import parseFASTA_from_file

def edit(s, t):
    n, m = len(s), len(t)
    #initializing matrix (n+1) x (m+1), time complexity O(n*m)
    #allows us to efficiently compute the edit dist using dynamic programming. 
    dp = [[0] * (m+1) for _ in range(n+1)]
    #these loops initialize the first row and column as the indices, handles base case of empty strings as well
    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j

    #fill table
    for i in range(1, n+1):
        for j in range(1, m+1):
            #if char match, no operation needed and set current matrix index as equal to the upper left diagonal
            if s[i-1] == t[j-1]:                
                dp[i][j] = dp[i-1][j-1]
            #if char not match, add 1 to the minimum of the three possible operations 
            else:
                dp[i][j] = 1 + min(dp[i-1][j],  #deletion
                                  dp[i][j-1],   #insertion
                                  dp[i-1][j-1]) #substitution

    return dp[n][m]

if __name__ == "__main__":
    data = parseFASTA_from_file("data/rosalind_edit.txt")
    seqs = list(data.values())
    print(edit(seqs[0], seqs[1]))