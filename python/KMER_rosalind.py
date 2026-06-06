from LEXF_rosalind import lexf
from rosalind_utils import read_input

def k_mer(s: str, k: int) -> list:
    characters = ['A', 'C', 'G', 'T']
    #generate all possible k-mers reusing the lexf function
    kmers = lexf(characters, k)
    #create a dictionary to count the occurrences of each k-mer in  s, initializing counts at 0
    kmerDict = {item: 0 for item in kmers}
    #sliding window of size k to count occurences of each k-mer in s
    for i in range(len(s)-k+1):
        kmerDict[s[i:i+k]] += 1
    return ' '.join(map(str, list(kmerDict.values())))

data = read_input("data/rosalind_kmer.txt").split('\n')
s = ''.join(data[1:])
k = 4
print(k_mer(s, k))
