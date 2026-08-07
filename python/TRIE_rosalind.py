from rosalind_utils import read_input

def trie(dna_strings):
    #building the trie of characters
    #each node is a dict, key is characters, and values are child nodes
    root = {}
    for dna in dna_strings:
        #start at root for each new string
        node = root
        for char in dna:
            if char not in node:
                #create new child node, signifies new character path
                node[char] = {}
            node = node[char]

    edges = []
    node_counter = [1]  #root is node 1, tracks next available node number

    #dfs alg to traverse the trie and collect edges
    def dfs(node, parent_num):
        #visit each character branch from the current node going depth first
        for char, child in node.items():
            node_counter[0] += 1
            child_num = node_counter[0]
            #assign number to the child node and record edge as parent to child connection with char label
            edges.append(f"{parent_num} {child_num} {char}")
            #recursion with child node to go deeper in branch before moving to next branch
            dfs(child, child_num)
    
    dfs(root, 1)
    return "".join(edge + "\n" for edge in edges)

if __name__ == "__main__":
    data = read_input("data/rosalind_trie.txt").strip().split("\n")
    result = trie(data)
    with open("output/trie_output.txt", "w") as f:
        f.write(result)