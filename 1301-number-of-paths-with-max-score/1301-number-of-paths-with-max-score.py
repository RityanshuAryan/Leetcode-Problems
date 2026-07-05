class Solution:
    def pathsWithMaxScore(self, board):
        n = len(board)
        MOD = 10**9 + 7
        dp = [[(-1, 0) for _ in range(n)] for _ in range(n)]
        dp[n-1][n-1] = (0, 1)
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] == 'X' or (i == n-1 and j == n-1):
                    continue
                maxScore = -1
                ways = 0
                for dx, dy in [(1,0), (0,1), (1,1)]:
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < n and 0 <= nj < n:
                        prevScore, prevWays = dp[ni][nj]
                        if prevWays == 0:
                            continue
                        val = 0 if board[i][j] in 'SE' else int(board[i][j])
                        currScore = prevScore + val
                        if currScore > maxScore:
                            maxScore = currScore
                            ways = prevWays
                        elif currScore == maxScore:
                            ways = (ways + prevWays) % MOD
                if maxScore != -1:
                    dp[i][j] = (maxScore, ways % MOD)
        result = dp[0][0]
        return [result[0], result[1]] if result[1] != 0 else [0,0]
