def parseFASTA_from_file(filename):
    with open(filename) as f:
        data = f.read().split('>')[1:]  # split and remove empty chunk
        return {
            entry.split('\n', 1)[0]: entry.split('\n', 1)[1].replace('\n', '')
            for entry in data
        }

def tran(s1: str, s2: str):
    if len(s1) != len(s2):
        return 1
    
    transitions = {("A", "G"), ("G", "A"), ("C", "T"), ("T", "C")}
    transition = 0 
    transversion = 0
    for a, b in zip(s1, s2):
        if a==b:
            continue
        elif (a, b) in transitions:
            transition += 1
        else:
            transversion += 1

    return transition/transversion

fasta = parseFASTA_from_file("rosalind_tran (1).txt")
seqs = list(fasta.values())
print(tran(seqs[0], seqs[1]))
