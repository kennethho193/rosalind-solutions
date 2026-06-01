from rosalind_utils import read_input

def RNAtransform(t: str):
    assert len(t)<1000
    r = ''
    for nucleotide in t:
        if nucleotide != 'T':
            r += nucleotide
        elif nucleotide == 'T':
            r += "U"
        else:
            continue
    return r

rna = read_input('rosalind_rna.txt')
print(RNAtransform(rna))