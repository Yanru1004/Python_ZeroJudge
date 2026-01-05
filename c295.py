#c295. 最大和

#取得N(群數)及M(每群個數)
N,M = map(int,input().split())

#初始化資料串列
data = []

for group in range(N):
    data.append(list(map(int,input().split())))

print(sum([max(group) for group in data]))





