def count_islands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        # Boundary check + water/visited check
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] == 0 or visited[r][c]:
            return
        
        visited[r][c] = True
        
        # Check all 4 directions (up, down, left, right)
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                dfs(r, c)
                islands += 1

    return islands


# Reading input
grid = []
print("Enter 10 rows of 10 digits (0 for sea, 1 for land):")
for _ in range(10):
    row = list(map(int, list(input().strip())))
    grid.append(row)

# Counting islands
result = count_islands(grid)
print("Number of islands:", result)
