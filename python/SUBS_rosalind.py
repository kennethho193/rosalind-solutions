def read_input(file_path: str) -> str:
    """Reads the entire contents of a Rosalind input file as a string (stripped of trailing newlines)."""
    with open(file_path, 'r') as f:
        return f.read().strip().split()

def motifs(s: str, t: str):
    positions = []
    for i in range(0, len(s)-len(t)-1):
        if s[i:i+len(t)] == t:
            positions.append(i+1)
        else: 
            continue
    return ' '.join(map(str, positions))

string, substring = read_input('rosalind_subs.txt')
print(motifs(string, substring))