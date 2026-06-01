import math

def read_input(file_path: str) -> str:
    #Will need to adjust if the input is not just one string
    """Reads the entire contents of a Rosalind input file as a string (stripped of trailing newlines)."""
    with open(file_path, 'r') as f:
        return map(int, f.read().strip().split())
    
def lia(k: int, N: int):
    #binomial formula needed
    probAaBb = 1/4
    probNotAaBb = 1-probAaBb
    total_offspring = 2**k

    prob = 0.0
    for i in range(0, N):
        binomial_coefficient = math.comb(total_offspring, i)
        prob += binomial_coefficient * probAaBb**i * probNotAaBb**(total_offspring-i)
    return 1 - prob

k, N = read_input('rosalind_lia.txt')
result = lia(k, N)
print(f"{result:.3f}")