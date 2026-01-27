#c295. 最大和
#2026.01.06 AC

#取得N(群數)及M(每群個數)
N,M = map(int,input().split())

#初始化資料串列
data = []

for group in range(N):
    data.append(list(map(int,input().split())))

max_num = [max(group) for group in data]
max_sum = sum(max_num)

#輸出最大和
print(max_sum)

can_div = [str(n) for n in max_num if max_sum % n == 0]

if can_div == []:
    print('-1')
else:
    print(' '.join(can_div))