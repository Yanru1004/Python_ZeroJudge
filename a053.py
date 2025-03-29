while True:
    try:
        n = int(input())
        if n <= 10:
            score = n * 6
        elif n <= 20:
            score = 60 + (n-10) * 2
        elif n <= 40:
            score = 80 + (n-20)
        else:
            score = 100
        print(score)

    except:
        break