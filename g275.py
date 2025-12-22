#g275. 七言對聯
#2025.12.14 AC

#取得對聯組數
n = int(input())

#讀取對聯

for i in range(n):
    #a,b為第一句及第二具
    a = [int(s) for s in input().split()]
    b = [int(s) for s in input().split()]

    no_wrong = True
    #規則A
    if (a[1] == a[3]) or (a[1] != a[5]) or (b[1] == b[3]) or (b[1] != b[5]):
        print('A',end='')
        no_wrong = False
    
    #規則B
    if a[-1] == 0 or b[-1] == 1:
        print('B',end='')
        no_wrong = False
    
    #規則C
    if (a[1] == b[1]) or (a[3] == b[3]) or (a[5] == b[5]):
        print('C',end='')
        no_wrong = False
    
    if no_wrong:
        print(None)
    
    print('')  