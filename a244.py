while True:
    try:
        n = int(input())
        for i in range(n):
            a,b,c = [int(i) for i in input().strip().split(' ')]

            if a == 1:
                print(int(b+c))
            elif a==2:
                print(int(b-c))
            elif a==3:
                print(int(b*c))
            elif a==4:
                print(int(b/c))
    except:
        break
