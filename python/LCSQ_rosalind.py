from rosalind_utils import parseFASTA_from_file

def lcsq(s, t):
    #Dynamic problem to find the longest common substring
    #initialize a n+1 x m+1 table with zeros
    n, m = len(s), len(t)
    table = [[0] * (m+1) for _ in range(n+1)]

    #fill table with the length of the LCS up to the string s[0:i] and t[0:j]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                #if characters match, extend LCS from the diagonal
                table[i][j] = table[i-1][j-1] + 1
            else:
                #if characters don't match, progress the best LCS from either direction
                table[i][j] = max(table[i-1][j], table[i][j-1])
    
    #tracing back as table[n][m] should be equal to the highest number (length of longest common substring)
    result = []
    i, j = n, m
    while i>0 and j>0:
        if s[i-1] == t[j-1]:
            #characters matched here, append the character to result and move diagonally up and left
            result.append(s[i-1])
            i -= 1
            j -= 1
        elif table[i-1][j] < table[i][j-1]:
            #LCS came from the left so move traceback left
            j -= 1
        else:
            #LCS came from above so move traceback up
            i -= 1
    #reverse result to get LCS as collection of characters was done in reverse            
    result.reverse()
    return ''.join(result)

if __name__ == "__main__":
    data = parseFASTA_from_file("data/rosalind_lcsq.txt")
    seqs = list(data.values())
    print(lcsq(seqs[0], seqs[1]))
    




