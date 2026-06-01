CODON_TABLE = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

def translateTranscribe(DNAs):
    #Separate out Main DNA, Intron 1 and Intron 2
    mainStr = DNAs[0]
    #print(mainStr)
   
    #Removing intron seq from DNA
    #could do this in rna but nothing changes and easier to do here
    for i in range(1, len(DNAs)):
        mainStr = mainStr.replace(DNAs[i], "")
    #print(mainStr)
   
    #Transcribes DNA to RNA
    rna = mainStr.replace("T", "U")
    #print(rna)
   
    #Translates RNA to Protein
    protein = ""
    for i in range(0, len(rna)-2, 3):
        codon = rna[i:i+3]
        aa = CODON_TABLE.get(codon)
        if aa == "Stop":
            break
        elif aa:
            protein += aa
   
    return protein

def read_input(filename):
    sequences = {}
    current_id = None
    realSeq = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                current_id = line[1:]
                sequences[current_id] = []
            else:
                sequences[current_id].append(line)
    for key in sequences:
        sequences[key] = "".join(sequences[key])
    for value in sequences.values():
        realSeq.append(value)
   
    return realSeq

sequences = read_input("rosalind_splc (2).txt")
#sequences = ["ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG", "ATCGGTCGAA", "ATCGGTCGAGCGTGT"]

print(translateTranscribe(sequences))
#print("MVYIADKQHVASREAYGHMFKVCA")
