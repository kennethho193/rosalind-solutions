from rosalind_utils import parseFASTA_from_file

#Given a collection of n being less than or equal to 10 DNA strings s1 to sn of equal length and such that the strings are given in FASTA format
#Return the matrix D corresponding to the p-distance dp on the given strings. as always not that your answer is allowed an abosolute error of 0.001
def pdst(DNA_str: list[str]):
    n = len(DNA_str)
    l = len(DNA_str[0])
    #initialize nxn istance matrix with 0.0
    D = [[0.0] * n for _ in range(n)]
    #nested loop to compute only upper triangle as matrix is symmetric along the diagonal which remains 0
    for i in range(n):
        for j in range(i+1, n):
            #count mismatches btw str i and j 
            count = sum(ci != cj for ci, cj in zip(DNA_str[i], DNA_str[j]))
            #p dist is proportion of mismatches over total string length so assign to both D[i][j] and D[j][i]
            D[i][j] = D[j][i] = count/l
    return D
                
sequences = parseFASTA_from_file("data/rosalind_pdst.txt")
DNA_list = list(sequences.values())
result = pdst(DNA_list)
for row in result:
     print(" ".join(f'{val:.5f}' for val in row))