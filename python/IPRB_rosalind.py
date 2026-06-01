def read_input(file_path: str) -> str:
    """Reads the entire contents of a Rosalind input file as a string (stripped of trailing newlines)."""
    with open(file_path, 'r') as f:
        return map(int, f.read().strip().split())
    
def probabilityOfDominantAllele(k: int, m: int, n: int):
    total = k + m + n

#when k*k, 100% dominant, 0% recessive
#when k*m, 100% dominant, 0% recessive
#When k*n, 100% dominant, 0% recessive
#When m*m, 75% dominant, 25% recessive
#When m*n, 50% dominant, 50% recessive
#When n*n, 0% dominant, 100% recessive

    probabilityMM = 0.25*((m/total)*(m-1)/(total-1))
    probabilityMN = 0.50*((m/total)*(n)/(total-1))
    probabilityNM = 0.50*((n/total)*(m)/(total-1))
    probabilityNN = ((n/total)*(n-1)/(total-1))

    return 1- (probabilityMM + probabilityMN + probabilityNM + probabilityNN)

k, m, n = read_input('rosalind_iprb.txt')
print(probabilityOfDominantAllele(k, m, n))
    