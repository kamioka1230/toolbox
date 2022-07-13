def max_num(n, arr):
    dp = [0] * (n + 1)
    for i in range(n):
        dp [i + 1] = max(dp[i], dp[i] + arr[i])
    return dp[n]

import random
arr = [random.randint(-50,50) for i in range(10)]

print(arr)
print(max_num(10, arr))