from rosalind_utils import read_input

def rstr(N, x, s):
    #N is number of random DNA strings, x is the GC content, and s is the DNA string
    gcProb = x/2
    atProb = (1-x)/2
    prob = 1
    for base in s:
        if base == "G" or base == "C":
            prob *= gcProb
        if base == "A" or base == "T":
            prob *= atProb
    return 1 - (1 - prob)**N

if __name__ == "__main__":
    data = read_input("data/rosalind_rstr.txt").splitlines()
    N, x = map(float, data[0].split())
    N = int(N)
    s = data[1]
    print(f"{rstr(N, x, s):.3f}")