from rosalind_utils import read_input

def inod(n):
    assert 3 <= n <= 10000
    #for a unrooted binary tree we can set up the unknowns: n = leaves, m = internal nodes
    #the total nodes would be n+m while total node degrees would be n+3m since each leaf has degree 1 and each internal node has degree 3
    #as the graph is a tree, we have n+m-1 edges and thus multiplying by 2 gives us the total node degrees, which is 2(n+m-1)
    #set up the equation n+3m = 2(n+m-1), which simplifies to m = n-2
    m = n - 2
    return m

data = read_input("data/rosalind_inod.txt").strip()
n = int(data)
print(inod(n))