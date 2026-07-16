from rosalind_utils import read_input

def rstr(N, x, s):
    #N is number of random DNA strings, x is the GC content, and s is the DNA string
    #find probability that at least one of the N random strings equals s
    gcProb = x/2
    atProb = (1-x)/2

    #multiply probabilities across each base to get P(one random string == s)
    prob = 1
    for base in s:
        if base == "G" or base == "C":
            prob *= gcProb
        if base == "A" or base == "T":
            prob *= atProb
    #use complement rule: easier to calculate P(no matches in N strings) = (1-prob)^N
    #then P(at least one match) = 1 - (1-prob)^N since each string is independent
    return 1 - (1 - prob)**N

if __name__ == "__main__":
    data = read_input("data/rosalind_rstr.txt").splitlines()
    N, x = map(float, data[0].split())
    N = int(N)
    s = data[1]
    print(f"{rstr(N, x, s):.3f}")