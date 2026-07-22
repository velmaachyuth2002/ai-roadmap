from collections import deque


def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    count = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        visited.add((r, c))

        while queue:
            row, col = queue.popleft()

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                # Check bounds first
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Then check visited
                    if (nr, nc) not in visited:
                        # Then check land
                        if grid[nr][nc] == "1":
                            visited.add((nr, nc))
                            queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                count += 1
                bfs(r, c)

    return count


grid1 = [["1", "1", "0", "0"],
         ["1", "1", "0", "0"],
         ["0", "0", "1", "0"],
         ["0", "0", "0", "1"]]

grid2 = [["1", "1", "1"],
         ["1", "1", "1"],
         ["1", "1", "1"]]

grid3 = [["0", "0"],
         ["0", "0"]]

grid4 = []

print(num_islands(grid1))  # 3
print(num_islands(grid2))  # 1
print(num_islands(grid3))  # 0
print(num_islands(grid4))  # 0