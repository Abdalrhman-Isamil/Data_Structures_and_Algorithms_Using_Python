graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('G', 12)],
    'B': [('C', 2)],
    'C': [('G', 3),]
}

hTable = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 2,
    'G': 0
}

def pathHCost(path):
    gCost = 0
    for (node, cost) in path:
        gCost += cost
    lastNode = path[-1][0]
    hCost = hTable[lastNode]
    return hCost, lastNode

def pathCost(path):
    gCost = 0
    for (node, cost) in path:
        gCost += cost
    return gCost

def greedyBestFirstSearch(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=pathHCost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacentNodes = graph.get(node, [])
            for (node2, cost) in adjacentNodes:
                newPath = path.copy()
                newPath.append((node2, cost))
                queue.append(newPath)

path = greedyBestFirstSearch(graph, 'S', 'G')
print(f"Path is {path}")
print(f"Path cost is {pathCost(path)}")