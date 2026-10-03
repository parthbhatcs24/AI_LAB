
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


def get_neighbors(state):
    neighbors = []

    blank = state.index(0)
    row = blank // 3
    col = blank % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r = row + dr
        c = col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_blank = r * 3 + c

            new_state = list(state)
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append(tuple(new_state))

    return neighbors


def dfs(state, goal, path, visited, depth, limit):
    if state == goal:
        return path

    # Depth limit reached
    if depth == limit:
        return None

    visited.add(state)

    for neighbor in get_neighbors(state):
        if neighbor not in visited:

            result = dfs(
                neighbor,
                goal,
                path + [neighbor],
                visited,
                depth + 1,
                limit
            )

            if result is not None:
                return result

    visited.remove(state)

    return None


def solve(start, goal):
    for limit in range(50):
        result = dfs(
            start,
            goal,
            [start],
            set(),
            0,
            limit
        )

        if result is not None:
            return result

    return None


print("Enter initial state (use 0 for blank):")
start = tuple(map(int, input().split()))

print("Enter goal state (use 0 for blank):")
goal = tuple(map(int, input().split()))


solution = solve(start, goal)


if solution:
    print("\nOptimal solution found!")
    print("Number of moves:", len(solution) - 1)

    for i, state in enumerate(solution):
        print("Step", i)
        print_puzzle(state)
else:
    print("No solution found.")
