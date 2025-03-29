while True:
    try:
        n = int(input())
        li = input().strip().split(' ')

        for i in range(n-1,0,-1):
            for j in range(i):
                if int(li[j]) > int(li[j+1]):
                    li[j],li[j+1] = li[j+1],li[j]
        print(' '.join(li))        
    except:
        break