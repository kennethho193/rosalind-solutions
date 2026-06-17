from rosalind_utils import read_input
import math

def perm(n):
    assert n<=7
    #number of permutations possible is n!
    numPerms = math.factorial(n)
    perms = []
    #for loop to generate each permutation without duplicates
    for i in range(numPerms):
        perm = []
        #available numbers to be used in the permutation
        available = list(range(1, n+1))
        #for loop to generate the permutation based on the index i
        for j in range(n):
            #calculate the index of the available number to be used in the permutation
            idx = (i // math.factorial(n-1-j)) % (n-j)
            perm.append(available[idx])
            #remove the used number from the available list
            del available[idx]
        #append the generated permutation to the list of permutations
        perms.append(perm)
    print(numPerms)
    for p in perms:
        print(' '.join(map(str, p)))

n = int(read_input("data/rosalind_perm.txt"))
perm(n)