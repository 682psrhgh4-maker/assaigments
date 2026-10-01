from collections import deque
import heapq


grid = [
    ['S', '.', '.', '#', '.', '.'],
    ['.', '#', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '#'],
    ['.', '#', '#', '#', '.', '.'],
    ['.', '.', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.', 'G']
]

start = (0, 0)
goal = (5, 5)



def neighbors(cell):
    r, c = cell

    directions = [
        (-1, 0),   # жоғары
        (1, 0),    # төмен
        (0, -1),   # солға
        (0, 1)     # оңға
    ]

    result = []

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < 6 and 0 <= nc < 6:
            if grid[nr][nc] != '#':
                result.append((nr, nc))

    return result



def bfs():

    queue = deque([start])

    parent = {start: None}

    expanded = 0

    while queue:

        current = queue.popleft()
        expanded += 1

        if current == goal:
            break

        for next_cell in neighbors(current):

           if next_cell not in parent:
                parent[next_cell] = current
                queue.append(next_cell)


    path = []

    current = goal

    while current is not None:
        path.append(current)
        current = parent.get(current)

    path.reverse()

    cost = len(path) - 1

    return path, cost, expanded



def heuristic(cell):

    r, c = cell

    return abs(r - 5) + abs(c - 5)



def astar():

    queue = []

    heapq.heappush(queue, (0, start))

    parent = {start: None}

    g = {start: 0}

    expanded = 0

    while queue:

        f, current = heapq.heappop(queue)

        expanded += 1

        if current == goal:
            break

        for next_cell in neighbors(current):

            new_g = g[current] + 1

            if next_cell not in g or new_g < g[next_cell]:

                g[next_cell] = new_g
                parent[next_cell] = current

                f = new_g + heuristic(next_cell)

                heapq.heappush(
                    queue,
                    (f, next_cell)
                )


    path = []

    current = goal

    while current is not None:
        path.append(current)
        current = parent.get(current)

    path.reverse()

    cost = len(path) - 1

    return path, cost, expanded



bfs_path, bfs_cost, bfs_expanded = bfs()

print("BFS")
print("Жол:", bfs_path)
print("Жол құны:", bfs_cost)
print("Кеңейтілген түйіндер:", bfs_expanded)



astar_path, astar_cost, astar_expanded = astar()

print("A*")
print("Жол:", astar_path)
print("Жол құны:", astar_cost)
print("Кеңейтілген түйіндер:", astar_expanded)
