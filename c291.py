#c291. 小群體
#2025.12.22 AC

#取得團體人數
n = int(input())

#取得好友編號
friend = [int(num) for num in input().split()]
check = [0 for i in range(n)]
group = 0
for i in range(n):
    if check[i] == -1:
        continue
    else:
        next = i
        
        while friend[next] != i:            
            check[next] = -1            
            next = friend[next]
        check[next] = -1
        group += 1
print(group)

            