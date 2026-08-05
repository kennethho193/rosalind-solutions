from rosalind_utils import read_input, MONOISOTOPIC_MASS

def spec(l) -> str:
    result = []
    for i in range(1, len(l)):
        #diff btw consecutive masses give individual amino acid masses
        diff = l[i] - l[i-1]
        #iterate over the monoisotopic table to find matching amino acid
        for aa, aa_mass in MONOISOTOPIC_MASS.items():
            #handle floating point precision
            if abs(diff - aa_mass) < 0.001:
                result.append(aa)
                break
    return "".join(result)

if __name__ == "__main__":
    data = read_input("data/rosalind_spec.txt")
    data = list(map(float, data.split()))
    result = spec(data)
    print(result)