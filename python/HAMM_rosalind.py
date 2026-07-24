def hammingDist(s: str, t: str):
    count = 0
    for a, b in zip(s,t):
        if a != b:
            count +=1
    return count

def parseHammingStrings(filename):
    with open(filename, 'r') as f:
        line = f.read().strip().split('\n')
        line1 = line[0]
        line2 = line[1]
    return line1, line2

if __name__ == "__main__":
    line1, line2 = parseHammingStrings('rosalind_hamm.txt')
    print(hammingDist(line1,line2))