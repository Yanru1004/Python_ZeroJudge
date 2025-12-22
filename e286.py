#e286. 籃球比賽
#2025.12.13 AC

#A隊第一場
score_1 = sum(map(int,input().split()))
#B隊第一場
score_2 = sum(map(int,input().split()))
#A隊第二場
score_3 = sum(map(int,input().split()))
#B隊第二場
score_4 = sum(map(int,input().split()))

#輸出
print(f'{score_1}:{score_2}')
print(f'{score_3}:{score_4}')

result = ['Lose','Tie','Win'][(score_1>score_2)+(score_3>score_4)]

print(result)