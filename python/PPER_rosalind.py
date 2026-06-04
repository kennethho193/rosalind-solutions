from rosalind_utils import read_input
import math

def pper(n, k):
    """
    Given: POsitive integers n and k such taht 100 >= n > 0 and 10 >= k > 0
    Return: The total number of partial permutations P(n,k), modulo 1000000
    """
    #we divide n! by (n-k)! to get the number of partial permutations
    #As P(n, n) = n!, we can get the number of permutations with only k objects by dividing n! by the factorial of the difference between n and k, which is (n-k)!
    numPerms = math.factorial(n) // math.factorial(n-k)
    result = numPerms % 1000000
    return result

n, k = map(int, read_input("data/rosalind_pper.txt").split())
print(pper(n, k))