while True:
    try:
        num = int(input())
        if num != 0:
            print(str(bin(num^(num+1))).count('1')-1)

    except:
        break