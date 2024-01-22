import heapq

def min_path_sum_with_constraints(grid):
    rows, cols = len(grid), len(grid[0])

    # Convert grid strings to integers
    grid = [[int(cell) for cell in row] for row in grid]

    # Directions: down (1,0), right (0,1), up (-1,0), left (0,-1)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    opposite_direction = {(1, 0): (-1, 0), (0, 1): (0, -1), (-1, 0): (1, 0), (0, -1): (0, 1)}

    # Priority queue: (cost, row, col, last_direction, straight_moves)
    pq = [(0, 0, 0, None, 0)]

    # Visited states: (row, col, last_direction, straight_moves)
    visited = set()

    while pq:
        cost, r, c, last_dir, straight_moves = heapq.heappop(pq)

        # Check if bottom-right cell is reached
        if r == rows - 1 and c == cols - 1:
            return cost

        if (r, c, last_dir, straight_moves) in visited:
            continue

        visited.add((r, c, last_dir, straight_moves))

        for dy, dx in directions:
            nr, nc = r + dy, c + dx
            new_dir = (dy, dx)

            # Check for boundary and reverse direction
            if 0 <= nr < rows and 0 <= nc < cols and new_dir != opposite_direction.get(last_dir, None):
                if new_dir == last_dir and straight_moves < 3:  # Continue in the same direction
                    new_cost = cost + grid[nr][nc]
                    heapq.heappush(pq, (new_cost, nr, nc, new_dir, straight_moves + 1))
                elif new_dir != last_dir:  # Change direction
                    new_cost = cost + grid[nr][nc]
                    heapq.heappush(pq, (new_cost, nr, nc, new_dir, 1))

    return float('inf')  # Path not found

# Example usage
with open('./day17/input.txt', 'r') as fp:
    grid = [list(line.strip()) for line in fp.readlines()]

print(min_path_sum_with_constraints(grid))