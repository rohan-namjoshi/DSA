def combinations(c,n,s):
  dp = [0]*(s+1)
  dp[0] = 1
  for i in c:
    for j in range(i,s+1):
      dp[j] += dp[j-i]
  return dp[s]

c = [1,2,3]
n = len(c)
s = 4

print("combinations: ", combinations(c,n,s))


