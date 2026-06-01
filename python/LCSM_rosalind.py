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

def longestCommonSub(sequences):
    shortest_string = None
    for value in sequences.values():
        if isinstance(value, str):
            if shortest_string is None or len(value) < len(shortest_string):
                shortest_string = value

    for length in range(len(shortest_string), 0, -1):
        for start in range(len(shortest_string) - length + 1):
            longestCommonSubstring = shortest_string[start:start+length]
            if all(longestCommonSubstring in seq for seq in sequences.values()):
                return longestCommonSubstring


sequences = parseFASTA_from_file('rosalind_lcsm (1).txt')
print(longestCommonSub(sequences))