from rosalind_utils import read_input

def lexf(s, n):
    #generate all possible strings of length n ordered lexicographically using s as the alphabet
    if n == 0: 
        return [""]
    #initialize an empty list to store the results
    results = []
    #for loop to get strings of length n-1 and append each character in s to the front of each string
    for c in s:
        #recursive call to get strings of length n-1
        for suffix in lexf(s, n-1):
            results.append(c + suffix)
    return results


data = read_input("data/rosalind_lexf.txt").split('\n')
s = data[0].split()
n = int(data[1])
results = lexf(s, n)
#.join the results with newlines and print them
print("\n".join(results))