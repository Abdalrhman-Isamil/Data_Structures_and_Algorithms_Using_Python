tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []
}

def dfs_recursive(tree, node, limit, visited=None):
    if visited is None:
        visited = set()  

    if limit < 0:
        return
    
    visited.add(node)    
    print(node, end=" ")        

    if limit == 0:
        return

    for child in tree[node]:  
        if child not in visited:
            dfs_recursive(tree, child, limit - 1, visited)

def ids(tree, node, limit):
    for i in range(limit + 1):
        print(f"\nlimit = {i}")
        dfs_recursive(tree, node, i)

ids(tree, 'A', 3)