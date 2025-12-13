#c294. APCS-2016-1029-1三角形辨別
#2025.12.12 AC

#讀取輸入資訊並排序
a,b,c = sorted([int(n) for n in input().split(' ')])

#第一行輸出(排序後邊長)
print(f'{a} {b} {c}')

check = a*a + b*b

if a+b <= c:
    print('No')
elif check < c*c:
    print('Obtuse')
elif check == c*c:
    print('Right')
else:
    print('Acute')