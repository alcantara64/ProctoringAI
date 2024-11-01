import numpy as np
import math


integers = np.array([[1, 4, 5], [6, 2, 8]])
# print(np.arange(5))
# for value in integers:
#     for colum in value:
        
#         print(f'{colum}', end=" ")
# print(integers)

# print(integers.max(axis=1))

items = [4,3,2,7,8,2,3,1]

dic = {}
twice = []
for item in items:
    if dic.get(item):
        twice.append(item)
        dic[item] += 1
    else:
        dic[item] = 1
# print(twice)


def findUniquePart(m,n):
    dp = [[0] * n for _ in range(m)]
    for i in range(len(dp)):
        print(dp[i])
        for j in range(len(dp[i])):
            if i == 0 or j == 0 :
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] +dp[i][j-1]
            
    return dp[m-1][n-1]

print(findUniquePart(2,3))
