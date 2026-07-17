import rosalind_utils
from REVC_rosalind import reverseComplement
from RNA_rosalind import RNAtransform

#Aim to find every distinct protein string that can be translated from a given string

def find_orf(rna: str, orfs: set):
    #search the 3 reading frames of a given strand
    for i in range(3):
        for j in range(i, len(rna)-2, 3):
            if rna[j:j+3] != "AUG":
                continue
            #found start codon, read forward in triplets until amino acid is a stop codon
            protein = []
            for k in range(j, len(rna)-2, 3):
                amino_acid = rosalind_utils.CODON_TABLE.get(rna[k:k+3], '')
                if amino_acid == 'Stop':
                    if protein:
                        orfs.add("".join(protein))
                    break
                elif amino_acid:
                    protein.append(amino_acid)

def orf(dna:str):
    orfs = set()
    #search forward and reverse strand, 6 reading frames total
    find_orf(RNAtransform(dna), orfs)
    find_orf(RNAtransform(reverseComplement(dna)), orfs)
    return "\n".join(orfs)

if __name__ == "__main__":
    sequences = rosalind_utils.parseFASTA_from_file('data/rosalind_orf.txt')
    dna = list(sequences.values())[0]
    print(orf(dna))