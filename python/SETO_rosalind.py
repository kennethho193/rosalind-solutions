from rosalind_utils import read_input

def union(set1, set2):
    result = set1 | set2
    return result
def intersection(set1, set2):
    result = set1 & set2
    return result
def setDifference(set1, set2):
    result = set1 - set2
    return result
def setComplement(n, set1):
    setU = set(range(1, n+1))
    setC = setDifference(setU, set1)
    return setC

if __name__ == "__main__":
    data = read_input("data/rosalind_seto.txt").split("\n")
    n = int(data[0])
    A = set(map(int, data[1].strip("{}").split(",")))
    B = set(map(int, data[2].strip("{}").split(",")))

    results = [
        union(A, B),
        intersection(A, B),
        setDifference(A, B),
        setDifference(B, A),
        setComplement(n, A),
        setComplement(n, B)
    ]
    
    with open("output/seto_output.txt", "w") as f:
        for r in results:
            f.write(str(r) + "\n")