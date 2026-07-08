from rosalind_utils import parseFASTA_from_file

def long(strings):
    #greedy apprach to merge best overlapping pair until one string remains
    while len(strings) > 1:
        a, b, ov = best_overlap(strings)
        strings.remove(a)
        strings.remove(b)
        strings.append(a + b[ov:])
    return strings[0]

def best_overlap(strings):
    #finds the fair of strings with the largest overlap
    #best overlap tells which two reads should be mergeed
    best_a, best_b, best_len = None, None, 0
    for a in strings:
        for b in strings:
            if a == b:
                continue
            ov = overlap(a, b)
            if ov > best_len:
                best_a, best_b, best_len = a, b, ov
    return best_a, best_b, best_len

def overlap(a, b):
    #finds longest suffix a that matches prefix b
    #tells how much of b is covered by a
    max_overlap = 0
    for i in range(1, min(len(a), len(b) + 1)):
        if a[-i:] == b[:i]:
            max_overlap = i
    return max_overlap

if __name__ == "__main__":
    sequences = parseFASTA_from_file("data/rosalind_long.txt")
    strings = list(sequences.values())
    print(long(strings))