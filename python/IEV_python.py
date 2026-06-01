def read_input(file_path: str) -> str:
    """Reads the entire contents of a Rosalind input file as a string (stripped of trailing newlines)."""
    with open(file_path, 'r') as f:
        return list(map(int, f.read().strip().split()))
    
def iev(numbers):
    #when k*k, 100% dominant, 0% recessive
    #when k*m, 100% dominant, 0% recessive
    #When k*n, 100% dominant, 0% recessive
    #When m*m, 75% dominant, 25% recessive
    #When m*n, 50% dominant, 50% recessive
    #When n*n, 0% dominant, 100% recessive
    probDom = [1, 1, 1, 0.75, 0.5, 0]

    avgOffSpringDom = 0
    for n,w in zip(numbers, probDom):
        avgOffSpringDom += (n*2*w)

    return avgOffSpringDom

numbers = read_input('rosalind_iev.txt')
print(iev(numbers))
