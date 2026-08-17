from rosalind_utils import parseFASTA_from_file

def motz(s):
    n = len(s)
    base_pairs = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
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
            if base_pairs.get(s[i]) == s[k]:
                total += f(i+1, k-1) * f(k+1, j)

        total %= 1000000
        memo[(i, j)] = total
        return total

    return f(0, n-1)

if __name__ == "__main__":
    data = parseFASTA_from_file("data/rosalind_motz.txt")
    print(motz(list(data.values())[0]))