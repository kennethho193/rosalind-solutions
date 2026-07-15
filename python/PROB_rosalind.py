import math

def GC(s, A):
    at, gc = 0, 0
    for base in s:
        if base == "G" or base == "C":
            gc += 1
        if base == "A" or base == "T":
            at += 1

    B = []
    for prob in A:
        gcProb = math.log10(prob/2)
        atProb = math.log10(((1-prob)/2))
        B.append((gc*gcProb) + (at*atProb))

    print(*B)

if __name__ == "__main__":
    DNA = "TACCCCGAGAGGCCCTATCGCTCTCCGAAGAGTGCGTGATACTTTCACACCAAACGGGTGGTCTGACAATCTTTCGCCCATTGTCTG"
    Array = [0.074, 0.125, 0.209, 0.219, 0.268, 0.334, 0.396, 0.428, 0.487, 0.551, 0.587, 0.648, 0.721, 0.771, 0.828, 0.856, 0.906]
    print(GC(DNA, Array))