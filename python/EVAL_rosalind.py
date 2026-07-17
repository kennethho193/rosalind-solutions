from rosalind_utils import read_input

def eval(n, s, A):
    #n is length of random sting, s is target substring, A is list of GC content values
    result = []
    for x in A:
        gcProb = x/2
        atProb = (1-x)/2

        prob = 1
        for base in s:
            if base in "GC":
                prob *= gcProb
            if base in "AT":
                prob *= atProb
        #n-len(s)+1 possible starting positions for s in t
        #expected occurances = positions * P(match at one position)
        result.append((n - len(s) + 1) * prob)
    return result

if __name__ == "__main__":
    data = read_input("data/rosalind_eval.txt").splitlines()
    n = int(data[0])
    s = data[1]
    A = list(map(float, data[2].split()))
    result = eval(n, s, A)
    print(" ".join(f'{val:.3f}'for val in result))