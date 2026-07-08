from rosalind_utils import read_input

def lis(perm_seq, increasing=True):
    n = len(perm_seq)
    #dp[i] holds length of longest inc/dec subseq ending at position i
    #every element is at a minimum a subsequence of length 1
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            #check all prev positions to see if we can extend the subsequence
            #increasing=True param uses "<" for increasing and False uses ">" for decreasing
            if (perm_seq[j] < perm_seq[i]) == increasing:
                dp[i] = max(dp[i], dp[j] + 1)

    #reconstruct the subsequence by tracing back through dp
    #starts at position where the longest subsequence ends and works backwards to find the previous elements
    max_len = max(dp)
    result = []
    i = dp.index(max_len) 
    result.append(perm_seq[i])

    #walk backwards, looking for j where perm_seq[j] satisfies the order condition and dp[j] is one less than the current max_len
    while max_len > 1:
        for j in range(i-1, -1, -1):
            if (perm_seq[j] < perm_seq[i]) == increasing and dp[j] == max_len - 1:
                result.append(perm_seq[j])
                i = j
                max_len -= 1
                break

    #reverse bc elements were collected in reverse order
    result.reverse()
    return result

def LGIS(n, perm_seq):
    #find both longest increasing and decreasing subsequences
    print(' '.join(map(str, lis(perm_seq, increasing=True))))
    print(' '.join(map(str, lis(perm_seq, increasing=False))))

if __name__ == "__main__":
    data = read_input("data/rosalind_lgis.txt").strip().split('\n')
    n = int(data[0])
    perm_seq = list(map(int, data[1].split()))
    LGIS(n, perm_seq)