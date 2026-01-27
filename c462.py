#c462 交錯字串
#2026.0.27 AC

#讀入k值
k = int(input())

#讀入字串
text = input()
#大小寫判斷及轉換 =>輸出upper
upper = [int(ord(a)<97) for a in text]

#連續次數計算 => 輸出 count_list
count = 1
stat = None
count_list = []
for s in upper:
    if stat == None:
        stat = s
    else:
        if stat == s:
            count += 1
        else:
            count_list.append(count)
            count = 1
            stat = s
count_list.append(count)

#最長交錯統計
max_num = 0
num = 0

for n in count_list:

    if  n<k:
        max_num = max([max_num,num])
        num = 0
  
    elif n == k:
        num += k
        max_num = max([max_num,num])

    elif n > k:
        num += k
        max_num = max([max_num,num])
        num = k

print(max_num)
