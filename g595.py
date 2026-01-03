#g595. 修補圍籬
#2025.12.14 AC

#取得圍籬寬度
n = int(input())

#取得圍籬高度
fence = list(map(int,input().split()))

#初始化花費
cost = 0

for f in range(len(fence)):
    if fence[f] == 0:
        #左邊界損壞
        if f == 0:
            cost += fence[1]
        #右邊界損壞
        elif f == len(fence)-1:
            cost += fence[-2]
        #中間損壞
        else:
            cost += min([fence[f-1],fence[f+1]])

print(cost)