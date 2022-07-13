def levenshtein(s, t):
    m = len(s)
    n = len(t)
    inf = float('inf')
    dp = [[inf for i in range(n + 1)] for j in range(m + 1)]
    dp[0][0] = 0

    for i in range(-1, m):
        for j in range(-1, n):
            if i == -1 and j == -1:
                continue
            elif i >= 0 and j >= 0:
                if s[i] == t[j]:
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i][j + 1] + 1, dp[i + 1][j] + 1)
                else:
                    dp[i + 1][j + 1] = min(dp[i][j] + 1, dp[i][j + 1] + 1, dp[i + 1][j] + 1)
            elif i >= 0:
                dp[i + 1][j + 1] = dp[i][j + 1] + 1
            elif j >= 0:
                dp[i + 1][j + 1] = dp[i + 1][j] + 1
    return dp[m][n]

                
print(levenshtein('sample', 'test'))