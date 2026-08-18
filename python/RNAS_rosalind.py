from rosalind_utils import read_input

def rnas(s):
    n = len(s)
    #wobble pairing allows for U-G matching
    base_pairs = {'A': ['U'], 'U': ['A', 'G'], 'C': ['G'], 'G': ['C', 'U']}
    memo = {}

    def f(i, j):
        #empty interval (i > j) has exactly 1 way: the empty matching
        if i > j:
            return 1
        if (i, j) in memo:
            return memo[(i, j)]

        #case 1: s[i] is unmatched
        total = f(i + 1, j)

        #case 2: s[i] is complementary to s[k]
        for k in range(i+1, j+1):
            #k-i >= 4 ensures that there are at least 3 unpaired nucleotides between the paired nucleotides, which is a requirement for valid RNA secondary structures
            if k-i >= 4 and s[k] in base_pairs.get(s[i], []):
                total += f(i+1, k-1) * f(k+1, j)

        memo[(i, j)] = total
        return total
    return f(0, n-1)

if __name__ == "__main__":
    data = read_input("data/rosalind_rnas.txt")
    print(rnas(data))