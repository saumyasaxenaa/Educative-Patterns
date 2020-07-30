'''
Algorithm
1. Initialize the graph
2. Build the graph
3. Find all sources ie., vertices with 0 in-degrees
4. Add each source to the sorted list and subtract one from all of its children,
if a child's in-degree becomes 0, add it to the source queue
'''

from collections import deque

def TopologicalSort(v,e):
    sortedList = []
    if v <= 0:
        return sortedList

    # Initialize the graph
    inDegrees = {i:0 for i in range(v)}
    graph = {i:[] for i in range(v)}

    # Build the graph
    for edge in e:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        inDegrees[child] += 1

    # Find all sources
    sources = deque()
    for key in inDegrees:
        if inDegrees[key] == 0:
            sources.append(key)

    while sources:
        vertex = sources.popleft()
        sortedList.append(vertex)
        for child in graph[vertex]:
            inDegrees[child] -= 1
            if inDegrees[child] == 0:
                sources.append(child)

    if len(sortedList) != v:
        return []

    return sortedList

print(TopologicalSort(5,[[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]))
