while True:
    try:
        s = input()
        result = ''
        for i in range(len(s)-1):
            result += str(abs(ord(s[i])-ord(s[i+1])))
        print(result)
    except:
        break