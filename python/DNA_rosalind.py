#testing

from rosalind_utils import read_input

def countingNucleotides(s: str):
    assert len(s) < 1000
    return s.count('A'), s.count('C'), s.count('G'), s.count('T')

dna = read_input("rosalind_dna (1).txt")
print(*countingNucleotides(dna))