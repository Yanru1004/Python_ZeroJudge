#c461. apcs 邏輯運算子 (Logic Operators)
#2025.12.13 AC

#輸入並轉換為布林
check = lambda n: bool(int(n))
a,b,r = map(check,input().strip().split())

no_ans = True

#分別驗證 AND、OR、XOR
if (a & b) == r:
    print('AND')
    no_ans = False
if (a | b) == r:
    print('OR')
    no_ans = False
if (a ^ b) == r:
    print('XOR')
    no_ans = False

#不可能得到的結果
if no_ans == True:
    print('IMPOSSIBLE')