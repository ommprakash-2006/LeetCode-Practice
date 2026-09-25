from functools import cache
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        @cache
        def func(i, j):
            if i == len(triangle) - 1:
                return triangle[i][j]
            return triangle[i][j] + min(func(i + 1, j),func(i + 1, j + 1))
        return func(0, 0)