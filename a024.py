while True:
    try:
        s = input()
        a,b = s.split(' ')
        a,b = int(a),int(b)

        while b != 0:
            m = a%b
            a = b
            b = m
        print(a)
    except:
        break