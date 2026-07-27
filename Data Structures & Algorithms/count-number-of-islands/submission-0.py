class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            grid[r][c] = "0"

            for dr, dc in moves:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != "0":
                    dfs(nr, nc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    num_islands += 1
        
        return num_islands