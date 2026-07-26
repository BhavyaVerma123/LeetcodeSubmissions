class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        maxarea = 0

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or grid[r][c] == 0:
                return 0    
            visited.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    maxarea = max(maxarea,dfs(i,j))

        return maxarea