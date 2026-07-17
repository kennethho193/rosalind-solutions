from rosalind_utils import read_input

def eval(n, s, A):
    #n is positive integer
    #s is DNA string of even length at most 10 bp
    #A is an array of integers of length at most 20, each element between 0 to 1

    #return an array of floats of length n, where the ith element is the sum of the products of the ith element of A and the corresponding character in s, converted to a float
    result = []
    for i in A:
        gcProb = i/2
        atProb = (1-i)/2

        prob = 1
        for base in s:
            if base in "GC":
                prob *= gcProb
            if base in "AT":
                prob *= atProb

        result.append((n - len(s) + 1) * prob)
    return result

if __name__ == "__main__":
    data = read_input("data/rosalind_eval.txt").splitlines()
    n = int(data[0])
    s = data[1]
    A = list(map(float, data[2].split()))
    result = eval(n, s, A)
    print(" ".join(f'{val:.3f}'for val in result))