from rosalind_utils import read_input

def aspc(n, m):
    assert 0<=m<=n<=2000
    result = 0
    #sum C(n,k) for all subset sizes k from m to n
    for k in range(m, n+1):
        #compute C(n,k) iteratively, avoid factorials
        #builds up the result at each step, using the previous value of c to compute the next one
        c = 1
        for i in range(1, k+1):
            c = c * (n-i+1) // i
        result += c
    return result % 1000000

if __name__ == "__main__":
    n, m = map(int, read_input("data/rosalind_aspc.txt").split())
    print(aspc(n, m))