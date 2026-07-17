from rosalind_utils import read_input

def sset(n):
    #for each elements in n, independently choose to include or exclude it
    #gives 2 choices for each element
    return (2**n) % 1000000

if __name__ == "__main__":
    n = int(read_input("data/rosalind_sset.txt").strip())
    print(sset(n))