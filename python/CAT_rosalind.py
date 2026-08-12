from rosalind_utils import parseFASTA_from_file

def cat(s):
    #dynammic programming approach
    n = len(s)
    matrix = [[0] * (n+1) for _ in range(n+1)]
    base_pairs = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}

    #base case 
    for i in range(n+1):
        matrix[i][i] = 1

    #technique of interval dynamic programming
    #outer loop is the interval size
    #middle loop slides interval across the string
    #inner loop attempts to find complement to s[i]
    for length in range(2, n+1, 2):
        for i in range(n-length+1):
            j = i + length
            for k in range(i+1, j+1, 2):
                if base_pairs.get(s[i]) == s[k]:
                    matrix[i][j] += matrix[i + 1][k] * matrix[k + 1][j]
                    matrix[i][j] %= 1000000
    return matrix[0][n]

if __name__ == "__main__":
    data = parseFASTA_from_file("data/rosalind_cat.txt")
    s = list(data.values())[0]
    print(cat(s))
