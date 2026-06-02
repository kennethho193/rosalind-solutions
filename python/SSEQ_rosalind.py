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

def sseq(s: str, t: str):
    positions = []
    t_index = 0
    s_index = 0
    while t_index < len(t) and s_index < len(s):
        if t[t_index] == s[s_index]:
            positions.append(s_index + 1)
            t_index += 1
        s_index += 1
        if t_index == len(t):
            break
    if t_index < len(t):
        return "Not a subsequence"
    return ' '.join(map(str, positions))

sequences = parseFASTA_from_file('data/rosalind_sseq.txt')
seqs= list(sequences.values())
s, t = seqs[0], seqs[1]
print(sseq(s, t))