def rabbitFib(n: int, k: int) -> int:
    assert 0<=n<= 40 and 0<=k<=5
    if n == 1 or n ==2:
        return 1
    a, b = 1, 1
    for i in range(3, n+1):
        a, b = b, b + k*a
    return b

def read_input(path: str):
    with open(path) as f:
        return map(int,f.read().strip().split())
    
n, k = read_input('rosalind_fib (1).txt')
print(rabbitFib(n,k))