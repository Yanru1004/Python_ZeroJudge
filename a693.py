#a693. 吞食天地

while True:

    try:
        n,m = map(int,input().split(' '))

        #取得食物飽食度陣列
        food = list(map(int,input().split(' ')))

        for i in range(m):
            l,r = map(int,input().split(' '))
            print(sum(food[l-1:r]))

    except EOFError:
        break
    