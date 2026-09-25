from functools import cache
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        @cache
        def solve(i, j):
            if i == 0 and j == 0:
                return grid[0][0]

            if i < 0 or j < 0:
                return float('inf')

            return grid[i][j] + min(solve(i - 1, j), solve(i, j - 1))

        return solve(m - 1, n - 1)