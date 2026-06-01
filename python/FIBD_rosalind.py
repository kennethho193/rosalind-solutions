import numpy as np

def read_input(file_path: str) -> str:
    """Reads the entire contents of a Rosalind input file as a string (stripped of trailing newlines)."""
    with open(file_path, 'r') as f:
        return map(int, f.read().strip().split())
    
def fibd(n: int, m: int):
    population = np.zeros([n+1,m], dtype=np.int64)
    population[1][0] = 1
    
    for month in range(2,population.shape[0]):
        for age in range(0,population.shape[1]):
            if age == 0:
                population[month][age] = np.sum(population[month-1,1:])
            else:
                population[month][age] = population[month-1][age-1]
    return np.sum(population[n])

n, m = read_input('rosalind_fibd.txt')
print(fibd(n,m))