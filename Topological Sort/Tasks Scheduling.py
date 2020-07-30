from collections import deque

def TasksScheduling(tasks,e):
    sortedList = []
    if tasks <= 0:
        return sortedList

    inDegree = {i:0 for i in range(tasks)}
    graph = {i:[] for i in range(tasks)}

    for edge in e:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        inDegree[child] += 1

    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    while sources:
        vertex = sources.popleft()
        sortedList.append(vertex)
        for child in graph[vertex]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    if len(sortedList) != tasks:
        return False

    return True

print(TasksScheduling(6,[[2, 5], [0, 5], [0, 4], [1, 4], [3, 2
], [1, 3]]))
