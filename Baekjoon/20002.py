# N = int(input())

# arr=[]
# for i in range(N):
#     temp = [0 for i in range(N)]
#     arr.append(temp)

# for i in range(N) :
#     arr[i] = list(map(int, input().split()))

# arr_sum=[]
# for i in range(N+1):
#     temp2 = [0 for i in range(N+1)]
#     arr_sum.append(temp2)


# for i in range(N):
#     for j in range(N):
#         arr_sum[i+1][j+1] = arr_sum[i+1][j] + arr[i][j]
#     for k in range(N):
#         arr_sum[i+1][k+1] += arr_sum[i][k+1]

# result = max(max(arr))

# if result < arr_sum[N][N]: result = arr_sum[N][N]

# for s in range(2,N+1):
#     for i in range(s,N+1):
#         for j in range(s,N+1):
#             tmp = arr_sum[i][j] - arr_sum[i-s][j] - arr_sum[i][j-s] + arr_sum[i-s][j-s]
#             if tmp > result: result = tmp

# print(result)

import sys
input = sys.stdin.readline

n = int(input())
pre = [[-1001]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    arr = list(map(int, input().split()))
    for j in range(1, n+1):
        pre[i][j] = pre[i][j-1] + pre[i-1][j] - pre[i-1][j-1] + arr[j-1]

max_profit = pre[0][0]

for k in range(n):
    for i in range(1,n-k+1):
        for j in range(1, n-k+1):
            profit = pre[i+k][j+k] - pre[i-1][j+k] - pre[i+k][j-1] + pre[i-1][j-1]
            max_profit = max(max_profit, profit)

print(max_profit)