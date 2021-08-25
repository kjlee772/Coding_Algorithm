count_arr = [[1, 0],
             [0, 1],]

def make_arr():
    for i in range(2, 41):
        tmp_0 = count_arr[i-2][0] + count_arr[i-1][0]
        tmp_1 = count_arr[i-2][1] + count_arr[i-1][1]
        count_arr.append([tmp_0, tmp_1])

make_arr()
T = int(input())
arr = []

for i in range(0, T):
    temp = int(input())
    arr.append(temp)

for i in arr:
    tmp = count_arr[i]
    print(tmp[0], tmp[1])