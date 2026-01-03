#b965. 矩陣轉換
#2025.12.18 AC

#讀取行列樹及操作數
r,c,m = map(int,input().split())

#讀取陣列資訊
mat_b = []

for i in range(r):
    mat_b.append([int(a) for a in input().split()])

matrix = list[list[int]]
#翻轉函式
def filp(mat:matrix):
    new_mat = []
    rows = len(mat)
    for r in range(rows):
        new_mat.append(mat[-1-r])
    return new_mat

#旋轉函式
def rotate(mat:matrix):
    rows = len(mat)
    cols = len(mat[0])
    #初始化新陣列
    new_mat = [[None]*rows for i in range(cols)]
    #填入元素
    

    for r in range(cols):
        for c in range(rows):
            new_mat[r][c] = mat[c][cols-1-r]
            
    return new_mat

#讀取操作及執行
op = list(map(int,input().split()))

for o in op[::-1]:
    if o == 0:
        mat_b = rotate(mat_b)
    elif o == 1:
        mat_b = filp(mat_b)

#輸出
print(f'{len(mat_b)} {len(mat_b[0])}')

for li in mat_b:
    print(' '.join(map(str,li)))
