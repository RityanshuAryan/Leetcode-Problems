class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        q = collections.deque()
        dist_grid = [[-1] * n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    dist_grid[r][c] = 0
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            r, c = q.popleft()
            current_dist = dist_grid[r][c]
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist_grid[nr][nc] == -1:
                    dist_grid[nr][nc] = current_dist + 1
                    q.append((nr, nc))

        def check(safeness_factor):
            if dist_grid[0][0] < safeness_factor or dist_grid[n-1][n-1] < safeness_factor:
                return False

            q_check = collections.deque([(0, 0)])
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True

            while q_check:
                r, c = q_check.popleft()

                if r == n - 1 and c == n - 1:
                    return True

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and dist_grid[nr][nc] >= safeness_factor:
                        visited[nr][nc] = True
                        q_check.append((nr, nc))
            
            return False

        low, high = 0, n * 2
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans