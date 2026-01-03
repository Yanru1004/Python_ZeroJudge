#f579. 購物車
#2025.12.14 AC

#讀取物品編號
a,b = map(int,input().split())
#讀取客人數量
c = int(input())

#客人購物迴圈
result = 0
for i in range(c):
    #初始化購物車
    cart = [0,0]
    #讀取購物清單並迴圈
    buy_list = map(int,input().split())

    for buy in buy_list:
        if buy == a:
            cart[0] += 1
        elif buy == -a:
            cart[0] -= 1
        
        elif buy == b:
            cart[1] += 1
        elif buy == -b:
            cart[1] -= 1
        else:
            pass
    
    #是否購物判斷
    if cart[0] >0 and cart[1]>0:
        result +=1
#輸出
print(result)