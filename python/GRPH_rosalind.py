from collections import defaultdict

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

def overlapSeq(sequences, k:int) ->list:
    adjList = []
    for seqID, seq in sequences.items():
        for seqID2, seq2 in sequences.items():
            if seq != seq2 and seq[-k:] == seq2[:k]:
                adjList.append((seqID,seqID2))
    return adjList

sequences = parseFASTA_from_file('rosalind_grph (1).txt')
k = 3

for a, b in overlapSeq(sequences, k):
    print(f"{a} {b}")
