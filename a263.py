from datetime import datetime

while True:
    try:
        a = [int(i) for i in input().strip().split()]
        b = [int(i) for i in input().strip().split()]

        a = datetime(a[0],a[1],a[2])
        b = datetime(b[0],b[1],b[2])

        print(abs((b-a).days))

    except:
        break