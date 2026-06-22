from rosalind_utils import parseFASTA_from_file
from REVC_rosalind import reverseComplement

def revp(dna):
    #check every position in string as potential start of palindrome
    for i in range(0, len(dna)-1):
        #check all valid palindrome lengths (4-12 as specified in this problem)
        for j in range(4, 13):
            #breaks out of loop if substring would extend past length of the string
            if i+j>len(dna):
                break
            substring = dna[i:i+j]
            if substring == reverseComplement(substring):
                print(str(i+1) + " " + str(j))
    return

if __name__ == "__main__":
    dna = list(parseFASTA_from_file("data/rosalind_revp.txt").values())[0]
    revp(dna)