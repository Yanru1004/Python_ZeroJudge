while True:
    try:
        pw = input() #取得正確密碼
        if pw == '': #跳過空行
            continue 
        pw = pw.strip().split(' ')
        n = int(input()) #取得猜數字次數

        #猜數字迴圈開始
        for i in range(n):
            guess = input().strip().split(' ') #取得猜數字資訊

            index = [0,1,2,3]
            #a = 0
            b = 0
            #計算數字及位置皆正確數量
            print(pw,guess)
            for x in range(4):
                if pw[x] == guess[x]:
                    print
                    guess[x] = 'x'
                    index.pop(x)
            print(guess,index)
            for y in index:
                if pw[y] in guess:
                    b += 1
            
            print(f'{4-len(index)}A{b}B')
        
    except:
        break