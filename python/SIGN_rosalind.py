from rosalind_utils import read_input
import itertools

def sign(n):
    #generate all possible permutations of length n but each introducing signs to each element in the permutation as a factor
    results = []
    #itertools used to generate all permutations of the numbers from 1 to n and then itertools product used to generate all combinations of signs for each permutation
    for perm in itertools.permutations(range(1, n+1)):
        for signs in itertools.product([1, -1], repeat=n):
            #multiply each element by its sign to get full permutation with signs
            signed = [p * s for p, s in zip(perm, signs)]
            results.append(signed)
    return results


if __name__ == "__main__":
    n = int(read_input("data/rosalind_sign.txt").strip())
    results = sign(n)
    with open("output/rosalind_sign_output.txt", "w") as f:
        f.write(str(len(results)) + "\n")
        for r in results:
            f.write(" ".join(map(str, r)) + "\n")