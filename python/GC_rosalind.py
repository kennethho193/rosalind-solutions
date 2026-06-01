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


def gcContent(s):
    if len(s) == 0:
        return 0.0
    gc_count = 0
    for base in s:
        if base == 'G' or base =='C':
            gc_count +=1
    gc_percent = (gc_count / len(s)) * 100
    return gc_percent

sequences = parseFASTA_from_file('rosalind_gc.txt')

max_id = None
max_gc = 0
for seq_id, seq in sequences.items():
    gc = gcContent(seq)
    if gc > max_gc:
        max_gc = gc
        max_id = seq_id

print(max_id)
print(f"{max_gc:.6f}")