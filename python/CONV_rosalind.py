from rosalind_utils import read_input

def conv(s1, s2):
    counters = {}
    #get all differences btw s1 and s2
    for x in s1:
        for y in s2:
            diff = round(x-y, 5)
            counters[diff] = counters.get(diff, 0) + 1
    #finds the shift value x with the greatest multiplicity
    #multiplicity in this case is the number of times that difference appears
    max_count = max(counters.values())
    for diff, count in counters.items():
        if count == max_count:
            return f"{max_count}\n{abs(diff)}"

if __name__ == "__main__":
    data = read_input("data/rosalind_conv.txt")
    s1, s2 = data.split("\n")
    s1 = list(map(float, s1.split()))
    s2 = list(map(float, s2.split()))
    print(conv(s1, s2))