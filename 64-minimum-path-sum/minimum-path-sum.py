from functools import cache
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        @cache
        def func(i, j):
            if i == 0 and j == 0:
                return grid[0][0]
            if i < 0 or j < 0:
                return 1e9
            return grid[i][j] + min(func(i - 1, j), func(i, j - 1))
        return func(m - 1, n - 1)