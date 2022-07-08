import json

initial = json.loads(input())

with_children = {element['name']: [] for element in initial}

for eli in initial:
    for elc in with_children:
        if elc in eli['parents']:
            with_children[elc].append(eli['name'])

for element in with_children:
    with_children[element] = set(with_children[element])

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

for element in sorted(with_children.keys()):
    print(element, ':', len(dfs(with_children, element)))
