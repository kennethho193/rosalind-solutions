import math

def parseFASTA_from_file(filename):
    sequences = {}
    current_id = None
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                current_id = line[1:]
                sequences[current_id] = []
            else:
                sequences[current_id].append(line)
    
    for key in sequences:
        sequences[key] = ''.join(sequences[key])
    return sequences

def pmch(s):
    """
    Given: An RNA string s
    of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

    Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s
    """
    a = s.count('A')
    c = s.count('C')
    return math.factorial(a) * math.factorial(c)
    
sequences = parseFASTA_from_file('data/rosalind_pmch.txt')
for seqID, seq in sequences.items():
    print(pmch(seq))