from rosalind_utils import read_input

def scsp(s:str, t:str) -> str:
    n, m = len(s), len(t)
    #initialize (n+1) x (m+1) DP table with zeros
    #extra row and column represent the empty string base case
    table = [[0] * (m+1) for _ in range(n+1)]
 
    #fill table — table[i][j] = length of LCS of s[0:i] and t[0:j]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                #characters match — extend the LCS from the diagonal
                table[i][j] = table[i-1][j-1] + 1
            else:
                #no match — carry forward the best LCS from either direction
                table[i][j] = max(table[i-1][j], table[i][j-1])
 
    #traceback collecting ALL characters from both strings
    #follow the path that built the table in reverse
    result = []
    i, j = n, m
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            #characters matched here — include in result and move diagonally
            result.append(s[i-1])
            i -= 1
            j -= 1
        elif table[i-1][j] < table[i][j-1]:
            #better LCS came from the left — move left
            result.append(t[j-1])
            j -= 1
        else:
            #better LCS came from above — move up
            result.append(s[i-1])
            i -= 1

    #adds any remaining chaaracters from either string not included yet
    while i > 0:
        result.append(s[i-1])
        i -= 1
    while j > 0:
        result.append(t[j-1])
        j -= 1

    result.reverse()
    return ''.join(result)

if __name__ == "__main__":
    data = read_input("data/rosalind_scsp.txt").strip().split('\n')
    s = data[0]
    t = data[1]
    print(scsp(s, t))

