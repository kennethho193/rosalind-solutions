import requests
from rosalind_utils import read_input

def mprt(id, conditions):
    """
    since we are given a list of IDs, we can loop through for each ID
    Maybe have something that deciphers the N{P}[ST]{P} as the thing we are looking for and sliding window through each item in the list
    Rules: {} means anything but that, [] is any letter in that
    """
    sequence = uniProtID(id)
    positions = []
    n = len(conditions)
    for i in range(len(sequence) - n + 1):
        if all(conditions[j](sequence[i+j]) for j in range(n)):
            positions.append(i+1)
    return " ".join(map(str,positions))

def uniProtID(id):
    clean_id = id.split("_")[0]
    url = f"http://www.uniprot.org/uniprot/{clean_id}.fasta"
    fasta = requests.get(url).text
    lines = fasta.split("\n")
    sequence = "".join(lines[1:])
    return sequence

def parse_motif(motif):
    conditions = []
    i = 0
    while i < len(motif):
        if motif[i] == "{":
            j = motif.index('}', i)
            exclude = motif[i+1:j]
            conditions.append(lambda c, ex = exclude: c not in ex)
            i = j + 1
        elif motif[i] == "[":
            j = motif.index(']', i)
            include = motif[i+1:j]
            conditions.append(lambda c, inc = include: c in inc)
            i = j + 1
        else:
            conditions.append(lambda c, ch = motif[i]: c == ch)
            i += 1
    return conditions

#print(mprt("B5ZC00"))

protein_ids = read_input("data/rosalind_mprt.txt").strip().split("\n")
motif = "N{P}[ST]{P}"
conditions = parse_motif(motif)

for pid in protein_ids:
    result = mprt(pid, conditions)
    if result:
        print(pid)
        print(result)