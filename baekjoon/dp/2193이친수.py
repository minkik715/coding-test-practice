n=int(input())
dp=[0,1,1]
for i in range(3, 91):
    result=dp[i-1]+dp[i-2]
    dp.append(result)
print(dp[n])

