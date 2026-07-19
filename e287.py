#e287 機器人的路徑

#讀取地圖大小
n,m = map(int,input().split())

#創建及讀取地圖
#地圖初始化
space = [[-1] * (m+2) for i in range(n+2)]

print(space)

pos_x = 0
pos_y = 0
min_num = 2000000

for i in range(1,n+1):
    li = [int(num) for num in input().split()]
    for j in range(m):
        num = li[j]
        space[i][j+1] = num
        #更新最小值及其位置
        if num < min_num:
            min_num = num
            pos_x = j+1
            pos_y = i

print(pos_x,pos_y)
print(min_num)
print(space)





