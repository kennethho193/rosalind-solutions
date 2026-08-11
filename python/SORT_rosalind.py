from collections import deque
from rosalind_utils import read_input

def reversal(perm):
    #generates all possible reversals of a permutation
    #return (new_perm, i, j) so BFS can record which reversal was applied
    reversals = []
    n = len(perm)
    for i in range(n):
        for j in range(i+1, n):
            #reverses the subarray from i to j and append the new permutation
            new_perm = perm[:i] + perm[i:j+1][::-1] + perm[j+1:]
            reversals.append((new_perm, i, j))
    return reversals

def sort(p1, p2):
    start = tuple(p1)
    target = tuple(p2)

    if start == target:
        return 0

    #BFS
    #path carries history of i, j enpoints applied
    queue = deque([(start, 0, [])])
    visited = {start}

    while queue:
        curr_perm, dist, path = queue.popleft()
        for next_perm, i, j in reversal(curr_perm):
            next_perm = tuple(next_perm)
            #extend path with this reversal's endpoints
            new_path = path + [(i+1,j+1)]

            #target reached, return distance and reversal path
            if next_perm == target:
                return dist + 1, new_path

            #target not reached yet, ensure each perm only visited once 
            if next_perm not in visited:
                visited.add(next_perm)
                queue.append((next_perm, dist + 1, new_path))

    return dist, path

if __name__ == "__main__":
    data = read_input("data/rosalind_sort.txt").strip().split('\n')
    p1 = list(map(int, data[0].split()))
    p2 = list(map(int, data[1].split()))
    dist, path = sort(p1, p2)
    print(dist)
    for i, j in path:
        print(i, j)