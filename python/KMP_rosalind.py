from rosalind_utils import parseFASTA_from_file

def kmp(s):
    n = len(s)
    failure = [0] * n
    #failure array keeps track of the length of the longest proper prefix which is also a suffix for each prefix of the string

    #j keeps track of the length of the current matching prefix
    j = 0
    i = 1
    while i < n:
        if s[i] == s[j]:
            #current character extends the prefix match, updating length and incrementing indices
            failure[i] += j + 1
            j += 1
            i += 1
        elif j > 0:
            #mismatch but j > 0, so we fall back to the previous longest valid prefix
            j = failure[j-1]
        else:
            #mismatch and j == 0, so no valid prefix, set failure[i] to 0
            failure[i] = 0
            i += 1
    
    return failure

if __name__ == "__main__":
    data = parseFASTA_from_file("data/rosalind_kmp.txt")
    s = list(data.values())[0]
    result = ' '.join(map(str, kmp(s)))
    with open("output/kmp_output.txt", "w") as f:
        f.write(result)

        
        

