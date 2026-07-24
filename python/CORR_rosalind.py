from HAMM_rosalind import hammingDist
from REVC_rosalind import reverseComplement
from rosalind_utils import parseFASTA_from_file
from collections import Counter

def corr(seqDict):
    correct = set()
    incorrect = []
    #classify each read, correct if it or its reverse comp appears twice or more
    for seq, count in seqDict.items():
        if seqDict[seq] >= 2 or seqDict.get(reverseComplement(seq), 0) >= 2:
            correct.add(seq)
        else:
            incorrect.append(seq)

    results = []
    #generate all single base substitutions for bad reads
    #checks each candidate against the correct set
    for bad in incorrect:
        for i in range(len(bad)):
            for base in "ACGT":
                if base != bad[i]:
                    candidate = bad[:i] + base + bad[i+1:]
                    if candidate in correct:
                        results.append(f"{bad}->{candidate}")
                        break
                        #one correction per incorrect read
    return results

if __name__ == "__main__":
    #Counter counts occurances of each sequence across all FASTA entries of input file
    seqDict = Counter(parseFASTA_from_file("data/rosalind_corr.txt").values())
    results = corr(seqDict)
    with open("output/corr_output.txt", "w") as f:
        f.write('\n'.join(results))
    