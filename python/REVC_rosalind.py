from rosalind_utils import read_input

def reverseComplement(s: str) -> str:
    assert len(s) <= 1000
    complement_table = str.maketrans("ACGT", "TGCA")
    return s.translate(complement_table)[::-1]

if __name__ == "__main__":
    revc = read_input('rosalind_revc (1).txt')
    print(reverseComplement(revc))