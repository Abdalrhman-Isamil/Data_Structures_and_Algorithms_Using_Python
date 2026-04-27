from collections import deque

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

def bfs(tree, start, goal):
    isFound = False
    path = ""
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            path += node + ' '
            if node == goal:
                isFound = True
                break

            for neighbor in tree[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    if isFound:
        print(path)
    else:
        print("Not Found")

bfs(tree, 'A', "Z")