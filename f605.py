#f605. 購買力
#2025.12.14 AC

#讀取商品數及期望價格差異
n,d = map(int,input().split())

#初始化購買數量及花費
item,pay = 0,0

#商品判斷迴圈
for i in range(n):
    #讀取價格資訊
    price = list(map(int,input().split()))
    
    if max(price) - min(price) >= d:
        item += 1
        pay += sum(price)//3

print(item,pay)