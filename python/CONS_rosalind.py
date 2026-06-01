import numpy as np

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
    
    return list(sequences.values())

def profileMatrix(sequences) -> dict:
    matrix = np.array([list(seq) for seq in sequences])

    profile = {
        'A': np.sum(matrix == 'A', axis=0),
        'C': np.sum(matrix == 'C', axis=0),
        'G': np.sum(matrix == 'G', axis=0),
        'T': np.sum(matrix == 'T', axis=0),
    }
    return profile

def consensusString(profile: dict) -> str:
    bases = 'ACGT'
    counts = np.vstack([profile[base]for base in bases])
    max_indicies = np.argmax(counts, axis=0)
    consensus = ''.join(bases[i] for i in max_indicies)
    return consensus

sequences = parseFASTA_from_file('rosalind_cons.txt')
profile_Matrix = profileMatrix(sequences)
consensus_String = consensusString(profile_Matrix)

print(consensus_String)
for base in 'ACGT':
    print(f"{base}: {' '.join(map(str, profile_Matrix[base]))}")