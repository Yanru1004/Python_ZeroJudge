#a647. 投資專家
#2025.07.01 AC

for i in range(int(input())):

    m,q = map(int,input().split(' '))
    
    #計算獲利
    profit = (q-m) / m
    if profit > 0:
        profit += 0.0000001
    else:
        profit -= 0.0000001
    
    if 0 > profit > -0.00001:
        profit = abs(profit)
    

    if profit >= 0.1 or profit <= -0.07:
        dispose = 'dispose'
    else:
        dispose = 'keep'

    print(f'{profit*100:2.2f}% {dispose}')