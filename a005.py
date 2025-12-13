#a005. Eva 的回家作業

#取得數列組數
n = int(input())

#迴圈
for i in range(n):
    #讀入數列
    nums = [int(num) for num in input().split(' ')]

    #等差數列判斷
    if (nums[0] - nums[1]) == (nums[1] - nums[2]):
        diff = nums[1] - nums[0]
        nums.append(nums[3] + diff)
        print(' '.join(map(str,nums)))

    else:
        diff = nums[1] // nums[0]
        nums.append(nums[3] * diff)
        print(' '.join(map(str,nums)))