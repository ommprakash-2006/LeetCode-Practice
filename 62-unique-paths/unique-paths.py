from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:      
        @cache
        def func(i, j):
            if i == 0 and j == 0:
                return 1          
            if i < 0 or j < 0:
                return 0            
            return func(i - 1, j) + func(i, j - 1)        
        return func(m - 1, n - 1)  