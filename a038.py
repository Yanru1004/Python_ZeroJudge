while True:
    try:
        s = input()
        result = ''
        while s != '':
            result += s[-1]
            s = s[:-1]
        
        while result[0] == '0'and len(result) > 1:
            result = result[1:]
        print(result)

    except:
        break
